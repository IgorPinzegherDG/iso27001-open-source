# ISO/IEC 27001 com ferramentas open source

Para cada um dos **93 controles do Anexo A da ISO/IEC 27001:2022**, uma ou
mais ferramentas de código aberto que ajudam a implementá-lo, com a licença de
cada uma e uma frase sobre por que ela serve naquele ponto.

São **311 indicações** cobrindo **177 ferramentas distintas**, todas com link
verificado.

| Tema | Controles | Arquivo |
|---|---|---|
| A.5 Organizacionais | 37 | [controles/A5-organizacionais.md](controles/A5-organizacionais.md) |
| A.6 Pessoas | 8 | [controles/A6-pessoas.md](controles/A6-pessoas.md) |
| A.7 Físicos | 14 | [controles/A7-fisicos.md](controles/A7-fisicos.md) |
| A.8 Tecnológicos | 34 | [controles/A8-tecnologicos.md](controles/A8-tecnologicos.md) |

Há também o [índice invertido](ferramentas/README.md): dada uma ferramenta,
quais controles ela ajuda a atender.

## Leia isto antes de usar

**Ferramenta não dá conformidade.** A certificação avalia um sistema de gestão:
contexto, liderança, análise de risco, competência, operação, avaliação de
desempenho e melhoria. Ferramenta é apoio à operação de um controle e à
produção de evidência. Implantar as 177 e não ter processo não aproxima
ninguém de um certificado; ter processo maduro e nenhuma dessas ferramentas é
perfeitamente possível.

**O Anexo A não é uma lista de obrigações.** Os controles aplicáveis saem da
sua análise de risco e ficam registrados na Declaração de Aplicabilidade. Um
controle pode ser justificadamente excluído.

**O texto da norma não está aqui.** O conteúdo da ISO/IEC 27001 e da
ISO/IEC 27002 é protegido por direitos autorais. Este repositório traz o
identificador do controle, um título curto de referência e um objetivo escrito
por mim, nunca o texto normativo. Para implementar de fato, adquira a norma
pela [ABNT](https://www.abntcatalogo.com.br/) ou pela
[ISO](https://www.iso.org/standard/27001).

## Por onde começar

Algumas ferramentas aparecem em muitos controles, então rendem mais no início:

| Ferramenta | Controles | O que resolve de uma vez |
|---|---|---|
| [Snipe-IT](https://snipeitapp.com/) | 10 | inventário de ativos, responsável, devolução e descarte |
| [Wazuh](https://wazuh.com/) | 8 | registro, monitoramento, malware, integridade e conformidade técnica |
| [Keycloak](https://www.keycloak.org/) | 7 | identidade, acesso, autenticação e segregação de funções |
| [GLPI](https://glpi-project.org/) | 7 | inventário, chamados, mudanças e manutenção |
| [Eramba Community](https://www.eramba.org/) | 7 | política, risco, fornecedor e obrigação legal |
| [Zabbix](https://www.zabbix.com/) | 6 | capacidade, ambiente físico, disponibilidade e nível de serviço |

## Sobre as licenças

A licença de cada ferramenta está na tabela, porque ela muda o que você pode
fazer. Duas observações:

O **HashiCorp Vault** aparece marcado como `BUSL-1.1 (não OSI)`: a licença
deixou de ser livre em 2023. O [OpenBao](https://openbao.org/) é a derivação
mantida pela Linux Foundation e é a recomendação quando a licença importa.

O **Graylog** usa SSPL em parte do produto e o **Outline** usa BSL 1.1,
licenças que a Open Source Initiative não reconhece como livres. Os dois estão
no catálogo pela utilidade, com a ressalva registrada e, no caso do Outline,
com [Wiki.js](https://js.wiki/) e [BookStack](https://www.bookstackapp.com/)
indicados como equivalentes livres.

O **Fleet** é de licença mista: o núcleo é MIT e o diretório `ee/` é comercial.
Para o uso previsto aqui, o núcleo basta.

## Estrutura

```
dados/controles.yaml      fonte de verdade, único arquivo a editar
controles/*.md            gerado
ferramentas/README.md     gerado
scripts/gerar.py          regenera a documentação a partir do YAML
scripts/validar_links.py  verifica se todas as URLs respondem
```

```bash
pip install pyyaml
python3 scripts/gerar.py
python3 scripts/validar_links.py
```

A verificação automática desses dois passos está pronta em
[ci/validar.yml](ci/validar.yml), à espera de ser movida para
`.github/workflows/`. O [ci/README.md](ci/README.md) explica.

## Contribuindo

Correções e novas indicações são bem-vindas, principalmente para os controles
físicos (A.7), onde a oferta de software livre é naturalmente mais escassa, e
para alternativas brasileiras. Veja [CONTRIBUTING.md](CONTRIBUTING.md).

## Licença

O conteúdo deste repositório está sob
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br) e os
scripts sob [MIT](LICENSE). Cada ferramenta citada mantém a própria licença.
