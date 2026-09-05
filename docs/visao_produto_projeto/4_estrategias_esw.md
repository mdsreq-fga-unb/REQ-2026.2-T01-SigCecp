# 4. Estratégias de Engenharia de Software

## 4.1. Estratégia Priorizada

- **Abordagem:** Híbrida
- **Ciclo de Vida:** Iterativo e Incremental
- **Processo:** RAD

## 4.2. Quadro Comparativo

A fim de fundamentar a escolha do processo de desenvolvimento, o quadro a seguir compara o RAD e o Scrum a partir de características relevantes para o contexto do projeto.

| Características | Scrum | RAD |
|---|---|---|
| **Abordagem Geral** | Ágil, iterativo e incremental, organizado em sprints com entregas frequentes e adaptação contínua. | Híbrido, iterativo e incremental, com forte ênfase em prototipação rápida e entrega acelerada de módulos funcionais. |
| **Estrutura do Processo** | Estrutura leve baseada em eventos (Sprint Planning, Daily, Review e Retrospective), com menor formalização de fases. | Fases definidas (Planejamento de Requisitos, Design com o Usuário, Construção Rápida e Implantação), o que confere previsibilidade ao andamento do projeto. |
| **Papel do Cliente** | Envolvimento contínuo ao longo de todo o projeto, com feedback ao final de cada sprint e um Product Owner dedicado priorizando o backlog. | Participação intensa e concentrada na fase de Design com o Usuário, validando protótipos que evoluem até a solução final. |
| **Uso de Protótipos** | Protótipos podem ser usados, mas não são elemento estrutural do processo; o refinamento ocorre sobre incrementos do produto. | Prototipação é o núcleo do processo: os requisitos são refinados diretamente sobre protótipos, reduzindo ambiguidades. |
| **Velocidade de Entrega** | Entregas incrementais a cada sprint (2 a 4 semanas), mas a velocidade depende da maturidade da equipe com as cerimônias. | Voltado a ciclos curtos com escopo controlado, priorizando a entrega rápida de um produto funcional. |
| **Requisitos** | Mais adequado quando os requisitos mudam com frequência ao longo do projeto. | Mais adequado quando os requisitos centrais são conhecidos desde o início e podem ser modelados rapidamente com o usuário. |
| **Papéis e Cerimônias** | Exige papéis definidos (Product Owner, Scrum Master, Time de Desenvolvimento) e cerimônias regulares, que demandam disponibilidade constante. | Exige poucos papéis formais, com sobrecarga de gestão reduzida. |
| **Adequação à Equipe** | Compatível com equipes pequenas e médias, mas pressupõe dedicação e disponibilidade regulares para as cerimônias. | Compatível com equipes pequenas que utilizam ferramentas de desenvolvimento rápido e componentes reutilizáveis. |
| **Adaptação ao Projeto do CECP** | Viável, porém, o envolvimento contínuo exigido do cliente conflita com a disponibilidade limitada da equipe, que participa por reuniões periódicas. | Ideal para o contexto: requisitos centrais já mapeados junto ao cliente, validação por protótipos/wireframes já prevista na ER, prazo de um semestre e necessidade de entregar um MVP funcional rapidamente. |

## 4.3. Justificativa

Com base nas características do projeto e no contexto do CECP, o RAD é o processo mais adequado pelos seguintes motivos:

**Requisitos centrais conhecidos e escopo enxuto**

O levantamento realizado junto à coordenação do CECP já permitiu identificar com clareza o núcleo do problema (cadastro de alunos, frequência, acompanhamento escolar e registro de doações). O RAD é indicado justamente para cenários em que os requisitos principais são conhecidos desde o início e podem ser rapidamente modelados e validados com o usuário, sem a necessidade de um processo desenhado para absorver mudanças constantes de escopo.

**Centralidade da prototipação**

A equipe já definiu, nas atividades de Engenharia de Requisitos, o uso de wireframes e protótipos como técnica de representação e validação de requisitos. Esse fluxo é o coração do RAD, cuja fase de Design com o Usuário se apoia em protótipos que evoluem até a solução final, garantindo alinhamento natural entre o processo de desenvolvimento e as técnicas de ER adotadas.

**Disponibilidade limitada do cliente**

A coordenação do CECP é formada por voluntários e o contato ocorre por reuniões periódicas por videoconferência e mensagens. O RAD concentra a participação do cliente em momentos-chave de validação de protótipos, exigindo menos disponibilidade contínua do que o Scrum, que pressupõe um Product Owner presente e feedback a cada sprint.

**Prazo da disciplina e entrega de MVP**

Com um semestre para entregar um MVP funcional, a ênfase do RAD em construção rápida, ciclos curtos e uso de ferramentas de desenvolvimento acelerado favorece a entrega de valor dentro do prazo, priorizando as funcionalidades essenciais ao modelo de funcionamento do CECP.

**Equipe pequena e baixa sobrecarga de gestão**

Por exigir poucos papéis formais e menos cerimônias, o RAD reduz o esforço de coordenação interna, permitindo que uma equipe reduzida de estudantes concentre seu tempo no desenvolvimento e na validação com o cliente, em vez de na manutenção de ritos do processo.

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) | [Rafael Melatti](https://github.com/Romm-0) |