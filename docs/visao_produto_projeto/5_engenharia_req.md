# 5 ENGENHARIA DE REQUISITOS

## 5.1 Atividades e Técnicas de ER

**Elicitação e Descoberta:**

- **Entrevista com Stakeholders:** Reuniões com a equipe de coordenação de CECP para reconhecer e compreender os maiores desafios dentro do fluxo atual de operação e ouvir deles suas necessidades, desejos e expectativas e identificar o caráter do problema.
- **Brainstorming dos desenvolvedores:** Sessões de brainstorming entre os desenvolvedores servirão para elencar os desafios e sugerir soluções que possam transformar o atual fluxo manual em um processo digital.

**Análise e Consenso:**

- **Priorização de Requisitos (Matriz de Avaliação Técnica x Valor de Negócio):** Técnica utilizada entre equipe e cliente para classificar as funcionalidades levantadas cruzando dois eixos — complexidade/esforço técnico de implementação e valor gerado para o negócio — permitindo identificar quais funcionalidades entregam mais valor com menor esforço, chegando a um consenso sobre o núcleo essencial do sistema (a definição do MVP), reduzindo escopo e resolvendo conflitos sobre o que é prioritário para entrega.

**Declaração de Requisitos:**

- **Declaração Estruturada de Requisitos:** Técnica de declaração utilizada para especificar os requisitos descobertos em formato tabular estruturado, contendo identificador único, descrição, classificação como Requisito Funcional (RF) ou Requisito Não Funcional (RNF), e critério de aceitação, a fim de garantir rastreabilidade, testabilidade e comunicação clara entre equipe e cliente.


**Representação de Requisitos:**

- **Protótipos e Wireframes:** Protótipos de baixa fidelidade tipo wireframes serão utilizados para representar visualmente os requisitos, como eles serão implementados na solução, e protótipos de maior fidelidade definirão a identidade visual a fim de construir uma interface intuitiva para os usuários.

**Verificação e Validação de Requisitos:**

- **Revisão por pares (Verificação):** Os requisitos descobertos serão revisados internamente entre os desenvolvedores antes da apresentação ao cliente, examinando consistência, completude e testabilidade.
- **Revisão de Requisitos com Stakeholders (Validação):** Os requisitos especificados serão apresentados ao representante e à equipe do CECP para confirmar se refletem corretamente as necessidades identificadas, podendo ser aprovados, rejeitados ou ajustados conforme o entendimento dos stakeholders. Essa técnica pode ser aplicada sempre que houver necessidade de revisar requisitos, especialmente antes da existência de protótipos que permitam uma validação mais visual.
- **Sessão de Validação com Protótipo (Validação):** A validação dos requisitos ocorrerá por meio da apresentação dos protótipos ao representante e à equipe do CECP, que poderão aprovar, rejeitar ou sugerir ajustes para que os requisitos alcancem o resultado esperado.

**Organização e Atualização de Requisitos:**

- **Gestão de Backlog de Requisitos:** Técnica utilizada para registrar, categorizar e acompanhar o progresso de cada requisito ao longo do desenvolvimento, garantindo rastreabilidade e visibilidade do que está pendente, em andamento ou concluído. Essa técnica é operacionalizada por meio do GitHub Projects, ferramenta escolhida pela equipe para visualizar e gerenciar as issues correspondentes.


## 5.2 Engenharia de Requisitos e o RAD

| Fases do RAD | Atividades de ER | Prática Técnica | Resultado Esperado |
|---|---|---|---|
| **Planejamento de Requisitos** | Elicitação e Descoberta — Identificação de necessidades e contexto | Entrevista com stakeholders e brainstorming dos desenvolvedores | Necessidades, dificuldades e requisitos de alto nível\* identificados |
| | Análise e Consenso — Definição de prioridades e escopo acordado | Priorização de Requisitos (Matriz de Avaliação Técnica x Valor de Negócio) | Funcionalidades essenciais priorizadas e acordadas |
| | Declaração — Comunicação estruturada dos requisitos | Declaração Estruturada de Requisitos | Requisitos identificados, classificados e numerados |
| | Verificação e Validação — Verificação de qualidade interna e validação com stakeholders | Revisão por Pares (Verificação) e Revisão de Requisitos com Stakeholders (Validação) | Requisitos verificados quanto à consistência interna e confirmados como representativos das necessidades reais do CECP |
| | Organização e Atualização — Estruturação inicial dos requisitos | Gestão de Backlog de Requisitos (via GitHub Projects) | Requisitos organizados e acompanhados por meio de issues |
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