from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel

from config import PROJECT_ID


def run_gemini(project_id, model_name):
  def init_gemini(project_id: str, model_name: str):
    """
    Inicia a comunicação com Gemini API.
    
    Parâmetros:
    project_id (str): Id do projeto GCP.
    model_name (str): O nome do modelo do Vertex IA que será usado.
    """
    aiplatform.init(project=project_id)
    return GenerativeModel(model_name)


  def generate_code(model, prompt: str):
    """
    Envia o prompt para o modelo e retorna o código de resposta.
    
    Parâmetros:
    model (GenerativeModel): Modelo que será usado. 
    prompt (str): Texto do prompt que será enviado ao modelo. 
    """
    response = model.generate_content(prompt)
    return response.text


  def save_to_file(file_path: str, content: str):
    """
    Escreve a resposta obtida do modelo no arquivo 'gemini_datagen.py'.
    
    Parâmetros:
    file_path (str): Caminho do arquivo para gravar a resposta do modelo.
    content (str): O código obtido do modelo.
    """
    with open(file_path, 'a') as file:
        file.write('\n')
        file.write(content)


  project_id = PROJECT_ID
  model_name = "gemini-1.5-flash-002"
  gemini_model = init_gemini(project_id, model_name)

  prompt = """Você é um assistente especializado em gerar código Python de alta qualidade e aderente às melhores práticas. Você segue as instruções com precisão, sem fornecer explicações ou informações extras além do código solicitado.

  Exemplo generico de como deve ser as funções que você irá gerar:

  Observação 1: se algum atributo for id você deve preencher com:
  next(id_serial).

  Observação 2: se algum atributo for data ou coisa do tipo você deve preencher as datas com a seguinte formatação:
  strftime('%Y-%m-%d %H:%M:%S')

  Observação 3: Em nenhuma hipotese, use acentos em palavras, escreva sem o acento mesmo.

  Observação 4: Colunas que nao tiverem amostras de dados no exemplo,  você deve criar uma função fake correspondente para cada uma delas tomando como base o tipo e o nome da coluna.

  def criar_<nome_do_modelo>_faker():
      id_serial = itertools.count(start=0)
      return {{
          "id": next(id_serial),
          "nome_do_atributo": função_fake_correspondente,
      }}
  Dado o seguinte modelo Pydantic, crie uma função Python que instancia um objeto estritamente deste modelo e preencha os atributos com valores gerados por funções adequadas da biblioteca Faker. A função deve retornar o objeto como um dicionário. Use as funções Faker que melhor correspondem a cada tipo de dado. Retorne apenas a função Python, sem explicações adicionais, importações de bibliotecas, tratamento de exceções, apenas a implementação da função.
  para criar a função para o model abaixo, utilize do mapping que estou enviando:


  utilize exatamente este modelo Pydantic:
  #colocar nessa linha o modelo:

  abaixo esta um exemplo de como deveria ser os dados que satisfazem cada coluna desta tabela: 
  #colocar nessa linha o json com os parâmetros!!
  """


  code = generate_code(gemini_model, prompt)
  save_to_file('gemini_datagen.py', code)
