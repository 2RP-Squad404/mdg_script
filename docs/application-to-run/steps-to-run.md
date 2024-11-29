<div style="text-align: justify;">

# **Passos para gerar os dados mockados**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Explicação do Diretório
Dentro de "src" há as pastas e arquivos que estão organizadas de acordo com a aplicação.  
## Pastas
* **"bq_schemas"** contém os datasets que estão divididos em pastas e dentro delas as respectivas tabelas.
* **"py_models"** contém as classes que representam os dados separadas por datasets.
* **"py_schemas"** contém os schemas do tipo schemafield para a criação das tabelas no Big Query separadas por datasets.
* **"datagen"** contem os arquivos que recebem as funções criadas pelo gemini para a criação dos dados mockados.

## Arquivos Python
* **"main.py"** é o arquivo principal da aplicação nele é onde todas as funções são chamadas através de um **CLI**.
* **"utils.py"** é o arquivo das funções principais.
* **"test_connection.py"** é o  arquivo de teste da conexão com o Big Query.
* **"generate_models.py"** é  o arquivo que gera as classes apartir dos arquivos do bq_schemas.
* **"gemini_interface"** é o arquivo que contém o funcionamento do Gemini

## Passo 1: Dependências
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Instale as dependencias necessárias para que a aplicação ocorra corretamente antes de executar qualquer arquivo. Após a instalação das dependencias, terá que criar um arquivo .env na raiz do projeto, onde  irá inserir as credenciais do seu projeto no Google Cloud, seguindo o exemplo no arquivo `.env.example`, com o `PROJECT_ID e o SECRET_NAME`


## Passo 2: Autenticação com o Big Query
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Precisa autenticar-se ao Big Query. Para isso escreva no terminal: 

```
gcloud auth application-default login
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Execute, onde abrirá o navegador para que possa logar na sua conta do GCP.

## Passo 3: Schemas em JSON
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Precisará de arquivos JSON com os schemas de origem das tabelas que deseja-se criar no Big Query. Pois o código principal usa como base a pasta local `bq_schemas` como repositório do Big Query.

## Passo 4: Schemas JSON para Schemas Pydantic e SchemasFields
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Já tendo os schemas extraidos das pastas no `bq_schemas` execute o main usando o `poetry` ou o `python` que será criado os modelos em pydantic e big query schemas. 

## Passo 5: Subir as tabelas
 > ⚠️ **ATENÇÃO** Em caso de particionamento das tabelas, a função `create_tables()` contém uma classificação de particionamento por MONTHY e DAY. Esse contexto de particionamento o código procura a última coluna de cada tabela e analisa se precisa do particionamento ou não baseado no nome que está destacado no código. Se tiver mais algum parametro precisa ser adicionado direto no código.  

<Img src="../Images/particioning.png">

* **Tabela particionada:** Execute o main e selecione a opção `1 - Criar tabelas por dataset no BigQuery` que serão usos os big query schemas para criar o dataset caso não exista ainda e as tabelas particionadas.
* **Tabela não particionada:** Precisa adicionar o nome da tabela no array "excluded_partition_tables".

## Passo 6: Atualizações das tabelas
Caso precise atualizar o tipo da tabela ou adicionar uma descrição à coluna precisa modificar a coluna que queira dentro da pasta `py_models`.


Ex: Adição de descrição. 

Antes
```
bigquery.SchemaField('id_conta', 'INTEGER', 'NULLABLE'),
```
    
Depois
```
bigquery.SchemaField('id_conta', 'INTEGER', 'NULLABLE', description='ID único da conta do cartão.'),
```
 

## Passo 7: Geração de dados mockados
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Esse é o fluxo de criação dos dados mockados partindo do ponto que você ja criou as tabelas ou elas ja existam.

* **Prompt do Gemini:** A opção `2 - Gerar o prompt completo para o Gemini` lista os datasets fazendo uma comparação dos que estão na pasta `bq_schemas` e os que estão no big query. Após selecionar um deles sera gerado um arquivo chamado `full_prompt_output.txt` que contém toda a formatação do prompt que será enviado para o gemini para ele gerar as funções faker, assim é possível fazer alterações se quiser.

* **Funções Faker:** A opção `3 - Gerar funções Faker com Gemini` utiliza o `full_prompt_output.txt` como base para gerar a funções faker e o arquivo `select_dataset.json` que contém o dataset escolhido anteriormente salvo para saber em qual arquivo datagen salvar as funções faker.

* **Geração dos Dados:** A opção `4 - Gerar dados em JSONL` utiliza as funções do arquivo com o nome do dataset que está localizado na pasta `datagen` para gerar os dados mockados e os salva na pasta `mock_data` em formato JSON.

* **Envio dos Dados** A opção `5 - Enviar JSONL para o BigQuery` entra na pasta `mock_data` e com base nas pastas com nome dos datasets, fazem novamente a validação dos que existem no `mock_data` e os que existem no big query e sobe os dados divididos por tabela em JSON no big query.


</div>