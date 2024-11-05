# **Como preparar o ambiente para rodar a aplicação via `Ubuntu WSL Terminal`:**

[![Ubuntu WSL](https://img.shields.io/badge/Ubuntu%20WSL-Download-e95420?logo=ubuntu)](https://ubuntu.com/desktop/wsl)

OBS.: Todos os procedimentos a seguir será feito através do `Ubuntu WSL Terminal`

# **Configuração do ambiente no Ubuntu:**

## **1. Gerenciamento de Ambiente:**

### **1.1. Instalação do `gcloud`:**

[![Google Cloud CLI](https://img.shields.io/badge/Google%20Cloud%20CLI%2FSDK-498.0.0-4285f4?logo=google-cloud)](https://cloud.google.com/sdk/docs/install#deb)

O `gcloud` possibilita autenticar-se com o Google Cloud Platform via CLI.

Siga os passos abaixo para fazer a instalação dessa ferramenta:

- Atualizar os pacotes do sistema (Recomendado antes de qualquer instalação):

    ```shell
    sudo apt update && sudo apt upgrade
    ```

- Instalar o `gcloud`:

    ```shell
    sudo snap install google-cloud-cli --classic
    ```

- Reiniciar o terminal:

    ```shell
    exec bash
    ```

----

### **1.2. Instalação do `pyenv`:**

[![Pyenv](https://img.shields.io/badge/Pyenv-2.4.13-3776ab?logo=python)](https://github.com/pyenv/pyenv)

O `pyenv` possibilita trabalhar com a versão desejada do Python.

Siga os passos abaixo para fazer a instalação dessa ferramenta:

- Atualizar os pacotes do sistema (Recomendado antes de qualquer instalação):

    ```shell
    sudo apt update && sudo apt upgrade
    ```

- Instalar as dependências necessárias para o pyenv:

    ```shell
    sudo apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    ```

- Clonar o repositório do `pyenv`:

    ```shell
    curl https://pyenv.run | bash
    ```

- Adicionar o pyenv ao PATH:

    ```shell
    echo -e '\n# Pyenv Configuration\nexport PYTHON_BUILD_ARIA2_OPTS="-x 10 -k 1M"\nexport PATH="${HOME}/.pyenv/bin:$PATH"\neval "$(pyenv init --path)"\neval "$(pyenv init -)"\neval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
    ```

- Reiniciar o terminal:

    ```shell
    exec bash
    ```

#### **1.2.1. Linguagem de Programação:**

- Atualizar o `pyenv` e verificar se foi corretamente instalado, o comando abaixo listará a versão do `pyenv` e os seus comandos:

    ```shell
    pyenv update
    pyenv
    ```

- Instalar a versão do python desejada:

    ```shell
    pyenv install 3.12.6
    ```
- Caso você tiver uma versão antiga do python instalada:

    ```shell
    pyenv global 3.12.6
    ```

## **2. Gerenciamento de Dependências:**

[![Pipx](https://img.shields.io/badge/Pipx-1.7.1-2cffaa?logo=pipx)](https://pipx.pypa.io/stable/)
[![Poetry](https://img.shields.io/badge/Poetry-1.8.3-60a5fa?logo=poetry)](https://python-poetry.org)

- Atualizar os pacotes do sistema (Recomendado antes de qualquer instalação):

    ```shell
    sudo apt update && sudo apt upgrade
    ```

- Instalar `pip`:

    ```shell
    sudo apt install pip
    ```

- Instalar `pipx` via `pip`:

    ```shell
    pip install pipx
    ```

- Instalar `poetry` via `pipx`:

    ```shell
    pipx install poetry
    ```

- Reiniciar o terminal:

    ```shell
    exec bash
    ```

## **3. Clonar o repositório com o `git`:**

[![Git](https://img.shields.io/badge/Git-Download-f05032?logo=git)](https://git-scm.com/downloads)

O `git` possibilita trabalhar com versionamento e gerenciamento de projetos.

Siga os passos abaixo para fazer a instalação dessa ferramenta:

- Acessar no Terminal o diretório onde a aplicação será instalada.

- Clonar o repositório:

    ```shell
    git clone https://github.com/2RP-Squad404/mdg_script.git
    ```

- Abrir a aplicação:

    ```shell
    cd mdg_script
    ```

## **4. Autenticação via `gcloud`:**

- Autenticar-se via "Google Cloud SDK" (A conta que conectar deverá possuir as permissões necessárias):
    
    ```shell
    gcloud auth login
    ```

- Autenticar-se via "Google Auth Library" (A conta que conectar deverá possuir as permissões necessárias):

    ```shell
    gcloud auth application-default login
    ```

## **5. Instalar Dependências (Bibliotecas e Ferramentas de Desenvolvimento):**

- Lembre-se do terminal estar no diretório da aplicação.

- Executar uma opção:

    - Instalar somente as bibliotecas:

        ```shell
        poetry install --no-dev
        ```

    - Instalar as bibliotecas + ferramentas de desenvolvimento:

        ```shell
        poetry install
        ```

- Iniciar o ambiente virtual:

    ```shell
    poetry shell
    ```

## **6. Rodar a aplicação:**

- Atualizar as dependências do `poetry`:

    ```shell
    poetry update
    ```

- Ativar o ambiente virtual do `poetry`:

    ```shell
    source $(poetry env info --path)/bin/activate
    ```

- Executar a aplicação via `taskipy`:

    ```shell
    task run
    ```

----

### [**> Voltar página.**](/README.md)