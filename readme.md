# SigCECP - Ambiente de desenvolvimento e execução

Este guia explica como configurar o ambiente de desenvolvimento, instalar as dependências, preparar o banco de dados e executar a aplicação **SigCECP**, desenvolvida com Python e FastAPI.

Os comandos devem ser executados no terminal, a partir da raiz do projeto.

## 1. Criar o ambiente virtual

Um ambiente virtual isola as bibliotecas Python utilizadas pelo projeto, evitando misturá-las com as de outros projetos ou com a instalação global do Python.

Execute o comando correspondente ao seu sistema:

### Windows, Linux e macOS

```bash
python -m venv .venv
```

O comando cria uma pasta chamada `.venv` dentro do projeto.

> Em geral, não é necessário criar o ambiente virtual novamente. Se a pasta `.venv` já existe e está configurada, avance para a etapa de ativação.

## 2. Ativar o ambiente virtual

A ativação depende do sistema operacional e do terminal utilizado.

### Windows - PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows - Prompt de Comando (CMD)

```bat
.venv\Scripts\activate.bat
```

### Linux ou macOS - Bash/Zsh

```bash
source .venv/bin/activate
```

Quando a ativação funcionar, normalmente aparecerá `(.venv)` no início da linha do terminal. Isso indica que os comandos Python e `pip` estão utilizando o ambiente virtual.

## 3. Instalar as dependências

Com o ambiente virtual ativado, instale as dependências registradas no `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Sempre execute esse comando com o ambiente virtual ativado.

## 4. Configurar e preparar o banco de dados

O projeto utiliza SQLAlchemy para o mapeamento objeto-relacional e Alembic para controlar as alterações na estrutura do banco de dados.

Antes de iniciar a aplicação, prepare o banco pelas migrações. A aplicação não cria tabelas nem executa migrações automaticamente.

### 4.1. Aplicar as migrações

Na raiz do projeto, com o ambiente virtual ativo, configure a conexão desejada.

Para utilizar SQLite:

```powershell
$env:DATABASE_URL = "sqlite:///sigcecp.db"
python -m alembic upgrade head
```

No Linux ou macOS:

```bash
export DATABASE_URL="sqlite:///sigcecp.db"
python -m alembic upgrade head
```

O Alembic reutiliza `DATABASE_URL` (ambiente ou `.env`) e a conexão definida em `backend/database.py`.

Não salve credenciais no `alembic.ini`.

### 4.2. Banco de dados existente

A revisão `0001_baseline_publicacoes` contém somente as tabelas preexistentes `publicacoes` e `publicacao_midias`.

Para um banco existente criado por `create_all`, não execute a baseline diretamente. Compare antes tabelas, colunas, tipos, nulabilidade, índices e chaves com essa revisão.

Somente depois de confirmar equivalência e preparar um backup, marque manualmente a baseline e aplique as migrações posteriores:

```bash
python -m alembic stamp 0001_baseline_publicacoes
python -m alembic upgrade head
```

O comando `stamp` apenas registra a revisão atual; ele não cria tabelas nem corrige diferenças de estrutura.

Se houver diferenças, reconcilie-as antes de marcar a baseline. Utilize sempre a conexão pretendida e, para verificações, prefira um banco SQLite descartável.

Nenhum desses comandos é executado automaticamente durante a inicialização da aplicação.

## 5. Executar a aplicação

Com o ambiente virtual ativado e as migrações aplicadas, inicie o servidor de desenvolvimento:

```bash
uvicorn backend.main:app --reload
```

O terminal mostrará o endereço local da aplicação.

Normalmente, a aplicação estará disponível em:

- Aplicação: `http://127.0.0.1:8000`
- Documentação interativa: `http://127.0.0.1:8000/docs`

O parâmetro `--reload` permite reiniciar automaticamente o servidor quando arquivos Python são modificados.

> O comando depende da estrutura do projeto. Se o módulo ou a instância tiver outro nome, ajuste o comando de acordo com a configuração da aplicação.

## 6. Persistência e serviços de eventos

O módulo de eventos utiliza SQLAlchemy para persistir os registros e serviços específicos para executar as operações de criação, consulta, atualização e remoção.

As migrações relacionadas aos eventos são aplicadas em sequência:

- `0002_cria_eventos`: adiciona a tabela `eventos`.
- `f18d744809e3_adicionar_imagem_e_video_aos_eventos`: adiciona os campos de imagem e vídeo à estrutura de eventos.

As migrações devem estar aplicadas antes de utilizar os serviços em `backend/eventos/services.py`.

### 6.1. Operações disponíveis

O módulo disponibiliza as seguintes operações:

| Serviço | Responsabilidade |
|---|---|
| `criar_evento(db, dados, imagem, video)` | Cria um evento e salva suas mídias opcionais. |
| `listar_eventos(db)` | Retorna os eventos ordenados por data, horário de início e identificador. |
| `buscar_evento_por_id(db, evento_id)` | Retorna o evento ou `None`. |
| `buscar_evento(db, evento_id)` | Retorna o evento ou gera erro 404 quando não encontrado. |
| `atualizar_evento(db, evento_id, dados, imagem, video)` | Atualiza os dados e, quando fornecidas, as mídias do evento. |
| `remover_evento(db, evento_id)` | Remove o registro do evento. |

Os serviços recebem uma `Session` do SQLAlchemy. As consultas não fazem commit.

`criar_evento` confirma a transação, executa rollback em falhas anteriores à confirmação e não fecha a sessão recebida. O chamador, incluindo o router, não deve repetir o commit.

Se a leitura de atualização após o commit falhar, o evento já estará gravado e não será desfeito por rollback.

`atualizar_evento` modifica os campos recebidos e substitui as mídias somente quando novos arquivos são enviados. Se nenhuma nova mídia for informada, os arquivos existentes são preservados.

### 6.2. Estrutura dos dados

As escolhas técnicas de armazenamento incluem:

- `titulo`, `subtitulo` e `nome`: `String(120)`, acompanhando os formulários.
- `local` e `meio_pagamento`: `String(255)`.
- `descricao`: `Text`, com limite de 16.000 caracteres no schema para caber no `TEXT` do MySQL mesmo com caracteres UTF-8 de quatro bytes.
- `valor`: `Numeric(12, 2)`, retornado como `Decimal`. O schema rejeita valores fora da precisão para evitar arredondamento silencioso.
- `pesagem`: `String(13)` com restrição `CHECK`, aceitando `sim`, `nao` e `nao_se_aplica`, sem tipo ENUM específico de um banco.
- Horários locais: sem fuso nem frações de segundo, para não perder informação no `TIME` padrão do MySQL.

O schema valida os limites textuais antes da persistência e não corta textos.

Continuam pendentes as regras de virada de dia, relação entre início e término, prazo de pagamento, valores permitidos e tratamento de dados de pagamento em eventos gratuitos.

Dados de pagamento válidos informados em eventos gratuitos são mantidos. RF17 e RF20 seguem parciais.

## 7. Upload e armazenamento de mídias dos eventos

O módulo de eventos permite anexar imagens e vídeos durante a publicação e a edição de eventos.

As mídias são enviadas por formulários HTML com `multipart/form-data` e recebidas pelo FastAPI como `UploadFile`.

### 7.1. Formatos aceitos

Os formatos de imagem permitidos são:

- JPEG (`image/jpeg`);
- PNG (`image/png`);
- WebP (`image/webp`).

Os formatos de vídeo permitidos são:

- MP4 (`video/mp4`);
- WebM (`video/webm`);
- OGG (`video/ogg`).

A validação é realizada em `backend/eventos/media.py`, por meio do tipo MIME informado no arquivo recebido.

### 7.2. Organização dos arquivos

Os arquivos são armazenados no diretório:

```text
backend/
└── media/
    └── eventos/
        ├── identificador-unico.jpeg
        ├── identificador-unico.png
        └── identificador-unico.mp4
```

Os nomes dos arquivos são gerados com UUID, evitando conflitos entre arquivos enviados com o mesmo nome original.

O banco de dados armazena somente os caminhos relativos das mídias nos campos `imagem` e `video` da tabela `eventos`.

Exemplo:

```text
imagem = eventos/identificador-unico.jpeg
video = eventos/identificador-unico.mp4
```

Os arquivos físicos permanecem no sistema de arquivos, enquanto o banco mantém suas referências.

### 7.3. Acesso às mídias

O diretório de mídias é disponibilizado pela aplicação por meio da rota `/media`.

Exemplo de endereço:

```text
http://127.0.0.1:8000/media/eventos/identificador-unico.jpeg
```

As páginas públicas utilizam os caminhos armazenados no banco para exibir imagens e vídeos associados aos eventos.

### 7.4. Pré-visualização

Os formulários de publicação e edição permitem visualizar imagens e vídeos selecionados antes do envio.

A pré-visualização é realizada no navegador com JavaScript e URLs temporárias criadas por `URL.createObjectURL()`.

Essas URLs são utilizadas somente para exibição local e não representam os caminhos definitivos dos arquivos armazenados no servidor.

### 7.5. Atualização e remoção de mídias

Ao editar um evento:

- Se uma nova imagem for enviada, a imagem anterior é substituída.
- Se um novo vídeo for enviado, o vídeo anterior é substituído.
- Se nenhuma mídia nova for enviada, os arquivos existentes são preservados.

O serviço utiliza as funções `salvar_midia()` e `remover_midia()` para administrar os arquivos.

Na criação, se ocorrer uma falha durante a operação, o serviço executa rollback da transação e tenta remover as mídias que já haviam sido salvas.

> Os arquivos de mídia devem ser preservados em backups separados do banco de dados, pois as referências armazenadas no SQLite não contêm os próprios arquivos.

## 8. Consulta pública e gerenciamento de eventos

O módulo de eventos possui páginas destinadas à coordenação e páginas de consulta pública.

### 8.1. Rotas de gerenciamento

As principais rotas do módulo são:

| Método | Rota | Finalidade |
|---|---|---|
| GET | `/coordenacao/eventos` | Lista os eventos cadastrados. |
| GET | `/coordenacao/eventos/novo` | Apresenta o formulário de publicação. |
| POST | `/coordenacao/eventos/novo` | Cadastra um evento e suas mídias opcionais. |
| GET | `/coordenacao/eventos/{evento_id}/editar` | Apresenta o formulário de edição. |
| POST | `/coordenacao/eventos/{evento_id}/editar` | Atualiza os dados e as mídias do evento. |
| GET | `/coordenacao/eventos/{evento_id}/remover` | Apresenta a confirmação de remoção. |
| POST | `/coordenacao/eventos/{evento_id}/remover` | Remove o registro do evento. |

As operações de cadastro e edição recebem os dados do formulário e os arquivos enviados, utilizando os serviços do módulo de eventos.

### 8.2. Consulta pública

As rotas públicas são:

| Método | Rota | Finalidade |
|---|---|---|
| GET | `/eventos` | Lista os eventos disponíveis publicamente. |
| GET | `/eventos/{evento_id}` | Apresenta os detalhes de um evento. |

A consulta pública não exige cadastro ou login.

Um identificador inexistente retorna erro 404.

### 8.3. Estado dos eventos

O estado do evento é calculado durante a consulta, sem armazenar uma coluna específica no banco.

São utilizados três estados:

- **Em breve:** quando o instante atual é anterior ao início do evento.
- **Em andamento:** quando o instante atual está entre o início e o término, incluindo os dois instantes.
- **Encerrado:** quando o instante atual é posterior ao término.

O cálculo utiliza o fuso `America/Sao_Paulo`, seguindo a indicação de horário de Brasília dos formulários.

O pacote `tzdata` fornece as regras de fuso em ambientes sem base de fusos do sistema, como Windows.

A documentação de RF20 não define o fuso nem eventos que atravessam a meia-noite. Provisoriamente, início e término são interpretados na data cadastrada.

Se o término for anterior ao início, a duração noturna não pode ser representada corretamente sem uma regra ou data final definida pelo grupo.

## 9. Como sair do ambiente virtual

Quando terminar de trabalhar, você pode desativar o ambiente virtual com:

```bash
deactivate
```

Isso não apaga o ambiente virtual; apenas encerra a ativação naquele terminal.

Na próxima vez que abrir um terminal para trabalhar no projeto, entre na pasta do projeto e ative o ambiente virtual novamente.

## 10. Estrutura principal do projeto

A organização principal dos diretórios é:

```text
SigCECP/
├── alembic/
│   └── versions/
├── backend/
│   ├── eventos/
│   │   ├── media.py
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── services.py
│   ├── publicacoes/
│   │   ├── router.py
│   │   └── services.py
│   ├── media/
│   │   └── eventos/
│   ├── config.py
│   ├── database.py
│   └── main.py
├── frontend/
│   ├── assets/
│   │   ├── img/
│   │   ├── js/
│   │   └── style/
│   ├── coordenacao/
│   │   ├── conteudo/
│   │   └── eventos/
│   ├── publico/
│   └── base.html
├── requirements.txt
├── alembic.ini
└── README.md
```

O diretório `backend` concentra a lógica da aplicação, incluindo rotas, modelos, schemas, serviços e persistência.

O diretório `frontend` contém os templates Jinja2, arquivos CSS, JavaScript e imagens utilizados pelas interfaces.

O diretório `backend/media` armazena os arquivos enviados pelos usuários.

O diretório `alembic` contém as configurações e revisões utilizadas para controlar a evolução do banco de dados.

## 11. Autenticação da área administrativa

Somente `/coordenacao/*` exige login; todo o restante do site é público. O administrador é um registro da tabela `administradores` (senha apenas como hash bcrypt).

### 11.1. Configuração

1. Copie `.env.example` para `.env` e defina `AUTH_SECRET_KEY` (obrigatória em produção; `python -c "import secrets; print(secrets.token_urlsafe(48))"`). Em produção use `APP_ENV=production` e sirva por HTTPS.
2. Aplique as migrações (`python -m alembic upgrade head`); a revisão `0003_cria_administradores` cria as tabelas de administrador e de refresh tokens.
3. Crie o administrador (a senha é pedida no terminal, mínimo de 12 caracteres e no máximo 72 bytes):

```bash
python -m backend.auth.criar_admin --usuario CECP0001
python -m backend.auth.criar_admin --usuario CECP0001 --redefinir-senha   # troca a senha e encerra as sessões
```

### 11.2. Rotas

| Método | Rota | Finalidade |
|---|---|---|
| GET/POST | `/coordenacao/auth/login` | Página e envio do login. |
| POST | `/coordenacao/auth/refresh` | Renovação explícita (exige CSRF); rotaciona o refresh token. |
| POST | `/coordenacao/auth/logout` | Encerra a sessão no servidor e apaga os cookies (exige CSRF). |

Sessão: access token (JWT, 15 min) e refresh token (opaco, 7 dias de inatividade, teto de 30 dias) em cookies `HttpOnly` distintos. Com o access expirado, a renovação é transparente (`backend/auth/middleware.py`).

### 11.3. Ao criar novas rotas ou formulários administrativos

- Rotas sob `/coordenacao` devem estar em um router com `dependencies=PROTECAO_ADMIN` (`backend.auth.dependencies`). Um teste (`test_todas_as_rotas_administrativas_exigem_admin`) falha se alguma ficar sem proteção.
- Todo `<form method="post">` administrativo deve conter `{{ csrf_input }}`.
- Nos testes de rotas administrativas a autenticação é substituída automaticamente; para testá-la de verdade use `pytestmark = pytest.mark.auth_real`.

