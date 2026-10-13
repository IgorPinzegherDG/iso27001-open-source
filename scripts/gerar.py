#!/usr/bin/env python3
"""Gera os arquivos de controles e o índice de ferramentas a partir do YAML.

Fonte única de verdade: dados/controles.yaml. Rode este script depois de
qualquer alteração lá, para que a documentação não divirja do dado.
"""

import os
import re
from collections import defaultdict

import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTE = os.path.join(RAIZ, "dados", "controles.yaml")

AVISO = (
    "> Gerado por `scripts/gerar.py` a partir de `dados/controles.yaml`.\n"
    "> Edite o YAML, não este arquivo.\n"
)

NOTA_NORMA = (
    "> O texto normativo da ISO/IEC 27001 e da ISO/IEC 27002 é protegido por\n"
    "> direitos autorais e **não é reproduzido aqui**. Os títulos servem apenas\n"
    "> de referência e os objetivos são redação própria. Para implementar, use\n"
    "> a norma adquirida da ABNT ou da ISO.\n"
)

ARQUIVOS = {
    "A.5": "A5-organizacionais.md",
    "A.6": "A6-pessoas.md",
    "A.7": "A7-fisicos.md",
    "A.8": "A8-tecnologicos.md",
}


def ancora(texto):
    """Âncora no formato que o GitHub gera para um título."""
    limpo = re.sub(r"[^\w\s-]", "", texto.lower(), flags=re.UNICODE)
    return re.sub(r"[\s]+", "-", limpo.strip())


def carregar():
    with open(FONTE, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def escrever(caminho, conteudo):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as fh:
        fh.write(conteudo)
    print(f"  {os.path.relpath(caminho, RAIZ)}")


def gerar_tema(tema):
    linhas = [f"# {tema['id']} {tema['nome']}", "", AVISO, "", NOTA_NORMA, ""]
    linhas.append(f"{len(tema['controles'])} controles.")
    linhas.append("")

    # Sumário, porque o arquivo é longo demais para rolar procurando.
    for ctrl in tema["controles"]:
        titulo = f"{ctrl['id']} {ctrl['titulo']}"
        linhas.append(f"- [{titulo}](#{ancora(titulo)})")
    linhas.append("")

    for ctrl in tema["controles"]:
        linhas.append(f"## {ctrl['id']} {ctrl['titulo']}")
        linhas.append("")
        linhas.append(ctrl["objetivo"])
        linhas.append("")
        linhas.append("| Ferramenta | Licença | Por que serve aqui |")
        linhas.append("|---|---|---|")
        for f in ctrl["ferramentas"]:
            linhas.append(f"| [{f['nome']}]({f['url']}) | {f['licenca']} | {f['nota']} |")
        linhas.append("")
    return "\n".join(linhas)


def gerar_indice_ferramentas(doc):
    por_ferramenta = defaultdict(lambda: {"url": "", "licenca": "", "controles": []})
    for tema in doc["temas"]:
        for ctrl in tema["controles"]:
            for f in ctrl["ferramentas"]:
                reg = por_ferramenta[f["nome"]]
                reg["url"] = f["url"]
                reg["licenca"] = f["licenca"]
                reg["controles"].append(ctrl["id"])

    linhas = ["# Índice de ferramentas", "", AVISO, ""]
    linhas.append(
        "O caminho inverso: dada uma ferramenta, quais controles ela ajuda a\n"
        "atender. Útil para decidir o que implantar primeiro, já que algumas\n"
        "cobrem muita coisa de uma vez.")
    linhas.append("")
    linhas.append(f"{len(por_ferramenta)} ferramentas distintas.")
    linhas.append("")
    linhas.append("| Ferramenta | Licença | Controles | Quantos |")
    linhas.append("|---|---|---|---|")

    ordenado = sorted(por_ferramenta.items(),
                      key=lambda kv: (-len(kv[1]["controles"]), kv[0].lower()))
    for nome, reg in ordenado:
        ctrls = ", ".join(sorted(set(reg["controles"])))
        linhas.append(f"| [{nome}]({reg['url']}) | {reg['licenca']} | {ctrls} "
                      f"| {len(set(reg['controles']))} |")
    linhas.append("")
    return "\n".join(linhas), por_ferramenta


def main():
    doc = carregar()
    print("gerando:")
    for tema in doc["temas"]:
        escrever(os.path.join(RAIZ, "controles", ARQUIVOS[tema["id"]]),
                 gerar_tema(tema))

    indice, por_ferramenta = gerar_indice_ferramentas(doc)
    escrever(os.path.join(RAIZ, "ferramentas", "README.md"), indice)

    total = sum(len(t["controles"]) for t in doc["temas"])
    indic = sum(len(c["ferramentas"]) for t in doc["temas"] for c in t["controles"])
    print(f"\n{total} controles · {indic} indicações · "
          f"{len(por_ferramenta)} ferramentas distintas")


if __name__ == "__main__":
    main()
