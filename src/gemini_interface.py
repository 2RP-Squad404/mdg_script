from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel

# Inicialização do cliente da API em uma função para reaproveitamento
def init_gemini(project_id: str, model_name: str):
    aiplatform.init(project=project_id)
    return GenerativeModel(model_name)

# Função para geração do código a partir de um prompt
def generate_code(model, prompt: str):
    response = model.generate_content(prompt)
    return response.text

# Função para gravar o código gerado em um arquivo
def save_to_file(file_path: str, content: str):
    with open(file_path, 'a') as file:
        file.write('\n')
        file.write(content)

# Inicialização da API
project_id = 'big-maxim-430019-g7'
model_name = "gemini-1.5-flash-002"
gemini_model = init_gemini(project_id, model_name)

# Definição do prompt
prompt = """Você é um assistente especializado em gerar código Python de alta qualidade e aderente às melhores práticas. Você segue as instruções com precisão, sem fornecer explicações ou informações extras além do código solicitado.

Exemplo generico de como deve ser as funções que você irá gerar:
Observação 1: se algum atributo for id você deve preencher com:
next(id_serial).
Observação 2: se algum atributo for data ou coisa do tipo você deve preencher as datas com a seguinte formatação:
strftime('%Y-%m-%d %H:%M:%S')

def criar_<nome_do_modelo>_faker():
    id_serial = itertools.count(start=0)
    return {
        "id": next(id_serial),
        "nome_do_atributo": função_fake_correspondente,
    }
Dado o seguinte modelo Pydantic, crie uma função Python que instancia um objeto estritamente deste modelo e preencha os atributos com valores gerados por funções adequadas da biblioteca Faker. A função deve retornar o objeto como um dicionário. Use as funções Faker que melhor correspondem a cada tipo de dado. Retorne apenas a função Python, sem explicações adicionais, importações de bibliotecas, tratamento de exceções, apenas a implementação da função.
utilize exatamente este modelo Pydantic:

"""

# Geração e salvamento do código
code = generate_code(gemini_model, prompt)
save_to_file('gemini_datagen.py', code)
