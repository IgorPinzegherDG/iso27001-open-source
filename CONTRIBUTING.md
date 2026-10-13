# Como contribuir

## O que entra

Uma indicação é útil quando atende a tudo isto:

1. **É software livre ou de código aberto.** Se a licença não for reconhecida
   pela OSI, diga isso na coluna de licença, como foi feito com o Vault e o
   Graylog. Produto proprietário com camada gratuita não entra.
2. **O projeto está vivo.** Commit ou versão nos últimos doze meses.
3. **A relação com o controle é direta.** A coluna "por que serve aqui" precisa
   explicar o que a ferramenta resolve naquele controle específico, não o que
   ela faz em geral. "Monitora a rede" não diz nada; "mede disponibilidade real
   contra o acordo de nível de serviço" diz.
4. **O link responde.** `python3 scripts/validar_links.py` precisa passar.

## O que não entra

Texto da norma, mesmo parafraseado de perto. O repositório existe para indicar
ferramenta, não para substituir a ISO/IEC 27002. Se a descrição começar a
parecer tradução do guia de implementação, está fora do lugar.

Também não entram listas de "melhores ferramentas" sem vínculo com controle:
cada linha pertence a um controle específico.

## Como editar

Só `dados/controles.yaml`. Os arquivos em `controles/` e `ferramentas/` são
gerados e serão sobrescritos.

```bash
pip install pyyaml
# edite dados/controles.yaml
python3 scripts/gerar.py
python3 scripts/validar_links.py
```

Inclua no mesmo commit o YAML e os arquivos gerados.

## Estilo

Português do Brasil. Termo técnico consagrado fica em inglês (firewall, SIEM,
backup); o resto se traduz. Frase direta, sem adjetivo de propaganda: a nota
explica o que a ferramenta faz naquele controle, não que ela é excelente.
