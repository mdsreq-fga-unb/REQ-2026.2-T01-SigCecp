# Requisitos: Plataforma CECP

Documento único de requisitos. Cada requisito tem uma ficha que concentra tudo o que a equipe de desenvolvimento precisa (detalhamento, dados, regras, critérios de aceitação) e que **evolui a cada etapa da iteração** (protótipo, user design e construção), sem precisar consultar outros arquivos.


### RF13: Publicar conteúdo institucional

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | Deve ser possível à coordenação publicar conteúdos institucionais, como informações da organização, fotos e vídeos, no módulo público. |
| **Ator principal** | Coordenação |
| **Prioridade** | Alta |
| **Entradas** | Título (obrigatório); texto, imagens e vídeos (opcionais) |
| **Pré-condições** | Coordenador autenticado no sistema |
| **Processamento** | Valida a presença do título, armazena os anexos informados e grava a publicação como visível no módulo público |
| **Saídas** | Conteúdo exibido no módulo público; mensagem de erro quando o título não for informado |
| **Regras de negócio** | RN01: todo conteúdo institucional deve ter título.<br>RN02: apenas a coordenação pode publicar, editar e remover conteúdos institucionais e eventos; professores solicitam à coordenação.<br>RN03: não há conjunto fixo de campos além do título (exemplo a publicação pode ser só uma imagem que já contém todas as informações). |
| **Critérios de aceitação** | 1. Dado um conteúdo com título, quando a coordenação publica, então ele passa a ser exibido no módulo público para qualquer visitante, sem login.<br>2. Dado um conteúdo sem título, quando a coordenação tenta publicar, então o sistema bloqueia a publicação e informa que o título é obrigatório.<br>3. Dado um conteúdo apenas com título e imagem, quando publicado, então o sistema o aceita sem exigir texto ou vídeo. |



### RF14: Editar conteúdo institucional

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | Deve ser possível à coordenação editar conteúdos institucionais já publicados, como informações da organização, fotos e vídeos, no módulo público. |
| **Ator principal** | Coordenação |
| **Prioridade** | Alta |
| **Entradas** | Título, texto, imagens e vídeos (alterados, adicionados ou removidos) |
| **Pré-condições** | Coordenador autenticado; conteúdo institucional já publicado |
| **Processamento** | Carrega o conteúdo existente, permite alterar texto e substituir ou remover fotos e vídeos, valida o título e grava as alterações |
| **Saídas** | Conteúdo atualizado exibido no módulo público |
| **Regras de negócio** | RN01 e RN02 (ver RF13).<br>RN04: o sistema não precisa sinalizar ao visitante que o conteúdo foi editado; a coordenação é responsável por comunicar mudanças relevantes (por exemplo, publicando um novo aviso institucional). |
| **Critérios de aceitação** | 1. Dado um conteúdo publicado, quando a coordenação altera o texto e salva, então a nova versão é exibida no módulo público.<br>2. Dado um conteúdo com vídeo ou foto, quando a coordenação os remove ou substitui, então o módulo público exibe apenas a mídia atual.<br>3. Dado que a coordenação apagou o título, quando tenta salvar, então o sistema bloqueia a gravação. |



### RF15: Consultar conteúdo institucional

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | Deve ser possível a qualquer visitante consultar as informações institucionais publicadas, sem necessidade de autenticação. |
| **Ator principal** | Visitante (qualquer pessoa) |
| **Prioridade** | Alta |
| **Entradas** | Acesso ao módulo público |
| **Pré-condições** | Existir ao menos um conteúdo institucional publicado |
| **Processamento** | Recupera os conteúdos publicados e os exibe com título, texto, fotos e vídeos |
| **Saídas** | Lista e visualização dos conteúdos institucionais; mensagem informativa quando não houver conteúdo publicado |
| **Regras de negócio** | RN05: a consulta é pública e não exige login nem cadastro. |
| **Critérios de aceitação** | 1. Dado um visitante não autenticado, quando acessa o módulo público, então visualiza os conteúdos institucionais publicados.<br>2. Dado um conteúdo removido pela coordenação, quando o visitante consulta, então ele não aparece. |

### RF16: Remover conteúdo institucional

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | Deve ser possível à coordenação remover um conteúdo institucional publicado. |
| **Ator principal** | Coordenação |
| **Prioridade** | Alta |
| **Entradas** | Identificação do conteúdo a ser removido; confirmação da remoção |
| **Pré-condições** | Coordenador autenticado; conteúdo institucional existente |
| **Processamento** | Solicita confirmação, exclui o conteúdo e seus anexos do sistema |
| **Saídas** | Confirmação da remoção; conteúdo deixa de ser exibido a qualquer usuário |
| **Regras de negócio** | RN02 (ver RF13).<br>RN06: a remoção é total e definitiva; o conteúdo deixa de ser visível para todos. |
| **Critérios de aceitação** | 1. Dado um conteúdo publicado, quando a coordenação confirma a remoção, então ele deixa de ser exibido no módulo público e na área da coordenação.<br>2. Dado um usuário sem perfil de coordenação, quando tenta remover, então o sistema nega a operação. |

### RF17: Publicar evento

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | Deve ser possível à coordenação publicar um evento ou campeonato, informando: nome do evento ou competição, data, local, horário e descrição. |
| **Ator principal** | Coordenação |
| **Prioridade** | Alta |
| **Entradas** | Obrigatórias: título, subtítulo, nome do evento/competição, data, horário (início e término), local, descrição, informação sobre alimentação (haverá ou não), informação sobre pesagem (haverá ou não, quando aplicável), informações de pagamento (se é cobrado, valor, data limite e meio de pagamento, como PIX). Opcionais: vídeo e imagens |
| **Pré-condições** | Coordenador autenticado |
| **Processamento** | Valida todos os campos obrigatórios, grava o evento, define seu estado conforme a data e o torna visível no módulo público |
| **Saídas** | Evento exibido no módulo público; mensagem indicando os campos pendentes quando a validação falhar |
| **Regras de negócio** | RN02 (ver RF13).<br>RN07: o evento só pode ser publicado com todos os campos obrigatórios preenchidos; não se publica evento vago.<br>RN08: o vídeo é opcional.<br>RN09: o estado do evento é Em breve, Em andamento ou Encerrado. |
| **Critérios de aceitação** | 1. Dado um evento com todos os campos obrigatórios, quando a coordenação publica, então ele aparece no módulo público.<br>2. Dado um evento com qualquer campo obrigatório vazio, quando a coordenação tenta publicar, então o sistema bloqueia a publicação e indica o que falta.<br>3. Dado um evento sem vídeo, quando publicado, então o sistema o aceita normalmente. |

### RF18: Editar evento

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | Deve ser possível à coordenação editar os dados de um evento ou campeonato já publicado. |
| **Ator principal** | Coordenação |
| **Prioridade** | Alta |
| **Entradas** | Qualquer dado do evento (data, horário, local, descrição, informações de pagamento, mídias etc.) |
| **Pré-condições** | Coordenador autenticado; evento já publicado |
| **Processamento** | Carrega os dados atuais, aplica as alterações, revalida os campos obrigatórios e grava |
| **Saídas** | Evento atualizado exibido no módulo público |
| **Regras de negócio** | RN02 e RN07 (ver RF13 e RF17).<br>RN10: a coordenação é responsável por avisar os interessados sobre alterações (por exemplo, publicando um aviso institucional); o sistema não precisa sinalizar a edição ao visitante. |
| **Critérios de aceitação** | 1. Dado um evento com data incorreta, quando a coordenação corrige e salva, então a nova data é exibida no módulo público.<br>2. Dado que a coordenação esvaziou um campo obrigatório, quando tenta salvar, então o sistema bloqueia a gravação. |

### RF19: Remover evento

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | Deve ser possível à coordenação remover um evento ou campeonato. |
| **Ator principal** | Coordenação |
| **Prioridade** | Alta |
| **Entradas** | Identificação do evento; confirmação da remoção |
| **Pré-condições** | Coordenador autenticado; evento existente |
| **Processamento** | Solicita confirmação e exclui o evento e seus anexos |
| **Saídas** | Confirmação da remoção; evento deixa de ser exibido |
| **Regras de negócio** | RN02 (ver RF13).<br>RN06: a remoção é total e definitiva. |
| **Critérios de aceitação** | 1. Dado um evento publicado, quando a coordenação confirma a remoção, então ele deixa de aparecer em qualquer listagem.<br>2. Dado um usuário sem perfil de coordenação, quando tenta remover, então o sistema nega a operação. |

### RF20: Consultar eventos

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | Deve ser possível consultar os eventos ou campeonatos já publicados, em uma listagem que indique o estado de cada um. |
| **Ator principal** | Coordenação |
| **Prioridade** | Alta |
| **Entradas** | Acesso à listagem de eventos |
| **Pré-condições** | Existir ao menos um evento publicado. Não exige autenticação para visitantes |
| **Processamento** | Recupera os eventos, calcula o estado de cada um e os exibe em lista; a coordenação acessa também as opções de editar e remover |
| **Saídas** | Lista com título, data, local e estado (Em breve, Em andamento, Encerrado); detalhes completos ao selecionar um evento |
| **Regras de negócio** | RN09: os estados possíveis são Em breve (ainda vai ocorrer), Em andamento (está ocorrendo) e Encerrado (já ocorreu). |
| **Critérios de aceitação** | 1. Dado um visitante, quando acessa a listagem, então vê eventos futuros, em andamento e encerrados, cada um com seu estado.<br>2. Dado um evento cuja data já passou, quando listado, então aparece como Encerrado.<br>3. Dado um coordenador autenticado, quando consulta um evento, então tem acesso às ações de editar e remover. |

#### Andamento da Iteração 5

| Etapa | Status | Link / Observação |
| :---  | :--- | :--- |
| Detalhamento | Feito | [Evidência do detalhamento](../organizacao_e_planejamento/detalhamento_iteracao5.md)|
| Design do usuário (protótipo) | Em Andamento | [Protótipo Realizado](https://www.figma.com/proto/7CtbGEyLbEpIpD0nCLVOLu/Sem-t%C3%ADtulo?node-id=26-92&t=aYHzBAmVutgMVEvI-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1)
|||[Evidência design user](../organizacao_e_planejamento/designUser_iteracao5.md)|
| Construção: início | Pendente | |
| Construção: implementação | Pendente | |
| Teste de aceite | Pendente | |

### RF03: Cadastrar turma

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: A turma só é salva com modalidade, horário e capacidade máxima de alunos preenchidos. Após salva, a turma aparece na lista de turmas. Campo obrigatório vazio impede o salvamento e indica qual campo precisa ser preenchido. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 4 (12/10 a 18/10) | Pendente | |
| Design do usuário (protótipo) | 5 (19/10 a 25/10), protótipo do dashboard de turmas | Pendente | |
| Construção | 6 (26/10 a 01/11) | Pendente | |
| Teste de aceite | 6 (26/10 a 01/11) | Pendente | |
### RF06: Associar aluno à turma

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Um aluno cadastrado pode ser associado a uma turma, e a associação aparece na lista da turma e na ficha do aluno. Ao remover a associação, o aluno sai da lista da turma e o histórico de participação é mantido. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 4 (12/10 a 18/10) | Pendente | |
| Design do usuário (protótipo) | 5 (19/10 a 25/10), protótipo do dashboard de turmas | Pendente | |
| Construção | 6 (26/10 a 01/11) | Pendente | |
| Teste de aceite | 6 (26/10 a 01/11) | Pendente | |
### RF07: Consultar alunos de uma turma

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Ao selecionar uma turma, o sistema lista todos os alunos associados a ela e somente eles. Turma sem alunos exibe a lista vazia com mensagem informativa. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 4 (12/10 a 18/10) | Pendente | |
| Design do usuário (protótipo) | 5 (19/10 a 25/10), protótipo do dashboard de turmas | Pendente | |
| Construção | 6 (26/10 a 01/11) | Pendente | |
| Teste de aceite | 6 (26/10 a 01/11) | Pendente | |
### 4.3 Iteração 7: Cadastro e histórico de alunos (CP4)

Cronograma: detalhamento na iteração 5; protótipo da ficha do aluno na iteração 6; na iteração 7 (02/11 a 08/11), escopo dos dados cadastrais e documentais, protótipo das medidas disciplinares, construção e testes de segurança com a coordenação. Reuniões com o cliente: 05/11 e 06/11.

### RF21: Cadastrar aluno

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: O aluno é salvo com seus dados cadastrais e com a documentação exigida pelo CECP (identidade, CPF, comprovante de residência, foto 3x4, atestado para prática de esporte e as duas fichas assinadas). Após salvo, o aluno pode ser localizado na consulta. Campo obrigatório vazio impede o salvamento e indica qual campo precisa ser preenchido. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 5 (19/10 a 25/10) e 7 (02/11 a 08/11), escopo dos dados | Pendente | |
| Design do usuário (protótipo) | 6 (26/10 a 01/11), ficha do aluno | Pendente | |
| Construção | 7 (02/11 a 08/11) | Pendente | |
| Teste de aceite | 7 (02/11 a 08/11) | Pendente | |
### RF22: Editar aluno

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Os dados cadastrais alterados são salvos e exibidos atualizados na ficha do aluno. O histórico do aluno é mantido. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 5 (19/10 a 25/10) e 7 (02/11 a 08/11), escopo dos dados | Pendente | |
| Design do usuário (protótipo) | 6 (26/10 a 01/11), ficha do aluno | Pendente | |
| Construção | 7 (02/11 a 08/11) | Pendente | |
| Teste de aceite | 7 (02/11 a 08/11) | Pendente | |
### RF23: Consultar ficha do aluno

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: A ficha exibe os dados cadastrais do aluno e seu histórico de participação em turmas. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 5 (19/10 a 25/10) e 7 (02/11 a 08/11), escopo dos dados | Pendente | |
| Design do usuário (protótipo) | 6 (26/10 a 01/11), ficha do aluno | Pendente | |
| Construção | 7 (02/11 a 08/11) | Pendente | |
| Teste de aceite | 7 (02/11 a 08/11) | Pendente | |
### RF24: Inativar aluno

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Após a confirmação, o aluno passa a constar como inativo. O histórico do aluno é preservado e continua consultável na ficha. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 5 (19/10 a 25/10) e 7 (02/11 a 08/11), escopo dos dados | Pendente | |
| Design do usuário (protótipo) | 6 (26/10 a 01/11), ficha do aluno | Pendente | |
| Construção | 7 (02/11 a 08/11) | Pendente | |
| Teste de aceite | 7 (02/11 a 08/11) | Pendente | |
### RF29: Registrar medida disciplinar

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: A medida (advertência, suspensão ou desligamento) só é salva após confirmação e passa a constar no histórico do aluno. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 5 (19/10 a 25/10) | Pendente | |
| Design do usuário (protótipo) | 7 (02/11 a 08/11), telas de medidas disciplinares | Pendente | |
| Construção | 7 (02/11 a 08/11) | Pendente | |
| Teste de aceite | 7 (02/11 a 08/11) | Pendente | |

### RF30: Publicar aviso

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: O aviso publicado, com destinatário voluntários, familiares ou ambos, passa a ser exibido no módulo público. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | 10 (23/11 a 29/11), módulo de avisos | Pendente | |
| Teste de aceite | 10 (23/11 a 29/11) | Pendente | |
### RF35: Acessar formulário de matrícula online

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: O formulário de matrícula abre pelo link público, sem necessidade de login. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11) | Pendente | |
| Design do usuário (protótipo) | 8 (09/11 a 15/11), formulário público de matrícula | Pendente | |
| Construção | 9 (16/11 a 22/11) | Pendente | |
| Teste de aceite | 10 (23/11 a 29/11) | Pendente | |
### RF36: Preencher dados do aluno

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: O formulário aceita nome, data de nascimento, contato e modalidade ou turma de interesse do aluno. O envio é bloqueado enquanto algum desses campos estiver vazio. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11) | Pendente | |
| Design do usuário (protótipo) | 8 (09/11 a 15/11), formulário público de matrícula | Pendente | |
| Construção | 9 (16/11 a 22/11) | Pendente | |
| Teste de aceite | 10 (23/11 a 29/11) | Pendente | |
### RF37: Informar dados do responsável legal

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Quando a data de nascimento indica aluno menor de 18 anos, o formulário exige nome, contato e vínculo do responsável legal. Para aluno com 18 anos ou mais, esses dados não são exigidos. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11) | Pendente | |
| Design do usuário (protótipo) | 8 (09/11 a 15/11), formulário público de matrícula | Pendente | |
| Construção | 9 (16/11 a 22/11) | Pendente | |
| Teste de aceite | 10 (23/11 a 29/11) | Pendente | |
### RF38: Registrar consentimento de dados pessoais

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: O envio do formulário só é permitido após o aceite do termo de tratamento de dados pessoais. O aceite é registrado com data, hora, versão do termo e identificação de quem aceitou (aluno ou responsável legal). |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11) | Pendente | |
| Design do usuário (protótipo) | 8 (09/11 a 15/11), formulário público de matrícula | Pendente | |
| Construção | 9 (16/11 a 22/11) | Pendente | |
| Teste de aceite | 10 (23/11 a 29/11) | Pendente | |
### RF39: Registrar termo de uso de imagem

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: O termo de uso de imagem é apresentado em item separado do consentimento de dados pessoais, e a resposta do aluno ou do responsável legal é registrada. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11) | Pendente | |
| Design do usuário (protótipo) | 8 (09/11 a 15/11), formulário público de matrícula | Pendente | |
| Construção | 9 (16/11 a 22/11) | Pendente | |
| Teste de aceite | 10 (23/11 a 29/11) | Pendente | |
### 4.5 Iteração 10: Protocolo e análise de matrículas (CP7)

Cronograma: protótipo da análise de solicitações na iteração 9; construção e fechamento do MVP na iteração 10 (23/11 a 29/11). Reuniões com o cliente: 26/11 e 27/11.

### RF41: Emitir comprovante de solicitação

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Após o envio bem-sucedido do formulário, o sistema exibe ao solicitante um número de protocolo. Cada solicitação recebe um número de protocolo distinto. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11) | Pendente | |
| Design do usuário (protótipo) | 9 (16/11 a 22/11), análise de solicitações | Pendente | |
| Construção | 10 (23/11 a 29/11) | Pendente | |
| Teste de aceite | 10 (23/11 a 29/11) | Pendente | |
### RF42: Analisar solicitações de matrícula

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: A coordenação consulta as solicitações recebidas e define cada uma como aprovada, recusada ou em lista de espera. O status definido é exibido atualizado na consulta. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11) | Pendente | |
| Design do usuário (protótipo) | 9 (16/11 a 22/11), análise de solicitações | Pendente | |
| Construção | 10 (23/11 a 29/11) | Pendente | |
| Teste de aceite | 10 (23/11 a 29/11) | Pendente | |
### 4.6 Sem iteração listada no cronograma

RFs que não aparecem em "Requisitos previstos" de nenhuma iteração. As observações abaixo indicam onde o cronograma menciona o assunto, para ajudar a decidir a iteração.

- **RF00, RF01, RF02 (autenticação e acesso):** MVP com prioridade alta e pré-condição dos RFs de coordenação. Precisam ser construídos antes ou junto da iteração 5.
- **RF04, RF05 (turmas):** não MVP.
- **RF08 a RF12 (doações e prestação de contas):** o cronograma cita "registro de doações e prestação de contas" na iteração 9, mas sem listar RFs. Não MVP.
- **RF25 a RF28 (remoção de dados, frequência e alertas):** não MVP.
- **RF31 a RF34 (avisos):** o cronograma cita o módulo de avisos na iteração 10. Não MVP.
- **RF40 (pessoas autorizadas a retirar o aluno):** não MVP, mas faz parte do formulário de matrícula.

### RF00: Encerrar sessão

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Ao encerrar a sessão, as credenciais do usuário são invalidadas e ele é redirecionado para a tela de login. Após o encerramento, o acesso a qualquer funcionalidade administrativa exige novo login. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | (a definir) | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF01: Autenticar usuário

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Com identificação e credenciais válidas, o coordenador acessa o sistema. Com credenciais inválidas, o acesso é negado e uma mensagem de erro é exibida. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | (a definir) | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF02: Controlar acesso

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Usuário autenticado com perfil de coordenador acessa as funcionalidades administrativas. Requisição sem autenticação ou sem o perfil de coordenador a essas funcionalidades é negada. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | (a definir) | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF04: Editar turma

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Os dados alterados da turma são salvos e exibidos atualizados na consulta. Os alunos já associados à turma são mantidos. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | (a definir) | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF05: Inativar turma

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Após a confirmação, a turma passa a constar como inativa. Os alunos e as frequências vinculados a ela continuam consultáveis, sem exclusão de registros. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | (a definir) | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF08: Registrar doação recebida

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: A doação é salva com o doador ou parceiro, o tipo de recurso e as demais informações obrigatórias, e passa a constar no histórico de doações. Campo obrigatório vazio impede o registro. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11), registro de doações | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | 9 (16/11 a 22/11), registro de doações e prestação de contas | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF09: Editar doação recebida

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Os dados alterados da doação são salvos e exibidos atualizados no histórico. A edição é registrada em log com data e usuário responsável. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11), registro de doações | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | 9 (16/11 a 22/11), registro de doações e prestação de contas | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF10: Registrar documentos de prestação de contas

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Cada documento (orçamento, nota fiscal, registro fotográfico ou audiovisual) só é salvo vinculado a uma doação ou recurso recebido. Após salvo, o documento pode ser aberto na consulta da doação. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11), registro de doações | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | 9 (16/11 a 22/11), registro de doações e prestação de contas | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF11: Editar documentos de prestação de contas

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: O documento já registrado pode ser substituído ou ter seus dados alterados, mantendo o vínculo com a doação ou recurso. A versão atualizada é exibida na consulta. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11), registro de doações | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | 9 (16/11 a 22/11), registro de doações e prestação de contas | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF12: Consultar doações e prestações de contas

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Ao informar um período, o sistema lista as doações registradas nele com os documentos de prestação de contas vinculados. Período sem registros exibe mensagem informativa. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | 8 (09/11 a 15/11), registro de doações | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | 9 (16/11 a 22/11), registro de doações e prestação de contas | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF25: Remover dados do aluno

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: A remoção só é executada após confirmação e mediante pedido do responsável legal ou do próprio aluno, se ele tiver 18 anos ou mais. São removidos a identidade, o CPF e o comprovante de residência, e os demais registros são mantidos. A remoção é registrada em log. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | (a definir) | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF26: Registrar frequência

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Para cada aula de uma turma, a presença ou falta de cada aluno associado é registrada com a data da aula e passa a constar no histórico de frequência do aluno. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | (a definir) | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF27: Consultar frequência

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: O histórico de frequência de um aluno lista as aulas com a data e a situação (presença ou falta) de cada uma. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | (a definir) | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF28: Emitir alerta de faltas críticas

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Quando o número de faltas de um aluno atinge o limite configurado (inicialmente 8 faltas), o sistema gera uma notificação para a coordenação. Abaixo do limite, nenhuma notificação é gerada. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | (a definir) | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF31: Consultar avisos

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Voluntários e familiares visualizam no módulo público os avisos publicados. Aviso removido não é exibido. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | 10 (23/11 a 29/11), módulo de avisos | Pendente | |
| Teste de aceite | (a definir) | Pendente | |
### RF32: Editar aviso

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: As alterações salvas no aviso são exibidas atualizadas no módulo público. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | 10 (23/11 a 29/11), módulo de avisos | Pendente | |
| Teste de aceite | (a definir) | Pendente | |

### RF33: Remover aviso

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Após a confirmação, o aviso deixa de ser exibido no módulo público. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | 10 (23/11 a 29/11), módulo de avisos | Pendente | |
| Teste de aceite | (a definir) | Pendente | |

### RF34: Consultar histórico de avisos

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: O sistema lista os avisos publicados anteriormente com seus destinatários e a data de publicação. |

#### Andamento

| Etapa | Iteração | Status | Link / Observação |
| :--- | :--- | :--- | :--- |
| Detalhamento | (a definir) | Pendente | |
| Design do usuário (protótipo) | (a definir) | Pendente | |
| Construção | 10 (23/11 a 29/11), módulo de avisos | Pendente | |
| Teste de aceite | (a definir) | Pendente | |


### RF40: Informar pessoas autorizadas a retirar o aluno

#### Detalhamento

| Campo | Descrição |
| :--- | :--- |
| **Declaração** | (a detalhar) |
| **Ator principal** | (a detalhar) |
| **Rastreabilidade** | US-XX / UC-XX |
| **Dados** | (a detalhar) |
| **Pré-condições** | (a detalhar) |
| **Processamento** | (a detalhar) |
| **Saídas** | (a detalhar) |
| **Regras de negócio** | (a detalhar) |
| **Critérios de aceitação** | Do backlog, a reescrever em Dado/Quando/Então: Para aluno menor de idade, o formulário exige ao menos uma pessoa autorizada, com nome e contato, ou a indicação de que o menor pode ir embora sozinho. Para aluno maior de idade, essa informação não é exigida. |

## 6. Registro de alterações

| Data | Alteração | Autor |
| :--- | :--- | :--- |
| (a definir) | Criação do documento com o detalhamento dos RF13 a RF20 | (a definir) |
| (a definir) | Alinhamento com o cronograma (seção 6) e o backlog (seção 10): RF13 a RF20 nas iterações 4 a 6; prioridades e MVP conforme matriz 4 x 4 | (a definir) |
| (a definir) | Inclusão das fichas de todos os RFs (RF00 a RF42), agrupadas por iteração | (a definir) |
| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 20/10/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) | |