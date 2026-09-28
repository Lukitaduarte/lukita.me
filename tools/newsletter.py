"""Manda um e-mail pelo Kit para cada post novo publicado. Roda no GitHub Actions depois do deploy do Pages.

Post novo = arquivo em _posts sem `published: false`, com data já passada e slug fora de _data/newsletter_enviados.yml.
O e-mail é um convite (imagem, título, descrição e link), não o post inteiro: os includes do Chirpy não viram HTML de e-mail.
Posts em pt vão para o segmento pt, os demais para o en. O agendamento fica 10 min à frente, o que dá tempo de cancelar no Kit.

    KIT_API_KEY=... python tools/newsletter.py            # envia e registra
    KIT_API_KEY=... python tools/newsletter.py --ensaio   # só mostra o que faria
"""
from __future__ import annotations

import argparse, datetime as dt, html, json, os, re, sys, urllib.request
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parents[1]
ENVIADOS = RAIZ / "_data/newsletter_enviados.yml"
MAX_POR_VEZ = 2   # trava contra disparo em massa por engano


def front_matter(p: Path) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", p.read_text(), re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def data_do_post(p: Path, fm: dict) -> dt.datetime:
    d = fm.get("date")
    if isinstance(d, dt.datetime):
        return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)
    if isinstance(d, str):
        return dt.datetime.strptime(d, "%Y-%m-%d %H:%M:%S %z")
    return dt.datetime.strptime(p.name[:10], "%Y-%m-%d").replace(tzinfo=dt.timezone.utc)


def corpo(titulo: str, descricao: str, url: str, imagem: str | None, pt: bool) -> str:
    botao = "Ler o post" if pt else "Read the post"
    img = f'<p><a href="{url}"><img src="{imagem}" alt="" style="max-width:100%;border-radius:8px"></a></p>' if imagem else ""
    return (f'{img}<h2 style="margin:0 0 8px">{html.escape(titulo)}</h2>'
            f'<p>{html.escape(descricao)}</p><p><a href="{url}"><strong>{botao} →</strong></a></p>')


def kit(caminho: str, corpo_json: dict) -> dict:
    req = urllib.request.Request(f"https://api.kit.com/v4/{caminho}", data=json.dumps(corpo_json).encode(), method="POST",
                                 headers={"X-Kit-Api-Key": os.environ["KIT_API_KEY"], "Content-Type": "application/json",
                                          "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--ensaio", action="store_true"); a = ap.parse_args()
    cfg = yaml.safe_load((RAIZ / "_config.yml").read_text())
    base, nl = cfg["url"].rstrip("/"), cfg.get("newsletter") or {}
    enviados = yaml.safe_load(ENVIADOS.read_text()) or []
    agora = dt.datetime.now(dt.timezone.utc)
    novos = []
    for p in sorted((RAIZ / "_posts").glob("*.md")):
        fm, slug = front_matter(p), p.stem[11:]
        if slug in enviados or fm.get("published") is False or data_do_post(p, fm) > agora:
            continue
        novos.append((p, fm, slug))
    if not novos:
        print("nenhum post novo"); return
    if len(novos) > MAX_POR_VEZ:
        sys.exit(f"{len(novos)} posts novos de uma vez ({[s for *_, s in novos]}); acima da trava de {MAX_POR_VEZ}. "
                 "Se for de propósito, envie um a um ou acrescente os slugs em _data/newsletter_enviados.yml.")
    for p, fm, slug in novos:
        pt = str(fm.get("lang") or cfg.get("lang", "")).startswith("pt")
        segmento = nl.get("segmento_pt" if pt else "segmento_en")
        if not segmento:
            sys.exit(f"segmento {'pt' if pt else 'en'} vazio em _config.yml (newsletter)")
        url = f"{base}/posts/{slug}/"
        imagem = (fm.get("image") or {}).get("path") if isinstance(fm.get("image"), dict) else fm.get("image")
        imagem = f"{base}{imagem}" if imagem and imagem.startswith("/") else imagem
        envio = (agora + dt.timedelta(minutes=10)).isoformat(timespec="seconds")
        pedido = {"subject": fm["title"], "description": f"post {slug}", "preview_text": fm.get("description", ""),
                  "content": corpo(fm["title"], fm.get("description", ""), url, imagem, pt),
                  "public": False, "published_at": agora.isoformat(timespec="seconds"), "send_at": envio,
                  "subscriber_filter": [{"all": [{"type": "segment", "ids": [int(segmento)]}], "any": None, "none": None}]}
        if a.ensaio:
            print(f"[ensaio] {slug} -> segmento {segmento} às {envio}\n{json.dumps(pedido, ensure_ascii=False, indent=1)}")
            continue
        r = kit("broadcasts", pedido)
        print(f"{slug}: broadcast {r.get('broadcast', {}).get('id')} agendado para {envio}")
        enviados.append(slug)
        ENVIADOS.write_text(ENVIADOS.read_text().rstrip("\n") + f"\n- {slug}\n")   # registra a cada envio, sem reescrever o arquivo


if __name__ == "__main__":
    main()
