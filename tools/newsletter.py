"""Schedules a Kit email for every newly published post. Runs on GitHub Actions after the Pages deploy.

A new post is a file in _posts without `published: false`, dated in the past, whose slug is not in
_data/newsletter_sent.yml. The email is a teaser (image, title, description and link), not the full post:
Chirpy includes don't render as email HTML. Portuguese posts go to the pt segment, everything else to the en one.
Sending is scheduled 10 minutes ahead, which leaves time to cancel it in Kit.

    KIT_API_KEY=... python tools/newsletter.py            # schedule and record
    KIT_API_KEY=... python tools/newsletter.py --dry-run  # only print what would be sent
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


def body(title: str, description: str, url: str, image: str | None, pt: bool) -> str:
    button = "Ler o post" if pt else "Read the post"
    img = f'<p><a href="{url}"><img src="{image}" alt="" style="max-width:100%;border-radius:8px"></a></p>' if image else ""
    return (f'{img}<h2 style="margin:0 0 8px">{html.escape(title)}</h2>'
            f'<p>{html.escape(description)}</p><p><a href="{url}"><strong>{button} →</strong></a></p>')


def kit(path: str, payload: dict) -> dict:
    req = urllib.request.Request(f"https://api.kit.com/v4/{path}", data=json.dumps(payload).encode(), method="POST",
                                 headers={"X-Kit-Api-Key": os.environ["KIT_API_KEY"], "Content-Type": "application/json",
                                          "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dry-run", action="store_true"); a = ap.parse_args()
    cfg = yaml.safe_load((ROOT / "_config.yml").read_text())
    base, nl = cfg["url"].rstrip("/"), cfg.get("newsletter") or {}
    sent = yaml.safe_load(SENT.read_text()) or []
    now = dt.datetime.now(dt.timezone.utc)
    new = []
    for p in sorted((ROOT / "_posts").glob("*.md")):
        fm, slug = front_matter(p), p.stem[11:]
        if slug in sent or fm.get("published") is False or post_date(p, fm) > now:
            continue
        new.append((p, fm, slug))
    if not new:
        print("no new posts"); return
    if len(new) > MAX_PER_RUN:
        sys.exit(f"{len(new)} new posts at once ({[s for *_, s in new]}), above the limit of {MAX_PER_RUN}. "
                 "If that's intended, publish them one at a time or add the slugs to _data/newsletter_sent.yml.")
    for p, fm, slug in new:
        pt = str(fm.get("lang") or cfg.get("lang", "")).startswith("pt")
        segment = nl.get("segment_pt" if pt else "segment_en")
        if not segment:
            sys.exit(f"segment_{'pt' if pt else 'en'} is empty in _config.yml (newsletter)")
        url = f"{base}/posts/{slug}/"
        image = (fm.get("image") or {}).get("path") if isinstance(fm.get("image"), dict) else fm.get("image")
        image = f"{base}{image}" if image and image.startswith("/") else image
        send_at = (now + dt.timedelta(minutes=10)).isoformat(timespec="seconds")
        payload = {"subject": fm["title"], "description": f"post {slug}", "preview_text": fm.get("description", ""),
                   "content": body(fm["title"], fm.get("description", ""), url, image, pt),
                   "public": False, "published_at": now.isoformat(timespec="seconds"), "send_at": send_at,
                   "subscriber_filter": [{"all": [{"type": "segment", "ids": [int(segment)]}], "any": None, "none": None}]}
        if a.dry_run:
            print(f"[dry run] {slug} -> segment {segment} at {send_at}\n{json.dumps(payload, ensure_ascii=False, indent=1)}")
            continue
        r = kit("broadcasts", payload)
        print(f"{slug}: broadcast {r.get('broadcast', {}).get('id')} scheduled for {send_at}")
        sent.append(slug)
        SENT.write_text(SENT.read_text().rstrip("\n") + f"\n- {slug}\n")   # record after each send, without rewriting the file


if __name__ == "__main__":
    main()
