# 5 ENGENHARIA DE REQUISITOS

## 5.1 Atividades e Técnicas de ER

<!--
GUIA RÁPIDO (apagar antes de publicar):
- Cada técnica tem "Status" e "Evidências".
- Onde está escrito PREENCHER, falta você decidir/completar.
- Onde está CONFIRMAR, sugeri o link/status com base no que existe no site, mas vale conferir.
- Links estão completos (https://...). Se o repositório usa links relativos, troque.
-->

**Elicitação e Descoberta:**

- **Entrevista com Stakeholders:** Reuniões com a equipe de coordenação do CECP para reconhecer e compreender os maiores desafios dentro do fluxo atual de operação, ouvir suas necessidades, desejos e expectativas e identificar o caráter do problema.
    - **Status:** realizada continuamente
    - **Evidências:** atas das reuniões com o cliente: [17/09](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_17_09/), [22/09](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_22_09/), [24/09](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_24_09/), [26/09](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_26_09/), [08/10](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_09_10/), [21/10](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_21_10/), [30/10](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_30_10/). Gravações: [17/09](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/gravacoes/reunioes_cliente/reuniao_audio_17_09/), [22/09](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/gravacoes/reunioes_cliente/reuniao_audio_22_09/), [24/09](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/gravacoes/reunioes_cliente/reuniao_audio_24_09/), [26/09](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/gravacoes/reunioes_cliente/reuniao_audio_26_09/), [09/10](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/gravacoes/reunioes_cliente/reuniao_audio_09_10/), [21/10](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/gravacoes/reunioes_cliente/reuniao_audio_21_10/). <!-- CONFIRMAR: a ata aparece como 08/10 no menu, mas o arquivo e a gravação são 09/10 -->

- **Brainstorming dos desenvolvedores:** Discussões entre os desenvolvedores serviram para elencar os desafios e sugerir soluções que transformassem o atual fluxo manual em um processo digital. A técnica foi aplicada de forma contínua e informal, sem sessões formais de brainstorming: as ideias eram acatadas ou descartadas ao longo do trabalho, servindo tanto à elicitação quanto ao refinamento dos requisitos.
    - **Status:** realizada continuamente, informalmente
    - **Evidências:** Sem registros formais, e houve uma Reunião não gravada entre os desenvolvedores em 24/10 em que foram tratados o Brainstorming dos Desenvolvedores e uma breve Revisão por Pares dos novos requisitos elicitados em tal reunião.

**Análise e Consenso:**

- **Priorização de Requisitos (Matriz de Avaliação Técnica x Valor de Negócio):** Técnica utilizada entre equipe e cliente para classificar as funcionalidades levantadas cruzando dois eixos: complexidade/esforço técnico de implementação e valor gerado para o negócio. Permite identificar quais funcionalidades entregam mais valor com menor esforço, chegando a um consenso sobre o núcleo essencial do sistema (a definição do MVP), reduzindo escopo e resolvendo conflitos sobre o que é prioritário para entrega.
    - **Status:** realizada <!-- CONFIRMAR -->
    - **Evidências:** [Evidências da priorização](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/priorizacao_geral_e_mvp/) e [Backlog e MVP](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/10_backlog_produto/)

- **MoSCoW:** Técnica de priorização utilizada para classificar os requisitos de acordo com seu grau de importância para o sistema. Os requisitos são divididos em quatro categorias: **Must have, Should have, Could have e Won’t have.** A técnica auxilia a equipe e o cliente a estabelecer prioridades claras, controlar o escopo e garantir que os recursos disponíveis sejam direcionados inicialmente às funcionalidades mais essenciais.
    - **Status:** realizada 
    - **Evidências:** [Reunião](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_09_10/) com Nova Priorização dos Requisitos.

**Declaração de Requisitos:**

- **Declaração Estruturada de Requisitos:** Técnica de declaração utilizada para especificar os requisitos descobertos em fichas para cada requisito, contendo identificador único, descrição, classificação como Requisito Funcional (RF) ou Requisito Não Funcional (RNF), Regras de Negócio (RN), Característica de Produto (CP) de origem, ator, entradas, pré-condições, processamento, saídas, critério de aceitação e andamento, a fim de garantir rastreabilidade, testabilidade e comunicação clara entre equipe e cliente. Todos os requisitos podem ser facilmente acessados pelo Painel do Escopo.
    - **Status:** realizada continuamente
    - **Evidências:** [Painel do Escopo](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/painel/) em modais com acesso às fichas, exemplo de ficha: [RF00](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/visao/escopo/requisitos/RF00/).

**Representação de Requisitos:**

- **Protótipos e Wireframes:** Protótipos de baixa fidelidade tipo wireframes serão utilizados para representar visualmente os requisitos, como eles serão implementados na solução, e protótipos de maior fidelidade definirão a identidade visual a fim de construir uma interface intuitiva para os usuários.
    - **Status:** em andamento
    - **Evidências:** [Design do usuário](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/designUser_iteracao5/)

**Verificação e Validação de Requisitos:**

- **Revisão por pares (Verificação):** Os requisitos descobertos serão revisados internamente entre os desenvolvedores antes da apresentação ao cliente, examinando consistência, completude e testabilidade.
    - **Status:** realizada informalmente.
    - **Evidências:** Sem registros formais, e houve uma Reunião não gravada entre os desenvolvedores em 24/10 em que foram tratados o Brainstorming dos Desenvolvedores e uma breve Revisão por Pares dos novos requisitos elicitados em tal reunião.

- **Revisão de Requisitos com Stakeholders (Validação):** Os requisitos especificados serão apresentados ao representante e à equipe do CECP para confirmar se refletem corretamente as necessidades identificadas, podendo ser aprovados, rejeitados ou ajustados conforme o entendimento dos stakeholders. Essa técnica pode ser aplicada sempre que houver necessidade de revisar requisitos, especialmente antes da existência de protótipos que permitam uma validação mais visual.
    - **Status:** realizada
    - **Evidências:** [Detalhamento dos Requisitos](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_21_10/) e atas das reuniões com o cliente (ver Entrevista com Stakeholders) 

- **Sessão de Validação com Protótipo (Validação):** A validação dos requisitos ocorrerá por meio da apresentação dos protótipos ao representante e à equipe do CECP, que poderão aprovar, rejeitar ou sugerir ajustes para que os requisitos alcancem o resultado esperado.
    - **Status:** em andamento
    - **Evidências:** [Design do Usuário](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/designUser_iteracao5/).

**Organização e Atualização de Requisitos:**

- **Gestão de Backlog de Requisitos:** Técnica utilizada para registrar, categorizar e acompanhar o progresso de cada requisito ao longo do desenvolvimento, garantindo rastreabilidade e visibilidade do que está pendente, em andamento ou concluído. Essa técnica é operacionalizada por meio do GitHub Projects, ferramenta escolhida pela equipe para visualizar e gerenciar as issues correspondentes, e pelo Painel do Escopo, um catálogo completo de organização e atualização dos requisitos que mostra todos os detalhes e andamento dos requisitos.
    - **Status:** realizada continuamente.
    - **Evidências:** [GitHub Projects](https://github.com/orgs/mdsreq-fga-unb/projects/118/views/1), [Backlog e MVP](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/historico/10_backlog_produto/) e o [Painel do Escopo](https://mdsreq-fga-unb.github.io/REQ-2026.2-T01-SigCecp/painel/).



## 5.2 Engenharia de Requisitos e o RAD

| Fases do RAD | Atividades de ER | Prática Técnica | Resultado Esperado |
|---|---|---|---|
| **Planejamento de Requisitos** | Elicitação e Descoberta — Identificação de necessidades e contexto | Entrevista com stakeholders e brainstorming dos desenvolvedores | Necessidades, dificuldades e requisitos de alto nível\* identificados |
| | Análise e Consenso — Definição de prioridades e escopo acordado | Priorização de Requisitos (Matriz de Avaliação Técnica x Valor de Negócio) | Funcionalidades essenciais priorizadas e acordadas |
| | Declaração — Comunicação estruturada dos requisitos | Declaração Estruturada de Requisitos | Requisitos identificados, classificados e numerados |
| | Verificação e Validação — Verificação de qualidade interna e validação com stakeholders | Revisão por Pares (Verificação) e Revisão de Requisitos com Stakeholders (Validação) | Requisitos verificados quanto à consistência interna e confirmados como representativos das necessidades reais do CECP |
| | Organização e Atualização — Estruturação inicial dos requisitos | Gestão de Backlog de Requisitos (via GitHub Projects e Painel do Escopo) | Requisitos organizados e acompanhados por meio de issues e de fichas |
| **Design do Usuário** | Representação — Visualização conceitual de interfaces | Protótipos e wireframes | Telas e fluxos representados para avaliação com os stakeholders |
| | Verificação e Validação — Verificação de qualidade interna e validação com stakeholders | Revisão por Pares (Verificação) e Sessão de Validação com Protótipo (Validação) | Protótipos com os requisitos e com os fluxos de uso esperados |
| | Elicitação e Descoberta — Refinamento dos requisitos | Entrevista com stakeholders | Novos requisitos ou ajustes detalhados a partir da interação visual do cliente com os protótipos |
| | Análise e Consenso — Revisão de prioridades a partir do protótipo | Priorização de Requisitos (Matriz de Avaliação Técnica x Valor de Negócio) | Prioridades revisadas e reacordadas conforme aprendizado obtido com os protótipos |
| | Declaração — Consolidação dos esclarecimentos | Declaração Estruturada de Requisitos | Detalhes acordados incorporados às declarações dos requisitos correspondentes |
| | Organização e Atualização — Registro das avaliações | Gestão de Backlog de Requisitos (via GitHub Projects) | Avaliações do cliente e protótipos vinculados às issues dos requisitos já definidos |
| **Construção** | Organização e Atualização — Manutenção dos requisitos | Gestão de Backlog de Requisitos (via GitHub Projects) | Requisitos e mudanças mantidos em estado atual |
| | Verificação e Validação — Verificação dos requisitos alterados | Revisão por Pares (Verificação) | Requisitos modificados verificados quanto à qualidade interna |
| | Elicitação, Análise, Declaração e Representação — Ajuste de requisitos emergentes | Entrevista com stakeholders, Priorização de Requisitos (Matriz de Avaliação Técnica x Valor de Negócio), Declaração Estruturada de Requisitos e Protótipos e Wireframes | Novos requisitos ou ajustes identificados durante a construção devidamente elicitados, analisados, declarados e representados |
| **Transição** | Verificação e Validação — Validação final dos requisitos | Sessão de Validação com Protótipo (Validação) | Confirmação de que os requisitos atendidos correspondem às necessidades do CECP |
| | Organização e Atualização — Consolidação dos requisitos | Gestão de Backlog de Requisitos (via GitHub Projects) | Estado final dos requisitos e itens futuros devidamente registrados |

> \*Requisitos de alto nível referem-se a requisitos amplos e ainda pouco detalhados, identificados na fase inicial de elicitação, antes do refinamento realizado nas etapas de Análise e Declaração.

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) |  |
| 1.1 | 19/09/2026 | Revisão das técnicas de Engenharia de Requisitos com base em feedback recebido durante o desenvolvimento do projeto | Ana Paula Jardim | Marcos Monteiro |
| 1.2 | 13/11/2026 | Inclusão de status e evidências por técnica de ER; atualização da descrição da Declaração Estruturada de Requisitos e Organização e Atualização | Ana Paula Jardim |  |