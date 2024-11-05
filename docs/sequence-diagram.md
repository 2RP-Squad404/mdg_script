# **Diagrama de sequência**:

```mermaid
sequenceDiagram
  participant Apt as Apt
  participant Pip as Pip
  participant Pipx as Pipx
  participant P as Poetry
  participant Pv as Pyenv
  participant Py as Python
  participant S as Snap
  participant G as Google Cloud CLI
  participant R as Repositório
  participant T as Ubuntu WSL Terminal
  participant App as MDG Script
  participant B as Browser
  participant U as User
  participant SM as Secret Manager API
  participant BQ as BigQuery
  participant GM as Gemini

  T ->> S: Instalar "google-cloud-cli" via snap
  S -->> G: 

  T ->> Apt: Instalar "pyenv" via apt
  Apt -->> Pv: 

  T ->> Pv: Instalar a versão desejada do Python via pyenv
  Pv -->> Py: 
  Py ->> T: Definir a versão do Python instalada como global do pyenv

  T ->> Apt: Instalar "pip" via apt
  Apt -->> Pip: 

  T ->> Pip: Instalar "pipx" via pip
  Pip -->> Pipx: 

  T ->> Pipx: Instalar "poetry" via pipx
  Pipx -->> P: 

  T ->> R: Clonar o repositório
  R -->> T: Repositório clonado
  T ->> App: Abrir pasta do projeto no terminal

  T ->> G: Solicitar login no serviço "Google Cloud SDK"
  G -->> T: Retorna o link para fazer login
  T ->> B: Acessar o link
  B -->> T: Fazer login na sua conta da organização

  T ->> G: Solicitar login no serviço "Google Auth Library"
  G -->> T: Retorna o link para fazer login
  T ->> B: Acessar o link
  B -->> T: Fazer login na sua conta da organização

  App ->> P: Instalar dependências
  P -->> App: 
  App ->> P: Inicia um ambiente virtual com o Poetry
  P -->> App: 
  App ->> P: Atualizar as dependências
  P -->> App: 
  App ->> P: Ativar o ambiente virtual do Poetry
  P -->> App: 
  App ->> App: Executar a aplicação via taskipy

  App ->> G: Solicita a lista de PROJECT_ID que o usuário tem acesso
  G -->> App: Retorna a lista de PROJECT_ID
  App ->> U: Solicita que o usuário escolha um PROJECT_ID da lista retornada
  U -->> App: Retorna e armazena o PROJECT_ID que o usuário escolheu

  App ->> G: Solicita a lista de SECRETS existentes no Projeto escolhido
  G -->> App: Retorna a lista de SECRETS
  App ->> U: Solicita que o usuário escolha um SECRET da lista retornada
  U -->> App: Retorna e armazena o SECRET que o usuário escolheu

  App ->> SM: Solicita as CREDENCIAIS da conta de serviço que estão salvas no Secret
  SM -->> App: Retorna e armazena as CREDENCIAIS da conta de serviço

  App ->> BQ: Solicita a lista de DATASETS que existem naquele Projeto
  BQ -->> App: Retorna a lista de DATASETS
  App ->> U: Solicita que o usuário escolha um DATASET da lista retornada
  U -->> App: Retorna e armazena o DATASET que o usuário escolheu
  
  App ->> BQ: Solicita os SCHEMAS de todas TABELAS do DATASET
  BQ -->> App: Retorna e armazena todos os SCHEMAS na pasta "bq_schemas_json"

  App ->> App: Cria os MODELS do Pydantic com base nos SCHEMAS e salva na pasta "py_models"

  App ->> GM: Envia o prompt que contém ("py_models" + "data_sample_json" + "example_of_expected_return") para o Gemini que cria a função faker para gerar dados mockados
  GM -->> App: Retorna e armazena a FUNÇÃO gerada pelo Gemini na pasta "gm_functions"

  App ->> App: Gera dados mockados utilizando "gm_functions" e armazena em JSONL na pasta "jsonl_mockdata"

  App ->> BQ: Grava dados mockados do JSONL nas tabelas do BigQuery
```

----

### [**> Voltar página.**](/README.md)