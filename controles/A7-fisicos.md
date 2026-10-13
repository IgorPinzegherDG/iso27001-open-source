# A.7 Controles físicos

> Gerado por `scripts/gerar.py` a partir de `dados/controles.yaml`.
> Edite o YAML, não este arquivo.


> O texto normativo da ISO/IEC 27001 e da ISO/IEC 27002 é protegido por
> direitos autorais e **não é reproduzido aqui**. Os títulos servem apenas
> de referência e os objetivos são redação própria. Para implementar, use
> a norma adquirida da ABNT ou da ISO.


14 controles.

- [A.7.1 Perímetros de segurança física](#a71-perímetros-de-segurança-física)
- [A.7.2 Entrada física](#a72-entrada-física)
- [A.7.3 Segurança de escritórios, salas e instalações](#a73-segurança-de-escritórios-salas-e-instalações)
- [A.7.4 Monitoramento de segurança física](#a74-monitoramento-de-segurança-física)
- [A.7.5 Proteção contra ameaças físicas e ambientais](#a75-proteção-contra-ameaças-físicas-e-ambientais)
- [A.7.6 Trabalho em áreas seguras](#a76-trabalho-em-áreas-seguras)
- [A.7.7 Mesa limpa e tela limpa](#a77-mesa-limpa-e-tela-limpa)
- [A.7.8 Localização e proteção de equipamentos](#a78-localização-e-proteção-de-equipamentos)
- [A.7.9 Segurança de ativos fora das instalações](#a79-segurança-de-ativos-fora-das-instalações)
- [A.7.10 Mídia de armazenamento](#a710-mídia-de-armazenamento)
- [A.7.11 Serviços de infraestrutura](#a711-serviços-de-infraestrutura)
- [A.7.12 Segurança do cabeamento](#a712-segurança-do-cabeamento)
- [A.7.13 Manutenção de equipamentos](#a713-manutenção-de-equipamentos)
- [A.7.14 Descarte ou reutilização segura de equipamentos](#a714-descarte-ou-reutilização-segura-de-equipamentos)

## A.7.1 Perímetros de segurança física

Definir perímetros que protejam as áreas com informação e ativos críticos.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [NetBox](https://netboxlabs.com/oss/netbox/) | Apache-2.0 | documenta sítios, salas e racks, que é a planta do perímetro |
| [Home Assistant](https://www.home-assistant.io/) | Apache-2.0 | integra sensores de abertura e alarme ao monitoramento |

## A.7.2 Entrada física

Controlar e registrar quem entra em cada área segura.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Access Control OS (OSDP/Wiegand)](https://github.com/goToMain/libosdp) | Apache-2.0 | biblioteca aberta para controladoras de acesso OSDP |
| [Home Assistant](https://www.home-assistant.io/) | Apache-2.0 | registra eventos de porta e integra com fechadura eletrônica |
| [GLPI](https://glpi-project.org/) | GPL-3.0 | registro de visitantes como chamado, quando não há catraca |

## A.7.3 Segurança de escritórios, salas e instalações

Projetar e aplicar segurança física para escritórios e salas.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [NetBox](https://netboxlabs.com/oss/netbox/) | Apache-2.0 | mantém a documentação do que existe em cada sala |
| [Home Assistant](https://www.home-assistant.io/) | Apache-2.0 | automação de alarme por horário e presença |

## A.7.4 Monitoramento de segurança física

Monitorar continuamente as instalações contra acesso não autorizado.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Frigate](https://frigate.video/) | MIT | CFTV com detecção de objeto local, sem enviar imagem para nuvem |
| [ZoneMinder](https://github.com/ZoneMinder/zoneminder) | GPL-2.0 | sistema de CFTV consolidado com retenção configurável |
| [Shinobi](https://shinobi.video/) | AGPL-3.0 | alternativa leve com API |
| [Viseron](https://viseron.netlify.app/) | MIT | NVR com detecção e retenção por evento |

## A.7.5 Proteção contra ameaças físicas e ambientais

Proteger contra incêndio, alagamento, falha de energia e eventos naturais.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Zabbix](https://www.zabbix.com/) | AGPL-3.0 | monitora sensores ambientais e dispara alerta |
| [Home Assistant](https://www.home-assistant.io/) | Apache-2.0 | integra sensor de fumaça, água e temperatura |
| [NUT (Network UPS Tools)](https://networkupstools.org/) | GPL-2.0 | monitora nobreak e desliga o ambiente com segurança |

## A.7.6 Trabalho em áreas seguras

Definir e aplicar regras para o trabalho dentro de áreas seguras.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Wiki.js](https://js.wiki/) | AGPL-3.0 | publica a regra da área e registra a ciência |
| [Frigate](https://frigate.video/) | MIT | verificação por vídeo do cumprimento da regra |

## A.7.7 Mesa limpa e tela limpa

Adotar e fazer cumprir a regra de mesa e tela limpas.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Ansible](https://www.ansible.com/) | GPL-3.0 | aplica bloqueio automático de tela em toda a frota |
| [osquery + Fleet](https://fleetdm.com/) | MIT | verifica se o bloqueio de tela está mesmo ativo em cada máquina |
| [Wazuh](https://wazuh.com/) | GPL-2.0 | monitora a política de tela como item de conformidade |

## A.7.8 Localização e proteção de equipamentos

Posicionar e proteger equipamentos conforme o risco do ambiente.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [NetBox](https://netboxlabs.com/oss/netbox/) | Apache-2.0 | posição exata em rack e unidade, com energia e cabeamento |
| [Snipe-IT](https://snipeitapp.com/) | AGPL-3.0 | localização do ativo e responsável |

## A.7.9 Segurança de ativos fora das instalações

Proteger ativos que saem das instalações, como notebooks e celulares.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [LUKS / cryptsetup](https://gitlab.com/cryptsetup/cryptsetup) | GPL-2.0 | cifra o disco inteiro, que é a única proteção real contra furto |
| [VeraCrypt](https://www.veracrypt.fr/) | Apache-2.0/TrueCrypt | alternativa multiplataforma |
| [Prey](https://github.com/prey/prey-node-client) | GPL-3.0 | rastreio e apagamento remoto de dispositivo |
| [Snipe-IT](https://snipeitapp.com/) | AGPL-3.0 | controle de quem está com o quê, fora do escritório |

## A.7.10 Mídia de armazenamento

Gerenciar mídias ao longo do ciclo de vida, da aquisição ao descarte.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Snipe-IT](https://snipeitapp.com/) | AGPL-3.0 | inventário de mídia com histórico de custódia |
| [Cryptomator](https://cryptomator.org/) | GPL-3.0 | cifra o conteúdo antes de gravar em mídia removível |
| [USBGuard](https://usbguard.github.io/) | GPL-2.0 | autoriza por regra quais dispositivos USB podem ser usados |

## A.7.11 Serviços de infraestrutura

Proteger as instalações contra falhas de energia e outros serviços de apoio.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [NUT (Network UPS Tools)](https://networkupstools.org/) | GPL-2.0 | gestão de nobreak com desligamento ordenado |
| [Zabbix](https://www.zabbix.com/) | AGPL-3.0 | alerta de falha de energia, clima e rede |
| [Prometheus + Grafana](https://prometheus.io/) | Apache-2.0 | séries históricas de consumo e temperatura |

## A.7.12 Segurança do cabeamento

Proteger cabos de energia e telecomunicações contra interceptação e dano.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [NetBox](https://netboxlabs.com/oss/netbox/) | Apache-2.0 | documenta cada cabo, porta e trajeto, inclusive o patch panel |
| [LibreNMS](https://www.librenms.org/) | GPL-3.0 | detecta mudança de porta e queda de enlace |

## A.7.13 Manutenção de equipamentos

Manter os equipamentos corretamente para preservar disponibilidade e integridade.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [GLPI](https://glpi-project.org/) | GPL-3.0 | plano de manutenção preventiva com histórico por ativo |
| [Snipe-IT](https://snipeitapp.com/) | AGPL-3.0 | registro de manutenção e garantia |
| [smartmontools](https://www.smartmontools.org/) | GPL-2.0 | antecipa falha de disco antes da perda |

## A.7.14 Descarte ou reutilização segura de equipamentos

Verificar que dados sensíveis foram removidos antes do descarte ou reuso.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [nwipe](https://github.com/martijnvanbrummelen/nwipe) | GPL-2.0 | apagamento seguro com relatório, que serve de evidência |
| [ShredOS](https://github.com/PartialVolume/shredos.x86_64) | GPL-2.0 | sistema inicializável dedicado ao apagamento em lote |
| [nvme-cli](https://github.com/linux-nvme/nvme-cli) | GPL-2.0 | apagamento pelo comando do próprio disco (format/sanitize), indicado para SSD NVMe |
| [Snipe-IT](https://snipeitapp.com/) | AGPL-3.0 | fecha o ciclo de vida do ativo com o registro do descarte |
