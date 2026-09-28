"""Schedules one Kit email per newly published article. Runs on GitHub Actions after the Pages deploy.

A new post is a file in _posts without `published: false`, dated in the past, whose slug is not in
_data/newsletter_sent.yml. The Portuguese post `slug` and its English version `slug-en` are one article and go
out as a single email with both links, to all subscribers. The email is a teaser (image, title, description and
link), not the full post: Chirpy includes don't render as email HTML. Nothing is sent while `newsletter.send` is
false in _config.yml. Sending is scheduled 10 minutes ahead, which leaves time to cancel it in Kit.

    KIT_API_KEY=... python tools/newsletter.py            # schedule and record
    KIT_API_KEY=... python tools/newsletter.py --dry-run  # only print what would be sent
    KIT_API_KEY=... python tools/newsletter.py --list-ids # print the Kit form ids to put in _config.yml
"""
from __future__ import annotations

import argparse, datetime as dt, html, json, os, re, sys, urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SENT = ROOT / "_data/newsletter_sent.yml"
MAX_PER_RUN = 2   # guard against an accidental mass send


def front_matter(p: Path) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", p.read_text(), re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def post_date(p: Path, fm: dict) -> dt.datetime:
    d = fm.get("date")
    if isinstance(d, dt.datetime):
        return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)
    if isinstance(d, str):
        return dt.datetime.strptime(d, "%Y-%m-%d %H:%M:%S %z")
    return dt.datetime.strptime(p.name[:10], "%Y-%m-%d").replace(tzinfo=dt.timezone.utc)


def section(title: str, description: str, url: str, image: str | None, button: str) -> str:
    img = f'<p><a href="{url}"><img src="{image}" alt="" style="max-width:100%;border-radius:8px"></a></p>' if image else ""
    return (f'{img}<h2 style="margin:0 0 8px">{html.escape(title)}</h2>'
            f'<p>{html.escape(description)}</p><p><a href="{url}"><strong>{button} →</strong></a></p>')


def kit(path: str, payload: dict) -> dict:
    req = urllib.request.Request(f"https://api.kit.com/v4/{path}", data=json.dumps(payload).encode(), method="POST",
                                 headers={"X-Kit-Api-Key": os.environ["KIT_API_KEY"], "Content-Type": "application/json",
                                          "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def kit_get(path: str) -> dict:
    req = urllib.request.Request(f"https://api.kit.com/v4/{path}", headers={"X-Kit-Api-Key": os.environ["KIT_API_KEY"], "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def list_ids():
    for kind in ("forms", "tags"):
        items = kit_get(kind).get(kind, [])
        print(f"{kind}: {len(items)}")
        for item in items:
            print(f"  {item.get('id')}  {item.get('name')}")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--list-ids", action="store_true")
    a = ap.parse_args()
    if a.list_ids:
        list_ids(); return
    cfg = yaml.safe_load((ROOT / "_config.yml").read_text())
    base, nl = cfg["url"].rstrip("/"), cfg.get("newsletter") or {}
    sent = yaml.safe_load(SENT.read_text()) or []
    now = dt.datetime.now(dt.timezone.utc)
    new = []
    for p in sorted((ROOT / "_posts").glob("*.md")):
        fm, slug = front_matter(p), p.stem[11:]
        if slug in sent or fm.get("published") is False or post_date(p, fm) > now:
            continue
        new.append((fm, slug))
    if not new:
        print("no new posts"); return
    articles: dict[str, dict[str, tuple[dict, str]]] = {}
    for fm, slug in new:
        pt = str(fm.get("lang") or cfg.get("lang", "")).startswith("pt")
        key = slug[:-3] if slug.endswith("-en") else slug
        articles.setdefault(key, {})["pt" if pt else "en"] = (fm, slug)
    if not a.dry_run and not (os.environ.get("KIT_API_KEY") and nl.get("send")):
        print(f"newsletter sending is off (needs KIT_API_KEY and newsletter.send: true), skipping {list(articles)}"); return
    if len(articles) > MAX_PER_RUN:
        sys.exit(f"{len(articles)} new articles at once ({list(articles)}), above the limit of {MAX_PER_RUN}. "
                 "If that's intended, publish them one at a time or add the slugs to _data/newsletter_sent.yml.")
    for key, versions in articles.items():
        parts = []
        for lang, button in (("pt", "Ler o post"), ("en", "Read in English")):
            if lang in versions:
                fm, slug = versions[lang]
                image = (fm.get("image") or {}).get("path") if isinstance(fm.get("image"), dict) else fm.get("image")
                image = f"{base}{image}" if image and image.startswith("/") and not parts else None
                parts.append(section(fm["title"], fm.get("description", ""), f"{base}/posts/{slug}/", image, button))
        main_fm = (versions.get("pt") or versions["en"])[0]
        send_at = (now + dt.timedelta(minutes=10)).isoformat(timespec="seconds")
        payload = {"subject": main_fm["title"], "description": f"article {key}", "preview_text": main_fm.get("description", ""),
                   "content": '<hr style="border:0;border-top:1px solid #e4e4e7;margin:24px 0">'.join(parts),
                   "public": False, "published_at": now.isoformat(timespec="seconds"), "send_at": send_at}
        slugs = [s for _, s in versions.values()]
        if a.dry_run:
            print(f"[dry run] {slugs} -> all subscribers at {send_at}\n{json.dumps(payload, ensure_ascii=False, indent=1)}")
            continue
        r = kit("broadcasts", payload)
        print(f"{slugs}: broadcast {r.get('broadcast', {}).get('id')} scheduled for {send_at}")
        for s in slugs:   # record after each send, without rewriting the file
            SENT.write_text(SENT.read_text().rstrip("\n") + f"\n- {s}\n")

if __name__ == "__main__":
    main()
