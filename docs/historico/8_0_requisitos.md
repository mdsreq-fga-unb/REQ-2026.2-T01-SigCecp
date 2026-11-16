!!! warning "Documento histórico"
    Esta é a lista original de requisitos e não é mais atualizada. A declaração vigente de cada requisito está na ficha (veja o [painel do escopo](../painel.md)). Nenhuma ficha depende dele: as definições dos RNFs estão nas fichas de RNF e a descrição dos CPs está na seção 2.3 da [solução proposta](../visao/contexto/2_solucao_proposta.md).

# 8. Requisitos Funcionais (RF) e Não Funcionais (RNF) - CECP

Derivados das Características de Produto (CP1 a CP6) da seção 2.3 do documento de Visão do Produto e Projeto.

## 8.1 Requisitos Funcionais - RFs

### Acesso e controle de usuários

**RF00 - Encerrar sessão:** deve ser possível ao usuário autenticado encerrar sua sessão ativa no sistema, invalidando suas credenciais de acesso e redirecionando-o para a tela de login.

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

**RF25 - Remover dados do aluno:** Deve ser possível à coordenação remover do sistema os dados de um aluno, mediante pedido do responsável legal ou do próprio aluno, caso ele tenha 18 anos ou mais.

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

**RF36 - Preencher dados do aluno:** deve ser possível o interesado inserir, no formulário, os dados do aluno (nome, data de nascimento, contato e modalidade ou turma de interesse).

**RF37 - Informar dados do responsável legal:** deve ser possível inserir os dados do responsável legal (nome, contato e vínculo) quando o aluno tiver menos de 18 anos.

**RF38 - Registrar consentimento de dados pessoais:** deve ser possível ao aluno, ou ao responsável legal no caso de menores, aceitar o termo de tratamento de dados pessoais, sendo o aceite condição para o envio e registrado com data, hora, versão do termo e identificação de quem aceitou.

**RF39 - Registrar termo de uso de imagem:** deve ser possível ao aluno ou ao responsável legal aceitar, separadamente do consentimento de dados, o termo de uso de imagem.

**RF40 - Informar pessoas autorizadas a retirar o aluno:** deve ser possível inserir ao menos uma pessoa autorizada a retirar o aluno quando ele for menor de idade, com nome e contato, ou se o menor pode ir embora só.

**RF41 - Emitir comprovante de solicitação:** deve ser possível ao solicitante receber, após o envio, um número de protocolo.

**RF42 - Analisar solicitações de matrícula:** deve ser possível à coordenação consultar as solicitações recebidas e defini-las como aprovada, recusada ou em lista de espera.

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
 RNF04 | Preservação de histórico ao inativar turma ou aluno | Registros preservados no banco após a inativação, permanecendo consultáveis na ficha/histórico |
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

!!! info "Versão vigente"
    A matriz-síntese e o grafo de rastreabilidade foram movidos para a página [Rastreabilidade](../visao/contexto/8_rastreabilidade.md), onde são mantidos atualizados com as fichas. Esta seção não é mais atualizada; a versão anterior está no histórico do repositório.

## Versionamento

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/09/2026 | Criação da lista original de RFs (RF00–RF34) e RNFs (RNF01–RNF13), com a matriz-síntese 8.3 e os primeiros OEs e CPs | Equipe One | — |
| 1.1 | 22/09/2026 | Adição de CP7 (Matrícula online) e dos RFs RF35–RF42 correspondentes, após identificação de lacuna no escopo (acompanhamento pedagógico sem RF de matrícula online); CP7 associada a OE1 como OE principal | Equipe One | — |
| 1.2 | 26/09/2026 | Ajuste da classificação URPS+ dos RNFs: RNF09 (Logs) movido de Suportabilidade para Segurança; RNF08 vinculado à matriz 8.3 | Equipe One | — |
| 1.3 | 30/10/2026 | Grafo interativo de rastreabilidade adicionado à seção 8.3 | [Marcos Monteiro](https://github.com/montmarcos) | — |
| 1.4 | 14/11/2026 | Correções de rastreabilidade: (1) CP7 movido de OE4 para OE1 na matriz 8.3 e no grafo, conforme tabela 2.3 da solução proposta; (2) RF33 recebeu RNFs ausentes (RNF03, RNF05, RNF11, RNF13) — linha estava em branco por erro de preenchimento; (3) grafo corrigido: OE_CP, EDGES, tooltip RF33 (estava copiado do RF31) e tooltip RF34 (typo e código faltante); (4) nó Objetivo Geral (OG) adicionado entre PROB e os OEs no grafo | — | — |
| 1.5 | 15/11/2026 | Matriz-síntese (8.3) e grafo de rastreabilidade movidos para a página vigente [Rastreabilidade](../visao/contexto/8_rastreabilidade.md) | — | — |
