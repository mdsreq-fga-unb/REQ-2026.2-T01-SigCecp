# 8. Requisitos Funcionais (RF) e Não Funcionais (RNF) - CECP

Derivados das Características de Produto (CP1 a CP6) da seção 2.3 do documento de Visão do Produto e Projeto.

## 8.1 Requisitos Funcionais - RFs

### Acesso e controle de usuários

**RF01 - Autenticar usuário:** deve ser possível aos coordenadores acessar o sistema mediante identificação e credenciais válidas.

**RF02 - Controlar acesso por perfil:** o sistema deve disponibilizar as funcionalidades administrativas exclusivamente para usuários autenticados com perfil de coordenador.

### CP1 - Gestão e acompanhamento de turmas

**RF03 - Cadastrar turma:** deve ser possível à coordenação cadastrar uma nova turma, informando modalidade, horário e capacidade máxima de alunos.

**RF04 - Editar turma:** deve ser possível à coordenação editar os dados de uma turma já cadastrada.

**RF05 - Inativar turma:** deve ser possível à coordenação inativar uma turma, preservando o histórico de alunos e frequências vinculados a ela, sem excluir os registros do sistema.

**RF06 - Associar aluno à turma:** deve ser possível à coordenação associar um aluno a uma turma ou remover sua associação, sem excluir seus registros históricos.

### CP2 - Registro de doações e prestação de contas

**RF07 - Registrar doação recebida:** deve ser possível à coordenação registrar uma doação ou recurso recebido, identificando o doador ou parceiro, o tipo de recurso e as informações correspondentes.

**RF08 - Registrar documentos de prestação de contas:** deve ser possível à coordenação registrar documentos utilizados na prestação de contas, como orçamentos, notas fiscais e registros fotográficos ou audiovisuais, vinculando-os à respectiva doação ou recurso recebido.

**RF09 - Consultar doações e prestações de contas:** deve ser possível à coordenação consultar o histórico consolidado de doações e prestações de contas registradas em um determinado período.

### CP3 - Gestão de conteúdo institucional

**RF10 - Publicar conteúdo institucional:** deve ser possível à coordenação publicar e editar conteúdos institucionais, como informações da organização, fotos e vídeos, no módulo público.

**RF11 - Publicar evento:** deve ser possível à coordenação publicar um evento ou campeonato, informando, no mínimo, sua data e descrição.

**RF12 - Consultar conteúdo institucional:** deve ser possível a qualquer visitante consultar as informações institucionais publicadas, sem necessidade de autenticação.

### CP4 - Cadastro e histórico de alunos

**RF13 - Cadastrar aluno:** deve ser possível à coordenação cadastrar um novo aluno, registrando seus dados cadastrais e a documentação exigida pelo CECP.

**RF14 - Editar aluno:** deve ser possível à coordenação atualizar os dados cadastrais de um aluno já registrado, sem excluir seu histórico no sistema.

**RF15 - Consultar ficha do aluno:** deve ser possível à coordenação consultar a ficha de um aluno, incluindo seus dados cadastrais e histórico de participação em turmas.

**RF16 - Inativar aluno:** deve ser possível à coordenação marcar um aluno como inativo ou ex-aluno, preservando seu histórico no sistema.

### CP5 - Acompanhamento pedagógico e disciplinar do aluno

**RF17 - Registrar frequência:** deve ser possível ao professor ou à coordenação registrar a frequência dos alunos em cada aula de uma turma.

**RF18 - Consultar frequência:** deve ser possível à coordenação consultar o histórico de frequência de um aluno.

**RF19 - Emitir alerta de faltas críticas:** o sistema deve gerar uma notificação para a coordenação quando um aluno atingir o número crítico de faltas definido pelo parâmetro configurado.

**RF20 - Registrar medida disciplinar:** deve ser possível à coordenação registrar uma medida disciplinar aplicada a um aluno, como advertência, suspensão ou desligamento, vinculada ao seu histórico.

### CP6 - Comunicação com voluntários e famílias

**RF21 - Publicar aviso:** deve ser possível à coordenação ou à gestão publicar avisos destinados aos voluntários e/ou familiares.

**RF22 - Consultar avisos:** deve ser possível aos voluntários e familiares consultar os avisos destinados a eles no sistema.

**RF23 - Direcionar aviso:** deve ser possível à coordenação ou à gestão direcionar um aviso para voluntários, familiares ou ambos.

**RF24 - Consultar histórico de avisos:** deve ser possível à coordenação ou à gestão consultar os avisos publicados anteriormente, incluindo seus destinatários e data de publicação.

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

A matriz apresenta a rastreabilidade entre os Objetivos Específicos (OE), as Características do Produto (CP), os Requisitos Funcionais (RF) e os Requisitos Não Funcionais (RNF).

```
OE1
 ├- CP4
 │    ├- RF13 - RNF01, RNF03, RNF11, RNF13
 │    ├- RF14 - RNF03, RNF06, RNF09, RNF11, RNF13
 │    ├- RF15 - RNF01, RNF06, RNF11, RNF13
 │    └- RF16 - RNF03, RNF04, RNF05, RNF09, RNF11, RNF13
 │
 └- CP1
      └- RF06 - RNF03, RNF04, RNF06, RNF11


OE2
 ├- CP1
 │    ├- RF03 - RNF01, RNF03, RNF06, RNF11
 │    ├- RF04 - RNF03, RNF06, RNF09, RNF11
 │    └- RF05 - RNF03, RNF04, RNF05, RNF09, RNF11
 │
 └- CP5
      ├- RF17 - RNF01, RNF03, RNF06, RNF11, RNF13
      ├- RF18 - RNF01, RNF06, RNF11, RNF13
      └- RF19 - RNF03, RNF06, RNF11, RNF13


OE3
 └- CP5
      └- RF20 - RNF03, RNF05, RNF09, RNF11, RNF13


OE4
 ├- CP3
 │    ├- RF10 - RNF01, RNF02, RNF07, RNF10
 │    ├- RF11 - RNF01, RNF02, RNF07, RNF10
 │    └- RF12 - RNF02, RNF07, RNF10
 │
 └- CP6
      ├- RF21 - RNF01, RNF03, RNF11, RNF13
      ├- RF22 - RNF01, RNF06, RNF11, RNF13
      ├- RF23 - RNF03, RNF11, RNF13
      └- RF24 - RNF01, RNF06, RNF09, RNF11, RNF13


OE5
 └- CP2
      ├- RF07 - RNF03, RNF09, RNF11, RNF13
      ├- RF08 - RNF03, RNF09, RNF11, RNF13
      └- RF09 - RNF06, RNF11, RNF13


Transversal
 └- Acesso
      ├- RF01 - RNF11, RNF12, RNF13
      └- RF02 - RNF11, RNF13

```