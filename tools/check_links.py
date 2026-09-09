#!/usr/bin/env python3
"""Prüft alle URLs in src.txt, praesentation.html und vorlagen/*.md auf Erreichbarkeit.

Aufruf:  python tools/check_links.py [--timeout 15] [--workers 8] [--report AENDERUNGEN_links.md]

Gibt eine Tabelle (URL, Status, Quelle) aus. Exit-Code 0, wenn alle URLs 2xx/3xx liefern
oder als bekannt bot-blockiert (403/429) eingestuft sind, sonst 1.
Nur Standardbibliothek – keine Abhängigkeiten.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = [ROOT / "src.txt", ROOT / "praesentation.html", ROOT / "README.md",
           ROOT / "eu_ai_act_recherche.md", ROOT / "glossar.md"] + sorted((ROOT / "vorlagen").glob("*.md"))

URL_RE = re.compile(r"https?://(?!www\.w3\.org)[^\s<>\"')\]]+")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
# Hosts, die Skript-Zugriffe blockieren, aber im Browser erreichbar sind:
BOT_BLOCKED_OK = {403, 429, 999}


def collect() -> dict[str, set[str]]:
    urls: dict[str, set[str]] = {}
    for src in SOURCES:
        if not src.exists():
            continue
        text = src.read_text(encoding="utf-8", errors="replace")
        for m in URL_RE.finditer(text):
            u = m.group(0).rstrip(".,;:")
            u = u.replace("&amp;", "&")
            urls.setdefault(u, set()).add(src.name)
    return urls


def probe(url: str, timeout: int) -> tuple[str, int | str]:
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method,
                                     headers={"User-Agent": UA, "Accept-Language": "de,en"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return url, r.status
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (405, 403, 404, 501):
                continue  # Server mag kein HEAD -> GET versuchen
            return url, e.code
        except Exception as e:  # noqa: BLE001
            if method == "HEAD":
                continue
            # urllib scheitert bei manchen Behördenseiten am TLS-Handshake -> curl als zweite Meinung
            code = curl_status(url, timeout)
            return url, code if code else type(e).__name__
    return url, "unknown"


def curl_status(url: str, timeout: int) -> int | None:
    """HTTP-Status via curl (falls installiert), sonst None."""
    if not shutil.which("curl"):
        return None
    try:
        out = subprocess.run(
            ["curl", "-s", "-o", os.devnull, "-w", "%{http_code}", "-L", "-A", UA,
             "--max-time", str(timeout), url],
            capture_output=True, text=True, timeout=timeout + 5, check=False,
        ).stdout.strip()
        return int(out) if out.isdigit() and int(out) > 0 else None
    except Exception:  # noqa: BLE001
        return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=15)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--report", type=Path, default=None)
    args = ap.parse_args()

    urls = collect()
    print(f"{len(urls)} URLs aus {len(SOURCES)} Dateien\n")
    results: list[tuple[str, int | str, str]] = []
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        for url, status in ex.map(lambda u: probe(u, args.timeout), sorted(urls)):
            results.append((url, status, ", ".join(sorted(urls[url]))))

    bad = []
    lines = ["| Status | URL | Quelle |", "|---|---|---|"]
    for url, status, src in results:
        ok = isinstance(status, int) and (200 <= status < 400)
        blocked = isinstance(status, int) and status in BOT_BLOCKED_OK
        mark = "OK" if ok else ("BOT-BLOCK" if blocked else "FEHLER")
        if not ok and not blocked:
            bad.append((url, status, src))
        lines.append(f"| {mark} {status} | {url} | {src} |")
        print(f"{mark:9} {str(status):5} {url}")

    print(f"\nErgebnis: {len(results) - len(bad)} erreichbar/bot-blockiert, {len(bad)} fehlerhaft")
    for url, status, src in bad:
        print(f"  FEHLER {status}: {url}  ({src})")

    if args.report:
        args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Report: {args.report}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
