from faker import Faker
import itertools

fake = Faker('pt_BR')
id_serial = itertools.count(start=0)

# As funções abaixo são responsáveis por criar dados mock para o dataset pfs_risco_raw_tivea
# observe que as funções correspondem a tabelas presentes no dataset.
    
def criar_produto_acordo():
    return {
        "id": next(id_serial),
        "idExterno": fake.ean8(),
        "nome": fake.company(),
        "descricao": fake.paragraph()
    }

def criar_negociacao():
    return {
        "id": next(id_serial),
        "nome": fake.company(),
        "descricao": fake.paragraph(),
        "situacao": fake.word(),
        "tipo": fake.word(),
        "gestao": fake.word(),
        "cor": fake.hex_color(),
        "icone": fake.word(),
        "tipoDesconto": fake.word(),
        "modalidade": {"chave": fake.word(), "valor": fake.random_number()}
    }


def criar_tributo():
    return {
        "id": str(next(id_serial)),
        "nome": fake.word(),
        "percentual": fake.numerify("%0.2f"),
        "percentualFixo": fake.numerify("%0.2f"),
        "percentualMaximo": fake.numerify("%0.2f"),
        "arredondamento": fake.random_element(elements=["0", "1"]),
        "dataCalculo": fake.date_time().strftime('%Y-%m-%d %H:%M:%S')
    }

def criar_Meiopagamento():
    return {
        "id": str(next(id_serial)),
        "tipo": fake.credit_card_provider(),
        "nome": fake.credit_card_number(),
        "cobrador": {"nome": fake.name(), "cpf": fake.cpf()}
    }

def criar_usuario():
    return {
        "id": str(next(id_serial)),
        "nome": fake.name()
    }

def criar_Assessoria():
    return {
        "id": str(next(id_serial)),
        "nome": fake.company()
    }


def criar_Parcelas():
    return {
        "id": str(next(id_serial)),
        "acordo": fake.word(),
        "numeroParcela": fake.word(),
        "dataVencimento": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "situacao": fake.word(),
        "nossoNumero": fake.word(),
        "valorPrincipal": fake.pydecimal(left_digits=5, right_digits=2),
        "valorJuros": fake.pydecimal(left_digits=5, right_digits=2),
        "valorTarifa": fake.pydecimal(left_digits=5, right_digits=2),
        "valorAdicionado": fake.pydecimal(left_digits=5, right_digits=2),
        "valorTotal": fake.pydecimal(left_digits=5, right_digits=2),
        "valorTributo": fake.pydecimal(left_digits=5, right_digits=2),
        "valorBaseTributo": fake.pydecimal(left_digits=5, right_digits=2),
        "valorPermanencia": fake.pydecimal(left_digits=5, right_digits=2),
        "valorMora": fake.pydecimal(left_digits=5, right_digits=2),
        "valorMulta": fake.pydecimal(left_digits=5, right_digits=2),
        "saldoPrincipal": fake.pydecimal(left_digits=5, right_digits=2),
        "saldoTotal": fake.pydecimal(left_digits=5, right_digits=2),
        "saldoAtual": fake.pydecimal(left_digits=5, right_digits=2),
        "registrado": fake.boolean()
    }

def criar_Pagamentos():
    return {
        "id": str(next(id_serial)),
        "dataProcessamento": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataLiquidacao": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataCredito": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataCnab": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataOperacao": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataHoraInclusao": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "formaLiquidacao": fake.word(),
        "valorRecebido": fake.numerify('R$ ###,##'),
        "valorDesconto": fake.numerify('R$ ###,##'),
        "valorEncargos": fake.numerify('R$ ###,##'),
        "valorDistorcao": fake.numerify('R$ ###,##'),
        "valorSobra": fake.numerify('R$ ###,##'),
        "situacao": fake.word(),
        "integracao": fake.word(),
        "agrupador": {},
        "abatimentos": {},
        "liquidacoes": {}
    }

def criar_origens():
    return {
        "id": next(id_serial),
        "valorContabil": fake.pystr(),
        "descontoContabil": fake.pystr(),
        "saldoContabil": fake.pystr(),
        "contrato": fake.pystr(),
        "contratoId": fake.pystr(),
        "numeroContrato": fake.pystr(),
        "parcela": fake.pystr(),
        "parcelaId": fake.pystr(),
        "numeroParcela": fake.pystr(),
        "diasAtraso": fake.pystr(),
        "ordem": fake.pystr(),
        "dataVencimento": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "nossoNumero": fake.pystr(),
        "notaFiscal": fake.pystr(),
        "situacao": fake.pystr(),
        "valorPrincipal": fake.pystr(),
        "valorTotal": fake.pystr(),
        "valorPermanencia": fake.pystr(),
        "valorMora": fake.pystr(),
        "valorMulta": fake.pystr(),
        "valorOutros": fake.pystr(),
        "valorDesconto": fake.pystr(),
        "valorJuros": fake.pystr(),
        "valorTarifa": fake.pystr(),
        "valorAdicionado": fake.pystr(),
        "valorAtual": fake.pystr(),
        "saldoPrincipal": fake.pystr(),
        "saldoTotal": fake.pystr(),
        "saldoPermanencia": fake.pystr(),
        "saldoMora": fake.pystr(),
        "saldoMulta": fake.pystr(),
        "saldoOutros": fake.pystr(),
        "saldoDesconto": fake.pystr(),
        "saldoJuros": fake.pystr(),
        "saldoTarifa": fake.pystr(),
        "saldoAdicionado": fake.pystr(),
        "saldoAtual": fake.pystr(),
        "descontoPrincipal": fake.pystr(),
        "descontoJuros": fake.pystr(),
        "descontoMora": fake.pystr(),
        "descontoMulta": fake.pystr(),
        "descontoOutros": fake.pystr(),
        "descontoPermanencia": fake.pystr(),
        "descontoTotal": fake.pystr(),
    }
    

def criar_pendencias():
    return {
        "id": str(next(id_serial)),
        "dataGeracao": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataProcessamento": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataParecer": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "situacao": fake.word(),
        "tipo": fake.word(),
        "observacao": fake.paragraph(),
        "pareceres": {"a": fake.word()}
    }

def criar_Emails():
    return {
        "id": str(next(id_serial)),
        "idExterno": fake.uuid4(),
        "email": fake.email(),
        "principal": fake.boolean(),
        "ranking": fake.word(),
        "dataHoraModificacao": fake.date_time().strftime('%Y-%m-%d %H:%M:%S')
    }


def criar_Enderecos():
    return {
        "id": str(next(id_serial)),
        "idExterno": fake.uuid4(),
        "cep": fake.postcode(),
        "codigoDne": fake.ean8(),
        "complemento": fake.random_digit(),
        "logradouro": fake.street_name(),
        "bairro": fake.street_address(),
        "cidade": fake.city(),
        "numero": fake.building_number(),
        "tipo": fake.random_element(elements=('Residencial', 'Comercial')),
        "tipoLogradouro": fake.random_element(elements=('Rua', 'Avenida', 'Praça')),
        "uf": fake.state_abbr(),
        "principal": fake.boolean(),
        "ranking": str(fake.random_int(min=1, max=10)),
        "dataHoraModificacao": fake.date_time().strftime('%Y-%m-%d %H:%M:%S')
    }

 
def criar_Telefones():
    return {
        "id": str(next(id_serial)),
        "idExterno": fake.uuid4(),
        "ddd": fake.random_number(digits=2),
        "telefone": fake.numerify('#########'),
        "ramal": fake.random_number(digits=4),
        "tipo": fake.word(),
        "observacao": fake.sentence(),
        "principal": fake.boolean(),
        "ranking": str(fake.random_int(min=1, max=10)),
        "dataHoraModificacao": fake.date_time().strftime('%Y-%m-%d %H:%M:%S')
    }


def criar_Informacoesadicionais():
    return {
        "id": next(id_serial),
        "nome": fake.word(),
        "linha": fake.word(),
        "coluna": fake.word(),
        "valor": fake.word(),
        "tipo": fake.word(),
        "tamanho": fake.word(),
    }

def criar_Assessorias():
    return {
        "id": str(next(id_serial)),
        "nome": fake.company(),
        "situacao": fake.random_element(elements=('Ativo', 'Inativo')),
        "cic": fake.bothify(text='CIC-??-#######'),
        "cep": fake.postcode(),
        "complemento": fake.random_digit(),
        "logradouro": fake.street_address(),
        "bairro": fake.street_name(),
        "cidade": fake.city(),
        "numero": fake.building_number(),
        "uf": fake.state_abbr(),
        "alterarInformacoesCadastrais": fake.boolean()
    }

def criar_marcadores():
    return {
        "id": str(next(id_serial)),
        "nome": fake .word(),
        "cor": fake .color_name()
    }


def criar_ProdutoContrato():
    return {
        "id": next(id_serial),
        "nome": fake.word(),
        "descricao": fake.paragraph(),
    }
 
 
def criar_cliente():
    return {
        "id": str(next(id_serial)),
        "idExterno": fake.uuid4(),
        "tipoPessoa": fake.random_element(elements=("Física", "Jurídica")),
        "situacao": fake.random_element(elements=("Ativo", "Inativo")),
        "nome": fake.name(),
        "cic": fake.bothify(text="??########"),
        "codigo": fake.ean13(),
        "sexo": fake.random_element(elements=("Masculino", "Feminino", "Outro")),
        "dataNascimento": fake.date_of_birth(minimum_age=18, maximum_age=100).strftime('%Y-%m-%d %H:%M:%S'),
        "dataConta": fake.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "naturalidade": fake.city(),
        "estadoCivil": fake.random_element(elements=("Solteiro", "Casado", "Divorciado", "Viúvo")),
        "rg": fake.bothify(text="??.???.???-?",),
        "rating": fake.random_int(min=1, max=5),
        "lp": fake.random_element(elements=("A", "B", "C")),
        "propensaoPagamento": fake.random_int(min=1, max=10),
        "historicoPagamento": fake.paragraph(nb_sentences=3),
        "numeroDiasMaiorAtraso": fake.random_int(min=0, max=365),
        "dataMaiorAtraso": fake.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "rendaTitular": fake.numerify(text="R$#######.##"),
        "rendaConjuge": fake.numerify(text="R$#######.##"),
        "outrasRendas": fake.numerify(text="R$#######.##"),
        "profissao": fake.job(),
        "categoriaProfissao": fake.random_element(elements=("A", "B", "C")),
        "tipoResidencia": fake.random_element(elements=("Casa", "Apartamento", "Outros")),
        "saldoAtraso": fake.numerify(text="R$#######.##"),
        "saldoAtual": fake.numerify(text="R$#######.##"),
        "saldoContabil": fake.numerify(text="R$#######.##"),
        "saldoProvisao": fake.numerify(text="R$#######.##"),
        "diasAtraso": fake.random_int(min=0, max=365),
        "dataHoraModificacao": fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S')
        
    }
 
def criar_parcelas():
    return {
        "id": str(next(id_serial)),
        "idExterno": fake.uuid4(),
        "contrato": fake.ean13(),
        "numeroContrato": fake.random_number(digits=8),
        "numeroParcela": fake.random_number(digits=2),
        "dataVencimento": fake.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "diasAtraso": fake.random_number(digits=2),
        "saldoPrincipal": fake.pydecimal(left_digits=10, right_digits=2),
        "saldoTotal": fake.pydecimal(left_digits=10, right_digits=2),
        "saldoAtual": fake.pydecimal(left_digits=10, right_digits=2),
        "saldoContabil": fake.pydecimal(left_digits=10, right_digits=2),
        "valorPrincipal": fake.pydecimal(left_digits=10, right_digits=2),
        "valorTotal": fake.pydecimal(left_digits=10, right_digits=2),
        "valorMulta": fake.pydecimal(left_digits=10, right_digits=2),
        "valorPermanencia": fake.pydecimal(left_digits=10, right_digits=2),
        "valorMora": fake.pydecimal(left_digits=10, right_digits=2),
        "valorOutros": fake.pydecimal(left_digits=10, right_digits=2),
        "valorDesconto": fake.pydecimal(left_digits=10, right_digits=2),
        "valorDespesa": fake.pydecimal(left_digits=10, right_digits=2),
        "valorBoleto": fake.pydecimal(left_digits=10, right_digits=2),
        "valorBaseTributo": fake.pydecimal(left_digits=10, right_digits=2),
        "valorPrincipalAberto": fake.pydecimal(left_digits=10, right_digits=2),
        "situacao": fake.word(),
        "agencia": fake.random_number(digits=4),
        "banco": fake.bank_country(),
        "conta": fake.iban(),
        "digito": fake.random_digit(),
        "numeroNossoNumero": fake.random_number(digits=10),
        "nossoNumero": fake.random_number(digits=10),
        "digitoNossoNumero": fake.random_digit(),
        "numeroDocumento": fake.ssn(),
        "notaFiscal": fake.ean13(),
        "cobrador": fake.name(),
        "cliente": fake.name(),
        "acordo": fake.boolean(),
        "bloqueio": fake.boolean(),
        "promessa": fake.boolean(),
        "tipoAcordo": fake.word()
    }


def criar_Acordo():
    return {
        "source": fake.word(),
        "id": fake.uuid4(),
        "cliente": fake.name(),
        "cobrador": fake.name(),
        "tipo": fake.word(),
        "numeroAcordo": str(fake.random_number(digits=8)),
        "numeroParcelas": fake.random_number(digits=2),
        "dataOperacao": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataEmissao": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataProcessamento": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataHoraInclusao": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataHoraModificacao": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "dataVencimento": fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        "situacao": fake.word(),
        "taxaOperacao": fake.random_number(digits=5),
        "valorPagoTributo": fake.random_number(digits=8),
        "valorPrincipal": fake.random_number(digits=8),
        "valorJuros": fake.random_number(digits=8),
        "valorTarifa": fake.random_number(digits=8),
        "valorTributo": fake.random_number(digits=8),
        "valorAdicionado": fake.random_number(digits=8),
        "valorTotal": fake.random_number(digits=8),
        "saldoPrincipal": fake.random_number(digits=8),
        "saldoTotal": fake.random_number(digits=8),
        "saldoAtual": fake.random_number(digits=8),
        "diasAtraso": fake.random_number(digits=3),
        "motivoCancelamento": fake.sentence(),
        "negociacao": criar_negociacao(),
        "criterioTributo": fake.word(),
        "produto": criar_produto_acordo(),
        "tributo": criar_tributo(),
        "meioPagamento": criar_Meiopagamento(),
        "usuario": criar_usuario(),
        "assessoria": criar_Assessoria(),
        "parcelas": criar_Parcelas(),
        "pagamentos": criar_Pagamentos(),
        "origens": criar_origens(),
        "pendencias": criar_pendencias(),
        "production_date": fake.date()
    }
