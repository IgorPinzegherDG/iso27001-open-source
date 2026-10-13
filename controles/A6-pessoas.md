# A.6 Controles de pessoas

> Gerado por `scripts/gerar.py` a partir de `dados/controles.yaml`.
> Edite o YAML, não este arquivo.


> O texto normativo da ISO/IEC 27001 e da ISO/IEC 27002 é protegido por
> direitos autorais e **não é reproduzido aqui**. Os títulos servem apenas
> de referência e os objetivos são redação própria. Para implementar, use
> a norma adquirida da ABNT ou da ISO.


8 controles.

- [A.6.1 Seleção](#a61-seleção)
- [A.6.2 Termos e condições de contratação](#a62-termos-e-condições-de-contratação)
- [A.6.3 Conscientização, educação e treinamento](#a63-conscientização-educação-e-treinamento)
- [A.6.4 Processo disciplinar](#a64-processo-disciplinar)
- [A.6.5 Responsabilidades após encerramento ou mudança da contratação](#a65-responsabilidades-após-encerramento-ou-mudança-da-contratação)
- [A.6.6 Acordos de confidencialidade ou não divulgação](#a66-acordos-de-confidencialidade-ou-não-divulgação)
- [A.6.7 Trabalho remoto](#a67-trabalho-remoto)
- [A.6.8 Relato de eventos de segurança da informação](#a68-relato-de-eventos-de-segurança-da-informação)

## A.6.1 Seleção

Verificar antecedentes dos candidatos de forma proporcional ao risco do cargo.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OrangeHRM](https://www.orangehrm.com/) | GPL-2.0 | registra a etapa de verificação dentro do processo seletivo |
| [Odoo Recruitment](https://www.odoo.com/app/recruitment) | LGPL-3.0 | fluxo de seleção com checklist por vaga |

## A.6.2 Termos e condições de contratação

Estabelecer em contrato as responsabilidades de segurança do empregado e do contratante.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Documenso](https://documenso.com/) | AGPL-3.0 | assinatura com trilha de auditoria e carimbo de tempo |
| [Docuseal](https://www.docuseal.com/) | AGPL-3.0 | modelos reutilizáveis de termo |
| [OrangeHRM](https://www.orangehrm.com/) | GPL-2.0 | guarda do contrato vinculado ao colaborador |

## A.6.3 Conscientização, educação e treinamento

Treinar o pessoal e medir se a mensagem chegou, de forma periódica.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Moodle](https://github.com/moodle/moodle) | GPL-3.0 | trilhas, avaliação e certificado, que é a evidência de eficácia |
| [Open edX](https://openedx.org/) | AGPL-3.0 | alternativa para programa grande |
| [Gophish](https://getgophish.com/) | MIT | simulação de phishing que mede comportamento, não só presença |
| [Mattermost](https://mattermost.com/) | AGPL-3.0 | canal de campanhas e lembretes contínuos |

## A.6.4 Processo disciplinar

Ter processo formal e comunicado para tratar violações de segurança.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OrangeHRM](https://www.orangehrm.com/) | GPL-2.0 | registro de ocorrência disciplinar com histórico |
| [Zammad](https://zammad.com/) | AGPL-3.0 | fluxo com partes envolvidas e prazo, mantendo a confidencialidade |

## A.6.5 Responsabilidades após encerramento ou mudança da contratação

Definir e comunicar o que permanece válido depois da saída ou da mudança de função.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Apache Syncope](https://syncope.apache.org/) | Apache-2.0 | desprovisionamento automático em todos os sistemas no desligamento |
| [midPoint](https://evolveum.com/midpoint/) | Apache-2.0 | recalcula acessos quando a função muda, evitando acúmulo |
| [Snipe-IT](https://snipeitapp.com/) | AGPL-3.0 | pendências de ativo que bloqueiam o encerramento |

## A.6.6 Acordos de confidencialidade ou não divulgação

Manter acordos de confidencialidade identificados, assinados e revisados.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Documenso](https://documenso.com/) | AGPL-3.0 | assinatura e verificação posterior do documento |
| [Mayan EDMS](https://www.mayan-edms.com/) | Apache-2.0 | guarda com vencimento e alerta de renovação |

## A.6.7 Trabalho remoto

Proteger a informação acessada e processada fora das instalações.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [WireGuard](https://www.wireguard.com/) | GPL-2.0 | túnel simples e auditável, com chave por dispositivo |
| [OpenVPN](https://openvpn.net/community/) | GPL-2.0 | alternativa consolidada com certificado por usuário |
| [Teleport](https://goteleport.com/) | AGPL-3.0 | acesso a servidor e banco sem expor a rede inteira |
| [Headscale](https://headscale.net/) | BSD-3-Clause | painel de controle próprio para malha Tailscale |

## A.6.8 Relato de eventos de segurança da informação

Dar a todos um canal simples e conhecido para relatar evento ou suspeita.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Zammad](https://zammad.com/) | AGPL-3.0 | canal de relato com acompanhamento e prazo |
| [GLPI](https://glpi-project.org/) | GPL-3.0 | service desk que já existe na maioria das empresas |
| [TheHive](https://strangebee.com/thehive/) | AGPL-3.0 | recebe o relato e o transforma em caso quando procede |
