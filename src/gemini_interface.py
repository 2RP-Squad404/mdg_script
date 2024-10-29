from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel
from py_models.pfs_risco_tivea_models import Cartao, Cobr_cliente_atraso, Cobranca_acordo, Cobranca_assessoria, Cobranca_cliente

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
    return {{
        "id": next(id_serial),
        "nome_do_atributo": função_fake_correspondente,
    }}
Dado o seguinte modelo Pydantic, crie uma função Python que instancia um objeto estritamente deste modelo e preencha os atributos com valores gerados por funções adequadas da biblioteca Faker. A função deve retornar o objeto como um dicionário. Use as funções Faker que melhor correspondem a cada tipo de dado. Retorne apenas a função Python, sem explicações adicionais, importações de bibliotecas, tratamento de exceções, apenas a implementação da função.
para criar a função para o model abaixo, utilize do mapping que estou enviando:


utilize exatamente este modelo Pydantic:
class Cobranca_campo_customizavel(BaseModel):
    id_cliente_cobranca: int
    nom_campo: str
    val_campo: str
    dat_referencia: date
{{cobranca_cliente}}
abaixo esta um exemplo de como deveria ser os dados que satisfazem cada coluna desta tabela: 
{{
    "cobranca_campo_customizavel": {{
        "id_cliente_cobranca": [
            857208642106765314
        ],
        "nom_campo": [
            "REACORDO",
            "NOVO_LIMITE",
            "ESTRATEGIA4"
        ],
        "val_campo": [
            "n",
            "150",
            "C",
            "CCOB",
            "21/07/2020",
            "SMS",
            "LIDERANCA_21_11_22",
            "Cura",
            "Atrasada",
            "INATIVO",
            "INSS",
            "Personal_Desenrola",
            "5",
            "2002",
            "19",
            "28",
            "2004",
            "N",
            "VALIDU",
            "05/07/2020",
            "SERVICE_PREMIUM, TUDO JUSTO, SERASA, VALIDU, Portal Pefisa - PPN, DIGICOB TECNOLOGIA LTDA",
            "Obito",
            "Inconsistencia",
            "27",
            "25/07/2020",
            "Eficaz_Desenrola",
            "15/07/2020",
            "colchao",
            "7",
            "Politica 20,00",
            "Pgto Pix",
            "SIM",
            "2001",
            "SERASA",
            "11/07/2020",
            "pefin",
            "47",
            "Disponivel",
            "200",
            "Colchao",
            "EP",
            "2003",
            "15",
            "49",
            "48",
            "Gomes_Desenrola",
            "01/08/2020",
            "TUDO JUSTO, SERASA, Quite Ja, VALIDU, LIDERANCA",
            "6",
            "50"
    "cobranca_cliente": {{
        "id_cliente_cobranca": [
            890494317912358912,
            886865441852366848,
            868202056548827137
        ],
        "id_cliente_externo": [
            "20126140359",
            "59743190600",
            "46184120972"
        ],
        "tip_pessoa": [
            "FISICA"
        ],
        "tip_situacao": [
            "COBRANCA",
            "DEVEDOR",
            "ATIVO",
            "BLOQUEADO"
        ],
        "nom_cliente": [
            "IRACILDA S DOEDERLEIN",
            "ANGELI DE OLIVEIRA PINTO",
            "LEONIR CUNHA"
        ],
        "num_cpf_cnpj_cliente": [
            20126140359,
            59743190600,
            46184120972
        ],
        "nom_uf": [
            "GO",
            "MG",
            "SC"
        ],
        "cod_rating": [
            "A",
            "HH",
            "B",
            "F",
            "G",
            "D",
            "H",
            "C",
            "E"
        ],
        "des_marcador": [],
        "num_dias_maior_atraso": [],
        "dat_maior_atraso": [],
        "val_saldo_atraso": [
            125.0,
            215.0,
            96.0,
            0.0,
            17547.0
        ],
        "val_saldo_atual": [
            125.0,
            215.0,
            96.0,
            70.0
        ],
        "val_saldo_contabil": [
            0.0,
            42.0,
            7.0,
            5191.0
        ],
        "val_saldo_provisao": [],
        "qtd_dias_atraso": [
            15,
            756,
            1904,
            -1
        ],
        "val_saldo_total": [
            125.0,
            42.0,
            7.0,
            5191.0
        ],
        "val_saldo_total_atraso": [
            125.0,
            42.0,
            7.0,
            5191.0
        ],
        "dth_modificacao": [
            "2024-09-20T03:42:51+00:00",
            "2024-09-25T03:47:02+00:00",
            "2024-01-31T20:16:04+00:00",
            "2024-07-03T08:07:05+00:00"
        ],
        "num_ddd_cel": [
            11
        ],
        "num_tel_cel": [
            980504731,
            953142051,
            940317282
        ],
        "num_ddd_res": [
            62,
            34,
            47
        ],
        "num_tel_res": [
            984740711,
            32422042,
            92054311
        ],
        "num_ddd_com": [
            34,
            11,
            13
        ],
        "num_tel_com": [
            32410205,
            38510962,
            32023500
        ],
        "nom_email": [
            "iracildapci@gmail.com",
            "marianabozzo@gmail.com",
            "mariaaparecidasantos2021ryan@gmail.com"
        ],
        "dat_referencia": [
            "2024-09-30"
        ]
    }}
}}
"""



code = generate_code(gemini_model, prompt)
save_to_file('gemini_datagen_pfs_risco_tivea.py', code)
