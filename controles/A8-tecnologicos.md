# A.8 Controles tecnológicos

> Gerado por `scripts/gerar.py` a partir de `dados/controles.yaml`.
> Edite o YAML, não este arquivo.


> O texto normativo da ISO/IEC 27001 e da ISO/IEC 27002 é protegido por
> direitos autorais e **não é reproduzido aqui**. Os títulos servem apenas
> de referência e os objetivos são redação própria. Para implementar, use
> a norma adquirida da ABNT ou da ISO.


34 controles.

- [A.8.1 Dispositivos endpoint do usuário](#a81-dispositivos-endpoint-do-usuário)
- [A.8.2 Direitos de acesso privilegiado](#a82-direitos-de-acesso-privilegiado)
- [A.8.3 Restrição de acesso à informação](#a83-restrição-de-acesso-à-informação)
- [A.8.4 Acesso ao código-fonte](#a84-acesso-ao-código-fonte)
- [A.8.5 Autenticação segura](#a85-autenticação-segura)
- [A.8.6 Gestão de capacidade](#a86-gestão-de-capacidade)
- [A.8.7 Proteção contra malware](#a87-proteção-contra-malware)
- [A.8.8 Gestão de vulnerabilidades técnicas](#a88-gestão-de-vulnerabilidades-técnicas)
- [A.8.9 Gestão de configuração](#a89-gestão-de-configuração)
- [A.8.10 Exclusão de informações](#a810-exclusão-de-informações)
- [A.8.11 Mascaramento de dados](#a811-mascaramento-de-dados)
- [A.8.12 Prevenção de vazamento de dados](#a812-prevenção-de-vazamento-de-dados)
- [A.8.13 Backup das informações](#a813-backup-das-informações)
- [A.8.14 Redundância dos recursos de tratamento de informações](#a814-redundância-dos-recursos-de-tratamento-de-informações)
- [A.8.15 Registro](#a815-registro)
- [A.8.16 Atividades de monitoramento](#a816-atividades-de-monitoramento)
- [A.8.17 Sincronização do relógio](#a817-sincronização-do-relógio)
- [A.8.18 Uso de programas utilitários privilegiados](#a818-uso-de-programas-utilitários-privilegiados)
- [A.8.19 Instalação de software em sistemas operacionais](#a819-instalação-de-software-em-sistemas-operacionais)
- [A.8.20 Segurança de redes](#a820-segurança-de-redes)
- [A.8.21 Segurança dos serviços de rede](#a821-segurança-dos-serviços-de-rede)
- [A.8.22 Segregação de redes](#a822-segregação-de-redes)
- [A.8.23 Filtragem da web](#a823-filtragem-da-web)
- [A.8.24 Uso de criptografia](#a824-uso-de-criptografia)
- [A.8.25 Ciclo de vida de desenvolvimento seguro](#a825-ciclo-de-vida-de-desenvolvimento-seguro)
- [A.8.26 Requisitos de segurança da aplicação](#a826-requisitos-de-segurança-da-aplicação)
- [A.8.27 Princípios de arquitetura e engenharia de sistemas seguros](#a827-princípios-de-arquitetura-e-engenharia-de-sistemas-seguros)
- [A.8.28 Codificação segura](#a828-codificação-segura)
- [A.8.29 Testes de segurança em desenvolvimento e aceitação](#a829-testes-de-segurança-em-desenvolvimento-e-aceitação)
- [A.8.30 Desenvolvimento terceirizado](#a830-desenvolvimento-terceirizado)
- [A.8.31 Separação dos ambientes de desenvolvimento, teste e produção](#a831-separação-dos-ambientes-de-desenvolvimento-teste-e-produção)
- [A.8.32 Gestão de mudanças](#a832-gestão-de-mudanças)
- [A.8.33 Informações de teste](#a833-informações-de-teste)
- [A.8.34 Proteção de sistemas de informação durante os testes de auditoria](#a834-proteção-de-sistemas-de-informação-durante-os-testes-de-auditoria)

## A.8.1 Dispositivos endpoint do usuário

Proteger a informação armazenada ou acessada pelos dispositivos dos usuários.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Wazuh](https://wazuh.com/) | GPL-2.0 | agente em cada estação com detecção, inventário e conformidade |
| [osquery + Fleet](https://fleetdm.com/) | MIT | visibilidade da frota por consulta SQL |
| [LUKS / cryptsetup](https://gitlab.com/cryptsetup/cryptsetup) | GPL-2.0 | cifra de disco |
| [USBGuard](https://usbguard.github.io/) | GPL-2.0 | controle de dispositivos removíveis |

## A.8.2 Direitos de acesso privilegiado

Restringir e controlar de perto a atribuição e o uso de privilégios.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Teleport](https://goteleport.com/) | AGPL-3.0 | acesso privilegiado com gravação de sessão e aprovação prévia |
| [sudo com registro em I/O](https://www.sudo.ws/) | ISC | registra o que foi executado como root |
| [FreeIPA](https://www.freeipa.org/) | GPL-3.0 | política de sudo centralizada por host e grupo |

## A.8.3 Restrição de acesso à informação

Restringir acesso conforme a política de controle de acesso definida.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Open Policy Agent](https://www.openpolicyagent.org/) | Apache-2.0 | autorização fina como código, auditável |
| [Cerbos](https://www.cerbos.dev/) | Apache-2.0 | autorização desacoplada da aplicação |
| [Keycloak](https://www.keycloak.org/) | Apache-2.0 | escopos e papéis aplicados na borda |

## A.8.4 Acesso ao código-fonte

Controlar leitura e escrita do código-fonte e das ferramentas de desenvolvimento.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Gitea](https://about.gitea.com/) | MIT | hospedagem própria com permissão por repositório e branch |
| [Forgejo](https://forgejo.org/) | MIT/GPL-3.0 | derivação comunitária do Gitea |
| [GitLab CE](https://gitlab.com/gitlab-org/gitlab-foss) | MIT | regras de proteção de branch e aprovação obrigatória |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | MIT | impede que segredo entre no repositório |

## A.8.5 Autenticação segura

Implementar autenticação conforme a restrição e a política de acesso.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Keycloak](https://www.keycloak.org/) | Apache-2.0 | MFA, políticas de senha e federação |
| [Authentik](https://goauthentik.io/) | MIT | fluxos de autenticação configuráveis, incluindo WebAuthn |
| [privacyIDEA](https://privacyidea.org/) | AGPL-3.0 | segundo fator com diversos tipos de token |
| [SSSD](https://sssd.io/) | GPL-3.0 | autenticação integrada em frota Linux |

## A.8.6 Gestão de capacidade

Monitorar e ajustar o uso de recursos conforme a necessidade futura.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Prometheus + Grafana](https://prometheus.io/) | Apache-2.0 | métricas com histórico e previsão de saturação |
| [Zabbix](https://www.zabbix.com/) | AGPL-3.0 | monitoramento com limiar e tendência |
| [Netdata](https://www.netdata.cloud/) | GPL-3.0 | alta resolução por segundo, útil para diagnóstico |

## A.8.7 Proteção contra malware

Implementar proteção contra malware apoiada em conscientização do usuário.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [ClamAV](https://www.clamav.net/) | GPL-2.0 | antivírus de arquivo e gateway de e-mail |
| [Wazuh](https://wazuh.com/) | GPL-2.0 | detecção por comportamento e integridade de arquivo |
| [YARA](https://virustotal.github.io/yara/) | BSD-3-Clause | regras de identificação de família de malware |
| [Falco](https://falco.org/) | Apache-2.0 | detecta comportamento anômalo em contêiner em tempo de execução |

## A.8.8 Gestão de vulnerabilidades técnicas

Obter informação sobre vulnerabilidades, avaliar a exposição e tratar.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OpenVAS / Greenbone](https://www.greenbone.net/) | GPL-2.0 | varredura de rede com base de testes mantida |
| [Trivy](https://trivy.dev/) | Apache-2.0 | imagem, sistema de arquivos, repositório e infraestrutura como código |
| [Grype](https://github.com/anchore/grype) | Apache-2.0 | vulnerabilidade a partir do SBOM |
| [DefectDojo](https://www.defectdojo.org/) | BSD-3-Clause | consolida o achado de várias ferramentas e controla o tratamento |
| [Nuclei](https://github.com/projectdiscovery/nuclei) | MIT | verificação por modelo, boa para confirmar exposição |

## A.8.9 Gestão de configuração

Estabelecer, documentar, aplicar e monitorar configurações seguras.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Ansible](https://www.ansible.com/) | GPL-3.0 | configuração declarada em código e reaplicável |
| [OpenSCAP](https://www.open-scap.org/) | LGPL-2.1 | verifica e corrige desvio contra referência de hardening |
| [OpenTofu](https://opentofu.org/) | MPL-2.0 | infraestrutura como código, derivação aberta do Terraform |
| [Rudder](https://www.rudder.io/) | GPL-3.0 | conformidade contínua de configuração com painel |

## A.8.10 Exclusão de informações

Excluir informação quando não for mais necessária.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [nwipe](https://github.com/martijnvanbrummelen/nwipe) | GPL-2.0 | apagamento com relatório |
| [Mayan EDMS](https://www.mayan-edms.com/) | Apache-2.0 | política de retenção que dispara o descarte |
| [GNU coreutils (shred)](https://www.gnu.org/software/coreutils/) | GPL-3.0 | sobrescrita de arquivo; em sistema com journaling, prefira apagar a chave de cifra |

## A.8.11 Mascaramento de dados

Mascarar dados conforme a política de controle de acesso e os requisitos aplicáveis.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Microsoft Presidio](https://microsoft.github.io/presidio/) | MIT | identifica e anonimiza dado pessoal em texto, imagem e estrutura |
| [PostgreSQL Anonymizer](https://postgresql-anonymizer.readthedocs.io/) | PostgreSQL | mascaramento dentro do próprio banco |
| [ARX](https://arx.deidentifier.org/) | Apache-2.0 | anonimização com medição de risco de reidentificação |

## A.8.12 Prevenção de vazamento de dados

Aplicar medidas para prevenir a extração indevida de informação.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OpenDLP](https://github.com/ezarko/opendlp) | GPL-3.0 | varredura de dado sensível em repouso |
| [Wazuh](https://wazuh.com/) | GPL-2.0 | detecta exfiltração por regra e integridade de arquivo |
| [Zeek](https://zeek.org/) | BSD-3-Clause | análise de tráfego que revela transferência anômala |
| [Gitleaks / TruffleHog](https://github.com/trufflesecurity/trufflehog) | AGPL-3.0 | impede vazamento de segredo por repositório |

## A.8.13 Backup das informações

Manter e testar cópias de segurança conforme a política acordada.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Restic](https://restic.net/) | BSD-2-Clause | cópia cifrada, deduplicada e verificável |
| [BorgBackup](https://www.borgbackup.org/) | BSD-3-Clause | alternativa consolidada com deduplicação |
| [Bacula](https://www.bacula.org/) | AGPL-3.0 | backup corporativo com catálogo e fitoteca |
| [UrBackup](https://www.urbackup.org/) | AGPL-3.0 | backup de estação com imagem e arquivo |
| [Velero](https://velero.io/) | Apache-2.0 | backup de Kubernetes, inclusive volumes |

## A.8.14 Redundância dos recursos de tratamento de informações

Implementar redundância suficiente para os requisitos de disponibilidade.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Keepalived](https://www.keepalived.org/) | GPL-2.0 | IP virtual com failover |
| [HAProxy](https://www.haproxy.org/) | GPL-2.0 | balanceamento com verificação de saúde |
| [Patroni](https://patroni.readthedocs.io/) | MIT | alta disponibilidade para PostgreSQL |
| [Proxmox VE](https://www.proxmox.com/) | AGPL-3.0 | cluster com migração e replicação |

## A.8.15 Registro

Produzir, armazenar, proteger e analisar registros de eventos.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Graylog](https://graylog.org/) | SSPL/GPL-3.0 | coleta, retenção e busca com controle de acesso |
| [OpenSearch](https://opensearch.org/) | Apache-2.0 | armazenamento e busca em escala |
| [Grafana Loki](https://grafana.com/oss/loki/) | AGPL-3.0 | log indexado por rótulo, barato de manter |
| [rsyslog](https://www.rsyslog.com/) | GPL-3.0 | coleta confiável com encaminhamento cifrado |

## A.8.16 Atividades de monitoramento

Monitorar redes, sistemas e aplicações para detectar comportamento anômalo.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Wazuh](https://wazuh.com/) | GPL-2.0 | SIEM e detecção em endpoint na mesma plataforma |
| [Security Onion](https://securityonionsolutions.com/) | GPL-2.0 | distribuição completa de monitoramento e caça |
| [Suricata](https://suricata.io/) | GPL-2.0 | detecção e prevenção de intrusão em rede |
| [Zeek](https://zeek.org/) | BSD-3-Clause | registro rico de rede para análise posterior |

## A.8.17 Sincronização do relógio

Sincronizar os relógios com fontes de tempo aprovadas.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [chrony](https://chrony-project.org/) | GPL-2.0 | cliente e servidor NTP preciso, o padrão atual em Linux |
| [NTPsec](https://www.ntpsec.org/) | BSD-2-Clause | implementação revisada com foco em segurança |
| [Zabbix](https://www.zabbix.com/) | AGPL-3.0 | alerta quando algum host sai de sincronia |

## A.8.18 Uso de programas utilitários privilegiados

Restringir e controlar rigidamente o uso de utilitários que burlam controles.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [SELinux](https://github.com/SELinuxProject) | GPL-2.0 | confina o que cada processo pode fazer, mesmo como root |
| [AppArmor](https://apparmor.net/) | GPL-2.0 | perfis por aplicação, mais simples de operar |
| [sudo](https://www.sudo.ws/) | ISC | lista explícita de comandos permitidos por usuário |
| [Teleport](https://goteleport.com/) | AGPL-3.0 | gravação da sessão em que o utilitário foi usado |

## A.8.19 Instalação de software em sistemas operacionais

Controlar a instalação de software nos sistemas em produção.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Ansible](https://www.ansible.com/) | GPL-3.0 | só entra o que está no código de configuração |
| [fapolicyd](https://github.com/linux-application-whitelisting/fapolicyd) | GPL-3.0 | lista de permissão de execução por política |
| [Pulp](https://pulpproject.org/) | GPL-2.0 | repositório interno que define o que pode ser instalado |
| [osquery + Fleet](https://fleetdm.com/) | MIT | detecta software não autorizado já instalado |

## A.8.20 Segurança de redes

Gerenciar e controlar redes para proteger a informação que trafega.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OPNsense](https://opnsense.org/) | BSD-2-Clause | firewall com IDS, VPN e relatório |
| [pfSense CE](https://www.pfsense.org/) | Apache-2.0 | alternativa consolidada |
| [nftables](https://netfilter.org/projects/nftables/) | GPL-2.0 | filtragem no próprio host |
| [CrowdSec](https://www.crowdsec.net/) | MIT | bloqueio colaborativo de endereços hostis |

## A.8.21 Segurança dos serviços de rede

Identificar e aplicar os mecanismos de segurança de cada serviço de rede.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Let's Encrypt + Certbot](https://certbot.eff.org/) | Apache-2.0 | TLS gratuito e renovado automaticamente |
| [step-ca](https://smallstep.com/docs/step-ca/) | Apache-2.0 | autoridade certificadora interna para serviços e mTLS |
| [testssl.sh](https://testssl.sh/) | GPL-2.0 | verifica a qualidade real da configuração TLS |
| [Unbound](https://nlnetlabs.nl/projects/unbound/) | BSD-3-Clause | DNS recursivo com validação DNSSEC |

## A.8.22 Segregação de redes

Segregar grupos de serviços, usuários e sistemas na rede.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OPNsense](https://opnsense.org/) | BSD-2-Clause | VLAN e regras entre segmentos |
| [Cilium](https://cilium.io/) | Apache-2.0 | política de rede entre cargas de trabalho em Kubernetes |
| [Calico](https://www.tigera.io/project-calico/) | Apache-2.0 | alternativa com política de rede declarativa |
| [Open vSwitch](https://www.openvswitch.org/) | Apache-2.0 | segmentação em ambiente virtualizado |

## A.8.23 Filtragem da web

Gerenciar o acesso a sites externos para reduzir exposição a conteúdo malicioso.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Pi-hole](https://pi-hole.net/) | EUPL-1.2 | bloqueio por DNS, simples de implantar |
| [Squid](https://www.squid-cache.org/) | GPL-2.0 | proxy com política por grupo e registro de acesso |
| [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) | GPL-3.0 | filtragem DNS com painel e listas |
| [Blocky](https://0xerr0r.github.io/blocky/) | Apache-2.0 | resolvedor DNS com listas e métricas |

## A.8.24 Uso de criptografia

Definir e aplicar regras para uso da criptografia, incluindo gestão de chaves.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OpenBao](https://openbao.org/) | MPL-2.0 | gestão de chaves e segredos com rotação e trilha |
| [step-ca](https://smallstep.com/docs/step-ca/) | Apache-2.0 | PKI interna com ciclo de vida curto |
| [age](https://github.com/FiloSottile/age) | BSD-3-Clause | cifra de arquivo moderna e simples |
| [GnuPG](https://gnupg.org/) | GPL-3.0 | assinatura e cifra com padrão OpenPGP |
| [SOPS](https://github.com/getsops/sops) | MPL-2.0 | cifra de segredo dentro do repositório |

## A.8.25 Ciclo de vida de desenvolvimento seguro

Estabelecer e aplicar regras de desenvolvimento seguro ao longo do ciclo.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OWASP SAMM](https://owaspsamm.org/) | CC BY-SA 4.0 | modelo de maturidade que estrutura o próprio ciclo |
| [GitLab CE](https://gitlab.com/gitlab-org/gitlab-foss) | MIT | pipeline com etapas obrigatórias de segurança |
| [Gitea Actions](https://about.gitea.com/) | MIT | mesma ideia em infraestrutura própria |

## A.8.26 Requisitos de segurança da aplicação

Especificar os requisitos de segurança ao desenvolver ou adquirir aplicação.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | CC BY-SA 4.0 | catálogo de requisitos verificáveis por nível |
| [OWASP MASVS](https://mas.owasp.org/MASVS/) | CC BY-SA 4.0 | equivalente para aplicação móvel |
| [DefectDojo](https://www.defectdojo.org/) | BSD-3-Clause | rastreia o requisito até o teste que o comprova |

## A.8.27 Princípios de arquitetura e engenharia de sistemas seguros

Estabelecer e aplicar princípios de engenharia segura em todo sistema.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) | Apache-2.0 | modelagem de ameaças com diagrama e mitigação |
| [pytm](https://github.com/OWASP/pytm) | MIT | modelagem de ameaças como código |
| [Threagile](https://threagile.io/) | MIT | modelagem de ameaças a partir de um arquivo YAML, boa para automatizar |

## A.8.28 Codificação segura

Aplicar princípios de codificação segura no desenvolvimento.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Semgrep](https://semgrep.dev/) | LGPL-2.1 | análise estática com regras legíveis e próprias |
| [SonarQube Community](https://www.sonarsource.com/products/sonarqube/) | LGPL-3.0 | qualidade e segurança com portão de qualidade |
| [Bandit](https://bandit.readthedocs.io/) | Apache-2.0 | análise estática para Python |
| [pre-commit](https://pre-commit.com/) | MIT | roda a verificação antes de o código entrar |

## A.8.29 Testes de segurança em desenvolvimento e aceitação

Definir e executar processos de teste de segurança durante o ciclo.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OWASP ZAP](https://www.zaproxy.org/) | Apache-2.0 | teste dinâmico automatizável em pipeline |
| [Nuclei](https://github.com/projectdiscovery/nuclei) | MIT | verificação por modelo em ambiente de homologação |
| [Trivy](https://trivy.dev/) | Apache-2.0 | varredura de imagem antes da promoção |
| [DefectDojo](https://www.defectdojo.org/) | BSD-3-Clause | consolida o resultado e bloqueia a entrega quando necessário |

## A.8.30 Desenvolvimento terceirizado

Dirigir, monitorar e revisar a atividade de desenvolvimento terceirizado.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Gitea](https://about.gitea.com/) | MIT | o código do terceiro fica na sua infraestrutura, com revisão obrigatória |
| [Semgrep](https://semgrep.dev/) | LGPL-2.1 | aplica a sua regra ao código que vem de fora |
| [Syft + Grype](https://github.com/anchore/syft) | Apache-2.0 | SBOM do que o terceiro entregou |

## A.8.31 Separação dos ambientes de desenvolvimento, teste e produção

Separar e proteger os ambientes ao longo do ciclo.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [Proxmox VE](https://www.proxmox.com/) | AGPL-3.0 | isolamento por cluster, VLAN e permissão |
| [Kubernetes + namespaces](https://kubernetes.io/) | Apache-2.0 | separação lógica com política de rede e cota |
| [OpenTofu](https://opentofu.org/) | MPL-2.0 | ambientes definidos em código, sem desvio manual |
| [Keycloak](https://www.keycloak.org/) | Apache-2.0 | realms distintos por ambiente |

## A.8.32 Gestão de mudanças

Submeter mudanças a procedimento formal de gestão de mudanças.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [GLPI](https://glpi-project.org/) | GPL-3.0 | fluxo de mudança com aprovação e janela |
| [Gitea / GitLab CE](https://about.gitea.com/) | MIT | toda mudança passa por revisão e fica no histórico |
| [Atlantis](https://www.runatlantis.io/) | Apache-2.0 | aplica mudança de infraestrutura só após aprovação no pedido |
| [Zammad](https://zammad.com/) | AGPL-3.0 | registro e comunicação da mudança |

## A.8.33 Informações de teste

Selecionar, proteger e gerenciar a informação usada em teste.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [PostgreSQL Anonymizer](https://postgresql-anonymizer.readthedocs.io/) | PostgreSQL | gera massa de teste a partir da produção, sem dado real |
| [Microsoft Presidio](https://microsoft.github.io/presidio/) | MIT | anonimiza antes de copiar para homologação |
| [Faker](https://faker.readthedocs.io/) | MIT | gera dado sintético do zero |
| [Synthea](https://synthetichealth.github.io/synthea/) | Apache-2.0 | massa sintética realista para saúde |

## A.8.34 Proteção de sistemas de informação durante os testes de auditoria

Planejar e acordar testes de auditoria para minimizar impacto na operação.

| Ferramenta | Licença | Por que serve aqui |
|---|---|---|
| [OpenVAS / Greenbone](https://www.greenbone.net/) | GPL-2.0 | permite agendar e limitar a intensidade da varredura |
| [Teleport](https://goteleport.com/) | AGPL-3.0 | acesso temporário e gravado para o auditor |
| [Zabbix](https://www.zabbix.com/) | AGPL-3.0 | acompanha o impacto do teste em tempo real |
| [Wazuh](https://wazuh.com/) | GPL-2.0 | registra a atividade do auditor para o relatório |
