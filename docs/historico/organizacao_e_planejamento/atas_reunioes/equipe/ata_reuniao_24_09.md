# Ata de Reunião - Inspeção e Verificação de Requisitos

## 1. Identificação da reunião

**Projeto:** Sistema de Gestão do Centro Esportivo Cultural de Planaltina (SigCECP)

**Data:** 24/09/2026

**Local:** Plataforma Online (Microsoft Teams)

**Participantes:** Alexandre, Ana, Enzo, Marcos, Maria, Rafael, Renato

**Responsável pelo registro:** Rafael Oliveira Montagner Melatti

**Pauta:** 
- Inspeção e verificação técnica dos requisitos funcionais e não funcionais elaborados pelo grupo Squad Guerreiros - Projeto Mães Guerreiras
- Divisão do escopo de análise entre os integrantes
- Identificação de inconsistências formais, omissão de agentes, falhas de categorização e rastreabilidade
- Planejamento das pendências operacionais do projeto.

## 2. Contexto e metodologia de verificação

Rafael e Marcos abriram a reunião contextualizando a dinâmica de verificação cruzada entre equipes, com foco na avaliação do documento de requisitos do grupo parceiro (Squad Guerreiros, Projeto Mães Guerreiras). Verificou-se que a documentação analisada continha 44 Requisitos Funcionais (RFs) e 14 Requisitos Não Funcionais (RNFs).

O grupo estabeleceu a utilização dos critérios formais recomendados pela disciplina e pela literatura de Engenharia de Software para orientar a inspeção:

- **Expressão da funcionalidade:** verificação da estrutura verbo-objeto.
- **Clareza e não-ambiguidade:** identificação de termos vagos, subjetivos ou sem definição explícita no domínio.
- **Completude e especificação de atores:** checagem da indicação clara sobre quem executa, interage ou se beneficia de cada funcionalidade.
- **Consistência e sobreposição:** detecção de requisitos duplicados, redundantes ou mutuamente conflitantes.
- **Rastreabilidade e vínculo com o problema:** avaliação da presença de matriz de rastreabilidade e correspondência com as necessidades do cliente.

## 3. Divisão do escopo de análise entre os participantes

Para maior agilidade da verificação e possibilitar o preenchimento simultâneo da planilha de inspeção, a equipe realizou a distribuição dos blocos de Requisitos Funcionais entre os participantes presentes:

| Participante | Escopo de Análise de Requisitos |
| :--- | :--- |
| Alexandre | Requisitos do Bloco 1 (RF01 a RF06) |
| Ana | Requisitos do Bloco 2 (RF07 a RF12) |
| Maria | Requisitos dos Blocos 3 e 4 (RF13 a RF25) |
| Marcos | Requisitos do Bloco 5 (RF26 a RF31) |
| Rafael | Requisitos do Bloco 6 (RF32 a RF37) |
| Renato | Requisitos do Bloco 7 (RF38 a RF44) |
| Enzo | Análise técnica transversal e apoio na revisão de RNFs |

## 4. Inspeção dos Requisitos Funcionais e inconsistências identificadas

Durante a análise dos 44 RFs, a equipe constatou falhas recorrentes no documento do Squad Guerreiros:

- **Ausência de atores/agentes:** a quase totalidade dos requisitos não definia o perfil de usuário com permissão para executar a ação (ex: quem possui autorização para gerar relatórios, efetuar cadastros ou consultas).
- **Termos vagos e referências a documentos ausentes:** observou-se o uso de expressões indeterminadas, como "encontro em chamada" e "ações críticas", sem a devida conceituação.
- **Redundância e sobreposição de relatórios:** constatou-se que requisitos distintos criados para emissão de relatórios (ex: relatórios de doações recebidas versus doações distribuídas) tratavam da mesma funcionalidade estrutural, podendo ser unificados em um único requisito parametrizado.
- **Falta de rastreabilidade formal:** ausência de uma matriz de rastreabilidade mapeando a origem dos requisitos em relação aos problemas e necessidades declarados pelo cliente.

## 5. Avaliação dos Requisitos Não Funcionais (RNFs) e categorização

A auditoria nos 14 RNFs revelou alguns equívocos de classificação e ausência de critérios objetivos de aceitação:

- **Classificação incorreta de categorias (FURPS+/Sommerville):** o RNF9 (facilidade de uso da interface) foi incorretamente categorizado como suportabilidade, quando deveria pertencer à categoria de usabilidade. O RNF12 ("restrição de design") foi apontado como apenas uma restrição, devendo ser reclassificado como requisito organizacional. O RNF10 também foi levantado nessa pauta.
- **Ambiguidade e redundância de segurança:** o RNF7 mencionava genericamente uma "conexão cifrada" sem definir algoritmos ou protocolos, gerando sobreposição com o RNF11, que estipulava a comunicação em formato JSON sobre protocolo HTTPS.
- **Desconformidade no conceito de Backup:** o RNF5 descrevia a rotina operacional diária de cópia de segurança (backup) em vez de focar na meta de qualidade do serviço. O grupo apontou que a execução do backup constitui um requisito funcional ou de infraestrutura, cabendo ao RNF apenas a especificação do tempo de recuperação de dados (RTO).
- **Incompatibilidade de versões de software:** no RNF8, observou-se a especificação simultânea do navegador Safari 14 em conjunto com o sistema iOS 13, combinação tecnicamente conflitante com as distribuições nativas da Apple.

## 6. Discussão sobre adequação à LGPD e retenção de dados

Em acréscimo à inspeção cruzada, a equipe discutiu os impactos da Lei Geral de Proteção de Dados (LGPD) sobre o projeto. Debateu-se a tensão existente entre o direito do titular à eliminação de seus dados pessoais e a obrigatoriedade da instituição em preservar históricos de frequência e participação para fins de prestação de contas aos órgãos fomentadores.

O grupo reafirmou que a conduta adotada no SigCECP, inativação do registro do participante combinada com o descarte específico de documentos de identificação crítica (preservando o histórico estatístico de atendimento), atende aos preceitos jurídicos da LGPD e às necessidades administrativas da ONG.

## 7. Organização interna do grupo e encaminhamento das pendências

Finalizada a verificação do material parceiro, Rafael e Marcos coordenaram o alinhamento das atividades internas necessárias para as próximas entregas da disciplina:

- **Regularização de documentação pendente:** elaboração e publicação imediata das atas de reuniões passadas ainda ausentes no repositório oficial (GitHub Pages).
- **Análise dos feedbacks do próprio projeto:** estruturação do processo de revisão dos feedbacks recebidos pela equipe, classificando cada item formalmente como aceito, parcialmente aceito, não aceito ou não aplicável.
- **Priorização de requisitos e definição do MVP:** necessidade de consolidar a priorização funcional e delimitar o Produto Mínimo Viável (MVP) até a aula do dia 29/09/2026.

## 8. Decisões

- **Consolidação do feedback de verificação:** a equipe aprovou o preenchimento da planilha de auditoria reunindo todos os apontamentos de ausência de agentes, inconsistências do FURPS+, termos vagos e falta de rastreabilidade identificados nos requisitos do Squad Guerreiros (seções 4 e 5).
- **Compartilhamento da planilha de inspeção:** definiu-se pelo envio direto do link da planilha de verificação ao grupo parceiro para facilitar a correção da documentação (seção 7).
- **Tratamento sistemático do feedback interno:** o grupo decidiu categorizar formalmente todas as observações recebidas sobre o seu próprio projeto, promovendo os ajustes necessários para a entrega da próxima etapa (seção 7).

## 9. Próximas etapas e pendências

- **Marcos:** finalizar a planilha de verificação dos requisitos do Squad Guerreiros e efetuar o envio formal ao grupo parceiro.
- **Rafael:** elaborar a proposta de divisão do trabalho para a revisão dos feedbacks internos e priorização do MVP.
- **Todo o grupo:** redigir e publicar no GitHub Pages do projeto as atas de reuniões pendentes.
- **Todo o grupo:** realizar reunião de alinhamento no dia seguinte para concluir a priorização de requisitos e a definição do MVP até 29/09/2026.