from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel
from py_models.pfs_risco_tivea_models import Cartao

from config import PROJECT_ID

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

prompt = f"""Você é um assistente especializado em gerar código Python de alta qualidade e aderente às melhores práticas. Você segue as instruções com precisão, sem fornecer explicações ou informações extras além do código solicitado.

Exemplo generico de como deve ser as funções que você irá gerar:

Observação 1: se algum atributo for id você deve preencher com:
next(id_serial).

Observação 2: se algum atributo for data ou coisa do tipo você deve preencher as datas com a seguinte formatação:
strftime('%Y-%m-%d %H:%M:%S')

Observação 3: Em nenhuma hipotese, use acentos em palavras, escreva sem o acento mesmo.

def criar_<nome_do_modelo>_faker():
    id_serial = itertools.count(start=0)
    "return {{
        "id": next(id_serial),
        "nome_do_atributo": função_fake_correspondente,
    }}
Dado o seguinte modelo Pydantic, crie uma função Python que instancia um objeto estritamente deste modelo e preencha os atributos com valores gerados por funções adequadas da biblioteca Faker. A função deve retornar o objeto como um dicionário. Use as funções Faker que melhor correspondem a cada tipo de dado. Retorne apenas a função Python, sem explicações adicionais, importações de bibliotecas, tratamento de exceções, apenas a implementação da função.
para criar a função para o model abaixo, utilize do mapping que estou enviando:


utilize exatamente este modelo Pydantic:
{{Cartao}}
abaixo esta um exemplo de como deveria ser os dados que satisfazem cada coluna desta tabela: 
{{
    "cartao": {{
        "id_cartao": [
            42709909
        ],
        "id_produto_cartao": [
            5,
            6,
            7
        ],
        "num_cartao": [
            "6505234656725505"
        ],
        "num_seq_via_cartao": [
            2,
            6,
            7
        ],
        "id_conta": [
            24861863,
            1397165,
            6562519
        ],
        "num_cpf_cliente": [
            15685253893
        ],
        "cod_tip_portador": [
            1,
            2,
            4,
            3
        ],
        "num_bin": [
            222989
        ],
        "cod_loja_emis_cartao": [
            646,
            106,
            312,
            529,
            502,
            595,
            752,
            134,
            150,
            122,
            358,
            310,
            458,
            878,
            494,
            48,
            180,
            248,
            62,
            531,
            916,
            558,
            430,
            468,
            500,
            712,
            100,
            730,
            406,
            382,
            732,
            130,
            394,
            70,
            860,
            448,
            164,
            578,
            691,
            152,
            378,
            98,
            294,
            536,
            438,
            418,
            28,
            218,
            124,
            204
        ],
        "id_cliente_so": [
            17760834
        ],
        "dth_emis_cartao": [
            "2023-10-02T12:28:37+00:00"
        ],
        "dth_embs_cartao": [
            "2023-10-03T14:10:00+00:00"
        ],
        "dth_valid_cartao": [
            "2026-10-02T15:19:00+00:00"
        ],
        "dth_desbloqueio": [
            "2023-10-02T17:23:00+00:00"
        ],
        "cod_sit_cartao": [
            1,
            2,
            3,
            6,
            33,
            10,
            68,
            4,
            61,
            37,
            11,
            15,
            54,
            17,
            55,
            200,
            30,
            5,
            32,
            21,
            34,
            8,
            50
        ],
        "des_sit_cartao": [
            "NORMAL",
            "BLOQUEADO",
            "CANCELADO",
            "CANCELADO CLIENTE",
            "CANCELADO EMBOSSING LOJA",
            "CANCELADO TARJA",
            "CADASTRO ERRO EMISSOR",
            "CANCELADO PERDA",
            "ALERTA PREVENTIVO MESA",
            "BLOQUEADO PREVENÇÃO",
            "CANCELADO EMBOSSING",
            "CANCELADO DESATIVADO",
            "FALSIFICAÇÃO NAC",
            "CANCELADO DEIXADO LOJA",
            "FALSIFICAÇÃO EXT",
            "BLOQUEIO PREVENTIVO FALCON",
            "CANCELADO CVV/CVV2 NAO GERADO",
            "CANCELADO ROUBO",
            "SUSPEITA DE FRAUDE - PREVENTIVO",
            "CANCELADO DEFINITIVO TARJA",
            "CANCELADO REEMISSÃO PERSONALIZADO",
            "CANCELADO EXTRAVIADO",
            "EXTRAVIO MALOTE CORREIOS"
        ],
        "dth_sit_cartao": [
            
            "2023-10-02T13:51:00+00:00"
        ],
        "cod_estagio_cartao": [
            6,
            1,
            16,
            17,
            22,
            18,
            0,
            4,
            19
        ],
        "des_estagio_cartao": [
            "DESBLOQUEADO SEM CODIGO",
            "CRIADO",
            "ENCAMINHADO"
        ],
        "dth_estagio_cartao": [
            "2023-10-02T16:25:00+00:00"
        ],
        "flg_embs_loja": [
            "S",
            "N"
        ],
        "flg_cartao_cancelado": [
            "N",
            "S"
        ],
        "flg_cartao_provisorio": [
            "N",
            "S"
        ],
        "flg_conta_cancelada": [
            "N",
            "S"
        ],
        "dth_ult_atu_so": [
            "2023-10-03T17:09:25+00:00"
        ],
        "num_seq_ult_alteracao": [
            2,
            1,
            4
        ],
        "dth_inclusao_reg": [
            "2023-10-04T03:56:13+00:00"
        ],
        "num_anomes_emis_cartao": [
            "2023-10-01"
        ]
    }}
}}
"""

code = generate_code(gemini_model, prompt)
save_to_file('gemini_datagen_pfs_risco_tivea.py', code)
