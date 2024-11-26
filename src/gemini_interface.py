import sys

from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel

from config import PROJECT_ID, SECRET_NAME, logger
from utils import (
  get_credentials,
  load_models_and_examples,
  save_code_from_gemini,
)

credentials, credentials_dict = get_credentials(
    f'projects/{PROJECT_ID}/secrets/{SECRET_NAME}/versions/1'
)


def generate_full_prompt(dataset) -> None:

  prompt = """Você é um assistente especializado em gerar código Python de alta qualidade e aderente às melhores práticas. Você segue as instruções com precisão, sem fornecer explicações ou informações extras além do código solicitado.

  Exemplo generico de como deve ser os dicionários que você irá gerar:

  Observação 1: se algum atributo for id você deve preencher com:
  next(id_serial).

  Observação 2: se algum atributo for data ou coisa do tipo você deve preencher as datas com a seguinte formatação:
  strftime('%Y-%m-%d %H:%M:%S')

  Observação 3: Em nenhuma hipotese, use acentos em palavras, escreva sem o acento mesmo.

  Observação 4: Colunas que nao tiverem amostras de dados no exemplo,  você deve criar uma função fake correspondente para cada uma delas tomando como base o tipo e o nome da coluna.

  Observação 5: se a tabela tiver coluna que se relaciona com outra tabela passar a referência da tabela exemplo: 'id': criar_produto_acordo['id']

  datagen_<nome_do_modelo>(num_records):
    data = {'acordo': [], 'cliente': [], 'contrato': []}

      for _ in range(num_records):

          criar_produto_acordo = {
              'id': str(faker.random_number(digits=10, fix_len=True)),
              'idExterno': faker.ean8(),
              'nome': faker.company(),
              'descricao': faker.paragraph(),
          }

          criar_Emails = {
              'id': str(faker.random_number(digits=10, fix_len=True)),
              'idExterno': faker.uuid4(),
              'email': faker.email(),
              'principal': faker.boolean(),
              'ranking': faker.word(),
              'dataHoraModificacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
          }

          criar_cliente = {
              'source': faker.word(),
              'id': criar_produto_acordo['id'],
              'idExterno': faker.uuid4(),
              'tipoPessoa': faker.random_element(elements=('Física', 'Jurídica')),
              'situacao': faker.random_element(elements=('Ativo', 'Inativo')),
              'nome': faker.name(),
              'cic': faker.bothify(text='??########'),
              'emails': criar_Emails
          }
          data['cliente'].append(criar_Cliente_faker)
        }
        
  Dado o seguinte modelo Pydantic, crie uma função Python que instancia um objeto estritamente deste modelo e preencha os atributos com valores gerados por funções adequadas da biblioteca Faker. A função deve retornar o dicionário data com as tabelas. Use as funções Faker que melhor correspondem a cada tipo de dado. Retorne apenas a função Python, sem explicações adicionais, importações de bibliotecas, tratamento de exceções, apenas a implementação da função.
  para criar a função para o model abaixo, utilize do mapping que estou enviando:


  utilize exatamente este modelo Pydantic:
  #colocar nessa linha os modelos do py_models/{dataset}/*.py

  abaixo está um exemplo de como deveria ser os dados que satisfazem cada coluna desta tabela: 
  #colocar nessa linha o json com os dados de exemplo do data_sample_json/{dataset}.json!!
  """

  full_prompt = load_models_and_examples(dataset, prompt)

  if not full_prompt:
      logger.info('\033[91mErro, prompt não gerado!\033[0m')
      sys.exit(1)

  with open('src/full_prompt_output.txt', 'w', encoding='utf-8') as file:
    file.write(full_prompt)

  logger.info('\033[32mPrompt gerado com sucesso!\033[0m')  


def generate_functions_with_gemini(project_id, model_name, dataset, full_prompt):

  def init_gemini(project_id: str, credentials: str, model_name: str):
    """
    Inicia a comunicação com Gemini API.

    Parâmetros:
    project_id (str): Id do projeto GCP.
    credentials (str): Credenciais do GCP.
    model_name (str): O nome do modelo do Vertex IA que será usado.
    """
    aiplatform.init(project=project_id, credentials=credentials)
    return GenerativeModel(model_name)
  
  gemini_model = init_gemini(project_id, credentials, model_name)

  def generate_code(model, prompt: str):
    """
    Envia o prompt para o modelo e retorna o código de resposta.
    
    Parâmetros:
    model (GenerativeModel): Modelo que será usado. 
    prompt (str): Texto do prompt que será enviado ao modelo. 
    """
    response = model.generate_content(prompt)
    return response.text
    
  code = generate_code(
      gemini_model, full_prompt
  )

  gemini_code = save_code_from_gemini(dataset=dataset, content=code)

  if gemini_code:
      logger.info('\033[32mGEMINI CODE: Generated successfully.\033[0m\n')
  else:
      logger.info('\033[91mGEMINI CODE: None or could not be retrieved.\033[0m')
      sys.exit(1)