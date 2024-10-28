import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting
from py_models.pfs_risco_raw_tivea_models import Acordo
import json

with open('pfs_raw_conductor/conta.json', 'r') as f:
    dados_conta = json.load(f)

def generate():
    vertexai.init(project="integracaohomologado", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-flash-002",
        system_instruction=[textsi_1]
    )
    responses = model.generate_content(
        [text1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")

   
textsi_1 = """Você é um assistente especializado em gerar código Python de alta qualidade e aderente às melhores práticas. Seu objetivo é criar funções em Python que instanciam um objeto estritamente deste modelo e preencha os atributos com valores gerados por funções adequadas da biblioteca Faker. A função deve retornar o objeto como um dicionário. Use as funções Faker que melhor correspondem a cada tipo de dado. Além do modelo será te fornecido um exemplo de parâmetros do dado que você deve levar em consideração para a criação de funções faker.
Algumas coisas que devem ser levadas em consideração. Alguns dos parâmetros tem colunas aninhadas, nos modelos essas colunas são tratadas como classes, então na criação dos dados no faker,
as classes que conterem outras classes anunciadas dentro, devem ser instânciadas na função do faker como o exemplo abaixo:

Exemplo:

class Acordo(BaseModel):
    ...
    produto: 'Produto'
    tributo: 'Tributo'
    meioPagamento: 'Meiopagamento'

{
    ...
    produto: criar_produto_acordo(),
    tributo: criar_tributo(),
    meioPagamento: criar_Meiopagamento(),
}

Dessa forma é feito o faker de colunas aninhadas. Com base nessas informações retorne apenas a função Python, sem explicações adicionais, importações de bibliotecas, tratamento de exceções, apenas a implementação da função.

*Restrições:*
* 'id' você deve preencher com: next(id_serial).
* 'hash_key' deve ser uma string aleatória de 32 caracteres hexadecimais.
* 'dataadesao' e 'datacancelamento' devem ser datas no formato '%Y-%m-%d %H:%M:%S', sendo 'datacancelamento' posterior a 'dataadesao' em no máximo 1 ano.
* 'descricaotipodebitoautomatico' deve ser uma frase curta e descritiva, como "Pagamento mensal de assinatura Netflix".


*Exemplos:*
* 'id_tipodebitoautomatico': 1 (assinatura), 2 (fatura de cartão de crédito), 3 (boleto)
* 'responsavel': 'João Silva', 'Maria Oliveira'"""

text1 = f"""Dado o seguinte modelo Pydantic: {Acordo} e os parâmetros: {dados_conta}"""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0.1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

generate()