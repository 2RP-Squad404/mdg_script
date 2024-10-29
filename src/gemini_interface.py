from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel

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
para criar a função para o model abaixo, utilize do mapping que estou enviando:
{
    emails: criar_Emails(),
    enderecos: criar_Enderecos(),
    telefones: criar_Telefones(),
    informacoesAdicionais: criar_Informacoesadicionais(),
    assessorias: criar_Assessorias(),
    marcadores: criar_marcadores()
}

utilize exatamente este modelo Pydantic:
class Contrato(BaseModel):
    SOURCE: str
    id: str
    idExterno: str
    numeroContrato: str
    numeroParcelas: str
    dataEmissao: str
    dataOperacao: str
    situacao: str
    tipo: str
    taxaOperacao: str
    valorDevolucao: str
    valorIof: str
    valorLiquido: str
    valorTarifa: str
    produto: 'Produto'
    valorTotal: str
    saldoAtual: str
    saldoTotal: str
    saldoContabil: str
    saldoAtraso: str
    gestao: str
    diasAtraso: str
    dataVencimento: str
    dataHoraModificacao: str
    lp: bool
    dataLp: str
    siglaAtraso: str
    cliente: 'Cliente'
    parcelas: 'Parcelas'
    production_date: date
Abaixo está um exemplo de como deveria ser os dados que satisfazem cada coluna desta tabela
{
    "contrato": {
        "SOURCE": [
            "https://pernambucanas.cobransaas.com.br/api/contratos?selector=parcelas&mode=CONTINUABLE&size=2000&situacao=ABERTO,PARCIAL,PENDENTE,CEDIDO&continuable=ODU3MjcxNTY4OTQ3Njg3NDI4",
            "https://pernambucanas.cobransaas.com.br/api/contratos?selector=parcelas&mode=CONTINUABLE&size=2000&situacao=ABERTO,PARCIAL,PENDENTE,CEDIDO&continuable=ODU3NDQ2ODU3MDc4MTU3MzE3"
        ],
        "id": [
            "857446856973299715",
            "857446848991539202",
            "857446863411556354"
        ],
        "idExterno": [
            "97512",
            "73409",
            "134129"
        ],
        "numeroContrato": [
            "9751220190817",
            "7340920190817",
            "13412920190817"
        ],
        "numeroParcelas": [
            "1"
        ],
        "dataEmissao": [
            "2018-07-13",
            "2018-10-27",
            "2018-05-23"
        ],
        "dataOperacao": [
            "2019-12-12",
            "2019-12-15",
            "2019-12-16"
        ],
        "situacao": [
            "CEDIDO",
            "LIQUIDADO"
        ],
        "tipo": [
            "FATURA"
        ],
        "taxaOperacao": [
            "0.0000000"
        ],
        "valorDevolucao": [
            "0.00"
        ],
        "valorIof": [
            "0.00"
        ],
        "valorLiquido": [],
        "valorTarifa": [
            "0.00"
        ],
        "produto": [
            {
                "nome": "STANDARD",
                "descricao": "Cart\u00e3o Mastercard Standard"
            },
            {
                "nome": "PL DIGITAL",
                "descricao": "Cart\u00e3o Private Label Pernambucanas"
            },
            {
                "nome": "ELO MAIS",
                "descricao": "CART\u00c3O BANDEIRADO ELO MAIS"
            },
            {
                "nome": "GOLD",
                "descricao": "Mastercard Gold"
            },
            {
                "nome": "ELO GRAFITE",
                "descricao": "CART\u00c3O BANDEIRADO ELO GRAFITE"
            },
            {
                "nome": "PERNAMBUCANAS ELO",
                "descricao": "Pernambucanas Elo"
            },
            {
                "nome": "PERNAMBUCANAS ELO MAIS",
                "descricao": "Pernambucanas Elo Mais"
            },
            {
                "nome": "EMPRESTIMO PESSOAL ONIDATA",
                "descricao": "EMPRESTIMO PESSOAL ONIDATA"
            },
            {
                "nome": "CARTAO TOP MASTERCARD",
                "descricao": "Cart\u00e3o Auto Pass"
            }
        ],
        "valorTotal": [
            "0.00",
            "-11.80",
            "-5.90",
            "655.09",
            "3718.67"
        ],
        "saldoAtual": [
            "0.00"
        ],
        "saldoTotal": [
            "0.00"
        ],
        "saldoContabil": [
            "0.00"
        ],
        "saldoAtraso": [
            "0.00"
        ],
        "gestao": [
            "EXTERNO",
            "INTERNO"
        ],
        "diasAtraso": [],
        "dataVencimento": [],
        "dataHoraModificacao": [
            "2019-12-13T15:15:23",
            "2019-12-13T15:15:25",
            "2019-12-13T15:15:27"
        ],
        "lp": [
            false,
            true
        ],
        "dataLp": [
            "2021-02-14",
            "2021-07-11",
            "2021-04-10"
        ],
        "siglaAtraso": [
            "Perda",
            "Creliq"
        ],
        "cliente": [
            {
                "id": "857298998029676546",
                "idExterno": "05407534916",
                "tipoPessoa": "FISICA",
                "situacao": "ATIVO",
                "nome": "POLIANA DE A GRACIANO",
                "cic": "05407534916",
                "codigo": "107378",
                "sexo": "FEMININO",
                "dataNascimento": "1986-05-27",
                "dataConta": "2011-09-06",
                "naturalidade": null,
                "estadoCivil": "CASADO",
                "rg": "00091205181",
                "rating": "HH",
                "lp": null,
                "propensaoPagamento": null,
                "historicoPagamento": null,
                "numeroDiasMaiorAtraso": null,
                "dataMaiorAtraso": null,
                "rendaTitular": "830.00",
                "rendaConjuge": "0.00",
                "outrasRendas": "0.00",
                "profissao": null,
                "categoriaProfissao": null,
                "tipoResidencia": null,
                "saldoAtraso": "0.00",
                "saldoAtual": "0.00",
                "saldoContabil": "0.00",
                "saldoProvisao": null,
                "diasAtraso": null,
                "dataHoraModificacao": "2019-08-18T17:35:51"
            }
        ],
        "parcelas": [
            [
                {
                    "id": "857446856973299715",
                    "idExterno": "1",
                    "contrato": "857446856973299715",
                    "numeroContrato": "9751220190817",
                    "numeroParcela": "1",
                    "dataVencimento": "2019-12-13",
                    "diasAtraso": null,
                    "saldoPrincipal": "0.00",
                    "saldoTotal": "0.00",
                    "saldoAtual": "0.00",
                    "saldoContabil": "0.00",
                    "valorPrincipal": "0.00",
                    "valorTotal": "0.00",
                    "valorMulta": "0.00",
                    "valorPermanencia": "0.00",
                    "valorMora": "0.00",
                    "valorOutros": "0.00",
                    "valorDesconto": "0.00",
                    "valorDespesa": null,
                    "valorBoleto": null,
                    "valorBaseTributo": null,
                    "valorPrincipalAberto": "0.00",
                    "situacao": "CEDIDO",
                    "agencia": null,
                    "banco": null,
                    "conta": null,
                    "digito": null,
                    "numeroNossoNumero": null,
                    "nossoNumero": null,
                    "digitoNossoNumero": null,
                    "numeroDocumento": null,
                    "notaFiscal": null,
                    "cobrador": null,
                    "cliente": null,
                    "acordo": false,
                    "bloqueio": false,
                    "promessa": false,
                    "tipoAcordo": null
                }
            ]
        ],
        "production_date": [
            "2024-10-24"
        ]
    }
}
"""

code = generate_code(gemini_model, prompt)
save_to_file('gemini_datagen.py', code)
