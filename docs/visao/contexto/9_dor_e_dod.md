# 9 DoR e DoD

Esta seção é a **fonte única** dos dois acordos. A [seção 7.3](7_interacao_equipe_e_cliente.md#73-processo-de-validacao) explica em que momento do fluxo cada um é aplicado, sem repetir os critérios.

## 9.1 Definition of Ready (DoR)

O **Definition of Ready (DoR)** é o conjunto de critérios que um requisito deve atender para entrar em construção. Ele é verificado na reunião de planejamento da iteração, **depois** da avaliação do protótipo com o cliente, e o resultado é registrado na seção 9.3.

| # | Critério | Como verificar |
|---|---|---|
| 1 | O requisito está claro e detalhado o suficiente para ser construído | A ficha está em estado *Detalhado* ou *Validado*, sem campos "(a detalhar)" nem marcas [PENDENTE], com entradas, regras de negócio e critérios de aceitação em Dado/Quando/Então, e sem pendência aberta no painel. Ser um requisito de produto não basta: ele também precisa ser inequívoco, completo, viável e verificável (ISO/IEC/IEEE 29148) |
| 2 | O protótipo foi aprovado pelo cliente | Ata ou gravação da avaliação com a aprovação do cliente, citada na linha *Design do usuário* do *Andamento* da ficha |
| 3 | O requisito cabe na capacidade efetiva da iteração | Na reunião de planejamento, cada membro informa as horas que tem disponíveis na iteração. A soma das estimativas dos itens selecionados, incluindo este, não ultrapassa essa capacidade, já descontadas as demais atividades da disciplina |
| 4 | Nenhuma dependência bloqueia o requisito | Os requisitos de que ele depende (ver *Dependências* no [backlog](../../historico/10_backlog_produto.md)) estão concluídos ou entram antes na mesma iteração |

## 9.2 Definition of Done (DoD)

O **Definition of Done (DoD)** é o conjunto de critérios para que um requisito construído seja considerado pronto tecnicamente. Ele é conferido pelo autor e por ao menos um revisor. Um requisito que não cumpra todos os critérios não é levado à validação com o cliente. A validação com o cliente é a etapa seguinte do fluxo (7.3), e não um critério do DoD.

| # | Critério | Como verificar |
|---|---|---|
| 1 | Testes automatizados cobrem o backend | O relatório de cobertura gerado no CI (por exemplo, pytest-cov) mostra cobertura de linhas ≥ 80% no código do backend. Medida separada: 100% dos testes passam |
| 2 | Testes e verificação de estilo rodam no CI | O GitHub Actions executa testes e linters em cada PR, e o PR só é integrado com a execução aprovada |
| 3 | Os critérios de aceitação da ficha foram executados e aprovados | Cada critério é executado no ambiente de homologação. O resultado (aprovado ou reprovado, data e responsável) é registrado na linha *Teste de aceite* do *Andamento* da ficha, com link para a evidência |
| 4 | O código foi revisado | O PR foi aprovado por ao menos um membro além do autor |
| 5 | O código segue os padrões da equipe | Python: PEP 8, verificado por linter (por exemplo, ruff ou flake8). HTML, CSS e JavaScript: linter e formatador definidos pela equipe (por exemplo, ESLint e Prettier) |
| 6 | A funcionalidade está documentada | A forma de uso está descrita na documentação do produto |

## 9.3 Aplicação registrada

Cada verificação do DoR e do DoD é registrada aqui, por incremento, com evidência. Um critério sem evidência é marcado como tal, e não como cumprido.

### DoR: conteúdo institucional e eventos (RF13 a RF20)

Verificação feita a partir das evidências publicadas até 14/11/2026. A construção de CP3 começou em 02/11/2026, antes desta verificação; por isso a tabela mostra a situação atual e, quando ela mudou, o que valia na entrada.

| # | Critério | Situação | Evidência |
|---|---|---|---|
| 1 | Claro e detalhado | Cumprido para RF13 a RF16, RF19 e RF20. Para RF17 e RF18, cumprido depois do encerramento da [PEN01](../../painel.md#PEN01) | Fichas em estado *Validado*; [detalhamento de 21/10](../../historico/detalhamento_iteracao5.md); [DEC27](../../painel.md#DEC27) |
| 2 | Protótipo aprovado | Cumprido | [ata 30/10](../../historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_30_10.md), [design do usuário](../../historico/designUser_iteracao5.md) |
| 3 | Cabe na capacidade | **Sem evidência**: não há registro das horas disponíveis nem das estimativas da iteração | — |
| 4 | Sem dependência bloqueante | **Não cumprido para as ações da coordenação** (RF13, RF14, RF16 a RF19): elas exigem coordenador autenticado, mas RF01 e RF02 estão previstos só para a Iteração 7. RF15 e RF20 (consulta pública) não têm esse bloqueio | Pré-condições das fichas; [cronograma](../../cronograma/6_cronograma.md) |

A dependência do critério 4 foi tratada construindo a autenticação (RF00 a RF02) junto com CP3.

### DoD: acesso, conteúdo institucional e eventos (RF00 a RF02, RF13 a RF20)

Verificação feita a partir das evidências publicadas até 14/11/2026. Nesta iteração, a validação com o cliente ocorreu em 10/11 ([ata](../../historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_10_11.md)), antes da verificação formal do DoD. A partir da próxima iteração, o DoD é verificado e registrado antes da validação com o cliente.

| # | Critério | Situação | Evidência |
|---|---|---|---|
| 1 | Testes automatizados cobrem o backend | Cumprido 289 testes passaram e ouveram 7 erros esperados | [PR #63](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/pull/63/checks) / [Execução CI](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/actions/runs/43797081941) |
| 2 | Testes e linters rodam no CI | Cumprido: suíte de testes e verificação PEP 8 executadas e aprovadas no GitHub Actions |[PR #63](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/pull/63/checks) / [Execução CI](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/actions/runs/43797081941)|
| 3 | Critérios de aceitação executados e aprovados | Executados com o cliente na reunião de 10/11; todos os comportamentos testados funcionaram. Falta registrar o resultado de cada critério na ficha | [Ata 10/11](../../historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_10_11.md), seção 4 |
| 4 | Código revisado |Cumprido: PR revisado e aprovado por [Alexandre](https://github.com/El-flipante), [Enzo](https://github.com/enzocostaj) e [Marcos](https://github.com/MontMarcos) também foi produzido em par programin com [Ana Paula](https://github.com/beibeharry) | [PR #63](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/pull/63) |
| 5 | Padrões de código | Cumprido: linter PEP 8 (ruff) aprovado sem erros na pipeline do PR |[Execução CI](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/actions/runs/43797081941)|
| 6 | Funcionalidade documentada | Cumprido: configuração, rotas e regras de autenticação (seção 13), eventos (seções 6 a 8) e conteúdo institucional (seção 14) descritas |Seções 6–8, 13 e 14 do `read.me` na branch `iteração_oito`|

**Pendências para fechar o DoD desta entrega:** relatório de cobertura, execução do CI, aprovação do PR, saída dos linters, link da documentação de uso e o resultado de cada critério de aceitação registrado na ficha.

### DoR: turmas (RF03, RF06 e RF07)

Verificação feita em 14/11/2026, depois da construção da Iteração 8. Como no registro de CP3, a tabela mostra a situação na entrada da construção.

| # | Critério | Situação | Evidência |
|---|---|---|---|
| 1 | Claro e detalhado | Cumprido. As pendências desses RFs foram encerradas pela [DEC23](../../painel.md#DEC23), pela [DEC24](../../painel.md#DEC24) e pela [DEC33](../../painel.md#DEC33) | Fichas em estado *Validado* |
| 2 | Protótipo aprovado | Cumprido | [ata 10/11](../../historico/organizacao_e_planejamento/atas_reunioes/cliente/ata_reuniao_10_11.md) |
| 3 | Cabe na capacidade | **Sem evidência**: não há registro das horas disponíveis nem das estimativas da iteração | — |
| 4 | Sem dependência bloqueante | Cumprido para RF03. **Não cumprido para RF06**, que depende do cadastro de alunos (RF21), previsto para a Iteração 10, nem para RF07, que depende do RF06 | [Backlog](../../historico/10_backlog_produto.md), seção 10.3 |

A dependência do critério 4 foi tratada assim: RF03 e RF07 foram concluídos com alunos de exemplo, e o RF06 só termina junto com o RF21 ([DEC33](../../painel.md#DEC33)).

### DoD: turmas (RF03, RF06 e RF07)

Verificação feita em 14/11/2026, antes da validação com o cliente, como previsto. O RF06 está construído só em parte e por isso não entra nesta verificação até ser concluído com o RF21.

| # | Critério | Situação | Evidência |
|---|---|---|---|
| 1 | Testes automatizados cobrem o backend | **Em parte**: há testes automatizados de turmas, e toda a suíte passa; a cobertura de linhas não foi medida | [PR #63](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/pull/63/checks) / [Execução CI](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/actions/runs/43797081941) |
| 2 | Testes e linters rodam no CI |  Cumprido: suíte de testes e verificação PEP 8 executadas e aprovadas no GitHub Actions |[PR #63](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/pull/63/checks) / [Execução CI](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/actions/runs/43797081941)|
| 3 | Critérios de aceitação executados e aprovados | **Pendente**: o teste de aceite com o cliente passou para a Iteração 10 ([DEC33](../../painel.md#DEC33)) | Linha *Teste de aceite* das fichas |
| 4 | Código revisado |Cumprido: PR revisado e aprovado por [Alexandre](https://github.com/El-flipante), [Enzo](https://github.com/enzocostaj) e [Marcos](https://github.com/MontMarcos) também foi produzido em par programin com [Ana Paula](https://github.com/beibeharry) | [PR #63](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/pull/63) |
| 5 | Padrões de código | Cumprido: linter PEP 8 (ruff) aprovado sem erros na pipeline do PR |[Execução CI](https://github.com/mdsreq-fga-unb/REQ-2026.2-T01-SigCecp/actions/runs/43797081941)|
| 6 | Funcionalidade documentada | Cumprido: rotas, regras e pendências de turmas descritas | Seção 9 do `readme.md` na branch `iteracao_oito` |

**Pendências para fechar o DoD desta entrega:** relatório de cobertura, execução do CI, aprovação do PR, saída dos linters e o resultado do teste de aceite registrado em cada ficha.

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 10/10/2026 | Documento inicial; os critérios foram definidos em reunião da equipe | [Rafael Melatti](https://github.com/Romm-0) |  |
| 1.1 | 14/11/2026 | Issues #30, #31 e #35: DoR critério 1 passa a exigir clareza e detalhamento (não só o nível de abstração); dimensionamento pela capacidade efetiva; DoR verificado após o protótipo; DoD com cobertura medida por relatório no CI, critérios de aceitação executados com resultado registrado, revisão de código e padrões para Python e frontend; aprovação do design movida para o DoR; nova seção 9.3 com a verificação registrada do DoR de CP3 | — |  |
| 1.2 | 14/11/2026 | Seção 9.3: DoR de CP3 atualizado e verificação do DoD de acesso e CP3 com a evidência da reunião de 10/11/2026 | — |  |
| 1.3 | 14/11/2026 | Seção 9.3: explicita que a validação de 10/11 ocorreu antes da verificação formal do DoD e que, a partir da próxima iteração, o DoD vem antes; registra as pendências de evidência do DoD; esclarece que o DoR de CP3 foi verificado depois do início da construção | [Maria Eduarda](https://github.com/Mariaeduardara) |  |
| 1.4 | 14/11/2026 | Seção 9.3 enxugada: o DoR 1 e o texto depois da tabela do DoR deixam de recontar o que a DEC12, a DEC27 e a PEN01 já registram e passam a apontar para elas | — |  |
| 1.5 | 14/11/2026 | Seção 9.3: verificação do DoR e do DoD de turmas (RF03, RF06 e RF07), da Iteração 8 | — |  |
| 1.6 | 14/11/2026 | DoR critério 2: a evidência da aprovação do protótipo passa a ser a ata citada no *Andamento* da ficha, e não mais uma decisão no painel (as decisões de aprovação foram retiradas) | — |  |
| 1.7 | 15/11/2026 | Atualização da Seção 9.3 (Issues #30 e #31): consolidação das evidências de execução da pipeline no GitHub Actions (testes automatizados e linters de Python e JavaScript), registro dos Pull Requests revisados e aprovados, vinculação da documentação técnica atualizada no readme.md e estruturação do controle de dependências e capacidade para o DoR. | [Maria Eduarda](https://github.com/Mariaeduardara) | [Alexandre](https://github.com/El-flipante) |

