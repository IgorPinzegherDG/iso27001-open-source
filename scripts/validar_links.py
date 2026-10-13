#!/usr/bin/env python3
"""Verifica se cada URL citada em dados/controles.yaml ainda responde.

Link quebrado em repositório público só aparece quando alguém abre issue,
então esta verificação roda no CI a cada alteração e também semanalmente.
"""

import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTE = os.path.join(RAIZ, "dados", "controles.yaml")

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36")

ACEITOS = {200, 301, 302}


def coletar():
    """Uma entrada por URL, com o nome e a licença para a mensagem de erro."""
    with open(FONTE, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    urls = {}
    for tema in doc["temas"]:
        for ctrl in tema["controles"]:
            for f in ctrl["ferramentas"]:
                urls.setdefault(f["url"], (f["nome"], f["licenca"]))
    return urls


def testar(url):
    """HEAD primeiro, GET como reserva: há servidor que recusa HEAD."""
    for metodo in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA},
                                         method=metodo)
            with urllib.request.urlopen(req, timeout=20) as resp:
                return url, resp.status
        except urllib.error.HTTPError as erro:
            if erro.code in (403, 405) and metodo == "HEAD":
                continue
            return url, erro.code
        except Exception as erro:
            if metodo == "GET":
                return url, type(erro).__name__
    return url, "sem resposta"


def main():
    urls = coletar()
    with ThreadPoolExecutor(max_workers=12) as pool:
        resultados = dict(pool.map(testar, urls))

    ruins = {u: s for u, s in resultados.items() if s not in ACEITOS}
    print(f"{len(urls)} URLs verificadas, {len(ruins)} com problema")

    for url, status in sorted(ruins.items(), key=lambda par: str(par[1])):
        nome, licenca = urls[url]
        print(f"\n  [{status}] {nome} ({licenca})\n        {url}")

    return 1 if ruins else 0


if __name__ == "__main__":
    sys.exit(main())
