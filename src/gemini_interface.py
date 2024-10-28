from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel

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

project_id = 'big-maxim-430019-g7'
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
class Acordo(BaseModel):
    source: str
    id: str
    cliente: str
    cobrador: str
    tipo: str
    numeroAcordo: str
    numeroParcelas: str
    dataOperacao: str
    dataEmissao: str
    dataProcessamento: str
    dataHoraInclusao: str
    dataHoraModificacao: str
    dataVencimento: str
    situacao: str
    taxaOperacao: str
    valorPagoTributo: str
    valorPrincipal: str
    valorJuros: str
    valorTarifa: str
    valorTributo: str
    valorAdicionado: str
    valorTotal: str
    saldoPrincipal: str
    saldoTotal: str
    saldoAtual: str
    diasAtraso: str
    motivoCancelamento: str
    negociacao: 'Negociacao'
    criterioTributo: str
    produto: 'Produto'
    tributo: 'Tributo'
    meioPagamento: 'Meiopagamento'
    usuario: 'Usuario'
    assessoria: 'Assessoria'
    parcelas: 'Parcelas'
    pagamentos: 'Pagamentos'
    origens: 'Origens'
    pendencias: 'Pendencias'
    production_date: date
Abaixo está um exemplo de como deveria ser os dados que satisfazem cada coluna desta tabela
{
    "acordo": {
        "source": [
            "https://pernambucanas.cobransaas.com.br/api/acordos?selector=parcelas,pagamentos,origens,pendencias&mode=CONTINUABLE&size=2000&continuable=MTE1MzA3NTc5NzkxNzk4MjcyMA=="
        ],
        "id": [
            "1153328453601218560"
        ],
        "cliente": [
            "44072244791"
        ],
        "cobrador": [
            "843886440258154496"
        ],
        "tipo": [
            "ACORDO",
            "RENEGOCIACAO"
        ],
        "numeroAcordo": [
            "7350376",
            "2260101",
            "7370553"
        ],
        "numeroParcelas": [
            "1",
            "7",
            "10"
        ],
        "dataEmissao": [
            "2021-11-22"
        ],
        "dataProcessamento": [
            "2021-11-26"
        ],
        "dataHoraInclusao": [
            "2021-11-18T11:20:51"
        ],
        "dataHoraModificacao": [
            "2021-11-26T12:25:30"
        ],
        "dataVencimento": [
            "2024-10-28"
        ],
        "situacao": [
            "NAO_CUMPRIDO",
            "CANCELADO",
            "LIQUIDADO",
            "PENDENTE",
            "RENEGOCIADO"
        ],
        "taxaOperacao": [
            "11.9900000"
        ],
        "valorPagoTributo": [
            "0.00"
        ],
        "valorPrincipal": [
            "8109.06"
        ],
        "valorJuros": [
            "6011.47"
        ],
        "valorTarifa": [
            "0.00"
        ],
        "valorTributo": [
            "58.83"
        ],
        "valorAdicionado": [
            "0.00"
        ],
        "valorTotal": [
            "8109.06"
        ],
        "saldoPrincipal": [
            "826.51"
        ],
        "saldoTotal": [
            "907.16"
        ],
        "saldoAtual": [
            "907.92"
        ],
        "diasAtraso": [
            "3",
            "1",
            "-4",
            "-1",
            "2",
            "-6",
            "0",
            "5"
        ],
        "motivoCancelamento": [
            "{\"id\":\"1075534269541007360\",\"nome\":\"Ajuste Pagto A vista\",\"situacao\":\"ATIVO\"}",
            "{\"id\":\"1068491285330968576\",\"nome\":\"Ajuste Credito - Encerramento Indevido CDT\",\"situacao\":\"ATIVO\"}"
        ],
        "negociacao": [
            {
                "id": "1142924267613077504",
                "nome": "5% Entrada com Juros 1,99_V5",
                "descricao": "Pol\u00edtica padr\u00e3o de negocia\u00e7\u00e3o de d\u00edvida, modalidade de desconto para todos os canais",
                "situacao": "INATIVO",
                "tipo": "ACORDO",
                "gestao": "EXTERNO",
                "cor": "#2412eb",
                "icone": "money",
                "tipoDesconto": "PARCELAMENTO",
                "modalidade": {
                    "id": "832641169862905856",
                    "nome": "Pol\u00edtica Padr\u00e3o",
                    "tipo": "ACORDO",
                    "situacao": "ATIVO",
                    "gestao": "EXTERNO",
                    "cor": "#2412eb",
                    "valorDistorcao": "0.00",
                    "percentualDistorcao": "0.00",
                    "atrasoMaximo": "31",
                    "atrasoEntrada": "4",
                    "acaoOrigemLiquidaca": "LIQUIDAR"
                }
            },
            {
                "id": "934852167867617280",
                "nome": "A\u00e7\u00e3o Covid_19- Entrada 30% Sem Juros",
                "descricao": "Pol\u00edtica padr\u00e3o de negocia\u00e7\u00e3o de d\u00edvida, modalidade de desconto para todos os canais",
                "situacao": "INATIVO",
                "tipo": "ACORDO",
                "gestao": "EXTERNO",
                "cor": "#2412eb",
                "icone": "money",
                "tipoDesconto": "PARCELAMENTO",
                "modalidade": {
                    "id": "832641169862905856",
                    "nome": "Pol\u00edtica Padr\u00e3o",
                    "tipo": "ACORDO",
                    "situacao": "ATIVO",
                    "gestao": "EXTERNO",
                    "cor": "#2412eb",
                    "valorDistorcao": "0.00",
                    "percentualDistorcao": "0.00",
                    "atrasoMaximo": "31",
                    "atrasoEntrada": "4",
                    "acaoOrigemLiquidaca": "LIQUIDAR"
                }
            },
            {
                "id": "1142923251761037312",
                "nome": "30% Entrada sem juros_V9",
                "descricao": "Pol\u00edtica padr\u00e3o de negocia\u00e7\u00e3o de d\u00edvida, modalidade de desconto para todos os canais",
                "situacao": "INATIVO",
                "tipo": "ACORDO",
                "gestao": "EXTERNO",
                "cor": "#2412eb",
                "icone": "money",
                "tipoDesconto": "PARCELAMENTO",
                "modalidade": {
                    "id": "832641169862905856",
                    "nome": "Pol\u00edtica Padr\u00e3o",
                    "tipo": "ACORDO",
                    "situacao": "ATIVO",
                    "gestao": "EXTERNO",
                    "cor": "#2412eb",
                    "valorDistorcao": "0.00",
                    "percentualDistorcao": "0.00",
                    "atrasoMaximo": "31",
                    "atrasoEntrada": "4",
                    "acaoOrigemLiquidaca": "LIQUIDAR"
                }
            }
        ],
        "criterioTributo": [
            "FINANCIA"
        ],
        "produto": [
            {
                "id": "1041022147775959040",
                "idExterno": "PERNAMBUCANAS ELO",
                "nome": "PERNAMBUCANAS ELO",
                "descricao": "Pernambucanas Elo"
            },
            {
                "id": "832289491826458624",
                "idExterno": "ELO GRAFITE",
                "nome": "ELO GRAFITE",
                "descricao": "CART\u00c3O BANDEIRADO ELO GRAFITE"
            },
            {
                "id": "1041022394388459520",
                "idExterno": "PERNAMBUCANAS ELO MAIS",
                "nome": "PERNAMBUCANAS ELO MAIS",
                "descricao": "Pernambucanas Elo Mais"
            },
            {
                "id": "832302081386430464",
                "idExterno": "GOLD",
                "nome": "GOLD",
                "descricao": "Mastercard Gold"
            }
        ],
        "tributo": [
            {
                "id": "833449491750080512",
                "nome": "IOF",
                "percentual": "0.0082000",
                "percentualFixo": "0.3800000",
                "percentualMaximo": "3.0000000",
                "arredondamento": "BAIXO",
                "dataCalculo": "VENCIMENTO"
            }
        ],
        "meioPagamento": [
            {
                "id": "846749035367653376",
                "tipo": "BOLETO",
                "nome": "Boleto Pefisa",
                "cobrador": {
                    "id": "843886440258154496",
                    "nome": "PEFISA",
                    "banco": "174"
                }
            },
            {
                "id": "832604700830035968",
                "tipo": "DINHEIRO",
                "nome": "PDV Taxa 1,99",
                "cobrador": null
            },
            {
                "id": "1213097518578049024",
                "tipo": "BOLETO_PIX",
                "nome": "Boleto e PIX",
                "cobrador": {
                    "id": "843886440258154496",
                    "nome": "PEFISA",
                    "banco": "174"
                }
            },
            {
                "id": "1315003911416909824",
                "tipo": "DINHEIRO",
                "nome": "D\u00e9bito em Conta",
                "cobrador": null
            }
        ],
        "usuario": [
            {
                "id": "870673617655635968",
                "nome": "GRB"
            },
            {
                "id": "896120615670083584",
                "nome": "Quite J\u00e1"
            },
            {
                "id": "832297581166673920",
                "nome": "Eficaz"
            }
        ],
        "assessoria": [
            {
                "id": "866048845195128832",
                "nome": "GRB"
            },
            {
                "id": "885866845264637952",
                "nome": "Quite Ja"
            },
            {
                "id": "832294019271442432",
                "nome": "EFICAZ_MG"
            }
        ],
        "parcelas": [
            [
                {
                    "id": "1541549287534628864",
                    "acordo": "1541549287534628864",
                    "numeroParcela": "0",
                    "dataVencimento": "2024-10-21",
                    "situacao": "ABERTO",
                    "nossoNumero": "5023084862",
                    "valorPrincipal": "50.00",
                    "valorJuros": "0.00",
                    "valorTarifa": "0.00",
                    "valorAdicionado": "0.00",
                    "valorTotal": "50.00",
                    "valorTributo": "0.19",
                    "valorBaseTributo": "50.00",
                    "valorPermanencia": "0.00",
                    "valorMora": "0.00",
                    "valorMulta": "0.00",
                    "saldoPrincipal": "50.00",
                    "saldoTotal": "50.00",
                    "saldoAtual": "50.00",
                    "registrado": true
                },
                {
                    "id": "1541549287534628865",
                    "acordo": "1541549287534628864",
                    "numeroParcela": "1",
                    "dataVencimento": "2024-11-21",
                    "situacao": "ABERTO",
                    "nossoNumero": "5023120531",
                    "valorPrincipal": "43.14",
                    "valorJuros": "0.00",
                    "valorTarifa": "0.00",
                    "valorAdicionado": "0.00",
                    "valorTotal": "43.14",
                    "valorTributo": "0.26",
                    "valorBaseTributo": "43.14",
                    "valorPermanencia": "0.00",
                    "valorMora": "0.00",
                    "valorMulta": "0.00",
                    "saldoPrincipal": "43.14",
                    "saldoTotal": "43.14",
                    "saldoAtual": "43.14",
                    "registrado": true
                }
            ]
        ],
        "pagamentos": [
            [],
            [
                {
                    "id": "1155228398805667840",
                    "dataProcessamento": "2021-11-17",
                    "dataLiquidacao": "2021-11-17",
                    "dataCredito": null,
                    "dataCnab": null,
                    "dataOperacao": "2021-11-17",
                    "dataHoraInclusao": "2021-11-17T20:40:55",
                    "formaLiquidacao": "DINHEIRO",
                    "valorRecebido": "44.25",
                    "valorDesconto": "0.00",
                    "valorEncargos": "0.00",
                    "valorDistorcao": "0.00",
                    "valorSobra": "0.00",
                    "situacao": "ATIVO",
                    "integracao": "CONCLUIDO",
                    "agrupador": null,
                    "abatimentos": [
                        {
                            "id": "1155228398843416576",
                            "origem": "1155152780013363200",
                            "valorPrincipal": "44.24",
                            "valorTotal": "44.24",
                            "valorPermanencia": "0.01",
                            "valorMora": "0.00",
                            "valorMulta": "0.00",
                            "valorOutros": "0.00",
                            "valorDesconto": "0.00",
                            "valorJuros": "0.00",
                            "valorTarifa": "0.00",
                            "valorTributo": "0.00",
                            "valorAdicionado": "0.00",
                            "valorAtual": "44.25",
                            "percentual": "100.000000000000",
                            "tipo": "TOTAL",
                            "integracao": "CONCLUIDO",
                            "mensagemIntegracao": null,
                            "dataHoraIntegracao": "2021-11-17T20:40:55"
                        }
                    ],
                    "liquidacoes": [
                        {
                            "id": "1155228398809862144",
                            "parcela": "1155152780013363200",
                            "valorPrincipal": "44.25",
                            "valorTotal": "44.25",
                            "valorJuros": "0.00",
                            "valorEncargos": "0.00",
                            "valorDesconto": "0.00",
                            "valorDistorcao": "0.00",
                            "diasAtraso": "0",
                            "numeroParcela": "0",
                            "tipo": "TOTAL"
                        }
                    ]
                }
            ]
        ],
        "origens": [
            [
                {
                    "id": "1153328453601218560",
                    "valorContabil": "672.17",
                    "descontoContabil": "74.68",
                    "saldoContabil": "672.17",
                    "contrato": "19554331",
                    "contratoId": "1122419554769760258",
                    "numeroContrato": "90019554331",
                    "parcela": "1",
                    "parcelaId": "1122419554769760259",
                    "numeroParcela": "1",
                    "diasAtraso": "79",
                    "ordem": "1",
                    "dataVencimento": "2021-08-25",
                    "nossoNumero": null,
                    "notaFiscal": null,
                    "situacao": "CANCELADO",
                    "valorPrincipal": "672.17",
                    "valorTotal": "672.17",
                    "valorPermanencia": "0.00",
                    "valorMora": "0.00",
                    "valorMulta": "0.00",
                    "valorOutros": "0.00",
                    "valorDesconto": "0.00",
                    "valorJuros": "0.00",
                    "valorTarifa": "0.00",
                    "valorAdicionado": "0.00",
                    "valorAtual": "672.17",
                    "saldoPrincipal": "672.17",
                    "saldoTotal": "672.17",
                    "saldoPermanencia": "0.00",
                    "saldoMora": "0.00",
                    "saldoMulta": "0.00",
                    "saldoOutros": "0.00",
                    "saldoDesconto": "0.00",
                    "saldoJuros": "0.00",
                    "saldoTarifa": "0.00",
                    "saldoAdicionado": "0.00",
                    "saldoAtual": "672.17",
                    "descontoPrincipal": "74.68",
                    "descontoJuros": "0.00",
                    "descontoMora": "0.00",
                    "descontoMulta": "0.00",
                    "descontoOutros": "0.00",
                    "descontoPermanencia": "70.29",
                    "descontoTotal": "74.68"
                }
            ],
            [
                {
                    "id": "949420872945418240",
                    "valorContabil": null,
                    "descontoContabil": null,
                    "saldoContabil": null,
                    "contrato": "5306308",
                    "contratoId": "885420290402562052",
                    "numeroContrato": "530630820191103",
                    "parcela": "1",
                    "parcelaId": "885420290402562052",
                    "numeroParcela": "1",
                    "diasAtraso": "179",
                    "ordem": "1",
                    "dataVencimento": "2019-11-01",
                    "nossoNumero": null,
                    "notaFiscal": null,
                    "situacao": "CANCELADO",
                    "valorPrincipal": "2475.20",
                    "valorTotal": "2475.20",
                    "valorPermanencia": "0.00",
                    "valorMora": "0.00",
                    "valorMulta": "0.00",
                    "valorOutros": "0.00",
                    "valorDesconto": "0.00",
                    "valorJuros": "0.00",
                    "valorTarifa": "0.00",
                    "valorAdicionado": "0.00",
                    "valorAtual": "2475.20",
                    "saldoPrincipal": "2475.20",
                    "saldoTotal": "2475.20",
                    "saldoPermanencia": "0.00",
                    "saldoMora": "0.00",
                    "saldoMulta": "0.00",
                    "saldoOutros": "0.00",
                    "saldoDesconto": "0.00",
                    "saldoJuros": "0.00",
                    "saldoTarifa": "0.00",
                    "saldoAdicionado": "0.00",
                    "saldoAtual": "2475.20",
                    "descontoPrincipal": "2475.19",
                    "descontoJuros": "0.00",
                    "descontoMora": "0.00",
                    "descontoMulta": "0.00",
                    "descontoOutros": "0.00",
                    "descontoPermanencia": "3077.64",
                    "descontoTotal": "2475.19"
                }
            ]
        ],
        "pendencias": [
            []
        ],
        "production_date": [
            "2024-10-24"
        ]
    }
}
"""

code = generate_code(gemini_model, prompt)
save_to_file('gemini_datagen.py', code)
