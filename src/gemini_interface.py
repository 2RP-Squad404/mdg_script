from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel
aiplatform.init(project='big-maxim-430019-g7')
model = GenerativeModel("gemini-1.5-flash-002")

prompt = f"""Dado o seguinte modelo Pydantic, crie uma função Python que instancia um objeto estritamente deste modelo e preencha os atributos com valores gerados por funções adequadas da biblioteca Faker. A função deve retornar o objeto como um dicionário. Use as funções Faker que melhor correspondem a cada tipo de dado. Retorne apenas a função Python, sem explicações adicionais, importações de bibliotecas, tratamento de exceções, apenas a implementação da função 

utilize exatamente este modelo Pydantic:
class Adesao_debito_automatico(BaseModel):
    hash_key: str
    source: str
    id: int
    dataadesao: datetime
    id_contadigital: int
    id_contacredito: int
    id_tipodebitoautomatico: int
    descricaotipodebitoautomatico: str
    responsavel: str
    datacancelamento: datetime
    responsavelcancelamento: str
    dh_relatorio: datetime
    operation: str
    operation_sequence: int
    production_date: date
"""

response = model.generate_content(prompt)

with open('gemini_datagen.py', 'a') as file:
    file.write(response.text)

print(response.text)





