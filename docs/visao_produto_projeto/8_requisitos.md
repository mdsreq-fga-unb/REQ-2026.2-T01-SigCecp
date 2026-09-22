# 8. Requisitos Funcionais (RF) e Não Funcionais (RNF) - CECP

Derivados das Características de Produto (CP1 a CP6) da seção 2.3 do documento de Visão do Produto e Projeto.

## 8.1 Requisitos Funcionais - RFs

### CP1 - Gestão e acompanhamento de turmas

**RF01 - Cadastrar turma:** deve ser possível à coordenação cadastrar uma nova turma, informando modalidade, horário e capacidade máxima de alunos.

**RF02 - Editar turma:** deve ser possível à coordenação editar os dados de uma turma já cadastrada.

**RF03 - Inativar turma:** deve ser possível à coordenação inativar uma turma, preservando o histórico de alunos e frequências vinculados a ela, sem excluir os registros do sistema.

**RF04 - Associar aluno à turma:** deve ser possível à coordenação associar ou remover um aluno de uma turma.

### CP2 - Registro de doações e prestação de contas

**RF05 - Registrar doação recebida:** deve ser possível à coordenação registrar uma doação recebida (bem, ofício ou repasse de parceria), identificando o doador/parceiro e o recurso recebido.

**RF06 - Registrar documentos de prestação de contas:** deve ser possível à coordenação registrar os documentos utilizados na prestação de contas (orçamento, nota fiscal, fotos/vídeos de comprovação), vinculados a uma solicitação.

**RF07 - Consultar doações e prestações de contas:** deve ser possível à coordenação consultar o histórico consolidado de doações e prestações de contas registradas em um determinado período.

### CP3 - Gestão de conteúdo institucional

**RF08 - Publicar conteúdo institucional:** deve ser possível à coordenação publicar e editar conteúdos institucionais (informações da ONG, fotos e vídeos) no módulo público.

**RF09 - Publicar evento:** deve ser possível à coordenação publicar um evento ou campeonato, informando data e descrição.

**RF10 - Consultar conteúdo institucional:** deve ser possível a qualquer visitante consultar as informações institucionais publicadas, sem necessidade de login.

### CP4 - Cadastro e histórico de alunos

**RF11 - Cadastrar aluno:** deve ser possível à coordenação cadastrar um novo aluno, registrando seus dados pessoais, como: -------------------------------------------------------------------- e a documentação exigida.

**RF12 - Consultar ficha do aluno:** deve ser possível à coordenação consultar a ficha de um aluno, incluindo seu histórico de participação em turmas.

**RF13 - Inativar aluno:** deve ser possível à coordenação marcar um aluno como inativo/ex-aluno, preservando seu histórico no sistema.

### CP5 - Acompanhamento pedagógico e disciplinar do aluno

**RF14 - Registrar frequência:** deve ser possível ao professor/coordenação registrar a frequência dos alunos em cada aula de uma turma.

**RF15 - Consultar frequência:** deve ser possível à coordenação consultar o histórico de frequência de um aluno.

**RF16 - Emitir alerta de faltas críticas:** o sistema deve gerar um notificação no sistema para a coordenação quando um aluno atingir um número crítico de faltas recorrentes (parâmetro configurável).

**RF17 - Registrar medida disciplinar:** deve ser possível à coordenação registrar uma medida disciplinar aplicada a um aluno (advertência, suspensão ou desligamento), vinculada ao seu histórico.

### CP6 - Comunicação com voluntários e famílias

**RF18 - Publicar aviso:** deve ser possível à coordenação publicar um aviso geral na parte publíca do sistema direcionado para os voluntários e/ou familiares.x

## 8.2 Requisitos Não Funcionais - RNFs

Os requisitos não funcionais foram classificados segundo o modelo URPS+ (Usabilidade, Confiabilidade, Desempenho, Suportabilidade e Segurança), permitindo rastreabilidade e avaliação objetiva de qualidade.

> **Ações críticas:** operações que podem alterar significativamente os dados ou registros do sistema, afetar o histórico dos usuários ou gerar consequências administrativas, exigindo confirmação ou feedback explícito ao usuário.

### Usabilidade (U)

| ID | Descrição | Critério de Aceitação |
|---|---|---|
| RNF01 | Interface que permite ao usuário realizar tarefas sem precisar de muito tempo de aprendizado ou treinamento para voluntários sem experiência técnica (CP1, CP3, CP4, CP5) | Usuários novatos no sistema deverão conseguir realizar as tarefas após de se familiarizarem com o sistema por no máximo 8 minutos. 80% dos usuários devem cumprir as tarefas para ser aceito. |
| RNF02 | O módulo público deve adaptar sua interface ao tamanho da tela, mantendo a legibilidade e a organização dos conteúdos em diferentes resoluções.| Conteúdos de divulgação institucional devem ser exibidos sem sobreposição ou corte em resoluções ≥ 360px. |
| RNF03 | Feedback ao usuário em ações críticas, como registrar frequência, aplicar medida disciplinar e inativar aluno ou turma. | Mensagem de sucesso/erro exibida em até 2s após a ação (ex.: registrar frequência, aplicar medida disciplinar) |

### Confiabilidade (R - Reliability)

| ID | Descrição | Critério de Aceitação |
|---|---|---|
| RNF04 | Preservação de histórico ao inativar turma (CP1) ou aluno (CP5) | Registros preservados no banco após a inativação, permanecendo consultáveis na ficha/histórico |
| RNF05 | O sistema deve solicitar confirmação antes da execução de ações críticas que possam alterar ou inativar registros relevantes. | Caixa de confirmação exibida antes de inativar turma, inativar aluno ou registrar medida disciplinar |

### Desempenho (P - Performance)

| ID | Descrição | Critério de Aceitação |
|---|---|---|
| RNF06 | Resposta das consultas internas em até 3s (ficha do aluno, frequência, turmas) | P95 das requisições autenticadas ≤ 3s sob carga normal |
| RNF07 | Carregamento da página pública em até 5s (CP2, CP3) | LCP ≤ 5s em conexão 3G, medido pelo Lighthouse |
| RNF08 | O sistema deve suportar o acesso simultâneo de usuários autenticados sem ultrapassar os limites de desempenho definidos para as operações internas. | Com 10 sessões autenticadas simultâneas, o P95 das requisições deve permanecer ≤ 3s sob carga normal. |

### Suportabilidade (S)

| ID | Descrição | Critério de Aceitação |
|---|---|---|
| RNF09 | Logs de operações críticas | Toda criação, edição e inativação (turma, aluno, doação, medida disciplinar) registrada com timestamp e usuário responsável |
| RNF10 |O sistema deve utilizar padrões e tecnologias web atuais e amplamente adotados, garantindo compatibilidade com navegadores modernos. | Compatível com Chrome, Firefox e Safari nas últimas 2 versões |

### + Segurança
 
| ID | Descrição | Critério de Aceitação |
|---|---|---|
| RNF11 | Controle de acesso por perfil (coordenação, professor/voluntário, família) | Rotas administrativas retornam 401/403 para requisições sem perfil autorizado |
| RNF12 | Senhas com hash e dados sensíveis criptografados | Nenhuma senha armazenada em texto claro; auditoria por inspeção de banco |
| RNF13 | O sistema deve tratar os dados pessoais de acordo com os princípios, direitos dos titulares e requisitos de segurança e tratamento estabelecidos pela Lei nº 13.709/2018 (LGPD). | O sistema deve permitir o atendimento às solicitações aplicáveis dos titulares ou responsáveis legais relacionadas aos seus dados pessoais, incluindo solicitação de eliminação quando cabível, além de classificar e proteger dados pessoais sensíveis conforme a LGPD|


## 8.3 Matriz-síntese de rastreabilidade - CECP

A matriz a seguir apresenta a rastreabilidade entre OE (Objetivos Específicos), CP (Características do Produto), RF (Requisitos Funcionais) e RNF (Requisitos Não Funcionais).

| Contribuição principal | Contribuição secundária | **CP** (Características do Produto) | **RFs** relacionados (Requisitos Funcionais) | **RNFs** relacionados (Requisitos Não Funcionais) |
| :--- | :--- | :--- | :--- | :--- |
| **OE2** (Acompanhar frequência e situação pedagógica) | **OE1**, **OE3** (Centralizar dados / Registrar medidas disciplinares) | **CP1** (Gestão e acompanhamento de turmas) | **RF01** (Cadastrar turma), **RF02** (Editar turma), **RF03** (Inativar turma), **RF04** (Associar aluno à turma) | **RNF01** (Interface intuitiva), **RNF03** (Feedback em ações críticas), **RNF04** (Preservação de histórico ao inativar), **RNF05** (Confirmação em ações críticas), **RNF06** (Resposta das consultas internas em até 3s), **RNF11** (Controle de acesso por perfil) |
| **OE5** (Transparência e prestação de contas) | **OE1** (Centralizar dados dos alunos) | **CP2** (Registro de doações e prestação de contas) | **RF05** (Registrar doação recebida), **RF06** (Registrar documentos de prestação de contas), **RF07** (Consultar doações e prestações de contas) | **RNF01** (Interface intuitiva), **RNF02** (Responsividade do módulo público), **RNF03** (Feedback em ações críticas), **RNF07** (Carregamento da página pública em até 5s), **RNF11** (Controle de acesso por perfil) |
| **OE4** (Melhorar comunicação com voluntários e famílias) | **OE5** (Transparência e prestação de contas) | **CP3** (Gestão de conteúdo institucional) | **RF08** (Publicar conteúdo institucional), **RF09** (Publicar evento), **RF10** (Consultar conteúdo institucional) | **RNF02** (Responsividade do módulo público), **RNF07** (Carregamento da página pública em até 5s) |
| **OE1** (Centralizar dados dos alunos) | - | **CP4** (Cadastro e histórico de alunos) | **RF11** (Cadastrar aluno), **RF12** (Consultar ficha do aluno), **RF13** (Inativar aluno) | **RNF01** (Interface intuitiva), **RNF04** (Preservação de histórico ao inativar), **RNF05** (Confirmação em ações críticas), **RNF06** (Resposta das consultas internas em até 3s), **RNF11** (Controle de acesso por perfil), **RNF13** (Conformidade com a LGPD) |
| **OE2** (Acompanhar frequência e situação pedagógica) | **OE3** (Registrar medidas disciplinares) | **CP5** (Acompanhamento pedagógico e disciplinar do aluno) | **RF14** (Registrar frequência), **RF15** (Consultar frequência), **RF16** (Emitir alerta de faltas críticas), **RF17** (Registrar medida disciplinar) | **RNF01** (Interface intuitiva), **RNF03** (Feedback em ações críticas), **RNF05** (Confirmação em ações críticas), **RNF06** (Resposta das consultas internas em até 3s), **RNF11** (Controle de acesso por perfil) |
| **OE4** (Melhorar comunicação com voluntários e famílias) | - | **CP6** (Comunicação com voluntários e famílias) | **RF18** (Publicar aviso) | - *(apenas RNFs transversais - ver nota abaixo)* |

## Nota - RNFs transversais (aplicáveis a todas as CPs)

Os RNFs a seguir não constam nas linhas acima por serem exigências de qualidade do sistema como um todo, e não de uma CP específica:

- **RNF08** - Suportar acesso concorrente
- **RNF09** - Logs de operações críticas
- **RNF10** - Padrões web modernos (compatibilidade de navegador)
- **RNF12** - Senhas com hash e dados sensíveis criptografados