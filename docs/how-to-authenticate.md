
# Autenticação no GCP e Identificação do Projeto

Este documento tem como objetivo ensinar a como fazer a autenticação pelo CLI do Google Cloud e como fazer a utilização das contas de serviço criadas, além de como fazer a identificação do projeto no GCP.

## Pré-requisitos

- Google Cloud CLI
- Conta de serviço criada no GCP
- Conta Google com acesso ao Secret Manager


---

### Instalar a CLI do Google Cloud

#### No Ubuntu:

Instale a CLI do Google Cloud com o comando:


    sudo snap install google-cloud-cli --classic


#### No Windows:

Baixe e instale a [Google Cloud CLI](https://cloud.google.com/sdk/docs/install?hl=pt_br&_gl=1*hqmbvj*_up*MQ..&gclid=Cj0KCQjwo8S3BhDeARIsAFRmkOOgrCgnl9O-8Xvb8r41OvcYyrZeWzpr-tLnO8mhQMm0cx8lWGYHrwkaAhmnEALw_wcB&gclsrc=aw.ds).

- Durante a instalação, clique em **Next** nas opções.

---

## Autenticação utilizando CLI

Após abrir o projeto é necessário abrir o terminal de comandos e executar o seguinte comando:

    gcloud auth login

Após isso você sera redirecionado para uma pagina do google para efetuar o login. Após terminar você deve fazer o login novamente utilizando a mesma conta, porém com um comando diferente para criar um login padrão:

    gcloud auth application-default login

Se quiser você pode visualizar os seus projetos para ter certeza que está na conta correta, porém não é necessário específicar nenhum projeto pelo terminal. Para visualizar os projetos é necessário o seguinte comando:

    gcloud projects list

---

## Contas de Serviço e Identificação dos Projetos

### 1. Conta de serviço e Secret

Para fazer a utilização do código é necessário ter criado uma conta de serviço no projeto GCP que esteja querendo inserir os dados, e as credênciais dessa conta devem estar localizados no secret manager.

Caso não saiba como criar uma conta de serviço ou um secret aqui estão os tutoriais fornecidos pela Google:

[Criação de Conta de Serviço](https://cloud.google.com/compute/docs/access/service-accounts?hl=pt-br)

[Criação de Secrets no Secret Manager](https://cloud.google.com/security/products/secret-manager?hl=pt-BR)

### 2. Criação das variáveis de ambiente

Esse projeto trabalha com variáveis de ambiente, dessa forma é necessário apenas criar um arquivo utilizando o que foi disponibilizado de exemplo e colocar os dados do seu projeto.

Um exemplo de como ficaria um arquivo final seria:

    PROJECT_ID=projeto-123
    SECRET_NAME=acesso-secret

O código de autenticação foi criado em volta dessas variáveis de ambiente, então é sempre necessário checar estão corretas. Caso queira utilizar outra conta de serviço ou outro projeto basta alterá-las para o projeto novo.

---

## Testes de Conexão

Foi criado um script que faz o teste de conexão com o GCP. Basta você entrar na pasta src e executar o arquivo `test_connection.py` e caso a conexão seja efetuada você recebera a seguinte saida:

    Usando a conta autenticada via CLI para acessar o Secret Manager.
    Usando a conta de serviço para autenticar no BigQuery.
    Conexão bem-sucedida! Data de hoje: 2024-10-17
    BigQuery está autenticado com a conta de serviço.

Esse script de teste serve apenas para ter certeza de que a autenticação está funcionando sem ter que executar o script completo.