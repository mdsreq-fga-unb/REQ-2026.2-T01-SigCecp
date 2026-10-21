# CP3 - Gestão de conteúdo institucional

### RF13: Publicar conteúdo institucional

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

| Versão | Data | Descrição | Autor(es/as) | Revisor(es/as) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 20/10/2026 | Transcrição do documento para markdown | [Marcos Monteiro](https://github.com/montmarcos) | |