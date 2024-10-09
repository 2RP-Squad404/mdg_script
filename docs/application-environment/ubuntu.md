# **Preparar o ambiente para rodar a aplicação via `Ubuntu WSL Terminal`**

O terminal utilizado pode ser instalado através da ["Microsoft Store - Ubuntu"](https://www.microsoft.com/store/productId/9PDXGNCFSCZV?ocid=pdpshare)

Após instalado, abra o terminal, todo o restante do processo será feito através dele.

## **1. Gerenciamento de Ambiente:**

[![Pyenv](https://img.shields.io/badge/Pyenv-2.4.13-3776ab?logo=python)](https://github.com/pyenv/pyenv)

Utilizaremos o `pyenv` para auxiliar no gerenciamento do ambiente e trabalhar com a versão desejada do Python.

Siga os passos abaixo para fazer a instalação dessa ferramenta

- Atualize os pacotes do sistema:
    ```shell
    sudo apt update && sudo apt upgrade
    ```

- Instale dependências necessárias para o pyenv:
    ```shell
    sudo apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    ```

- Clone o repositório pyenv:
    ```shell
    curl https://pyenv.run | bash
    ```

- Adicione o pyenv ao PATH:
    ```shell
    echo -e '\n# Pyenv Configuration\nexport PYTHON_BUILD_ARIA2_OPTS="-x 10 -k 1M"\nexport PATH="${HOME}/.pyenv/bin:$PATH"\neval "$(pyenv init --path)"\neval "$(pyenv init -)"\neval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
    ```

- Reiniciar o terminal.

## **2. Linguagem de Programação:**

- Atualizar o `pyenv` e verificar se foi corretamente instalado, o comando abaixo deverá listar a versão do `pyenv` e os seus comandos.
    ```shell
    pyenv update
    pyenv
    ```

- Instale a versão do python desejada

    ```shell
    pyenv install 3.12.6
    ```
- Caso você tiver uma versão antiga do python instalada rode esse comando:
    ```shell
    pyenv global 3.12.6
    ```
## **3. Gerenciamento de Dependências:**

[![Pipx](https://img.shields.io/badge/Pipx-1.7.1-2cffaa?logo=pipx)](https://pipx.pypa.io/stable/)
[![Poetry](https://img.shields.io/badge/Poetry-1.8.3-60a5fa?logo=poetry)](https://python-poetry.org)

- Instale o `pip` (caso não tenha)
    ```shell
    sudo apt install pip
    ```

- Instale o `pipx` (via `pip`)
    ```shell
    pip install pipx
    ```

- Instale o `poetry` (via `pipx`)
    ```shell
    pipx install poetry
    ```

- Reinicie o terminal.

## **4.Bibliotecas e Ferramentas de Desenvolvimento:**

- Execute uma opção:

    - Instalar somente as bibliotecas
        ```shell
        poetry install --no-dev
        ```

    - Instalar as bibliotecas + ferramentas de desenvolvimento
        ```shell
        poetry install
        ```

- Inicie o ambiente
    ```shell
    poetry shell
    ```

- Ative o ambiente
    ```shell
    source $(poetry env info --path)/bin/activate
    ```

## **Comando para rodar o script:**

```shell
task run
```

----

### [**> Voltar página.**](/README.md)