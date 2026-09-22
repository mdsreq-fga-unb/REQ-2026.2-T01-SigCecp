# 7. Interação entre Equipe e Cliente

## 7.1 Composição da Equipe

| Papel | Descrição | Responsável | Participantes |
|---|---|---|---|
| Líder / Gerente de Projeto | Coordenação geral do projeto, alinhamento com o cliente, gestão de prazos e entregas | Rafael | Rafael |
| Desenvolvedor | Implementação das funcionalidades do sistema | Marcos | Alexandre, Ana, Enzo, Renato, Maria, Rafael, Marcos |
| Analista de QA | Garante a qualidade do produto, executando testes de funcionalidade e usabilidade | Renato | Rafael, Marcos, Maria, Renato |
| Analista de Requisitos | Facilita e registra o processo de descoberta, análise, negociação e validação dos requisitos funcionais e não funcionais junto às fontes relevantes (cliente, professores, usuários), garantindo que sejam documentados e atendidos | Ana | Alexandre, Enzo, Marcos, Renato, Maria, Rafael, Ana |

> **Nota:** A participação nas atividades de Engenharia de Requisitos (elicitação, análise, declaração, representação, verificação e validação) é **mandatória para todos os membros da equipe**, independentemente do papel formal. O Analista de Requisitos facilita e registra esse processo, mas a descoberta, análise, negociação e validação dos requisitos são responsabilidade coletiva da equipe, em conjunto com o cliente e demais stakeholders.

## 7.2 Comunicação

### Ferramentas de Comunicação

- **WhatsApp:** utilizado em dois grupos — um grupo com o cliente, para comunicações rápidas, dúvidas pontuais e confirmações de datas/atividades; e outro grupo com a equipe, para alinhamento interno do dia a dia.
- **Google Meet ou Teams:** utilizado para as reuniões semanais da equipe e para as reuniões com o cliente.
- **Discord:** utilizado eventualmente pela equipe para comunicação interna, com uso reduzido no momento por limitações na transmissão de tela.
- **GitHub Projects:** ferramenta de gerenciamento do backlog, controle de tarefas e acompanhamento do progresso de cada unidade/iteração, permitindo que a equipe visualize o andamento do projeto.
- **GitHub Issues:** utilizado para o registro formal de decisões, aprovações, pendências e solicitações de mudança ao longo do projeto, com labels específicas para categorização (ex.: `decision`, `pending`, `change-request`).

### Definições de Iteração e Unidade

Para eliminar ambiguidades de terminologia:

- **Iteração:** ciclo de desenvolvimento de curta duração, conforme cronograma do processo RAD adotado pela equipe.
- **Unidade:** período avaliativo da disciplina (Unidade 1, 2, 3, 4), que pode conter múltiplas iterações internas.

### Disponibilidade do Cliente

O representante do cliente, Pedro Augusto Cajado Coutinho, confirmou disponibilidade para reuniões via videoconferência nas **segundas, quartas e sextas-feiras, a partir das 17h**, com possibilidade de encontros adicionais aos finais de semana em caso de necessidade.

Essa disponibilidade cobre três janelas semanais, o que permite alinhar pelo menos uma reunião a cada iteração do cronograma do processo RAD, mesmo em ciclos mais curtos, já que o intervalo entre as janelas (2 a 3 dias) é compatível com a duração das iterações previstas.

Para os casos em que uma iteração seja curta demais para uma reunião síncrona (ex.: ajustes pontuais em protótipos já validados), a equipe adota **validações assíncronas** por meio do grupo de WhatsApp com o cliente, permitindo que ele avalie entregas, wireframes ou pequenas mudanças sem a necessidade de uma videoconferência formal. Essas validações assíncronas são registradas como decisões no GitHub Issues, mantendo o mesmo rastreamento das reuniões formais.

### Métodos e Frequência de Reuniões

- **Reunião de Equipe (semanal):** a equipe se reúne semanalmente para alinhamento interno de progresso, obstáculos e prioridades.
- **Reunião com o Cliente (por iteração):** reuniões com o cliente ocorrem dentro da disponibilidade confirmada (segundas, quartas e sextas, 17h), com ao menos um encontro por Unidade acadêmica e reuniões adicionais conforme a necessidade de validação de cada iteração.
- **Retrospectiva (ao final de cada Unidade):** a equipe realiza uma retrospectiva interna, discutindo o que funcionou bem, o que pode ser melhorado e as lições aprendidas no ciclo anterior.

### Ampliação da Interação com Stakeholders

Além do representante Pedro, a interação incluirá, conforme a fase do projeto:

- **Professores do CECP:** consultados durante elicitação e validação de funcionalidades ligadas à gestão de turmas e acompanhamento pedagógico;
- **Responsáveis (famílias):** envolvidos em momentos de validação da experiência de matrícula online (ex.: teste de protótipo do formulário); <!-- Talvez ocorra alteração -->
- **Usuários administrativos (equipe de gestão do CECP):** consultados na validação de fluxos de doações e relatórios.

### Registro de Decisões, Aprovações e Mudanças

Todas as decisões, aprovações, pendências e solicitações de mudança são registradas em:

- **Issues do GitHub**, categorizadas por labels específicas;
- **Ata resumida das reuniões** com o cliente, publicada no site do projeto (GitHub Pages), contendo decisões tomadas e pendências em aberto.

## 7.3 Processo de Validação

O processo de validação segue a lógica do processo RAD, ocorrendo em múltiplos momentos ao longo do desenvolvimento, não apenas ao final:

1. **Durante a Elicitação e Análise:** requisitos de alto nível são levantados junto às fontes relevantes (cliente, professores, responsáveis, usuários administrativos). O Analista de Requisitos facilita e registra esse processo — os requisitos são descobertos, negociados e validados de forma colaborativa, não definidos unilateralmente pelo analista.
2. **Definition of Ready (DoR):** antes de iniciar o desenvolvimento de uma funcionalidade, o DoR é utilizado para verificar se os critérios de aceitação já definidos na etapa de elicitação/análise estão claros e documentados. O DoR não é o momento de criar esses critérios, apenas de confirmar que já existem.
3. **Avaliação de Protótipos:** protótipos e wireframes são validados com o cliente e demais stakeholders relevantes durante a construção, permitindo ajustes antes da implementação final — essa é a principal etapa de validação de conteúdo do processo RAD.
4. **Definition of Done (DoD) e Testes Internos:** confirmam a verificação técnica da funcionalidade (implementação correta, sem bugs, conforme especificado), mas não substituem a validação com os usuários reais.
5. **Validação Final com Usuários:** após passar pelo DoD, a funcionalidade é apresentada para validação com o cliente e, quando aplicável, com professores, responsáveis e usuários administrativos, confirmando que o requisito atende à necessidade real, não apenas à especificação técnica.

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) | [Rafael Melatti](https://github.com/Romm-0) |
| 1.1 | 12/09/2026 | [Unidade 1 - Interação Entre Equipe e Cliente #22](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/issues/22) | [Maria Eduarda](https://github.com/Mariaeduardara) | [Rafael Melatti](https://github.com/Romm-0) |