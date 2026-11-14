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
- **GitHub Issues:** utilizado para o registro formal de decisões, aprovações, pendências e solicitações de mudança ao longo do projeto, com labels específicas para categorização (ex.: `decision`, `pending`, `change-request`).

### Disponibilidade do Cliente e Stakeholders

O representante do cliente, Pedro Augusto Cajado Coutinho, confirmou disponibilidade para reuniões via videoconferência nas **segundas, quartas e sextas-feiras, a partir das 17h**, com possibilidade de encontros adicionais aos finais de semana em caso de necessidade.

Ivan (professor de jiu-jitsu do CECP, também envolvido na administração do projeto) e Sandra (dona do projeto/responsável administrativa) confirmaram disponibilidade em **qualquer dia da semana, a partir das 20:30**, com preferência por encontros **presenciais**.

Com base nessa disponibilidade, a equipe adota a seguinte rotina real de reuniões:

- **Reunião de equipe (semanal):** toda semana, para alinhamento interno de progresso e prioridades.
- **Reunião com Pedro (semanal):** uma reunião por semana de desenvolvimento, dentro da janela seg/qua/sex 17h, para apresentar avanços e validar entregas em andamento.
- **Reunião presencial com Ivan e/ou Sandra (quando necessário):** agendada conforme a demanda de validação de funcionalidades ligadas à gestão de turmas (Ivan) ou às decisões administrativas/financeiras (Sandra), aproveitando a disponibilidade noturna presencial de ambos.
- **Validações assíncronas por WhatsApp:** usadas quando um ajuste é pequeno o suficiente para não exigir uma reunião completa (ex.: aprovação de um texto de tela, confirmação de uma regra pontual), evitando sobrecarregar a agenda do cliente com reuniões desnecessárias.

Essa rotina foi desenhada para caber dentro do ritmo real de trabalho da equipe (reuniões internas semanais) sem exigir mais disponibilidade do cliente do que ele já confirmou.

### Registro de Decisões, Aprovações e Mudanças

Todas as decisões, aprovações, pendências e solicitações de mudança são registradas em:

- **Issues do GitHub**, categorizadas por labels específicas;
- **Ata resumida das reuniões** com o cliente, publicada no site do projeto (GitHub Pages), contendo decisões tomadas e pendências em aberto.

## 7.3 Processo de Validação

Esta seção descreve a participação das pessoas na validação. A estratégia de ESW está na [seção 4](4_estrategias_esw.md), as atividades e técnicas de ER na [seção 5](5_engenharia_req.md) e todos os critérios dos acordos na [seção 9](9_dor_e_dod.md).

| Momento | Participantes e atuação | Registro |
|---|---|---|
| Avaliação do protótipo | O analista de requisitos apresenta o fluxo a Pedro e aos stakeholders do tema: Ivan para turmas e Sandra para decisões administrativas e financeiras. A equipe incorpora o retorno antes da construção. | Ata ou gravação e decisão vinculadas à ficha pelo painel |
| Aplicação do DoR | Depois da avaliação do protótipo, a equipe confere o acordo da seção 9.1 no planejamento da iteração, antes de iniciar a construção. | Resultado e evidências na seção 9.3, com referência à ficha e à issue de trabalho |
| Aplicação do DoD | Ao concluir a implementação, o autor e ao menos um revisor conferem o acordo da seção 9.2; Renato acompanha a verificação de qualidade no papel de QA. | Resultado e evidências na seção 9.3; testes de aceite no Andamento da ficha |
| Validação da entrega | Após o DoD, a funcionalidade é apresentada a Pedro e aos usuários envolvidos na reunião seguinte. Aprovação, rejeição ou ajustes são registrados, sem substituir a verificação técnica. | Ata ou gravação e atualização das decisões, pendências e ficha |

Por exemplo, na **matrícula online / pré-matrícula (CP7, pós-MVP)**, a validação deve esclarecer com os representantes do CECP as lacunas da [PEN10](../../painel.md#PEN10), respeitando a assinatura presencial. O exemplo não define uma checklist alternativa nem indica que essa funcionalidade já passou por essas etapas. A aplicação já registrada e suas exceções históricas permanecem na seção 9.3.

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) | [Rafael Melatti](https://github.com/Romm-0) |
| 1.1 | 12/09/2026 | Correções da issue #22: composição da equipe, disponibilidade do cliente, definições de iteração/unidade, registro de decisões, ampliação de stakeholders e processo de validação | Maria Eduarda | — |
| 1.2 | 21/09/2026 | Adição da disponibilidade de Ivan e Sandra e detalhamento dos papéis na ampliação de stakeholders | Maria Eduarda | — |
| 1.3 | 22/09/2026 | Revisão para tornar o documento prático: remoção das definições de iteração/unidade, aplicação concreta de DoR/DoD com exemplo real (matrícula online), e detalhamento da atuação prática do Analista de Requisitos | Maria Eduarda | — |
| 1.4 | 14/11/2026 | Issue #35: critérios concentrados na seção 9; seção 7.3 delimita participação, momento e registro; exemplo corrigido para CP7 | Renato Gameiro | Pendente |
