"""Verifica se cada URL citada responde, antes de publicar."""
import sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, "dados")
from parte_a5 import A5
from parte_a6_a7 import A6, A7
from parte_a8 import A8

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36")

urls = {}
for ctrl in A5 + A6 + A7 + A8:
    for nome, url, lic, _ in ctrl[3]:
        urls.setdefault(url, (nome, lic))

def testar(url):
    for metodo in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA}, method=metodo)
            with urllib.request.urlopen(req, timeout=20) as r:
                return url, r.status
        except urllib.error.HTTPError as e:
            if e.code in (403, 405) and metodo == "HEAD":
                continue
            return url, e.code
        except Exception as e:
            if metodo == "GET":
                return url, type(e).__name__
    return url, "?"

with ThreadPoolExecutor(max_workers=12) as pool:
    resultados = dict(pool.map(testar, urls))

ruins = {u: s for u, s in resultados.items() if s not in (200, 301, 302)}
print(f"{len(urls)} URLs verificadas, {len(ruins)} com problema\n")
for url, status in sorted(ruins.items(), key=lambda x: str(x[1])):
    nome, lic = urls[url]
    print(f"  [{status}] {nome} ({lic})\n        {url}")
