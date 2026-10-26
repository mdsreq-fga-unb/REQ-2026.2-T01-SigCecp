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



