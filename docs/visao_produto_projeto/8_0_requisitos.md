# 8. Requisitos Funcionais (RF) e Não Funcionais (RNF) - CECP

Derivados das Características de Produto (CP1 a CP6) da seção 2.3 do documento de Visão do Produto e Projeto.

## 8.1 Requisitos Funcionais - RFs

### Acesso e controle de usuários

**RF01 - Autenticar usuário:** deve ser possível aos coordenadores acessar o sistema mediante identificação e credenciais válidas.

**RF02 - Controlar acesso:** o sistema deve disponibilizar as funcionalidades administrativas exclusivamente para usuários autenticados com perfil de coordenador.

### CP1 - Gestão e acompanhamento de turmas

**RF03 - Cadastrar turma:** deve ser possível à coordenação cadastrar uma nova turma, informando modalidade, horário e capacidade máxima de alunos.

**RF04 - Editar turma:** deve ser possível à coordenação editar os dados de uma turma já cadastrada.

**RF05 - Inativar turma:** deve ser possível à coordenação inativar uma turma, preservando o histórico de alunos e frequências vinculados a ela, sem excluir os registros do sistema.

**RF06 - Associar aluno à turma:** deve ser possível à coordenação associar um aluno a uma turma ou remover sua associação, sem excluir seus registros históricos.

**RF07 - Consultar alunos de uma turma:** deve ser possível à cordenação pode consultar os alunos que fazem parte de uma turma específica.

### CP2 - Registro de doações e prestação de contas

**RF08 - Registrar doação recebida:** deve ser possível à coordenação registrar uma doação ou recurso recebido, identificando o doador ou parceiro, o tipo de recurso e as informações correspondentes.

**RF09 - Editar doação recebida:** deve ser possível à coordenação editar uma doação ou recurso recebido, conseguindo mudar as dados informados.

**RF10 - Registrar documentos de prestação de contas:** deve ser possível à coordenação registrar documentos utilizados na prestação de contas, como orçamentos, notas fiscais e registros fotográficos ou audiovisuais, vinculando-os à respectiva doação ou recurso recebido.

**RF11 - Editar documentos de prestação de contas:** deve ser possível à coordenação conseguir editar os documentos já informado ou anexado utilizados na prestação de contas.

**RF12 - Consultar doações e prestações de contas:** deve ser possível à coordenação consultar o histórico consolidado de doações e prestações de contas registradas em um determinado período.

### CP3 - Gestão de conteúdo institucional

**RF13 - Publicar conteúdo institucional:** deve ser possível à coordenação publicar conteúdos institucionais, como informações da organização, fotos e vídeos, no módulo público.

**RF14 - Edição conteúdo institucional:** deve ser possível à coordenação editar conteúdos institucionais, como informações da organização, fotos e vídeos, no módulo público.

**RF15 - Consultar conteúdo institucional:** deve ser possível a qualquer visitante consultar as informações institucionais publicadas, sem necessidade de autenticação.

**RF16 - Remover conteúdo institucional:** deve ser possível à cordenação remover um conteúdo publicado.

**RF17 - Publicar evento:** deve ser possível à coordenação publicar um evento ou campeonato, informando: nome do evento ou competição, sua data, local, horário e descrição.

**RF18 - Editar evento:** deve ser possível à coordenação editar os dados um evento ou campeonato já publicado.

**RF19 - Remover evento:** deve ser possível à coordenação remover um evento ou campeonato.

**RF20 - Consultar eventos:** deve ser possível à coordenação consultar os eventos ou campeonatos já publicados.


### CP4 - Cadastro e histórico de alunos

**RF21 - Cadastrar aluno:** deve ser possível à coordenação cadastrar um novo aluno, registrando seus dados cadastrais e a documentação exigida pelo CECP, como: 
- Identidade;
- CPF;
- Comprovante de residência;
- Foto 3x4;
- Atestado para prática de esporte;
- Assinar duas fichas, uma de inscrição e outra que funciona como um questionário de liberação

**RF22 - Editar aluno:** deve ser possível à coordenação atualizar os dados cadastrais de um aluno já registrado, sem excluir seu histórico no sistema.

**RF23 - Consultar ficha do aluno:** deve ser possível à coordenação consultar a ficha de um aluno, incluindo seus dados cadastrais e histórico de participação em turmas.

**RF24 - Inativar aluno:** deve ser possível à coordenação marcar um aluno como inativo, preservando seu histórico no sistema.

**RF25 - Remover dados do aluno:** Deve ser possível à coordenação remover do sistema os dados críticos de um aluno, mediante pedido do responsável legal ou do próprio aluno, caso ele tenha 18 anos ou mais, sem manter esses dados críticos no histórico do sistema.

> Dados críticos são:
>- Identidade;
>- CPF;
>- Comprovante de residência;


### CP5 - Acompanhamento pedagógico e disciplinar do aluno

**RF26 - Registrar frequência:** deve ser possível à coordenação registrar a frequência dos alunos em cada aula de uma turma.

**RF27 - Consultar frequência:** deve ser possível à coordenação consultar o histórico de frequência de um aluno.

**RF28 - Emitir alerta de faltas críticas:** o sistema deve gerar uma notificação para a coordenação quando um aluno atingir o número crítico de faltas definido pelo parâmetro configurado.

**RF29 - Registrar medida disciplinar:** deve ser possível à coordenação registrar uma medida disciplinar aplicada a um aluno, como advertência, suspensão ou desligamento, vinculada ao seu histórico.

### CP6 - Comunicação com voluntários e famílias

**RF30 - Publicar aviso:** deve ser possível à coordenação publicar avisos no módulo público.

**RF31 - Consultar avisos:** deve ser possível aos voluntários e familiares consultar os avisos no módulo público.

**RF32 - Editar aviso:** deve ser possível à coordenação editar um aviso para voluntários, familiares ou ambos já publicado no módulo público.

**RF33 - Remover aviso:** deve ser possível à coordenação remover um aviso para voluntários, familiares ou ambos já publicado no módulo público.

**RF34 - Consultar histórico de avisos:** deve ser possível à coordenação consultar os avisos publicados anteriormente, incluindo seus destinatários e data de publicação.

### CP7 -  Matrícula online 

**RF35 - Acessar formulário de matrícula online:** deve ser possível a qualquer interessado acessar o formulário de matrícula por link público, sem necessidade de login.

**RF36 - Preencher dados do aluno:** deve ser possível o interesado inserir, no formulário, os dados do aluno (nome, data de nascimento, contato e modalidade ou turma de interesse), com validação dos campos obrigatórios antes do envio.

**RF37 - Informar dados do responsável legal:** deve ser obrigatório informar os dados do responsável legal (nome, contato e vínculo) quando o aluno tiver menos de 18 anos, com base na data de nascimento informada.

**RF38 - Registrar consentimento de dados pessoais:** deve ser possível ao aluno, ou ao responsável legal no caso de menores, aceitar o termo de tratamento de dados pessoais, sendo o aceite condição para o envio e registrado com data, hora, versão do termo e identificação de quem aceitou.

**RF39 - Registrar termo de uso de imagem:** deve ser possível ao aluno ou ao responsável legal aceitar, separadamente do consentimento de dados, o termo de uso de imagem, com finalidade e prazo descritos, que a recusa impeça a matrícula.

**RF40 - Informar pessoas autorizadas a retirar o aluno:** deve ser obrigatório informar ao menos uma pessoa autorizada a retirar o aluno quando ele for menor de idade, com nome e contato.

**RF41 - Emitir comprovante de solicitação:** deve ser possível ao solicitante receber, após o envio, um número de protocolo.

**RF42 - Analisar solicitações de matrícula:** deve ser possível à coordenação consultar as solicitações recebidas e defini-las como aprovada, recusada ou em lista de espera, sendo o cadastro do aluno criado a partir dos dados do formulário quando aprovada.

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
|--------------- RNF04 | Preservação de histórico ao inativar turma ou aluno | Registros preservados no banco após a inativação, permanecendo consultáveis na ficha/histórico |
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
| RNF10 |O sistema deve utilizar padrões e tecnologias web atuais e amplamente adotados, garantindo compatibilidade com navegadores modernos. | Compatível com Chrome, Firefox e Safari nas últimas 2 versões |

### + Segurança
 
| ID | Descrição | Critério de Aceitação |
|---|---|---|
| RNF09 | Logs de operações críticas | Toda criação, edição e inativação (turma, aluno, doação, medida disciplinar) registrada com timestamp e usuário responsável |
| RNF11 | Controle de acesso por perfil (coordenação, professor/voluntário, família) | Rotas administrativas retornam 401/403 para requisições sem perfil autorizado |
| RNF12 | Senhas com hash e dados sensíveis criptografados | Nenhuma senha armazenada em texto claro; auditoria por inspeção de banco |
| RNF13 | O sistema deve tratar os dados pessoais de acordo com os princípios, direitos dos titulares e requisitos de segurança e tratamento estabelecidos pela Lei nº 13.709/2018 (LGPD). | O sistema deve permitir o atendimento às solicitações aplicáveis dos titulares ou responsáveis legais relacionadas aos seus dados pessoais, incluindo solicitação de eliminação quando cabível, além de classificar e proteger dados pessoais sensíveis conforme a LGPD|


## 8.3 Matriz-síntese de rastreabilidade - CECP

A matriz apresenta a rastreabilidade entre os Objetivos Específicos (OE), as Características do Produto (CP), os Requisitos Funcionais (RF) e os Requisitos Não Funcionais (RNF).

```
OE1
 ├- CP4
 │    ├- RF21 - RNF01, RNF03, RNF11, RNF13
 │    ├- RF22 - RNF03, RNF06, RNF10, RNF11, RNF13
 │    ├- RF23 - RNF01, RNF06, RNF11, RNF13
 │    ├- RF24 - RNF03, RNF04, RNF05, RNF10, RNF11, RNF13
 │    └- RF25 - RNF03, RNF05, RNF10, RNF11, RNF13
 │
 └- CP1
      ├- RF06 - RNF03, RNF04, RNF06, RNF11
      └- RF07 - RNF01, RNF06, RNF11


OE2
 ├- CP1
 │    ├- RF03 - RNF01, RNF03, RNF06, RNF11
 │    ├- RF04 - RNF03, RNF06, RNF10, RNF11
 │    └- RF05 - RNF03, RNF04, RNF05, RNF10, RNF11
 │
 └- CP5
      ├- RF26 - RNF01, RNF03, RNF06, RNF11, RNF13
      ├- RF27 - RNF01, RNF06, RNF11, RNF13
      └- RF28 - RNF03, RNF06, RNF11, RNF13


OE3
 └- CP5
      └- RF29 - RNF03, RNF05, RNF10, RNF11, RNF13


OE4
 ├- CP3
 │    ├- RF13 - RNF01, RNF02, RNF07, RNF09
 │    ├- RF14 - RNF01, RNF02, RNF07, RNF09, RNF10
 │    ├- RF15 - RNF02, RNF07, RNF09
 │    ├- RF16 - RNF02, RNF05, RNF07, RNF09, RNF10
 │    ├- RF17 - RNF01, RNF02, RNF07, RNF09
 │    ├- RF18 - RNF01, RNF02, RNF07, RNF09, RNF10
 │    ├- RF19 - RNF02, RNF05, RNF07, RNF09, RNF10
 │    └- RF20 - RNF02, RNF07, RNF09
 │
 └- CP6
      ├- RF30 - RNF01, RNF03, RNF11, RNF13
      ├- RF31 - RNF01, RNF06, RNF11, RNF13
      ├- RF32 - RNF03, RNF11, RNF13
      ├- RF33
      └- RF34 - RNF01, RNF06, RNF10, RNF11, RNF13


OE5
 └- CP2
      ├- RF08 - RNF03, RNF10, RNF11, RNF13
      ├- RF09 - RNF03, RNF06, RNF10, RNF11, RNF13
      ├- RF10 - RNF03, RNF10, RNF11, RNF13
      ├- RF11 - RNF03, RNF06, RNF10, RNF11, RNF13
      └- RF12 - RNF06, RNF11, RNF13


OE4
 └- CP7
      ├- RF35 - RNF01, RNF02, RNF09
      ├- RF36 - RNF01, RNF03, RNF13
      ├- RF37 - RNF01, RNF03, RNF13
      ├- RF38 - RNF03, RNF10, RNF13
      ├- RF39 - RNF03, RNF10, RNF13
      ├- RF40 - RNF01, RNF03, RNF13
      ├- RF41 - RNF03, RNF06
      └- RF42 - RNF03, RNF05, RNF10, RNF11, RNF13


Transversal
 └- Acesso
      ├- RF01 - RNF11, RNF12, RNF13
      └- RF02 - RNF11, RNF13, RNF08

```

## Rastreabilidade Visual do Projeto

O grafo abaixo representa a cadeia de rastreabilidade do CECP — do problema central até cada Requisito Funcional — com indicação visual do status de execução por cor.

<div style="position:relative;width:100%;font-family:sans-serif;user-select:none;">
  <div style="display:flex;align-items:center;gap:6px;padding:8px 10px;background:rgba(128,128,128,0.08);border:1px solid rgba(128,128,128,0.2);border-bottom:none;border-radius:8px 8px 0 0;">
    <button id="tz-in" style="width:28px;height:28px;border:1px solid rgba(128,128,128,0.35);border-radius:4px;background:transparent;cursor:pointer;font-size:16px;line-height:1;">+</button>
    <button id="tz-out" style="width:28px;height:28px;border:1px solid rgba(128,128,128,0.35);border-radius:4px;background:transparent;cursor:pointer;font-size:16px;line-height:1;">−</button>
    <button id="tz-reset" style="height:28px;padding:0 10px;border:1px solid rgba(128,128,128,0.35);border-radius:4px;background:transparent;cursor:pointer;font-size:12px;">↺ Reset</button>
    <span style="font-size:11px;opacity:0.5;margin-left:4px;">Scroll para zoom · Arraste para mover · Passe o mouse nos nós para detalhes · Clique no texto para abrir documentação</span>
  </div>
  <div id="tz-wrap" style="width:100%;height:640px;overflow:hidden;border:1px solid rgba(128,128,128,0.2);border-radius:0 0 8px 8px;cursor:grab;box-sizing:border-box;">
    <svg id="tz-svg" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;height:100%;"></svg>
  </div>
  <div id="tz-tip" style="position:absolute;background:#222;color:#fff;padding:7px 11px;border-radius:6px;font-size:13px;pointer-events:none;display:none;max-width:340px;z-index:200;line-height:1.5;box-shadow:0 2px 8px rgba(0,0,0,0.4);"></div>
</div>

<script>
(function(){
  var R=23, PAD=42, SP=52, GRP_GAP=78, OE_MIN=54, H=600;
  var LY=[55,175,300,430];

  var CP_RF={
    CP1:['RF03','RF04','RF05','RF06','RF07'],
    CP2:['RF08','RF09','RF10','RF11','RF12'],
    CP3:['RF13','RF14','RF15','RF16','RF17','RF18','RF19','RF20'],
    CP4:['RF21','RF22','RF23','RF24','RF25'],
    CP5:['RF26','RF27','RF28','RF29'],
    CP6:['RF30','RF31','RF32','RF33', 'RF34'],
    CP7:['RF35','RF36','RF37','RF38','RF39','RF40','RF41','RF42'],
    ACESSO:['RF01','RF02']
  };
  var OE_CP={
    OE1:['CP1','CP2','CP4','CP7'],
    OE2:['CP1','CP5','CP7'],
    OE3:['CP1','CP5'],
    OE4:['CP3','CP6'],
    OE5:['CP2','CP3'],
    TRANSV:['ACESSO']
  };
  var CP_ORDER=['CP1','CP2','CP3','CP4','CP5','CP6','CP7','ACESSO'];
  var OE_ORDER=['OE1','OE2','OE3','OE4','OE5','TRANSV'];

  var EDGES=[
    ['PROB','OE1'],['PROB','OE2'],['PROB','OE3'],['PROB','OE4'],['PROB','OE5'],['PROB','TRANSV'],
    ['OE1','CP1'],['OE1','CP2'],['OE1','CP4'],
    ['OE2','CP1'],['OE2','CP5'],
    ['OE3','CP1'],['OE3','CP5'],
    ['OE4','CP3'],['OE4','CP6'],['OE4','CP7'], 
    ['OE5','CP2'],['OE5','CP3'],
    ['TRANSV','ACESSO'],
    ['CP1','RF03'],['CP1','RF04'],['CP1','RF05'],['CP1','RF06'],['CP1','RF07'],
    ['CP2','RF08'],['CP2','RF09'],['CP2','RF10'],['CP2','RF11'],['CP2','RF12'],
    ['CP3','RF13'],['CP3','RF14'],['CP3','RF15'],['CP3','RF16'],['CP3','RF17'],['CP3','RF18'],['CP3','RF19'],['CP3','RF20'],
    ['CP4','RF21'],['CP4','RF22'],['CP4','RF23'],['CP4','RF24'],['CP4','RF25'],
    ['CP5','RF26'],['CP5','RF27'],['CP5','RF28'],['CP5','RF29'],
    ['CP6','RF30'],['CP6','RF31'],['CP6','RF32'],['CP6','RF33'],['CP6','RF34'],
    ['CP7','RF35'],['CP7','RF36'],['CP7','RF37'],['CP7','RF38'],['CP7','RF39'],['CP7','RF40'],['CP7','RF41'],['CP7','RF42'],
    ['ACESSO','RF01'],['ACESSO','RF02']
  ];

  var ST={
    PROB:'vm',
    OE1:'vm',OE2:'vm',OE3:'vm',OE4:'vm',OE5:'vm',TRANSV:'vm',
    CP1:'vm',CP2:'vm',CP3:'vm',CP4:'vm',CP5:'vm',CP6:'vm',CP7:'vm',ACESSO:'vm',
    RF01:'vm',RF02:'vm',RF03:'vm',RF04:'vm',RF05:'vm',RF06:'vm',RF07:'vm',
    RF08:'vm',RF09:'vm',RF10:'vm',RF11:'vm',RF12:'vm',RF13:'vm',RF14:'vm',
    RF15:'vm',RF16:'vm',RF17:'vm',RF18:'vm',RF19:'vm',RF20:'vm',RF21:'vm',
    RF22:'vm',RF23:'vm',RF24:'vm',RF25:'vm',RF26:'vm',RF27:'vm',RF28:'vm',
    RF29:'vm',RF30:'vm',RF31:'vm',RF32:'vm',RF33:'vm',RF34:'vm',RF35:'vm',
    RF36:'vm',RF37:'vm',RF38:'vm',RF39:'vm',RF40:'vm',RF41:'vm',RF42:'vm'
  };
  var CL={
    vd:{f:'#4CAF50',s:'#388E3C',t:'#fff'},
    am:{f:'#FFC107',s:'#F9A825',t:'#333'},
    vm:{f:'#F44336',s:'#C62828',t:'#fff'}
  };
  var DESC={
    PROB:'Problema central do CECP — gestão manual e descentralizada, dificultando o controle interno e a prestação de contas',
    OE1:'OE1 — Centralizar os dados dos alunos em uma base tecnológica única',
    OE2:'OE2 — Garantir o acompanhamento pontual da assiduidade e das condicionalidades pedagógicas',
    OE3:'OE3 — Apoiar a aplicação e o histórico de medidas disciplinares',
    OE4:'OE4 — Facilitar a comunicação entre coordenação, voluntários e famílias',
    OE5:'OE5 — Assegurar transparência na prestação de contas a parceiros e órgãos de fiscalização',
    TRANSV:'Requisitos transversais de acesso e autenticação, aplicáveis a todo o sistema',
    CP1:'CP1 — Gestão e acompanhamento de turmas',
    CP2:'CP2 — Registro de doações e prestação de contas',
    CP3:'CP3 — Gestão de conteúdo institucional',
    CP4:'CP4 — Cadastro e histórico de alunos',
    CP5:'CP5 — Acompanhamento pedagógico e disciplinar do aluno',
    CP6:'CP6 — Comunicação com voluntários e famílias',
    CP7:'CP7 — Matrícula online',
    ACESSO:'Acesso e controle de usuários (transversal)',
    RF01:'RF01 — Autenticar usuário',RF02:'RF02 — Controlar acesso',
    RF03:'RF03 — Cadastrar turma',RF04:'RF04 — Editar turma',RF05:'RF05 — Inativar turma',
    RF06:'RF06 — Associar aluno à turma',RF07:'RF07 — Consultar alunos de uma turma',
    RF08:'RF08 — Registrar doação recebida',RF09:'RF09 — Editar doação recebida',
    RF10:'RF10 — Registrar documentos de prestação de contas',RF11:'RF11 — Editar documentos de prestação de contas',
    RF12:'RF12 — Consultar doações e prestações de contas',
    RF13:'RF13 — Publicar conteúdo institucional',RF14:'RF14 — Editar conteúdo institucional',
    RF15:'RF15 — Consultar conteúdo institucional',RF16:'RF16 — Remover conteúdo institucional',
    RF17:'RF17 — Publicar evento',RF18:'RF18 — Editar evento',RF19:'RF19 — Remover evento',RF20:'RF20 — Consultar eventos',
    RF21:'RF21 — Cadastrar aluno',RF22:'RF22 — Editar aluno',RF23:'RF23 — Consultar ficha do aluno',
    RF24:'RF24 — Inativar aluno',RF25:'RF25 — Remover dados do aluno',
    RF26:'RF26 — Registrar frequência',RF27:'RF27 — Consultar frequência',
    RF28:'RF28 — Emitir alerta de faltas críticas',RF29:'RF29 — Registrar medida disciplinar',
    RF30:'RF30 — Publicar aviso',RF31:'RF31 — Consultar avisos',RF32:'RF32 — Editar aviso',
    RF33:'RF31 — Remover avisos',RF34:'Consultar hostórico de avisos',
    RF35:'RF35 — Acessar formulário de matrícula online',RF36:'RF36 — Preencher dados do aluno',
    RF37:'RF37 — Informar dados do responsável legal',RF38:'RF38 — Registrar consentimento de dados pessoais',
    RF39:'RF39 — Registrar termo de uso de imagem',RF40:'RF40 — Informar pessoas autorizadas a retirar o aluno',
    RF41:'RF41 — Emitir comprovante de solicitação',RF42:'RF42 — Analisar solicitações de matrícula'
  };

  var LINKS={
    PROB:'../../visao_produto/1-cenario/',
    OE1:'../../visao_produto/2-solucao/#oe1',OE2:'../../visao_produto/2-solucao/#oe2',OE3:'../../visao_produto/2-solucao/#oe3',
    OE4:'../../visao_produto/2-solucao/#oe4',OE5:'../../visao_produto/2-solucao/#oe5',TRANSV:'../../visao_produto/8-requisitos/#acesso',
    CP1:'../../visao_produto/2-solucao/#cp1',CP2:'../../visao_produto/2-solucao/#cp2',CP3:'../../visao_produto/2-solucao/#cp3',
    CP4:'../../visao_produto/2-solucao/#cp4',CP5:'../../visao_produto/2-solucao/#cp5',CP6:'../../visao_produto/2-solucao/#cp6',
    CP7:'../../visao_produto/2-solucao/#cp7',ACESSO:'../../visao_produto/8-requisitos/#acesso',
    RF01:'../../visao_produto/8-requisitos/#rf01',RF02:'../../visao_produto/8-requisitos/#rf02',
    RF03:'../../visao_produto/8-requisitos/#rf03',RF04:'../../visao_produto/8-requisitos/#rf04',
    RF05:'../../visao_produto/8-requisitos/#rf05',RF06:'../../visao_produto/8-requisitos/#rf06',
    RF07:'../../visao_produto/8-requisitos/#rf07',RF08:'../../visao_produto/8-requisitos/#rf08',
    RF09:'../../visao_produto/8-requisitos/#rf09',RF10:'../../visao_produto/8-requisitos/#rf10',
    RF11:'../../visao_produto/8-requisitos/#rf11',RF12:'../../visao_produto/8-requisitos/#rf12',
    RF13:'../../visao_produto/8-requisitos/#rf13',RF14:'../../visao_produto/8-requisitos/#rf14',
    RF15:'../../visao_produto/8-requisitos/#rf15',RF16:'../../visao_produto/8-requisitos/#rf16',
    RF17:'../../visao_produto/8-requisitos/#rf17',RF18:'../../visao_produto/8-requisitos/#rf18',
    RF19:'../../visao_produto/8-requisitos/#rf19',RF20:'../../visao_produto/8-requisitos/#rf20',
    RF21:'../../visao_produto/8-requisitos/#rf21',RF22:'../../visao_produto/8-requisitos/#rf22',
    RF23:'../../visao_produto/8-requisitos/#rf23',RF24:'../../visao_produto/8-requisitos/#rf24',
    RF25:'../../visao_produto/8-requisitos/#rf25',RF26:'../../visao_produto/8-requisitos/#rf26',
    RF27:'../../visao_produto/8-requisitos/#rf27',RF28:'../../visao_produto/8-requisitos/#rf28',
    RF29:'../../visao_produto/8-requisitos/#rf29',RF30:'../../visao_produto/8-requisitos/#rf30',
    RF31:'../../visao_produto/8-requisitos/#rf31',RF32:'../../visao_produto/8-requisitos/#rf32',
    RF33:'../../visao_produto/8-requisitos/#rf33',RF34:'../../visao_produto/8-requisitos/#rf34',
    RF35:'../../visao_produto/8-requisitos/#rf35',RF36:'../../visao_produto/8-requisitos/#rf36',
    RF37:'../../visao_produto/8-requisitos/#rf37',RF38:'../../visao_produto/8-requisitos/#rf38',
    RF39:'../../visao_produto/8-requisitos/#rf39',RF40:'../../visao_produto/8-requisitos/#rf40',
    RF41:'../../visao_produto/8-requisitos/#rf41',RF42:'../../visao_produto/8-requisitos/#rf41'
  };

  /* ── LAYOUT (bottom-up): RF grouped by CP ── */
  var cpX={}, rfX={}, cx=PAD;
  CP_ORDER.forEach(function(cp){
    var rfs=CP_RF[cp], gw=(rfs.length-1)*SP;
    rfs.forEach(function(rf,i){rfX[rf]=cx+i*SP;});
    cpX[cp]=cx+gw/2;
    cx+=gw+GRP_GAP;
  });
  var W=cx-GRP_GAP+PAD;

  var oeIdeal={};
  OE_ORDER.forEach(function(oe){
    var cps=OE_CP[oe];
    oeIdeal[oe]=cps.reduce(function(s,c){return s+cpX[c];},0)/cps.length;
  });
  var sortedOEs=OE_ORDER.slice().sort(function(a,b){return oeIdeal[a]-oeIdeal[b];});
  var oeX={};
  sortedOEs.forEach(function(oe){oeX[oe]=oeIdeal[oe];});
  var j;
  for(j=1;j<sortedOEs.length;j++){
    var pr=sortedOEs[j-1],cu=sortedOEs[j];
    if(oeX[cu]<oeX[pr]+OE_MIN) oeX[cu]=oeX[pr]+OE_MIN;
  }
  for(j=sortedOEs.length-2;j>=0;j--){
    var cu2=sortedOEs[j],nx=sortedOEs[j+1];
    if(oeX[cu2]>oeX[nx]-OE_MIN) oeX[cu2]=oeX[nx]-OE_MIN;
  }

  var pos={};
  pos['PROB']={x:W/2,y:LY[0]};
  OE_ORDER.forEach(function(oe){pos[oe]={x:oeX[oe],y:LY[1]};});
  CP_ORDER.forEach(function(cp){pos[cp]={x:cpX[cp],y:LY[2]};});
  CP_ORDER.forEach(function(cp){
    CP_RF[cp].forEach(function(rf){pos[rf]={x:rfX[rf],y:LY[3]};});
  });

  /* ── BUILD SVG ── */
  var NS='http://www.w3.org/2000/svg';
  var svg=document.getElementById('tz-svg');
  var wrap=document.getElementById('tz-wrap');
  var tip=document.getElementById('tz-tip');

  var g=document.createElementNS(NS,'g');
  svg.appendChild(g);

  var didDrag=false;

  EDGES.forEach(function(e){
    var p1=pos[e[0]], p2=pos[e[1]];
    var dx=p2.x-p1.x, dy=p2.y-p1.y, d=Math.sqrt(dx*dx+dy*dy);
    var ln=document.createElementNS(NS,'line');
    ln.setAttribute('x1',p1.x+dx/d*R); ln.setAttribute('y1',p1.y+dy/d*R);
    ln.setAttribute('x2',p2.x-dx/d*R); ln.setAttribute('y2',p2.y-dy/d*R);
    ln.setAttribute('stroke','#888'); ln.setAttribute('stroke-width','1.4');
    ln.setAttribute('opacity','0.5');
    g.appendChild(ln);
  });

  Object.keys(pos).forEach(function(id){
    var p=pos[id], c=CL[ST[id]];
    var grp=document.createElementNS(NS,'g');

    var ci=document.createElementNS(NS,'circle');
    ci.setAttribute('cx',p.x); ci.setAttribute('cy',p.y); ci.setAttribute('r',R);
    ci.setAttribute('fill',c.f); ci.setAttribute('stroke',c.s); ci.setAttribute('stroke-width','2.2');
    ci.style.cursor='pointer';

    var tx=document.createElementNS(NS,'text');
    tx.setAttribute('x',p.x); tx.setAttribute('y',p.y);
    tx.setAttribute('text-anchor','middle'); tx.setAttribute('dominant-baseline','middle');
    tx.setAttribute('fill',c.t); tx.setAttribute('font-size','9');
    tx.setAttribute('font-weight','bold'); tx.setAttribute('font-family','monospace');
    tx.style.cursor='pointer';
    tx.textContent=id;

    grp.addEventListener('mouseenter',function(){
      ci.setAttribute('r',R+3); ci.setAttribute('stroke-width','3');
      tx.setAttribute('text-decoration','underline');
      tip.innerHTML=DESC[id]+'<br><span style="font-size:11px;opacity:0.6;font-style:italic;">Clique no texto para abrir documentação</span>';
      tip.style.display='block';
    });
    grp.addEventListener('mousemove',function(ev){
      var br=wrap.getBoundingClientRect();
      var lx=ev.clientX-br.left+14, ly=ev.clientY-br.top-60;
      if(lx+345>br.width) lx=lx-360;
      tip.style.left=lx+'px'; tip.style.top=ly+'px';
    });
    grp.addEventListener('mouseleave',function(){
      ci.setAttribute('r',R); ci.setAttribute('stroke-width','2.2');
      tx.setAttribute('text-decoration','none');
      tip.style.display='none';
    });

    tx.addEventListener('click',function(e){
      if(didDrag) return;
      window.open(LINKS[id],'_blank','noopener');
    });

    grp.appendChild(ci);
    grp.appendChild(tx);
    g.appendChild(grp);
  });

  /* ── ZOOM / PAN ── */
  var cw=wrap.clientWidth||820, ch=wrap.clientHeight||640;
  var CH=LY[LY.length-1]+R+PAD;
  var sc=Math.min((cw-16)/W,(ch-16)/CH,1);
  var tx0=(cw-W*sc)/2, ty0=Math.max((ch-CH*sc)/2,8);
  var scale=sc, txn=tx0, tyn=ty0, isDragging=false, sx,sy,stx,sty;

  function applyT(){g.setAttribute('transform','translate('+txn+','+tyn+') scale('+scale+')');}
  applyT();

  wrap.addEventListener('wheel',function(ev){
    ev.preventDefault();
    var br=wrap.getBoundingClientRect();
    var mx=ev.clientX-br.left, my=ev.clientY-br.top;
    var ns=Math.min(Math.max(scale*(ev.deltaY<0?1.12:0.89),0.2),4);
    txn=mx-(mx-txn)*(ns/scale); tyn=my-(my-tyn)*(ns/scale); scale=ns; applyT();
  },{passive:false});

  wrap.addEventListener('mousedown',function(ev){
    isDragging=true; didDrag=false;
    sx=ev.clientX; sy=ev.clientY; stx=txn; sty=tyn;
    wrap.style.cursor='grabbing';
  });
  document.addEventListener('mousemove',function(ev){
    if(!isDragging) return;
    if(Math.abs(ev.clientX-sx)>3||Math.abs(ev.clientY-sy)>3) didDrag=true;
    txn=stx+(ev.clientX-sx); tyn=sty+(ev.clientY-sy); applyT();
  });
  document.addEventListener('mouseup',function(){isDragging=false; wrap.style.cursor='grab';});

  document.getElementById('tz-in').addEventListener('click',function(){scale=Math.min(scale*1.2,4);txn=(cw-W*scale)/2;tyn=Math.max((ch-CH*scale)/2,8);applyT();});
  document.getElementById('tz-out').addEventListener('click',function(){scale=Math.max(scale*0.8,0.2);txn=(cw-W*scale)/2;tyn=Math.max((ch-CH*scale)/2,8);applyT();});
  document.getElementById('tz-reset').addEventListener('click',function(){scale=sc;txn=tx0;tyn=ty0;applyT();});
})();
</script>

| Cor | Status |
| :---: | :--- |
| 🟢 Verde | **Totalmente concluído** — entregue e validado com o cliente |
| 🟡 Amarelo | **Parcialmente concluído** — entregue com débito técnico ou dependente de itens incompletos |
| 🔴 Vermelho | **Não iniciado** — previsto em sprint futura ou em andamento sem entrega confirmada |