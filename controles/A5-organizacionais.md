# A.5 Controles organizacionais

> Gerado por `scripts/gerar.py` a partir de `dados/controles.yaml`.
> Edite o YAML, não este arquivo.


> O texto normativo da ISO/IEC 27001 e da ISO/IEC 27002 é protegido por
> direitos autorais e **não é reproduzido aqui**. Os títulos servem apenas
> de referência e os objetivos são redação própria. Para implementar, use
> a norma adquirida da ABNT ou da ISO.


37 controles.

- [A.5.1 Políticas de segurança da informação](#a51-políticas-de-segurança-da-informação)
- [A.5.2 Papéis e responsabilidades pela segurança da informação](#a52-papéis-e-responsabilidades-pela-segurança-da-informação)
- [A.5.3 Segregação de funções](#a53-segregação-de-funções)
- [A.5.4 Responsabilidades da direção](#a54-responsabilidades-da-direção)
- [A.5.5 Contato com autoridades](#a55-contato-com-autoridades)
- [A.5.6 Contato com grupos de interesse especial](#a56-contato-com-grupos-de-interesse-especial)
- [A.5.7 Inteligência de ameaças](#a57-inteligência-de-ameaças)
- [A.5.8 Segurança da informação na gestão de projetos](#a58-segurança-da-informação-na-gestão-de-projetos)
- [A.5.9 Inventário de informações e outros ativos associados](#a59-inventário-de-informações-e-outros-ativos-associados)
- [A.5.10 Uso aceitável de informações e outros ativos associados](#a510-uso-aceitável-de-informações-e-outros-ativos-associados)
- [A.5.11 Devolução de ativos](#a511-devolução-de-ativos)
- [A.5.12 Classificação da informação](#a512-classificação-da-informação)
- [A.5.13 Rotulagem de informações](#a513-rotulagem-de-informações)
- [A.5.14 Transferência de informações](#a514-transferência-de-informações)
- [A.5.15 Controle de acesso](#a515-controle-de-acesso)
- [A.5.16 Gestão de identidade](#a516-gestão-de-identidade)
- [A.5.17 Informação de autenticação](#a517-informação-de-autenticação)
- [A.5.18 Direitos de acesso](#a518-direitos-de-acesso)
- [A.5.19 Segurança da informação nas relações com fornecedores](#a519-segurança-da-informação-nas-relações-com-fornecedores)
- [A.5.20 Contemplar a segurança da informação nos acordos com fornecedores](#a520-contemplar-a-segurança-da-informação-nos-acordos-com-fornecedores)
- [A.5.21 Gestão da segurança da informação na cadeia de fornecimento de TIC](#a521-gestão-da-segurança-da-informação-na-cadeia-de-fornecimento-de-tic)
- [A.5.22 Monitoramento, análise crítica e gestão de mudanças dos serviços de fornecedores](#a522-monitoramento-análise-crítica-e-gestão-de-mudanças-dos-serviços-de-fornecedores)
- [A.5.23 Segurança da informação para uso de serviços em nuvem](#a523-segurança-da-informação-para-uso-de-serviços-em-nuvem)
- [A.5.24 Planejamento e preparação da gestão de incidentes](#a524-planejamento-e-preparação-da-gestão-de-incidentes)
- [A.5.25 Avaliação e decisão sobre eventos de segurança da informação](#a525-avaliação-e-decisão-sobre-eventos-de-segurança-da-informação)
- [A.5.26 Resposta a incidentes de segurança da informação](#a526-resposta-a-incidentes-de-segurança-da-informação)
- [A.5.27 Aprendizado com incidentes de segurança da informação](#a527-aprendizado-com-incidentes-de-segurança-da-informação)
- [A.5.28 Coleta de evidências](#a528-coleta-de-evidências)
- [A.5.29 Segurança da informação durante a disrupção](#a529-segurança-da-informação-durante-a-disrupção)
- [A.5.30 Prontidão de TIC para continuidade de negócios](#a530-prontidão-de-tic-para-continuidade-de-negócios)
- [A.5.31 Requisitos legais, estatutários, regulamentares e contratuais](#a531-requisitos-legais-estatutários-regulamentares-e-contratuais)
- [A.5.32 Direitos de propriedade intelectual](#a532-direitos-de-propriedade-intelectual)
- [A.5.33 Proteção de registros](#a533-proteção-de-registros)
- [A.5.34 Privacidade e proteção de dados pessoais](#a534-privacidade-e-proteção-de-dados-pessoais)
- [A.5.35 Análise crítica independente da segurança da informação](#a535-análise-crítica-independente-da-segurança-da-informação)
- [A.5.36 Conformidade com políticas, regras e normas de segurança](#a536-conformidade-com-políticas-regras-e-normas-de-segurança)
- [A.5.37 Procedimentos operacionais documentados](#a537-procedimentos-operacionais-documentados)

## A.5.1 Políticas de segurança da informação

Manter um conjunto de políticas aprovado pela direção, publicado para quem precisa cumprir e revisado em intervalos definidos.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Wiki.js](https://js.wiki/) | AGPL-3.0 | versiona a política, registra quem leu e quando, e mantém o histórico de revisão que o auditor pede |
| [BookStack](https://www.bookstackapp.com/) | MIT | alternativa mais simples, com organização por prateleira e livro |
| [Eramba Community](https://www.eramba.org/) | AGPL-3.0 | GRC que trata política como objeto com dono, ciclo de revisão e aceite registrado |
| [Outline](https://www.getoutline.com/) | BSL 1.1 (não OSI) | base de conhecimento com busca boa e permissão por coleção; licença não é livre, veja Wiki.js ou BookStack |

## A.5.2 Papéis e responsabilidades pela segurança da informação

Definir e atribuir formalmente quem responde por cada atividade de segurança.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Eramba Community](https://www.eramba.org/) | AGPL-3.0 | mantém matriz de responsabilidade ligada a políticas, riscos e controles |
| [SimpleRisk](https://www.simplerisk.com/) | MPL-2.0 | atribui dono a risco e a plano de tratamento |
| [OrangeHRM](https://www.orangehrm.com/) | GPL-2.0 | descrição de cargo e organograma, que é onde a responsabilidade formal costuma morar |

## A.5.3 Segregação de funções

Separar atividades conflitantes para que ninguém execute e aprove a mesma coisa sozinho.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Keycloak](https://www.keycloak.org/) | Apache-2.0 | papéis e grupos que permitem separar quem solicita de quem aprova |
| [Open Policy Agent](https://www.openpolicyagent.org/) | Apache-2.0 | escreve a regra de segregação como código e a aplica em pipeline e API |
| [Apache Syncope](https://syncope.apache.org/) | Apache-2.0 | governança de identidade com detecção de conflito de atribuição |

## A.5.4 Responsabilidades da direção

Assegurar que a direção exija de todos a aplicação da segurança conforme as políticas.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Eramba Community](https://www.eramba.org/) | AGPL-3.0 | registra aceite de política por colaborador, que é a evidência de cobrança |
| [Documenso](https://documenso.com/) | AGPL-3.0 | assinatura eletrônica de termos e políticas com trilha de auditoria |

## A.5.5 Contato com autoridades

Manter canais definidos com autoridades competentes, acionáveis em incidente.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [TheHive](https://strangebee.com/thehive/) | AGPL-3.0 | caso de incidente com tarefas que incluem a notificação à autoridade e o prazo |
| [Zammad](https://zammad.com/) | AGPL-3.0 | registra o contato e a resposta como ticket rastreável |

## A.5.6 Contato com grupos de interesse especial

Participar de fóruns e comunidades técnicas para acompanhar ameaças e boas práticas.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [MISP](https://www.misp-project.org/) | AGPL-3.0 | participação em comunidades de compartilhamento é o próprio contato previsto |
| [OpenCTI](https://filigran.io/solutions/open-cti/) | Apache-2.0 | conecta a feeds e comunidades e documenta a origem de cada informação |

## A.5.7 Inteligência de ameaças

Coletar e analisar informação sobre ameaças e transformá-la em ação.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OpenCTI](https://filigran.io/solutions/open-cti/) | Apache-2.0 | plataforma de inteligência com modelo STIX e ligação entre ator, técnica e indicador |
| [MISP](https://www.misp-project.org/) | AGPL-3.0 | compartilhamento de indicadores e correlação automática |
| [Yeti](https://yeti-platform.github.io/) | Apache-2.0 | mais leve, bom para começar |

## A.5.8 Segurança da informação na gestão de projetos

Tratar requisitos de segurança dentro do ciclo de qualquer projeto, não depois dele.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OpenProject](https://www.openproject.org/) | GPL-3.0 | modelo de projeto com fases e entregas obrigatórias de segurança |
| [Redmine](https://www.redmine.org/) | GPL-2.0 | fluxo configurável com campo de avaliação de risco por projeto |
| [Taiga](https://taiga.io/) | MPL-2.0 | ágil, com critério de pronto que inclui segurança |

## A.5.9 Inventário de informações e outros ativos associados

Manter inventário de ativos com dono identificado.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Snipe-IT](https://snipeitapp.com/) | AGPL-3.0 | inventário com responsável, ciclo de vida e termo de responsabilidade |
| [GLPI](https://glpi-project.org/) | GPL-3.0 | inventário com descoberta automática de rede e vínculo a chamados |
| [NetBox](https://netboxlabs.com/oss/netbox/) | Apache-2.0 | fonte de verdade de infraestrutura, endereçamento e racks |
| [osquery](https://www.osquery.io/) | Apache-2.0/GPL-2.0 | levanta software e hardware da frota por consulta SQL |
| [Fleet](https://fleetdm.com/) | MIT (núcleo; o diretório ee/ é comercial) | servidor para o osquery em escala, com política por máquina e relatório de desvio |

## A.5.10 Uso aceitável de informações e outros ativos associados

Definir e comunicar as regras de uso dos ativos, com aceite registrado.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Documenso](https://documenso.com/) | AGPL-3.0 | coleta aceite assinado da política de uso |
| [Wiki.js](https://js.wiki/) | AGPL-3.0 | publica a regra vigente com histórico |
| [Snipe-IT](https://snipeitapp.com/) | AGPL-3.0 | vincula o aceite ao ativo entregue à pessoa |

## A.5.11 Devolução de ativos

Garantir a devolução dos ativos no encerramento do vínculo ou contrato.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Snipe-IT](https://snipeitapp.com/) | AGPL-3.0 | check-in e check-out por pessoa, com pendências visíveis no desligamento |
| [GLPI](https://glpi-project.org/) | GPL-3.0 | mesma função dentro de um service desk |

## A.5.12 Classificação da informação

Classificar a informação conforme valor, criticidade e requisitos legais.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Apache Tika](https://tika.apache.org/) | Apache-2.0 | extrai conteúdo para apoiar a classificação automática |
| [OpenMetadata](https://open-metadata.org/) | Apache-2.0 | catálogo de dados com rótulo de sensibilidade e linhagem |
| [DataHub](https://datahubproject.io/) | Apache-2.0 | alternativa com governança e glossário de termos |

## A.5.13 Rotulagem de informações

Aplicar rótulos coerentes com o esquema de classificação adotado.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Mayan EDMS](https://www.mayan-edms.com/) | Apache-2.0 | gestão documental com metadados e rótulo obrigatório |
| [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | GPL-3.0 | etiquetagem automática de documentos digitalizados |
| [OpenMetadata](https://open-metadata.org/) | Apache-2.0 | rotula coluna e tabela em base de dados |

## A.5.14 Transferência de informações

Proteger a informação em trânsito, por qualquer meio e com qualquer parte.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Nextcloud](https://nextcloud.com/) | AGPL-3.0 | compartilhamento com validade, senha e registro de acesso |
| [Lufi](https://framagit.org/fiat-tux/hat-and-coat/lufi) | AGPL-3.0 | envio de arquivo com criptografia no navegador |
| [age](https://github.com/FiloSottile/age) | BSD-3-Clause | criptografia de arquivo simples, boa para troca pontual |
| [Mattermost](https://mattermost.com/) | AGPL-3.0/Apache-2.0 | mensageria interna sob seu controle, com retenção definida |

## A.5.15 Controle de acesso

Estabelecer e aplicar regras de acesso físico e lógico com base no negócio.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Keycloak](https://www.keycloak.org/) | Apache-2.0 | autenticação e autorização centralizadas com SSO |
| [Authentik](https://goauthentik.io/) | MIT | IdP moderno com fluxo de autorização visual |
| [FreeIPA](https://www.freeipa.org/) | GPL-3.0 | identidade e política de acesso para frota Linux |
| [Open Policy Agent](https://www.openpolicyagent.org/) | Apache-2.0 | decisão de autorização como código |

## A.5.16 Gestão de identidade

Gerenciar o ciclo de vida completo das identidades, da criação à remoção.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Keycloak](https://www.keycloak.org/) | Apache-2.0 | diretório de identidades com federação |
| [Apache Syncope](https://syncope.apache.org/) | Apache-2.0 | provisionamento e desprovisionamento automático entre sistemas |
| [midPoint](https://evolveum.com/midpoint/) | Apache-2.0 | governança de identidade com recertificação de acesso |

## A.5.17 Informação de autenticação

Controlar a alocação e o uso de senhas, chaves e outros segredos de autenticação.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Vaultwarden](https://github.com/dani-garcia/vaultwarden) | AGPL-3.0 | cofre de senhas corporativo leve, compatível com clientes Bitwarden |
| [Passbolt](https://www.passbolt.com/) | AGPL-3.0 | cofre com compartilhamento por grupo e trilha de auditoria |
| [HashiCorp Vault](https://github.com/hashicorp/vault) | BUSL-1.1 (não OSI) | segredos com rotação; a licença deixou de ser livre em 2023, prefira o OpenBao |
| [OpenBao](https://openbao.org/) | MPL-2.0 | derivação do Vault mantida pela Linux Foundation |
| [privacyIDEA](https://privacyidea.org/) | AGPL-3.0 | segundo fator com token físico ou OTP |

## A.5.18 Direitos de acesso

Conceder, revisar e revogar direitos de acesso ao longo do tempo.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [midPoint](https://evolveum.com/midpoint/) | Apache-2.0 | campanha de recertificação periódica, que é a evidência da análise crítica |
| [Keycloak](https://www.keycloak.org/) | Apache-2.0 | revogação central e imediata |
| [Teleport](https://goteleport.com/) | AGPL-3.0 | acesso a servidor e banco com aprovação e expiração automática |

## A.5.19 Segurança da informação nas relações com fornecedores

Definir e aplicar requisitos de segurança para o relacionamento com fornecedores.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Eramba Community](https://www.eramba.org/) | AGPL-3.0 | cadastro de terceiro com risco, contrato e revisão periódica |
| [SimpleRisk](https://www.simplerisk.com/) | MPL-2.0 | avaliação de risco de fornecedor |
| [GLPI](https://glpi-project.org/) | GPL-3.0 | contratos e fornecedores ligados aos ativos que eles sustentam |

## A.5.20 Contemplar a segurança da informação nos acordos com fornecedores

Levar os requisitos de segurança para dentro do contrato assinado.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Documenso](https://documenso.com/) | AGPL-3.0 | assinatura com trilha de auditoria e versão do anexo de segurança |
| [Docuseal](https://www.docuseal.com/) | AGPL-3.0 | alternativa com modelos reutilizáveis |
| [Mayan EDMS](https://www.mayan-edms.com/) | Apache-2.0 | guarda contratual com vencimento e lembrete |

## A.5.21 Gestão da segurança da informação na cadeia de fornecimento de TIC

Tratar o risco que entra pela cadeia de produtos e serviços de TIC.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Syft](https://github.com/anchore/syft) | Apache-2.0 | gera SBOM do que você consome de terceiros |
| [Grype](https://github.com/anchore/grype) | Apache-2.0 | cruza o SBOM com vulnerabilidades conhecidas |
| [Dependency-Track](https://dependencytrack.org/) | Apache-2.0 | monitora continuamente os componentes de todo o portfólio |
| [Sigstore Cosign](https://www.sigstore.dev/) | Apache-2.0 | assina e verifica artefato, fechando a porta da adulteração |

## A.5.22 Monitoramento, análise crítica e gestão de mudanças dos serviços de fornecedores

Acompanhar a entrega do fornecedor e avaliar mudanças no serviço.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Zabbix](https://www.zabbix.com/) | AGPL-3.0 | mede disponibilidade real contra o acordo de nível de serviço |
| [Uptime Kuma](https://github.com/louislam/uptime-kuma) | MIT | verificação simples de disponibilidade com histórico |
| [Eramba Community](https://www.eramba.org/) | AGPL-3.0 | agenda e registra a análise crítica periódica do fornecedor |

## A.5.23 Segurança da informação para uso de serviços em nuvem

Definir regras para aquisição, uso, gestão e saída de serviços em nuvem.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Prowler](https://github.com/prowler-cloud/prowler) | Apache-2.0 | avalia postura em AWS, Azure, GCP e Kubernetes contra referências conhecidas |
| [ScoutSuite](https://github.com/nccgroup/ScoutSuite) | GPL-2.0 | auditoria multinuvem com relatório navegável |
| [CloudQuery](https://www.cloudquery.io/) | MPL-2.0 | extrai o inventário da nuvem para SQL e permite consulta própria |
| [Steampipe](https://steampipe.io/) | AGPL-3.0 | consulta a nuvem como se fosse banco de dados |

## A.5.24 Planejamento e preparação da gestão de incidentes

Planejar o processo de resposta antes do incidente, com papéis e procedimentos.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [TheHive](https://strangebee.com/thehive/) | AGPL-3.0 | modelos de caso que já trazem as tarefas e os responsáveis |
| [IRIS](https://dfir-iris.org/) | LGPL-3.0 | plataforma colaborativa de resposta com linha do tempo |
| [Shuffle](https://shuffler.io/) | AGPL-3.0 | automação (SOAR) para padronizar os primeiros passos |

## A.5.25 Avaliação e decisão sobre eventos de segurança da informação

Classificar o que é evento e o que vira incidente, com critério definido.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Wazuh](https://wazuh.com/) | GPL-2.0 | gera e pontua alertas a partir de logs e agentes |
| [TheHive + Cortex](https://strangebee.com/) | AGPL-3.0 | triagem com enriquecimento automático do indicador |
| [Graylog](https://graylog.org/) | SSPL/GPL-3.0 | centraliza e correlaciona para separar ruído de evento |

## A.5.26 Resposta a incidentes de segurança da informação

Responder ao incidente conforme o procedimento, registrando cada passo.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [TheHive](https://strangebee.com/thehive/) | AGPL-3.0 | condução do caso com registro do que foi feito e por quem |
| [Velociraptor](https://docs.velociraptor.app/) | AGPL-3.0 | coleta e caça em endpoint durante a resposta |
| [GRR Rapid Response](https://github.com/google/grr) | Apache-2.0 | resposta remota em escala |

## A.5.27 Aprendizado com incidentes de segurança da informação

Usar o que foi aprendido para reduzir a probabilidade ou o impacto futuro.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [IRIS](https://dfir-iris.org/) | LGPL-3.0 | guarda o caso completo e permite revisão posterior |
| [Wiki.js](https://js.wiki/) | AGPL-3.0 | base de lições aprendidas pesquisável |
| [Eramba Community](https://www.eramba.org/) | AGPL-3.0 | liga o incidente ao risco e ao controle que falhou |

## A.5.28 Coleta de evidências

Preservar evidências de forma que mantenham valor probatório.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Velociraptor](https://docs.velociraptor.app/) | AGPL-3.0 | coleta forense remota preservando metadados |
| [Autopsy](https://www.autopsy.com/) | Apache-2.0 | análise forense com cadeia de custódia |
| [dcfldd](https://github.com/resurrecting-open-source-projects/dcfldd) | GPL-2.0 | imagem bit a bit com soma de verificação durante a cópia |
| [Plaso](https://plaso.readthedocs.io/) | Apache-2.0 | linha do tempo forense a partir de múltiplas fontes |

## A.5.29 Segurança da informação durante a disrupção

Manter a segurança no nível adequado também durante a crise.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Proxmox VE](https://www.proxmox.com/) | AGPL-3.0 | alta disponibilidade e replicação de máquinas virtuais |
| [Keepalived](https://www.keepalived.org/) | GPL-2.0 | failover de serviço sem perder o controle de acesso |
| [Restic](https://restic.net/) | BSD-2-Clause | backup cifrado que continua válido durante a contingência |

## A.5.30 Prontidão de TIC para continuidade de negócios

Planejar, implementar e testar a prontidão da TIC frente aos objetivos de continuidade.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Velero](https://velero.io/) | Apache-2.0 | backup e restauração de cluster Kubernetes, com teste de restauração |
| [Bacula](https://www.bacula.org/) | AGPL-3.0 | backup corporativo com agendamento e verificação |
| [Proxmox Backup Server](https://www.proxmox.com/proxmox-backup-server) | AGPL-3.0 | backup incremental com verificação de integridade |
| [Ansible](https://www.ansible.com/) | GPL-3.0 | reconstrução reproduzível do ambiente, que é o que faz o plano funcionar |

## A.5.31 Requisitos legais, estatutários, regulamentares e contratuais

Identificar e manter atualizados os requisitos aplicáveis e como atendê-los.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Eramba Community](https://www.eramba.org/) | AGPL-3.0 | registro de obrigações legais ligado a controles e evidências |
| [SimpleRisk](https://www.simplerisk.com/) | MPL-2.0 | mapeia requisito para controle |
| [OpenRegulatory](https://openregulatory.com/) | variável | modelos abertos de documentação regulatória |

## A.5.32 Direitos de propriedade intelectual

Proteger a propriedade intelectual própria e de terceiros, inclusive licenças de software.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [FOSSology](https://www.fossology.org/) | GPL-2.0 | varre o código e identifica licenças de terceiros |
| [ScanCode Toolkit](https://github.com/aboutcode-org/scancode-toolkit) | Apache-2.0 | detecção detalhada de licença e origem |
| [Syft](https://github.com/anchore/syft) | Apache-2.0 | SBOM que já traz a licença de cada componente |
| [Snipe-IT](https://snipeitapp.com/) | AGPL-3.0 | controle de licenças de software adquiridas |

## A.5.33 Proteção de registros

Proteger registros contra perda, destruição, falsificação e acesso indevido.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Mayan EDMS](https://www.mayan-edms.com/) | Apache-2.0 | gestão documental com retenção e permissão por documento |
| [MinIO](https://min.io/) | AGPL-3.0 | armazenamento de objetos com bloqueio de objeto (WORM) |
| [Restic](https://restic.net/) | BSD-2-Clause | cópias cifradas e verificáveis |
| [Chronicle / rsyslog com assinatura](https://www.rsyslog.com/) | GPL-3.0 | registro de log com assinatura e selo de tempo |

## A.5.34 Privacidade e proteção de dados pessoais

Atender aos requisitos de privacidade aplicáveis, como a LGPD.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Matomo](https://matomo.org/) | GPL-3.0 | analítica web autogerida, sem enviar dado de visitante a terceiro |
| [Microsoft Presidio](https://microsoft.github.io/presidio/) | MIT | identifica e anonimiza dados pessoais em texto e imagem |
| [OpenMetadata](https://open-metadata.org/) | Apache-2.0 | mapeia onde o dado pessoal está, que é o pré-requisito do resto |
| [Consent Manager (Klaro)](https://klaro.org/) | BSD-3-Clause | gestão de consentimento de cookies no site |

## A.5.35 Análise crítica independente da segurança da informação

Submeter a segurança a análise independente em intervalos planejados.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OpenSCAP](https://www.open-scap.org/) | LGPL-2.1 | avaliação técnica automatizada e repetível contra referência |
| [Lynis](https://cisofy.com/lynis/) | GPL-3.0 | auditoria de hardening de sistema com relatório |
| [Prowler](https://github.com/prowler-cloud/prowler) | Apache-2.0 | avaliação independente da postura em nuvem |

## A.5.36 Conformidade com políticas, regras e normas de segurança

Verificar regularmente se o que está escrito é o que acontece.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OpenSCAP](https://www.open-scap.org/) | LGPL-2.1 | mede a aderência técnica à norma interna |
| [osquery](https://www.osquery.io/) | Apache-2.0/GPL-2.0 | consulta a frota inteira e mostra o desvio por máquina |
| [Fleet](https://fleetdm.com/) | MIT (núcleo; o diretório ee/ é comercial) | servidor para o osquery em escala, com política por máquina e relatório de desvio |
| [Wazuh](https://wazuh.com/) | GPL-2.0 | monitora conformidade de configuração continuamente |

## A.5.37 Procedimentos operacionais documentados

Documentar os procedimentos e disponibilizá-los a quem precisa executá-los.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [BookStack](https://www.bookstackapp.com/) | MIT | procedimento organizado e pesquisável |
| [Wiki.js](https://js.wiki/) | AGPL-3.0 | com versionamento em Git, que dá rastreabilidade de alteração |
| [Ansible](https://www.ansible.com/) | GPL-3.0 | o procedimento vira código executável, eliminando a diferença entre o escrito e o feito |
| [Outline](https://www.getoutline.com/) | BSL 1.1 (não OSI) | base de conhecimento com busca boa e permissão por coleção; licença não é livre, veja Wiki.js ou BookStack |
