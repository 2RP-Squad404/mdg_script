from faker import Faker
import itertools
from datetime import date, datetime
import random 

faker = Faker('pt_BR')
id_serial = itertools.count(start=0)

#dados que o faker não conseguiu gerar 

num_pagamentos = 5
num_origens = 3
num_pendencias = 2

pagamentos = [
    {
        "data": faker.date(),
        "valor": faker.pydecimal(min_value=10, max_value=1000, positive=True),
        "forma_pagamento": faker.credit_card_provider()
    }
    for _ in range(num_pagamentos)
]

origens = [
    {
        "sistema": faker.company(),
        "data_importacao": faker.date_this_year().strftime('%Y-%m-%d %H:%M:%S')
    }
    for _ in range(num_origens)
]

pendencias = [
    {
        "descricao": faker.sentence(),
        "data_limite": faker.date_time_between(start_date='+1w').strftime('%Y-%m-%d %H:%M:%S')
    }
    for _ in range(num_pendencias)
]




# As funções abaixo são responsáveis por criar dados mock para o dataset pfs_risco_raw_tivea
# observe que as funções correspondem a tabelas presentes no dataset.
    
def criar_produto_acordo():
    return {
        "id": next(id_serial),
        "idExterno": faker.ean8(),
        "nome": faker.company(),
        "descricao": faker.paragraph()
    }

def criar_negociacao():
    return {
        "id": next(id_serial),
        "nome": faker.company(),
        "descricao": faker.paragraph(),
        "situacao": faker.word(),
        "tipo": faker.word(),
        "gestao": faker.word(),
        "cor": faker.hex_color(),
        "icone": faker.word(),
        "tipoDesconto": faker.word(),
        "modalidade": {"chave": faker.word(), "valor": faker.random_number()}
    }


def criar_tributo():
    return {
        "id": str(next(id_serial)),
        "nome": faker.word(),
        "percentual": faker.numerify("%0.2f"),
        "percentualFixo": faker.numerify("%0.2f"),
        "percentualMaximo": faker.numerify("%0.2f"),
        "arredondamento": faker.random_element(elements=["0", "1"]),
        "dataCalculo": faker.date_time().strftime('%Y-%m-%d %H:%M:%S')
    }

def criar_Meiopagamento():
    return {
        "id": str(next(id_serial)),
        "tipo": faker.credit_card_provider(),
        "nome": faker.credit_card_number(),
        "cobrador": {"nome": faker.name(), "cpf": faker.cpf()}
    }

def criar_usuario():
    return {
        "id": str(next(id_serial)),
        "nome": faker.name()
    }

def criar_Assessoria():
    return {
        "id": str(next(id_serial)),
        "nome": faker.company()
    }


def criar_Parcelas():
    return {
        "id": str(next(id_serial)),
        "acordo": faker.word(),
        "numeroParcela": faker.word(),
        "dataVencimento": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "situacao": faker.word(),
        "nossoNumero": faker.word(),
        "valorPrincipal": faker.pydecimal(left_digits=5, right_digits=2),
        "valorJuros": faker.pydecimal(left_digits=5, right_digits=2),
        "valorTarifa": faker.pydecimal(left_digits=5, right_digits=2),
        "valorAdicionado": faker.pydecimal(left_digits=5, right_digits=2),
        "valorTotal": faker.pydecimal(left_digits=5, right_digits=2),
        "valorTributo": faker.pydecimal(left_digits=5, right_digits=2),
        "valorBaseTributo": faker.pydecimal(left_digits=5, right_digits=2),
        "valorPermanencia": faker.pydecimal(left_digits=5, right_digits=2),
        "valorMora": faker.pydecimal(left_digits=5, right_digits=2),
        "valorMulta": faker.pydecimal(left_digits=5, right_digits=2),
        "saldoPrincipal": faker.pydecimal(left_digits=5, right_digits=2),
        "saldoTotal": faker.pydecimal(left_digits=5, right_digits=2),
        "saldoAtual": faker.pydecimal(left_digits=5, right_digits=2),
        "registrado": faker.boolean()
    }

def criar_Pagamentos():
    return {
        "id": str(next(id_serial)),
        "dataProcessamento": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataLiquidacao": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataCredito": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataCnab": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataOperacao": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataHoraInclusao": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "formaLiquidacao": faker.word(),
        "valorRecebido": faker.numerify('R$ ###,##'),
        "valorDesconto": faker.numerify('R$ ###,##'),
        "valorEncargos": faker.numerify('R$ ###,##'),
        "valorDistorcao": faker.numerify('R$ ###,##'),
        "valorSobra": faker.numerify('R$ ###,##'),
        "situacao": faker.word(),
        "integracao": faker.word(),
        "agrupador": {},
        "abatimentos": {},
        "liquidacoes": {}
    }

def criar_origens():
    return {
        "id": next(id_serial),
        "valorContabil": faker.pystr(),
        "descontoContabil": faker.pystr(),
        "saldoContabil": faker.pystr(),
        "contrato": faker.pystr(),
        "contratoId": faker.pystr(),
        "numeroContrato": faker.pystr(),
        "parcela": faker.pystr(),
        "parcelaId": faker.pystr(),
        "numeroParcela": faker.pystr(),
        "diasAtraso": faker.pystr(),
        "ordem": faker.pystr(),
        "dataVencimento": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "nossoNumero": faker.pystr(),
        "notaFiscal": faker.pystr(),
        "situacao": faker.pystr(),
        "valorPrincipal": faker.pystr(),
        "valorTotal": faker.pystr(),
        "valorPermanencia": faker.pystr(),
        "valorMora": faker.pystr(),
        "valorMulta": faker.pystr(),
        "valorOutros": faker.pystr(),
        "valorDesconto": faker.pystr(),
        "valorJuros": faker.pystr(),
        "valorTarifa": faker.pystr(),
        "valorAdicionado": faker.pystr(),
        "valorAtual": faker.pystr(),
        "saldoPrincipal": faker.pystr(),
        "saldoTotal": faker.pystr(),
        "saldoPermanencia": faker.pystr(),
        "saldoMora": faker.pystr(),
        "saldoMulta": faker.pystr(),
        "saldoOutros": faker.pystr(),
        "saldoDesconto": faker.pystr(),
        "saldoJuros": faker.pystr(),
        "saldoTarifa": faker.pystr(),
        "saldoAdicionado": faker.pystr(),
        "saldoAtual": faker.pystr(),
        "descontoPrincipal": faker.pystr(),
        "descontoJuros": faker.pystr(),
        "descontoMora": faker.pystr(),
        "descontoMulta": faker.pystr(),
        "descontoOutros": faker.pystr(),
        "descontoPermanencia": faker.pystr(),
        "descontoTotal": faker.pystr(),
    }
    

def criar_pendencias():
    return {
        "id": str(next(id_serial)),
        "dataGeracao": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataProcessamento": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataParecer": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "situacao": faker.word(),
        "tipo": faker.word(),
        "observacao": faker.paragraph(),
        "pareceres": {"a": faker.word()}
    }

def criar_Emails():
    return {
        "id": str(id_serial),
        "idExterno": faker.uuid4(),
        "email": faker.email(),
        "principal": faker.boolean(),
        "ranking": faker.word(),
        "dataHoraModificacao": faker.date_time().strftime('%Y-%m-%d %H:%M:%S')
    }


def criar_Enderecos():
    return {
        "id": str(id_serial),
        "idExterno": faker.uuid4(),
        "cep": faker.postcode(),
        "codigoDne": faker.ean8(),
        "complemento": faker.random_digit(),
        "logradouro": faker.street_name(),
        "bairro": faker.street_address(),
        "cidade": faker.city(),
        "numero": faker.building_number(),
        "tipo": faker.random_element(elements=('Residencial', 'Comercial')),
        "tipoLogradouro": faker.random_element(elements=('Rua', 'Avenida', 'Praça')),
        "uf": faker.state_abbr(),
        "principal": faker.boolean(),
        "ranking": str(faker.random_int(min=1, max=10)),
        "dataHoraModificacao": faker.date_time().strftime('%Y-%m-%d %H:%M:%S')
    }

 
def criar_Telefones():
    return {
        "id": str(id_serial),
        "idExterno": faker.uuid4(),
        "ddd": faker.random_number(digits=2),
        "telefone": faker.numerify('#########'),
        "ramal": faker.random_number(digits=4),
        "tipo": faker.word(),
        "observacao": faker.sentence(),
        "principal": faker.boolean(),
        "ranking": str(faker.random_int(min=1, max=10)),
        "dataHoraModificacao": faker.date_time().strftime('%Y-%m-%d %H:%M:%S')
    }


def criar_Informacoesadicionais():
    return {
        "nome": faker.word(),
        "linha": faker.word(),
        "coluna": faker.word(),
        "valor": faker.word(),
        "tipo": faker.word(),
        "tamanho": faker.word(),
    }

def criar_Assessorias():
    return {
        "id": str(id_serial),
        "nome": faker.company(),
        "situacao": faker.random_element(elements=('Ativo', 'Inativo')),
        "cic": faker.bothify(text='CIC-??-#######'),
        "cep": faker.postcode(),
        "complemento": faker.random_digit(),
        "logradouro": faker.street_address(),
        "bairro": faker.street_name(),
        "cidade": faker.city(),
        "numero": faker.building_number(),
        "uf": faker.state_abbr(),
        "alterarInformacoesCadastrais": faker.boolean()
    }

def criar_marcadores():
    return {
        "id": str(id_serial),
        "nome": faker .word(),
        "cor": faker .color_name()
    }


def criar_ProdutoContrato():
    return {
        "id": next(id_serial),
        "nome": faker.word(),
        "descricao": faker.paragraph(),
    }
 
 
def criar_cliente():
    return {
        "id": str(next(id_serial)),
        "idExterno": faker.uuid4(),
        "tipoPessoa": faker.random_element(elements=("Física", "Jurídica")),
        "situacao": faker.random_element(elements=("Ativo", "Inativo")),
        "nome": faker.name(),
        "cic": faker.bothify(text="??########"),
        "codigo": faker.ean13(),
        "sexo": faker.random_element(elements=("Masculino", "Feminino", "Outro")),
        "dataNascimento": faker.date_of_birth(minimum_age=18, maximum_age=100).strftime('%Y-%m-%d %H:%M:%S'),
        "dataConta": faker.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "naturalidade": faker.city(),
        "estadoCivil": faker.random_element(elements=("Solteiro", "Casado", "Divorciado", "Viúvo")),
        "rg": faker.bothify(text="??.???.???-?",),
        "rating": faker.random_int(min=1, max=5),
        "lp": faker.random_element(elements=("A", "B", "C")),
        "propensaoPagamento": faker.random_int(min=1, max=10),
        "historicoPagamento": faker.paragraph(nb_sentences=3),
        "numeroDiasMaiorAtraso": faker.random_int(min=0, max=365),
        "dataMaiorAtraso": faker.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "rendaTitular": faker.numerify(text="R$#######.##"),
        "rendaConjuge": faker.numerify(text="R$#######.##"),
        "outrasRendas": faker.numerify(text="R$#######.##"),
        "profissao": faker.job(),
        "categoriaProfissao": faker.random_element(elements=("A", "B", "C")),
        "tipoResidencia": faker.random_element(elements=("Casa", "Apartamento", "Outros")),
        "saldoAtraso": faker.numerify(text="R$#######.##"),
        "saldoAtual": faker.numerify(text="R$#######.##"),
        "saldoContabil": faker.numerify(text="R$#######.##"),
        "saldoProvisao": faker.numerify(text="R$#######.##"),
        "diasAtraso": faker.random_int(min=0, max=365),
        "dataHoraModificacao": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S')
        
    }
 
def criar_parcelas():
    return {
        "id": str(next(id_serial)),
        "idExterno": faker.uuid4(),
        "contrato": faker.ean13(),
        "numeroContrato": faker.random_number(digits=8),
        "numeroParcela": faker.random_number(digits=2),
        "dataVencimento": faker.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "diasAtraso": faker.random_number(digits=2),
        "saldoPrincipal": faker.pydecimal(left_digits=10, right_digits=2),
        "saldoTotal": faker.pydecimal(left_digits=10, right_digits=2),
        "saldoAtual": faker.pydecimal(left_digits=10, right_digits=2),
        "saldoContabil": faker.pydecimal(left_digits=10, right_digits=2),
        "valorPrincipal": faker.pydecimal(left_digits=10, right_digits=2),
        "valorTotal": faker.pydecimal(left_digits=10, right_digits=2),
        "valorMulta": faker.pydecimal(left_digits=10, right_digits=2),
        "valorPermanencia": faker.pydecimal(left_digits=10, right_digits=2),
        "valorMora": faker.pydecimal(left_digits=10, right_digits=2),
        "valorOutros": faker.pydecimal(left_digits=10, right_digits=2),
        "valorDesconto": faker.pydecimal(left_digits=10, right_digits=2),
        "valorDespesa": faker.pydecimal(left_digits=10, right_digits=2),
        "valorBoleto": faker.pydecimal(left_digits=10, right_digits=2),
        "valorBaseTributo": faker.pydecimal(left_digits=10, right_digits=2),
        "valorPrincipalAberto": faker.pydecimal(left_digits=10, right_digits=2),
        "situacao": faker.word(),
        "agencia": faker.random_number(digits=4),
        "banco": faker.bank_country(),
        "conta": faker.iban(),
        "digito": faker.random_digit(),
        "numeroNossoNumero": faker.random_number(digits=10),
        "nossoNumero": faker.random_number(digits=10),
        "digitoNossoNumero": faker.random_digit(),
        "numeroDocumento": faker.ssn(),
        "notaFiscal": faker.ean13(),
        "cobrador": faker.name(),
        "cliente": faker.name(),
        "acordo": faker.boolean(),
        "bloqueio": faker.boolean(),
        "promessa": faker.boolean(),
        "tipoAcordo": faker.word()
    }

def criar_Cliente_faker():
    produto_acordo = criar_produto_acordo()
    return {
        "source": faker.word(),
        "id": produto_acordo["id"],
        "idExterno": faker.uuid4(),
        "tipoPessoa": faker.random_element(elements=("Física", "Jurídica")),
        "situacao": faker.random_element(elements=("Ativo", "Inativo")),
        "nome": faker.name(),
        "cic": faker.bothify(text="??########"),
        "codigo": faker.ean13(),
        "sexo": faker.random_element(elements=("Masculino", "Feminino", "Outro")),
        "dataNascimento": faker.date_of_birth(minimum_age=18, maximum_age=100).strftime('%Y-%m-%d %H:%M:%S'),
        "dataConta": faker.date_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        "naturalidade": faker.city(),
        "estadoCivil": faker.random_element(elements=("Solteiro", "Casado", "Divorciado", "Viúvo")),
        "rg": faker.bothify(text="########-#"),
        "rating": str(faker.random_int(min=1, max=5)),
        "lp": faker.random_element(elements=("Sim", "Não")),
        "propensaoPagamento": faker.random_element(elements=("Alta", "Média", "Baixa")),
        "historicoPagamento": faker.text(),
        "numeroDiasMaiorAtraso": str(faker.random_int(min=0, max=365)),
        "dataMaiorAtraso": faker.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "rendaTitular": str(faker.random_int(min=1000, max=100000)),
        "rendaConjuge": str(faker.random_int(min=0, max=100000)),
        "outrasRendas": str(faker.random_int(min=0, max=50000)),
        "profissao": faker.job(),
        "categoriaProfissao": faker.random_element(elements=("A", "B", "C")),
        "tipoResidencia": faker.random_element(elements=("Casa", "Apartamento", "Outros")),
        "saldoAtraso": str(faker.random_int(min=0, max=10000)),
        "saldoAtual": str(faker.random_int(min=0, max=100000)),
        "saldoContabil": str(faker.random_int(min=0, max=100000)),
        "saldoProvisao": str(faker.random_int(min=0, max=10000)),
        "diasAtraso": str(faker.random_int(min=0, max=365)),
        "dataHoraModificacao": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "emails": criar_Emails(),
        "enderecos": criar_Enderecos(),
        "telefones": criar_Telefones(),
        "informacoesAdicionais": criar_Informacoesadicionais(),
        "assessorias": criar_Assessorias(),
        "marcadores": criar_marcadores(),
        "production_date": faker.date_this_year()
    }

def criar_Acordo_faker():
    return {
        "SOURCE": f"https://pernambucanas.cobransaas.com.br/api/contratos?" \
             f"selector=parcelas&mode=CONTINUABLE&size=2000&" \
             f"situacao={random.choice(['ABERTO', 'PARCIAL', 'PENDENTE', 'CEDIDO', 'LIQUIDADO'])}",
        "id": str(next(id_serial)),
        "cliente": faker.random_number(digits=11),
        "cobrador": faker.random_number(digits=16),
        "tipo": faker.random_element(elements=('ACORDO', 'RENEGOCIACAO')),
        "numeroAcordo": faker.random_number(digits=7),
        "numeroParcelas": faker.random_number(digits=2),
        "dataOperacao": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataEmissao": faker.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d'),
        "dataProcessamento": faker.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d'),
        "dataHoraInclusao": faker.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%dT%H:%M:%S'),
        "dataHoraModificacao": faker.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%dT%H:%M:%S'),
        "dataVencimento": faker.date_time_between(start_date='now', end_date='+1y').strftime('%Y-%m-%d'),
        "situacao": faker.random_element(elements=('NAO_CUMPRIDO', 'CANCELADO', 'LIQUIDADO', 'PENDENTE', 'RENEGOCIADO')),
        "taxaOperacao": str(faker.pyfloat(left_digits=2, right_digits=2)),
        "valorPagoTributo": str(faker.pydecimal(left_digits=5, right_digits=2)),
        "valorPrincipal": str(faker.pydecimal(left_digits=5, right_digits=2)),
        "valorJuros": str(faker.pydecimal(left_digits=5, right_digits=2)),
        "valorTarifa": str(faker.pydecimal(left_digits=5, right_digits=2)),
        "valorTributo": str(faker.pydecimal(left_digits=5, right_digits=2)),
        "valorAdicionado": str(faker.pydecimal(left_digits=5, right_digits=2)),
        "valorTotal": str(faker.pydecimal(left_digits=5, right_digits=2)),
        "saldoPrincipal": str(faker.pydecimal(left_digits=5, right_digits=2)),
        "saldoTotal": str(faker.pydecimal(left_digits=5, right_digits=2)),
        "saldoAtual": str(faker.pydecimal(left_digits=5, right_digits=2)),
        "diasAtraso": str(faker.random_int(min=-10, max=10)),
        "motivoCancelamento": faker.json(),
        "negociacao": {
            "id": str(id_serial),
            "nome": faker.word(),
            "descricao": faker.sentence(),
            "situacao": faker.word(),
            "tipo": faker.word(),
            "gestao": faker.word(),
            "cor": "#" + ''.join([faker.random_element(elements='0123456789abcdef') for _ in range(6)]),
            "icone": faker.word(),
            "tipoDesconto": faker.word(),
            "modalidade": {
                "id": str(id_serial),
                "nome": faker.word(),
                "tipo": faker.word(),
                "situacao": faker.word(),
                "gestao": faker.word(),
                "cor": "#" + ''.join([faker.random_element(elements='0123456789abcdef') for _ in range(6)]),
                "valorDistorcao": str(faker.pydecimal(left_digits=5, right_digits=2)),
                "percentualDistorcao": str(faker.pyfloat(left_digits=2, right_digits=2)),
                "atrasoMaximo": str(faker.random_int()),
                "atrasoEntrada": str(faker.random_int()),
                "acaoOrigemLiquidaca": faker.word()
            }
        },
        "criterioTributo": faker.word(),
        "produto": {"id": str(id_serial), "idExterno": faker.word(), "nome": faker.word(), "descricao": faker.sentence()},
        "tributo": {
            "id": str(id_serial),
            "nome": faker.word(),
            "percentual": str(faker.pyfloat(left_digits=2, right_digits=4)),
            "percentualFixo": str(faker.pyfloat(left_digits=2, right_digits=4)),
            "percentualMaximo": str(faker.pyfloat(left_digits=2, right_digits=4)),
            "arredondamento": faker.word(),
            "dataCalculo": faker.word()
        },
        "meioPagamento": {
            "id": str(id_serial),
            "tipo": faker.word(),
            "nome": faker.word(),
            "cobrador": {"id": str(id_serial), "nome": faker.word(), "banco": faker.random_number(digits=3)}
        },
        "usuario": {"id": str(id_serial), "nome": faker.word()},
        "assessoria": {"id": str(id_serial), "nome": faker.word()},
        "parcelas": [{
            "id": str(id_serial),
            "acordo": str(id_serial),
            "numeroParcela": str(faker.random_int()),
            "dataVencimento": faker.date_time_between(start_date='now', end_date='+1y').strftime('%Y-%m-%d'),
            "situacao": faker.word(),
            "nossoNumero": faker.random_number(digits=10),
            "valorPrincipal": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorJuros": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorTarifa": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorAdicionado": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorTotal": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorTributo": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorBaseTributo": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorPermanencia": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorMora": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorMulta": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "saldoPrincipal": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "saldoTotal": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "saldoAtual": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "registrado": True
        }],
        "pagamentos":  [{
            "id": str(id_serial),
            "dataProcessamento": str(id_serial),
            "dataLiquidacao": str(faker.random_int()),
            "dataCredito": faker.date_time_between(start_date='now', end_date='+1y').strftime('%Y-%m-%d'),
            "dataCnab": faker.word(),
            "dataOperacao": faker.random_number(digits=10),
            "dataHoraInclusao": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "formaLiquidacao": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorRecebido": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorDesconto": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorEncargos": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorDistorcao": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "valorSobra": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "situacao": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "integracao": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "agrupador": {
                'id' : str(id_serial),
                'idExterno':  str(faker.random_int()),
                'nome':  faker.word(),
                'cic':   faker.word(),
                'codigo':  faker.word(),
                'nomeFantasia':  faker.word(),
                'situacao':   faker.word(),
            },
            'abatimentos': {
                'id': str(id_serial),
                'origem':  faker.word(),
                'valorPrincipal': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'valorTotal': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'valorPermanencia': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'valorMora': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'valorMulta': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'valorOutros': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'valorDesconto': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'valorJuros': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'valorTarifa': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'valorTributo': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'valorAdicionado': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'valorAtual': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'percentual': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'tipo': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'integracao': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'mensagemIntegracao': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'dataHoraIntegracao': str(faker.pydecimal(left_digits=5, right_digits=2)),

            }

            "saldoPrincipal": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "saldoTotal": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "saldoAtual": str(faker.pydecimal(left_digits=5, right_digits=2)),
            "registrado": True
        }],
        "origens": origens,
        "pendencias": pendencias,
        "production_date": faker.date_this_year()
    }


def criar_Contrato_faker():
    return {
        "SOURCE": f"https://pernambucanas.cobransaas.com.br/api/contratos?" \
             f"selector=parcelas&mode=CONTINUABLE&size=2000&" \
             f"situacao={random.choice(['ABERTO', 'PARCIAL', 'PENDENTE', 'CEDIDO', 'LIQUIDADO'])}",
        "id": str(next(id_serial)),
        "idExterno": faker.random_number(digits=5),
        "numeroContrato": faker.bothify(text='?????????########'),
        "numeroParcelas": faker.random_number(digits=1),
        "dataEmissao": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataOperacao": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "situacao": faker.random_element(elements=['ABERTO', 'PARCIAL', 'PENDENTE', 'CEDIDO', 'LIQUIDADO']),
        "tipo": faker.random_element(elements=['FATURA']),
        "taxaOperacao": faker.numerify(text='0.########'),
        "valorDevolucao": faker.numerify(text='#.##'),
        "valorIof": faker.numerify(text='#.##'),
        "valorLiquido": faker.numerify(text='#.##'),
        "valorTarifa": faker.numerify(text='#.##'),
        "produto": {"nome": faker.word(), "descricao": faker.sentence()},
        "valorTotal": faker.numerify(text='#.##'),
        "saldoAtual": faker.numerify(text='#.##'),
        "saldoTotal": faker.numerify(text='#.##'),
        "saldoContabil": faker.numerify(text='#.##'),
        "saldoAtraso": faker.numerify(text='#.##'),
        "gestao": faker.random_element(elements=['EXTERNO', 'INTERNO']),
        "diasAtraso": faker.random_number(digits=2),
        "dataVencimento": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataHoraModificacao": faker.date_time().strftime('%Y-%m-%dT%H:%M:%S'),
        "lp": faker.boolean(),
        "dataLp": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "siglaAtraso": faker.random_element(elements=['Perda', 'Creliq']),
        "cliente": {"id": str(id_serial), "idExterno": faker.random_number(digits=10), "tipoPessoa": faker.random_element(elements=['FISICA', 'JURIDICA']), "situacao": "ATIVO", "nome": faker.name(), "cic": faker.random_number(digits=11), "codigo": faker.random_number(digits=5), "sexo": faker.random_element(elements=['MASCULINO', 'FEMININO']), "dataNascimento": faker.date_of_birth().strftime('%Y-%m-%d'), "dataConta": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'), "naturalidade": None, "estadoCivil": faker.random_element(elements=['SOLTEIRO', 'CASADO', 'DIVORCIADO', 'VIUVO']), "rg": faker.bothify(text='########-##'), "rating": faker.random_element(elements=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']), "lp": None, "propensaoPagamento": None, "historicoPagamento": None, "numeroDiasMaiorAtraso": None, "dataMaiorAtraso": None, "rendaTitular": faker.numerify(text='###.##'), "rendaConjuge": faker.numerify(text='###.##'), "outrasRendas": faker.numerify(text='###.##'), "profissao": None, "categoriaProfissao": None, "tipoResidencia": None, "saldoAtraso": faker.numerify(text='#.##'), "saldoAtual": faker.numerify(text='#.##'), "saldoContabil": faker.numerify(text='#.##'), "saldoProvisao": None, "diasAtraso": None, "dataHoraModificacao": faker.date_time().strftime('%Y-%m-%dT%H:%M:%S')},
        "parcelas":
            [
                {
                    "id": str(id_serial),
                    "idExterno": faker.random_number(digits=1),
                    "contrato": str(id_serial),
                    "numeroContrato": faker.bothify(text='?????????########'),
                    "numeroParcela": faker.random_number(digits=1),
                    "dataVencimento": faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                    "diasAtraso": None,
                    "saldoPrincipal": faker.numerify(text='#.##'),
                    "saldoTotal": faker.numerify(text='#.##'),
                    "saldoAtual": faker.numerify(text='#.##'),
                    "saldoContabil": faker.numerify(text='#.##'),
                    "valorPrincipal": faker.numerify(text='#.##'),
                    "valorTotal": faker.numerify(text='#.##'),
                    "valorMulta": faker.numerify(text='#.##'),
                    "valorPermanencia": faker.numerify(text='#.##'),
                    "valorMora": faker.numerify(text='#.##'),
                    "valorOutros": faker.numerify(text='#.##'),
                    "valorDesconto": faker.numerify(text='#.##'),
                    "valorDespesa": None,
                    "valorBoleto": None,
                    "valorBaseTributo": None,
                    "valorPrincipalAberto": faker.numerify(text='#.##'),
                    "situacao": faker.random_element(elements=['ABERTO', 'PARCIAL', 'PENDENTE', 'CEDIDO', 'LIQUIDADO']),
                    "agencia": None,
                    "banco": None,
                    "conta": None,
                    "digito": None,
                    "numeroNossoNumero": None,
                    "nossoNumero": None,
                    "digitoNossoNumero": None,
                    "numeroDocumento": None,
                    "notaFiscal": None,
                    "cobrador": None,
                    "cliente": None,
                    "acordo": faker.boolean(),
                    "bloqueio": faker.boolean(),
                    "promessa": faker.boolean(),
                    "tipoAcordo": None
                }
            ],
        "production_date": faker.date_this_year()
    }

