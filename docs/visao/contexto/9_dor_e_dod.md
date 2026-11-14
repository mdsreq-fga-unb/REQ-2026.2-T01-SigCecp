# 9 DoR e DoD

Esta seção é a fonte única dos dois acordos. A seção 7.3 explica em que momento do fluxo cada um é aplicado, sem repetir os critérios.

## 9.1 Definition of Ready (DoR)

O Definition of Ready (DoR) é o conjunto de critérios que um requisito deve atender para entrar em construção. Ele é verificado na reunião de planejamento da iteração, depois da avaliação do protótipo com o cliente, e o resultado é registrado na seção 9.3.

| # | Critério | Como verificar |
|---|---|---|
| 1 | O requisito está claro e detalhado o suficiente para ser construído | A ficha está em estado Detalhado ou Validado, sem campos "(a detalhar)" nem marcas [PENDENTE], com entradas, regras de negócio e critérios de aceitação em Dado/Quando/Então, e sem pendência aberta no painel. Ser um requisito de produto não basta: ele também precisa ser inequívoco, completo, viável e verificável (ISO/IEC/IEEE 29148) |
| 2 | O protótipo foi aprovado pelo cliente | Ata ou gravação da avaliação e decisão registrada no painel |
| 3 | O requisito cabe na capacidade efetiva da iteração | Na reunião de planejamento, cada membro informa as horas que tem disponíveis na iteração. A soma das estimativas dos itens selecionados, incluindo este, não ultrapassa essa capacidade, já descontadas as demais atividades da disciplina |
| 4 | Nenhuma dependência bloqueia o requisito | Os requisitos de que ele depende (ver Dependências no backlog) estão concluídos ou entram antes na mesma iteração |

## 9.2 Definition of Done (DoD)

O Definition of Done (DoD) é o conjunto de critérios para que um requisito construído seja considerado pronto tecnicamente. Ele é conferido pelo autor e por ao menos um revisor. Um requisito que não cumpra todos os critérios não é levado à validação com o cliente. A validação com o cliente é a etapa seguinte do fluxo (7.3), e não um critério do DoD.

| # | Critério | Como verificar |
|---|---|---|
| 1 | Testes automatizados cobrem o backend | O relatório de cobertura gerado no CI (por exemplo, pytest-cov) mostra cobertura de linhas ≥ 80% no código do backend. Medida separada: 100% dos testes passam |
| 2 | Testes e verificação de estilo rodam no CI | O GitHub Actions executa testes e linters em cada PR, e o PR só é integrado com a execução aprovada |
| 3 | Os critérios de aceitação da ficha foram executados e aprovados | Cada critério é executado no ambiente de homologação. O resultado (aprovado ou reprovado, data e responsável) é registrado na linha Teste de aceite do Andamento da ficha, com link para a evidência |
| 4 | O código foi revisado | O PR foi aprovado por ao menos um membro além do autor |
| 5 | O código segue os padrões da equipe | Python: PEP 8, verificado por linter (por exemplo, ruff ou flake8). HTML, CSS e JavaScript: linter e formatador definidos pela equipe (por exemplo, ESLint e Prettier) |
| 6 | A funcionalidade está documentada | A forma de uso está descrita na documentação do produto |

## 9.3 Aplicação registrada

Cada verificação do DoR e do DoD é registrada aqui, por incremento, com evidência. Um critério sem evidência é marcado como tal, e não como cumprido.

### DoR: conteúdo institucional e eventos (RF13 a RF20)

Verificação feita a partir das evidências publicadas até 14/11/2026. A construção de CP3 começou em 02/11/2026, antes desta verificação; por isso a tabela mostra a situação atual e, quando ela mudou, o que valia na entrada.

| # | Critério | Situação | Evidência |
|---|---|---|---|
| 1 | Claro e detalhado | Cumprido para RF13 a RF16, RF19 e RF20. Não cumprido para RF17 e RF18: a pendência PEN01 (subtítulo do evento) estava aberta; foi encerrada em 14/11/2026 pela DEC27 | Fichas em estado Validado (v1.1); detalhamento de 21/10 |
| 2 | Protótipo aprovado | Cumprido | DEC12, ata 30/10, design do usuário |
| 3 | Cabe na capacidade | Sem evidência: não há registro das horas disponíveis nem das estimativas da iteração | — |
| 4 | Sem dependência bloqueante | Não cumprido para as ações da coordenação (RF13, RF14, RF16 a RF19): elas exigem coordenador autenticado, mas RF01 e RF02 estão previstos só para a Iteração 7. RF15 e RF20 (consulta pública) não têm esse bloqueio | Pré-condições das fichas; cronograma |

Decisão: o cliente liberou a construção a partir de 02/11/2026 (DEC12). Pelo DoR, só RF15 e RF20 estavam prontos sem ressalvas. A equipe resolveu a dependência construindo a autenticação (RF00 a RF02) junto com CP3. A PEN01 foi encerrada em 14/11/2026 (DEC27).

### DoD: acesso e conteúdo institucional e eventos (RF00 a RF02, RF13 a RF20)

Verificação feita a partir das evidências publicadas até 14/11/2026. Nesta iteração, a validação com o cliente ocorreu em 10/11 (ata, DEC19), antes da verificação formal do DoD. A partir da próxima iteração, o DoD é verificado e registrado antes da validação com o cliente.

| # | Critério | Situação | Evidência |
|---|---|---|---|
| 1 | Testes automatizados cobrem o backend | Sem evidência publicada | — |
| 2 | Testes e linters rodam no CI | Sem evidência publicada | — |
| 3 | Critérios de aceitação executados e aprovados | Executados com o cliente na reunião de 10/11; todos os comportamentos testados funcionaram. Falta registrar o resultado de cada critério na ficha | Ata 10/11, seção 4 |
| 4 | Código revisado | Sem evidência publicada | — |
| 5 | Padrões de código | Sem evidência publicada | — |
| 6 | Funcionalidade documentada | Sem evidência publicada | — |

Pendências para fechar o DoD desta entrega: relatório de cobertura, execução do CI, aprovação do PR, saída dos linters, link da documentação de uso e o resultado de cada critério de aceitação registrado na ficha.

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 10/10/2026 | Documento inicial; os critérios foram definidos em reunião da equipe | Rafael Melatti | |
| 1.1 | 14/11/2026 | Issues #30, #31 e #35: DoR critério 1 passa a exigir clareza e detalhamento (não só o nível de abstração); dimensionamento pela capacidade efetiva; DoR verificado após o protótipo; DoD com cobertura medida por relatório no CI, critérios de aceitação executados com resultado registrado, revisão de código e padrões para Python e frontend; aprovação do design movida para o DoR; nova seção 9.3 com a verificação registrada do DoR de CP3 | — | |
| 1.2 | 14/11/2026 | Seção 9.3: DoR de CP3 atualizado e verificação do DoD de acesso e CP3 com a evidência da reunião de 10/11/2026 | — | |
| 1.3 | 14/11/2026 | Seção 9.3: explicita que a validação de 10/11 ocorreu antes da verificação formal do DoD e que, a partir da próxima iteração, o DoD vem antes; registra as pendências de evidência do DoD; esclarece que o DoR de CP3 foi verificado depois do início da construção | Maria Eduarda | |