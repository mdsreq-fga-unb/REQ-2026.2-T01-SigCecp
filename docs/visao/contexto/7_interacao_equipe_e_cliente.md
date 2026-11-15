# 7. Interação entre Equipe e Cliente

## 7.1 Composição da Equipe

| Papel | Descrição | Responsável | Participantes |
|---|---|---|---|
| Líder / Gerente de Projeto | Coordenação geral do projeto, alinhamento com o cliente, gestão de prazos e entregas | Rafael | Rafael |
| Desenvolvedor | Implementação das funcionalidades do sistema | Marcos | Alexandre, Ana, Enzo, Renato, Maria, Rafael, Marcos |
| Analista de QA | Garante a qualidade do produto, executando testes de funcionalidade e usabilidade | Renato | Rafael, Marcos, Maria, Renato |
| Analista de Requisitos | Facilita e registra o processo de descoberta, análise, negociação e validação dos requisitos junto às fontes relevantes | Ana | Alexandre, Enzo, Marcos, Renato, Maria, Rafael, Ana |

> **Nota:** A participação nas atividades de Engenharia de Requisitos é mandatória para todos os membros da equipe.

## 7.2 Comunicação

### Ferramentas de Comunicação

- **WhatsApp:** utilizado em dois grupos — um grupo com o cliente, para comunicações rápidas, dúvidas pontuais e confirmações de datas/atividades; e outro grupo com a equipe, para alinhamento interno do dia a dia.
- **Google Meet ou Teams:** utilizado para as reuniões semanais da equipe e para as reuniões com o cliente.
- **Discord:** utilizado eventualmente pela equipe para comunicação interna, com uso reduzido no momento por limitações na transmissão de tela.
- **GitHub Projects:** ferramenta de gerenciamento do backlog, controle de tarefas e acompanhamento do progresso do projeto.
- **GitHub Issues:** utilizado para as tarefas de construção de cada RF do MVP.

### Disponibilidade do Cliente e Stakeholders

O representante do cliente, Pedro Augusto Cajado Coutinho, confirmou disponibilidade para reuniões via videoconferência nas **segundas, quartas e sextas-feiras, a partir das 17h**, com possibilidade de encontros adicionais aos finais de semana em caso de necessidade.

Ivan (professor de jiu-jitsu do CECP, também envolvido na administração do projeto) e Sandra (dona do projeto/responsável administrativa) confirmaram disponibilidade em **qualquer dia da semana, a partir das 20:30**, com preferência por encontros **presenciais**.

Com base nessa disponibilidade, a equipe planejou a seguinte rotina de reuniões:

- **Reunião de equipe (planejada como semanal):** para alinhamento interno de progresso e prioridades.
- **Reunião com Pedro (planejada como semanal):** dentro da janela seg/qua/sex 17h, para apresentar avanços e validar entregas em andamento.
- **Reunião presencial com Ivan e/ou Sandra (quando necessário):** agendada conforme a demanda de validação de funcionalidades ligadas à gestão de turmas (Ivan) ou às decisões administrativas/financeiras (Sandra), aproveitando a disponibilidade noturna presencial de ambos.
- **Validações assíncronas por WhatsApp:** usadas quando um ajuste é pequeno o suficiente para não exigir uma reunião completa (ex.: aprovação de um texto de tela, confirmação de uma regra pontual), evitando sobrecarregar a agenda do cliente com reuniões desnecessárias.

Na prática, a frequência semanal não se manteve. As reuniões com o cliente registradas em ata são as de 17/09, 22/09, 24/09, 26/09, 08/10, 21/10, 30/10 e 10/11/2026, concentradas nos marcos de elicitação, priorização, detalhamento, avaliação de protótipo e teste de aceite; na Iteração 4 não houve reunião com o cliente. As reuniões de equipe têm ata até 26/09/2026. As datas previstas para as próximas reuniões com o cliente estão na coluna de reuniões do [cronograma](../../cronograma/6_cronograma.md).

### Registro de Decisões, Aprovações e Mudanças

Cada tipo de registro tem um lugar só:

- **Decisões e pendências** (DEC e PEN): na página de [decisões e pendências](../escopo/decisoes.md), que alimenta o [painel do escopo](../../painel.md). Uma mudança no escopo pedida pelo cliente também é registrada ali, como decisão;
- **Aprovações e testes do cliente**: na **ata** da reunião, publicada no site do projeto, e na seção *Andamento* da ficha de cada requisito, que aponta para essa ata;
- **Tarefas de construção**: nas **Issues do GitHub**.

## 7.3 Processo de Validação

Esta seção explica **quando** cada acordo é aplicado e quem participa. Os critérios do DoR e do DoD estão definidos uma única vez, na [seção 9](9_dor_e_dod.md); aqui eles apenas são referenciados.

### Fluxo por incremento

| # | Etapa | Responsável planejado (7.1) | Participação registrada até agora | Resultado |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Detalhamento com o cliente | Analista de Requisitos (Ana) | Marcos conduziu todas as reuniões com o cliente registradas em ata (17/09 a 10/11) | Ficha do requisito em estado *Detalhado*, regras de negócio e decisões registradas |
| 2 | Protótipo | Desenvolvedores | Marcos (protótipos de CP3 e das demais telas do MVP) | Telas por requisito |
| 3 | Avaliação do protótipo com o cliente | Analista de Requisitos | Marcos e Pedro (30/10 e 10/11) | Protótipo aprovado ou ajustado; decisões registradas |
| 4 | Verificação do [DoR](9_dor_e_dod.md#91-definition-of-ready-dor) | Equipe, na reunião de planejamento | — | Requisito liberado para construção |
| 5 | Construção | Desenvolvedores | — | Incremento implementado |
| 6 | Verificação do [DoD](9_dor_e_dod.md#92-definition-of-done-dod) | Analista de QA (Renato) e um revisor | — | Critérios de aceitação executados, com resultado registrado |
| 7 | Validação com o cliente | Analista de Requisitos | Marcos e Pedro (10/11) | Cliente confirma (ou não) que o comportamento implementado atende à necessidade |

O DoR é verificado **depois** da avaliação do protótipo, porque um de seus critérios é o protótipo aprovado pelo cliente.

A coluna "Participação registrada" mostra quem de fato aparece nas atas. A divisão de papéis da seção 7.1 é o planejamento, e não a prova de que cada pessoa executou a etapa.

### Aplicação ao primeiro incremento (CP3)

Para RF13 a RF20 (conteúdo institucional e eventos), as etapas 1, 2, 3, 5 e 7 têm evidência em [4.4](4_estrategias_esw.md#44-ciclo-do-rad-aplicado-a-um-incremento): o cliente testou e aceitou o incremento em 10/11. A verificação do DoR e do DoD está na [seção 9.3](9_dor_e_dod.md#93-aplicacao-registrada).

O mesmo fluxo se repete para as demais características do MVP (CP1 e CP4, além do acesso), ajustando quais stakeholders participam: Ivan para turmas e Sandra para decisões administrativas.

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) | [Rafael Melatti](https://github.com/Romm-0) |
| 1.1 | 12/09/2026 | Correções da issue #22: composição da equipe, disponibilidade do cliente, definições de iteração/unidade, registro de decisões, ampliação de stakeholders e processo de validação | Maria Eduarda | — |
| 1.2 | 21/09/2026 | Adição da disponibilidade de Ivan e Sandra e detalhamento dos papéis na ampliação de stakeholders | Maria Eduarda | — |
| 1.3 | 22/09/2026 | Revisão para tornar o documento prático: remoção das definições de iteração/unidade, aplicação concreta de DoR/DoD com exemplo real (matrícula online), e detalhamento da atuação prática do Analista de Requisitos | Maria Eduarda | — |
| 1.4 | 14/11/2026 | Corrigida referência da seção 7.3: "matrícula online (CP2)" passou a "matrícula online (CP7)" — CP2 é Registro de doações e prestação de contas, não matrícula | — | — |
| 1.5 | 14/11/2026 | Issues #26, #30, #31 e #35: 7.3 reescrita como fluxo por incremento que referencia o DoR e o DoD da seção 9 (sem checklists paralelos); DoR passa a vir depois da avaliação do protótipo; responsabilidade planejada separada da participação registrada nas atas; exemplo hipotético da matrícula substituído pelo incremento real de CP3 | — | — |
| 1.6 | 14/11/2026 | Participação registrada e aplicação a CP3 atualizadas com a reunião de 10/11/2026 | — | — |
| 1.7 | 14/11/2026 | Rotina de reuniões: a frequência semanal passa a ser a planejada, e o texto registra as reuniões que de fato ocorreram | — | — |
| 1.8 | 14/11/2026 | Registro de decisões: decisões e pendências ficam na página de decisões e no painel, aprovações nas atas e nas fichas, e as Issues do GitHub ficam para as tarefas de construção | — | — |
