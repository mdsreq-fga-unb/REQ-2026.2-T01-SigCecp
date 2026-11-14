# 9 DoR e DoD

Esta seção é a fonte única dos dois acordos. A seção 7.3 explica em que momento do fluxo cada um é aplicado, sem repetir os critérios.

## 9.1 Definition of Ready (DoR)

O Definition of Ready (DoR) é o conjunto de critérios que um requisito deve atender para entrar em construção. Ele é verificado na reunião de planejamento da iteração, depois da avaliação do protótipo com o cliente, e o resultado é registrado na seção 9.3.

| # | Critério | Como verificar |
|---|---|---|
| 1 | O requisito está claro e detalhado o suficiente para ser construído | A ficha está em estado Detalhado ou Validado, sem campos "(a detalhar)" nem marcas [PENDENTE], com entradas, regras de negócio e critérios de aceitação em Dado/Quando/Então, e sem pendência aberta no painel. Ser um requisito de produto não basta: ele também precisa ser inequívoco, completo, viável e verificável (ISO/IEC/IEEE 29148) |
| 2 | O protótipo foi aprovado pelo cliente | Ata ou gravação da avaliação e decisão registrada no painel |
| 3 | O requisito cabe na capacidade efetiva da iteração | Na reunião de planejamento, cada membro informa as horas que tem disponíveis na iteração. A soma das estimativas dos itens selecionados, incluindo este, não ultrapassa essa capacidade, já descontadas as demais atividades da disciplina |
| 4 | Nenhuma dependência bloqueia o requisito | Os requisitos de que ele depende, identificados nas pré-condições e regras da ficha e confrontados com o cronograma no painel, estão concluídos ou entram antes na mesma iteração |

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

!!! warning "Fontes a reconciliar — PEN12"
    A versão anterior desta seção cita DEC19, DEC27 e uma ata de 10/11 que não foram localizadas no catálogo de decisões nem nas atas publicadas na branch nesta revisão. Os relatos anteriores são preservados abaixo como relatos, sem comprovar execução ou aprovação. A [PEN12](../../painel.md#PEN12) registra a busca das fontes e a conciliação com as fichas; não se atribuem novas decisões ao cliente.

### DoR: conteúdo institucional e eventos (RF13 a RF20)

O registro anterior, datado de 14/11/2026, situa o início da construção de CP3 em 02/11/2026, antes da verificação formal. A DEC12 comprova a liberação para começar nessa data, não a execução; a evidência do início efetivo deve ser vinculada pela PEN12. A tabela preserva a avaliação registrada e explicita suas lacunas documentais.

| # | Critério | Situação | Evidência |
|---|---|---|---|
| 1 | Claro e detalhado | O registro anterior considera cumprido para RF13 a RF16, RF19 e RF20. Para RF17 e RF18, a PEN01 (subtítulo do evento) permanece aberta no catálogo; o encerramento antes atribuído à DEC27 não tem fonte publicada localizada | Fichas em estado Validado (v1.1); detalhamento de 21/10; PEN01 e PEN12 |
| 2 | Protótipo aprovado | Cumprido | DEC12, ata 30/10, design do usuário |
| 3 | Cabe na capacidade | Sem evidência: não há registro das horas disponíveis nem das estimativas da iteração | — |
| 4 | Sem dependência bloqueante | Não cumprido para as ações da coordenação (RF13, RF14, RF16 a RF19): elas exigem coordenador autenticado, mas RF01 e RF02 estão previstos só para a Iteração 7. RF15 e RF20 (consulta pública) não têm esse bloqueio | Pré-condições das fichas; cronograma |

A liberação do cliente para construir a partir de 02/11/2026 está registrada na DEC12. RF15 e RF20 não apresentam o bloqueio de autenticação, mas a ausência de evidência de capacidade impede afirmar cumprimento integral do DoR. O registro anterior relata que a autenticação (RF00 a RF02) foi construída junto com CP3; a evidência dessa execução ainda precisa ser vinculada (PEN12). A PEN01 permanece aberta, sem confirmação documental de encerramento pela DEC27.

### DoD: acesso e conteúdo institucional e eventos (RF00 a RF02, RF13 a RF20)

O registro anterior, datado de 14/11/2026, relata validação com o cliente em 10/11, antes da verificação formal do DoD, citando ata e DEC19. Essas fontes não foram localizadas entre os documentos publicados nesta revisão (PEN12); o relato não é uma nova comprovação de validação. Preserva-se a orientação já registrada: a partir da próxima iteração, o DoD deve ser verificado e registrado antes da validação com o cliente.

| # | Critério | Situação | Evidência |
|---|---|---|---|
| 1 | Testes automatizados cobrem o backend | Sem evidência publicada | — |
| 2 | Testes e linters rodam no CI | Sem evidência publicada | — |
| 3 | Critérios de aceitação executados e aprovados | Relato anterior de execução com o cliente em 10/11, com funcionamento dos comportamentos testados. Sem comprovação publicada localizada; falta o resultado de cada critério na ficha | Referência anterior: ata 10/11, seção 4, e DEC19; fontes a localizar pela PEN12 |
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
| 1.4 | 14/11/2026 | Issue #35: distingue relato histórico de evidência publicada; explicita lacunas de DEC19/DEC27/ata 10/11, mantém PEN01 aberta e referencia dependências nas fichas | Renato Gameiro | Pendente |
