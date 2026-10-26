# Como criar e ativar um ambiente virtual Python para um projeto FastAPI

Este guia explica como preparar o ambiente de desenvolvimento de um
projeto que utiliza **Python** e **FastAPI**. Os comandos abaixo devem
ser executados no terminal, dentro da pasta do projeto.


## 1. Crie o ambiente virtual

Um ambiente virtual isola as bibliotecas Python utilizadas pelo projeto,
evitando misturá-las com as de outros projetos ou com a instalação
global do Python.

Execute **uma** das opções abaixo, conforme seu sistema:

### Windows, Linux e MacOS

``` powershell
python -m venv .venv
```


O comando cria uma pasta chamada `.venv` dentro do projeto. Ela contém o
ambiente virtual.

> Em geral, não é necessário criar o ambiente virtual toda vez. Se a
> pasta `.venv` já existe e está configurada para o projeto, vá direto
> para a etapa de ativação.

## 2. Ative o ambiente virtual

A ativação depende do sistema operacional e do terminal utilizado.

### Windows --- PowerShell

``` powershell
.\.venv\Scripts\Activate.ps1
```

### Windows --- Prompt de Comando (CMD)

``` bat
.venv\Scripts\activate.bat
```

### Linux ou macOS --- Bash/Zsh

``` bash
source .venv/bin/activate
```

Quando a ativação funcionar, normalmente aparecerá `(.venv)` no início
da linha do terminal. Isso indica que os comandos Python e `pip` estão
usando o ambiente virtual.

## 3. Instale o Requirements

Instale o requirements.txt:

``` bash
python -m pip install -r requirements.txt
```

Execute esse comando com o ambiente virtual ativado.

## 4. Execute a aplicação

Antes de iniciar, prepare o banco pelas migrações. A aplicação não cria
tabelas nem executa migrações automaticamente.

Na raiz do projeto, com o ambiente virtual ativo, para um banco vazio:

``` powershell
# Opcional: selecione a conexão; sem isso, vale a configuração de backend/database.py.
$env:DATABASE_URL = "sqlite:///sigcecp.db"
python -m alembic upgrade head
```

O Alembic reutiliza `DATABASE_URL` (ambiente ou `.env`) e a conexão
definida em `backend/database.py`. Não salve credenciais no `alembic.ini`.
A revisão `0001_baseline_publicacoes` contém somente as tabelas
preexistentes `publicacoes` e `publicacao_midias`.

Para um banco existente criado por `create_all`, não execute a baseline
diretamente: compare antes tabelas, colunas, tipos, nulabilidade,
índices e chaves com essa revisão. Só depois de confirmar equivalência
e preparar um backup, marque manualmente a baseline e aplique as
migrações posteriores:

``` powershell
python -m alembic stamp 0001_baseline_publicacoes
python -m alembic upgrade head
```

O `stamp` apenas registra a revisão; não corrige diferenças de estrutura.
Se houver diferenças, reconcilie-as antes de marcar a baseline.
Use sempre a conexão pretendida; para verificações, escolha um SQLite
descartável. Nenhum desses comandos roda automaticamente no startup.

Inicie o servidor de desenvolvimento com:

``` bash
uvicorn backend.main:app --reload
```
O terminal mostrará o endereço local da aplicação. Normalmente, a
documentação interativa fica disponível em `http://127.0.0.1:8000/docs`.

> O comando depende da estrutura do projeto. Se o arquivo ou a instância
> tiver outro nome, ajuste o comando de acordo com a configuração da
> aplicação.

## 5. Como sair do ambiente virtual

Quando terminar de trabalhar, você pode desativá-lo com:

``` bash
deactivate
```

Isso não apaga o ambiente virtual; apenas encerra a ativação naquele
terminal.

Na próxima vez que abrir um terminal para trabalhar no projeto, entre na
pasta e ative o ambiente virtual novamente.

## 6. Persistência e serviços de eventos

A revisão `0002_cria_eventos`, posterior à baseline, adiciona somente
a tabela `eventos`. As migrações devem estar aplicadas antes de usar
os serviços em `backend/eventos/services.py`.

`criar_evento(db, dados)` recebe uma `Session` dedicada, sem alterações
pendentes de outras operações, e um `EventoCreate` validado. O serviço
confirma a transação, faz rollback em falhas anteriores à confirmação
e não fecha a sessão recebida. O chamador (incluindo o router futuro)
não deve repetir o commit. Se a leitura de atualização após o commit
falhar, o evento já estará gravado e não será desfeito por rollback.

`listar_eventos(db)` retorna uma lista ordenada por `data`, `inicio`
e `id`, crescentes. `buscar_evento_por_id(db, evento_id)` retorna o
registro ou `None`. As consultas não fazem commit.

Escolhas técnicas de armazenamento, ainda não regras aprovadas pelo cliente:

- `titulo`, `subtitulo` e `nome`: `String(120)`, acompanhando os formulários.
- `local` e `meio_pagamento`: `String(255)`.
- `descricao`: `Text`, com limite de 16.000 caracteres no schema para
  caber no `TEXT` do MySQL mesmo com caracteres UTF-8 de quatro bytes.
- `valor`: `Numeric(12, 2)`, retornado como `Decimal`. O schema rejeita
  valores fora da precisão (dez dígitos inteiros e dois decimais) para
  evitar arredondamento silencioso. Não foram definidos mínimo positivo
  ou proibição de zero/negativos.
- `pesagem`: `String(13)` com restrição `CHECK`, aceitando `sim`, `nao`
  e `nao_se_aplica`, sem tipo ENUM específico de um banco. Em MySQL,
  a aplicação da restrição depende de uma versão que execute `CHECK`.
- Horários locais, sem fuso nem frações de segundo, para não perder
  informação no `TIME` padrão do MySQL; o schema rejeita esses formatos.

O schema valida os limites textuais antes da persistência e não corta
textos. Continuam pendentes as regras de virada de dia, relação entre
início e término, prazo de pagamento, valores permitidos e tratamento
de dados de pagamento em eventos gratuitos. Dados de pagamento válidos
informados em eventos gratuitos são mantidos. RF17 e RF20 seguem parciais;
o formulário de cadastro ainda não está integrado ao serviço de criação.

## 7. Consulta pública de eventos

Com as migrações aplicadas, `/eventos` lista os registros e
`/eventos/{id}` mostra os detalhes, sem login. Um ID inexistente retorna
404. O estado é calculado em cada consulta, sem coluna no banco.

O fuso `America/Sao_Paulo` segue a indicação de horário de Brasília dos
formulários; `tzdata` fornece as regras de fuso em ambientes sem base
do sistema, como Windows. A documentação de RF20 não define fuso nem
eventos que atravessam a meia-noite. Provisoriamente, início e término
são interpretados na data cadastrada; o instante exato do início é
"Em andamento" e o instante exato do término ainda é "Em andamento".
Após o término, o estado é "Encerrado". Se o término for anterior ao
início, a duração noturna não pode ser representada corretamente sem
uma regra ou data final definida pelo grupo.



