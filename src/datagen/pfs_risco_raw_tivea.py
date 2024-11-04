import random

from faker import Faker
from jsonl_convert import jsonl_data

faker = Faker('pt_BR')


def Datagen_pfs_risco_raw_tivea(num_records):

    data = {'acordo': [], 'cliente': [], 'contrato': []}

    for _ in range(num_records):

        criar_produto_acordo = {
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'idExterno': faker.ean8(),
            'nome': faker.company(),
            'descricao': faker.paragraph(),
        }

        criar_Emails = {
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'idExterno': faker.uuid4(),
            'email': faker.email(),
            'principal': faker.boolean(),
            'ranking': faker.word(),
            'dataHoraModificacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        }

        criar_Enderecos = {
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'idExterno': faker.uuid4(),
            'cep': faker.postcode(),
            'codigoDne': faker.ean8(),
            'complemento': faker.random_digit(),
            'logradouro': faker.street_name(),
            'bairro': faker.street_address(),
            'cidade': faker.city(),
            'numero': faker.building_number(),
            'tipo': faker.random_element(elements=('Residencial', 'Comercial')),
            'tipoLogradouro': faker.random_element(
                elements=('Rua', 'Avenida', 'Praça')
            ),
            'uf': faker.state_abbr(),
            'principal': faker.boolean(),
            'ranking': str(faker.random_int(min=1, max=10)),
            'dataHoraModificacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        }

        criar_Telefones = {
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'idExterno': faker.uuid4(),
            'ddd': faker.random_number(digits=2),
            'telefone': faker.numerify('#########'),
            'ramal': faker.random_number(digits=4),
            'tipo': faker.word(),
            'observacao': faker.sentence(),
            'principal': faker.boolean(),
            'ranking': str(faker.random_int(min=1, max=10)),
            'dataHoraModificacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        }

        criar_Informacoesadicionais = {
            'nome': faker.word(),
            'linha': faker.word(),
            'coluna': faker.word(),
            'valor': faker.word(),
            'tipo': faker.word(),
            'tamanho': faker.word(),
        }

        criar_Assessorias = {
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'nome': faker.company(),
            'situacao': faker.random_element(elements=('Ativo', 'Inativo')),
            'cic': faker.bothify(text='CIC-??-#######'),
            'cep': faker.postcode(),
            'complemento': faker.random_digit(),
            'logradouro': faker.street_address(),
            'bairro': faker.street_name(),
            'cidade': faker.city(),
            'numero': faker.building_number(),
            'uf': faker.state_abbr(),
            'alterarInformacoesCadastrais': faker.boolean(),
       }

        criar_marcadores = {
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'nome': faker.word(),
            'cor': faker.color_name(),
        }

        criar_Cliente_faker = {
                'source': faker.word(),
                'id': criar_produto_acordo['id'],
                'idExterno': faker.uuid4(),
                'tipoPessoa': faker.random_element(elements=('Física', 'Jurídica')),
                'situacao': faker.random_element(elements=('Ativo', 'Inativo')),
                'nome': faker.name(),
                'cic': faker.bothify(text='??########'),
                'codigo': faker.ean13(),
                'sexo': faker.random_element(
                    elements=('Masculino', 'Feminino', 'Outro')
                ),
                'dataNascimento': faker.date_of_birth(
                    minimum_age=18, maximum_age=100
                ).strftime('%Y-%m-%d %H:%M:%S'),
                'dataConta': faker.date_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
                'naturalidade': faker.city(),
                'estadoCivil': faker.random_element(
                    elements=('Solteiro', 'Casado', 'Divorciado', 'Viúvo')
                ),
                'rg': faker.bothify(text='########-#'),
                'rating': str(faker.random_int(min=1, max=5)),
                'lp': faker.random_element(elements=('Sim', 'Não')),
                'propensaoPagamento': faker.random_element(
                    elements=('Alta', 'Média', 'Baixa')
                ),
                'historicoPagamento': faker.text(),
                'numeroDiasMaiorAtraso': str(faker.random_int(min=0, max=365)),
                'dataMaiorAtraso': faker.date_this_year().strftime(
                    '%Y-%m-%d %H:%M:%S'
                ),
                'rendaTitular': str(faker.random_int(min=1000, max=100000)),
                'rendaConjuge': str(faker.random_int(min=0, max=100000)),
                'outrasRendas': str(faker.random_int(min=0, max=50000)),
                'profissao': faker.job(),
                'categoriaProfissao': faker.random_element(elements=('A', 'B', 'C')),
                'tipoResidencia': faker.random_element(
                    elements=('Casa', 'Apartamento', 'Outros')
                ),
                'saldoAtraso': str(faker.random_int(min=0, max=10000)),
                'saldoAtual': str(faker.random_int(min=0, max=100000)),
                'saldoContabil': str(faker.random_int(min=0, max=100000)),
                'saldoProvisao': str(faker.random_int(min=0, max=10000)),
                'diasAtraso': str(faker.random_int(min=0, max=365)),
                'dataHoraModificacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                'emails': criar_Emails,
                'enderecos': criar_Enderecos,
                'telefones': criar_Telefones,
                'informacoesAdicionais': criar_Informacoesadicionais,
                'assessorias': criar_Assessorias,
                'marcadores': criar_marcadores,
                'production_date': faker.date_this_year(),
            }
        data['cliente'].append(criar_Cliente_faker)

        criar_Acordo_faker = {
            'SOURCE': f"https://pernambucanas.cobransaas.com.br/api/contratos?"
            f"selector=parcelas&mode=CONTINUABLE&size=2000&"
            f"situacao={random.choice(['ABERTO', 'PARCIAL', 'PENDENTE', 'CEDIDO', 'LIQUIDADO'])}",
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'cliente': faker.random_number(digits=11),
            'cobrador': faker.random_number(digits=16),
            'tipo': faker.random_element(elements=('ACORDO', 'RENEGOCIACAO')),
            'numeroAcordo': faker.random_number(digits=7),
            'numeroParcelas': faker.random_number(digits=2),
            'dataOperacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dataEmissao': faker.date_time_between(
                start_date='-1y', end_date='now'
            ).strftime('%Y-%m-%d'),
            'dataProcessamento': faker.date_time_between(
                start_date='-1y', end_date='now'
            ).strftime('%Y-%m-%d'),
            'dataHoraInclusao': faker.date_time_between(
                start_date='-1y', end_date='now'
            ).strftime('%Y-%m-%dT%H:%M:%S'),
            'dataHoraModificacao': faker.date_time_between(
            start_date='-1y', end_date='now'
            ).strftime('%Y-%m-%dT%H:%M:%S'),
            'dataVencimento': faker.date_time_between(
                start_date='now', end_date='+1y'
            ).strftime('%Y-%m-%d'),
            'situacao': faker.random_element(
                elements=(
                    'NAO_CUMPRIDO',
                    'CANCELADO',
                    'LIQUIDADO',
                    'PENDENTE',
                    'RENEGOCIADO',
                )
            ),
            'taxaOperacao': str(faker.pyfloat(left_digits=2, right_digits=2)),
            'valorPagoTributo': str(
                faker.pydecimal(left_digits=5, right_digits=2)
            ),
            'valorPrincipal': str(faker.pydecimal(left_digits=5, right_digits=2)),
            'valorJuros': str(faker.pydecimal(left_digits=5, right_digits=2)),
            'valorTarifa': str(faker.pydecimal(left_digits=5, right_digits=2)),
            'valorTributo': str(faker.pydecimal(left_digits=5, right_digits=2)),
            'valorAdicionado': str(faker.pydecimal(left_digits=5, right_digits=2)),
            'valorTotal': str(faker.pydecimal(left_digits=5, right_digits=2)),
            'saldoPrincipal': str(faker.pydecimal(left_digits=5, right_digits=2)),
            'saldoTotal': str(faker.pydecimal(left_digits=5, right_digits=2)),
            'saldoAtual': str(faker.pydecimal(left_digits=5, right_digits=2)),
            'diasAtraso': str(faker.random_int(min=-10, max=10)),
            'motivoCancelamento': faker.json(),
            'negociacao': {
                'id': str(faker.random_number(digits=10, fix_len=True)),
                'nome': faker.word(),
                'descricao': faker.sentence(),
                'situacao': faker.word(),
                'tipo': faker.word(),
                'gestao': faker.word(),
                'cor': '#'
                + ''.join([
                    faker.random_element(elements='0123456789abcdef')
                    for _ in range(6)
                ]),
                'icone': faker.word(),
                'tipoDesconto': faker.word(),
                'modalidade': {
                    'id': str(faker.random_number(digits=10, fix_len=True)),
                    'nome': faker.word(),
                    'tipo': faker.word(),
                    'situacao': faker.word(),
                    'gestao': faker.word(),
                    'cor': '#'
                    + ''.join([
                        faker.random_element(elements='0123456789abcdef')
                        for _ in range(6)
                    ]),
                    'valorDistorcao': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'percentualDistorcao': str(
                        faker.pyfloat(left_digits=2, right_digits=2)
                    ),
                    'atrasoMaximo': str(faker.random_int()),
                    'atrasoEntrada': str(faker.random_int()),
                    'acaoOrigemLiquidacao': faker.word(),
                },
            },
            'criterioTributo': faker.word(),
            'produto': {
                'id': str(faker.random_number(digits=10, fix_len=True)),
                'idExterno': faker.word(),
                'nome': faker.word(),
                'descricao': faker.sentence(),
            },
            'tributo': {
                'id': str(faker.random_number(digits=10, fix_len=True)),
                'nome': faker.word(),
                'percentual': str(faker.pyfloat(left_digits=2, right_digits=4)),
                'percentualFixo': str(
                    faker.pyfloat(left_digits=2, right_digits=4)
                ),
                'percentualMaximo': str(
                    faker.pyfloat(left_digits=2, right_digits=4)
                ),
                'arredondamento': faker.word(),
                'dataCalculo': faker.word(),
            },
            'meioPagamento': {
                'id': str(faker.random_number(digits=10, fix_len=True)),
                'tipo': faker.word(),
                'nome': faker.word(),
                'cobrador': {
                    'id': str(faker.random_number(digits=10, fix_len=True)),
                    'nome': faker.word(),
                    'banco': faker.random_number(digits=3),
                },
            },
            'usuario': {'id': str(faker.random_number(digits=10, fix_len=True)), 'nome': faker.word()},
            'assessoria': {'id': str(faker.random_number(digits=10, fix_len=True)), 'nome': faker.word()},
            'parcelas': [
                {
                    'id': str(faker.random_number(digits=10, fix_len=True)),
                    'acordo': str(faker.random_number(digits=10, fix_len=True)),
                    'numeroParcela': str(faker.random_int()),
                    'dataVencimento': faker.date_time_between(
                        start_date='now', end_date='+1y'
                    ).strftime('%Y-%m-%d'),
                    'situacao': faker.word(),
                    'nossoNumero': faker.random_number(digits=10),
                    'valorPrincipal': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorJuros': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorTarifa': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorAdicionado': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorTotal': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorTributo': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorBaseTributo': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorPermanencia': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorMora': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorMulta': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'saldoPrincipal': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'saldoTotal': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'saldoAtual': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'registrado': True,
                }
            ],
            'pagamentos': {
                'id': str(faker.random_number(digits=10, fix_len=True)),
                'dataProcessamento': str(faker.random_number(digits=10, fix_len=True)),
                'dataLiquidacao': str(faker.random_int()),
                'dataCredito': faker.date_time_between(
                    start_date='now', end_date='+1y'
                ).strftime('%Y-%m-%d'),
                'dataCnab': faker.word(),
                'dataOperacao': faker.random_number(digits=10),
                'dataHoraInclusao': str(
                    faker.pydecimal(left_digits=5, right_digits=2)
                ),
                'formaLiquidacao': str(
                    faker.pydecimal(left_digits=5, right_digits=2)
                ),
                'valorRecebido': str(
                    faker.pydecimal(left_digits=5, right_digits=2)
                ),
                'valorDesconto': str(
                    faker.pydecimal(left_digits=5, right_digits=2)
                ),
                'valorEncargos': str(
                    faker.pydecimal(left_digits=5, right_digits=2)
                ),
                'valorDistorcao': str(
                    faker.pydecimal(left_digits=5, right_digits=2)
                ),
                'valorSobra': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'situacao': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'integracao': str(faker.pydecimal(left_digits=5, right_digits=2)),
                'agrupador': {
                    'id': str(faker.random_number(digits=10, fix_len=True)),
                    'idExterno': str(faker.random_int()),
                    'nome': faker.word(),
                    'cic': faker.word(),
                    'codigo': faker.word(),
                    'nomeFantasia': faker.word(),
                    'situacao': faker.word(),
                },
                'abatimentos': {
                    'id': str(faker.random_number(digits=10, fix_len=True)),
                    'origem': faker.word(),
                    'valorPrincipal': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorTotal': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorPermanencia': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorMora': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorMulta': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorOutros': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorDesconto': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorJuros': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorTarifa': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorTributo': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorAdicionado': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'valorAtual': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'percentual': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'tipo': str(faker.pydecimal(left_digits=5, right_digits=2)),
                    'integracao': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'mensagemIntegracao': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                    'dataHoraIntegracao': str(
                        faker.pydecimal(left_digits=5, right_digits=2)
                    ),
                },
                'liquidacoes': {
                    'id': faker.uuid4(),
                    'parcela': faker.word(),
                    'valorPrincipal': faker.pyfloat(
                        positive=True, max_value=10000
                    ),
                    'valorTotal': faker.pyfloat(positive=True, max_value=15000),
                    'valorJuros': faker.pyfloat(positive=True, max_value=500),
                    'valorEncargos': faker.pyfloat(positive=True, max_value=200),
                    'valorDesconto': faker.pyfloat(positive=True, max_value=100),
                    'valorDistorcao': faker.pyfloat(positive=True, max_value=50),
                    'diasAtraso': faker.random_int(min=0, max=30),
                    'numeroParcela': faker.random_int(min=1, max=12),
                    'tipo': faker.word(),
                },



            },
            'origens': {
                    'id': faker.uuid4(),
                    'valorContabil': faker.pyfloat(positive=True, max_value=10000),
                    'descontoContabil': faker.pyfloat(
                        positive=True, max_value=500
                    ),
                    'saldoContabil': faker.pyfloat(positive=True, max_value=9500),
                    'contrato': faker.word(),
                    'contratoId': faker.uuid4(),
                    'numeroContrato': faker.numerify('###-####-###'),
                    'parcela': faker.word(),
                    'parcelaId': faker.uuid4(),
                    'numeroParcela': faker.random_int(min=1, max=12),
                    'diasAtraso': faker.random_int(min=0, max=30),
                    'ordem': faker.random_int(min=1, max=10),
                    'dataVencimento': faker.date_between(
                        start_date='-1y', end_date='today'
                    ),
                    'nossoNumero': faker.numerify('###-####-###'),
                    'notaFiscal': faker.numerify('###-####-###'),
                    'situacao': faker.word(),
                    'valorPrincipal': faker.pyfloat(
                        positive=True, max_value=10000
                    ),
                    'valorTotal': faker.pyfloat(positive=True, max_value=15000),
                    'valorPermanencia': faker.pyfloat(
                        positive=True, max_value=500
                    ),
                    'valorMora': faker.pyfloat(positive=True, max_value=200),
                    'valorMulta': faker.pyfloat(positive=True, max_value=100),
                    'valorOutros': faker.pyfloat(positive=True, max_value=50),
                    'valorDesconto': faker.pyfloat(positive=True, max_value=100),
                    'valorJuros': faker.pyfloat(positive=True, max_value=500),
                    'valorTarifa': faker.pyfloat(positive=True, max_value=200),
                    'valorAdicionado': faker.pyfloat(positive=True, max_value=100),
                    'valorAtual': faker.pyfloat(positive=True, max_value=15000),
                    'saldoPrincipal': faker.pyfloat(
                        positive=True, max_value=10000
                    ),
                    'saldoTotal': faker.pyfloat(positive=True, max_value=15000),
                    'saldoPermanencia': faker.pyfloat(
                        positive=True, max_value=500
                    ),
                    'saldoMora': faker.pyfloat(positive=True, max_value=200),
                    'saldoMulta': faker.pyfloat(positive=True, max_value=100),
                    'saldoOutros': faker.pyfloat(positive=True, max_value=50),
                    'saldoDesconto': faker.pyfloat(positive=True, max_value=100),
                    'saldoJuros': faker.pyfloat(positive=True, max_value=500),
                    'saldoTarifa': faker.pyfloat(positive=True, max_value=200),
                    'saldoAdicionado': faker.pyfloat(positive=True, max_value=100),
                    'saldoAtual': faker.pyfloat(positive=True, max_value=15000),
                    'descontoPrincipal': faker.pyfloat(
                        positive=True, max_value=500
                    ),
                    'descontoJuros': faker.pyfloat(positive=True, max_value=200),
                    'descontoMora': faker.pyfloat(positive=True, max_value=100),
                    'descontoMulta': faker.pyfloat(positive=True, max_value=50),
                    'descontoOutros': faker.pyfloat(positive=True, max_value=50),
                    'descontoPermanencia': faker.pyfloat(
                        positive=True, max_value=500
                    ),
                    'descontoTotal': faker.pyfloat(positive=True, max_value=1000),
                },
                'pendencias': {
                    'id': faker.uuid4(),
                    'dataGeracao': faker.date_between(
                        start_date='-1y', end_date='today'
                    ),
                    'dataProcessamento': faker.date_between(
                        start_date='-1y', end_date='today'
                    ),
                    'dataParecer': faker.date_between(
                        start_date='-1y', end_date='today'
                    ),
                    'situacao': faker.word(),
                    'tipo': faker.word(),
                    'observacao': faker.text(),
                    'pareceres': {
                        'situacao': faker.word(),
                        'observacao': faker.text(),
                        'usuario': {
                            'idExterno': faker.uuid4(),
                            'nome': faker.name(),
                            'id': faker.uuid4(),
                        },
                        'id': faker.uuid4(),
                        'dataHoraModificacao': faker.date_time_between(
                            start_date='-1y', end_date='now'
                        ),
                    },
                },

                'production_date': faker.date_this_year(),
        }
        data['acordo'].append(criar_Acordo_faker)

        criar_Contrato_faker = {
            'SOURCE': f"https://pernambucanas.cobransaas.com.br/api/contratos?"
            f"selector=parcelas&mode=CONTINUABLE&size=2000&"
            f"situacao={random.choice(['ABERTO', 'PARCIAL', 'PENDENTE', 'CEDIDO', 'LIQUIDADO'])}",
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'idExterno': faker.random_number(digits=5),
            'numeroContrato': faker.bothify(text='?????????########'),
            'numeroParcelas': faker.random_number(digits=1),
            'dataEmissao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dataOperacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'situacao': faker.random_element(
                elements=['ABERTO', 'PARCIAL', 'PENDENTE', 'CEDIDO', 'LIQUIDADO']
            ),
            'tipo': faker.random_element(elements=['FATURA']),
            'taxaOperacao': faker.numerify(text='0.########'),
            'valorDevolucao': faker.numerify(text='#.##'),
            'valorIof': faker.numerify(text='#.##'),
            'valorLiquido': faker.numerify(text='#.##'),
            'valorTarifa': faker.numerify(text='#.##'),
            'produto': {'nome': faker.word(), 'descricao': faker.sentence()},
            'valorTotal': faker.numerify(text='#.##'),
            'saldoAtual': faker.numerify(text='#.##'),
            'saldoTotal': faker.numerify(text='#.##'),
            'saldoContabil': faker.numerify(text='#.##'),
            'saldoAtraso': faker.numerify(text='#.##'),
            'gestao': faker.random_element(elements=['EXTERNO', 'INTERNO']),
            'diasAtraso': faker.random_number(digits=2),
            'dataVencimento': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dataHoraModificacao': faker.date_time().strftime('%Y-%m-%dT%H:%M:%S'),
            'lp': faker.boolean(),
            'dataLp': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'siglaAtraso': faker.random_element(elements=['Perda', 'Creliq']),
            'cliente': {
                'id': str(faker.random_number(digits=10, fix_len=True)),
                'idExterno': faker.random_number(digits=10),
                'tipoPessoa': faker.random_element(
                    elements=['FISICA', 'JURIDICA']
                ),
                'situacao': 'ATIVO',
                'nome': faker.name(),
                'cic': faker.random_number(digits=11),
                'codigo': faker.random_number(digits=5),
                'sexo': faker.random_element(elements=['MASCULINO', 'FEMININO']),
                'dataNascimento': faker.date_of_birth().strftime('%Y-%m-%d'),
                'dataConta': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                'naturalidade': faker.city(),
                'estadoCivil': faker.random_element(
                    elements=['SOLTEIRO', 'CASADO', 'DIVORCIADO', 'VIUVO']
                ),
                'rg': faker.bothify(text='########-##'),
                'rating': faker.random_element(
                    elements=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
                ),
                'lp': faker.word(),
                'propensaoPagamento': faker.word(),
                'historicoPagamento': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                'numeroDiasMaiorAtraso': str(faker.random_number(digits=3, fix_len=True)),
                'dataMaiorAtraso': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
                'rendaTitular': faker.numerify(text='###.##'),
                'rendaConjuge': faker.numerify(text='###.##'),
                'outrasRendas': faker.numerify(text='###.##'),
                'profissao': faker.job(),
                'categoriaProfissao': faker.random_element(elements=["Tecnologia", "Saúde", "Educação", "Artes", "Finanças"]),
                'tipoResidencia': faker.random_element(elements=["Apartamento", "Casa", "Sobrado", "Chácara", "Kitnet", "Cobertura", "Loft"]),
                'saldoAtraso': faker.numerify(text='#.##'),
                'saldoAtual': faker.numerify(text='#.##'),
                'saldoContabil': faker.numerify(text='#.##'),
                'saldoProvisao': faker.numerify(text='#.##'),
                'diasAtraso': str(faker.random_number(digits=3, fix_len=True)),
                'dataHoraModificacao': faker.date_time().strftime(
                    '%Y-%m-%dT%H:%M:%S'
                ),
            },
            'parcelas': [
                {
                    'id': str(faker.random_number(digits=10, fix_len=True)),
                    'idExterno': faker.random_number(digits=1),
                    'contrato': str(faker.random_number(digits=10, fix_len=True)),
                    'numeroContrato': faker.bothify(text='?????????########'),
                    'numeroParcela': faker.random_number(digits=1),
                    'dataVencimento': faker.date_time().strftime(
                        '%Y-%m-%d %H:%M:%S'
                    ),
                    'diasAtraso': faker.date_time().strftime(
                    '%Y-%m-%dT%H:%M:%S'
                ),
                    'saldoPrincipal': faker.numerify(text='#.##'),
                    'saldoTotal': faker.numerify(text='#.##'),
                    'saldoAtual': faker.numerify(text='#.##'),
                    'saldoContabil': faker.numerify(text='#.##'),
                    'valorPrincipal': faker.numerify(text='#.##'),
                    'valorTotal': faker.numerify(text='#.##'),
                    'valorMulta': faker.numerify(text='#.##'),
                    'valorPermanencia': faker.numerify(text='#.##'),
                    'valorMora': faker.numerify(text='#.##'),
                    'valorOutros': faker.numerify(text='#.##'),
                    'valorDesconto': faker.numerify(text='#.##'),
                    'valorDespesa': faker.pydecimal(left_digits=5, right_digits=2),
                    'valorBoleto': faker.pydecimal(left_digits=6, right_digits=2),
                    'valorBaseTributo': faker.pydecimal(left_digits=4, right_digits=2),
                    'valorPrincipalAberto': faker.numerify(text='#.##'),
                    'situacao': faker.random_element(
                        elements=[
                            'ABERTO',
                            'PARCIAL',
                            'PENDENTE',
                            'CEDIDO',
                            'LIQUIDADO',
                        ]
                    ),
                    'agencia': faker.numerify('####'),
                    'banco': faker.random_element(['Bradesco', 'Itaú', 'Santander', 'Caixa']),
                    'conta': faker.numerify('########-X'),
                    'digito': str(random.randint(0, 9)),
                    'numeroNossoNumero': faker.numerify('#########-X'),
                    'nossoNumero': faker.numerify('#########'),
                    'digitoNossoNumero': str(random.randint(0, 9)),
                    'numeroDocumento': faker.numerify('#########'),
                    'notaFiscal': faker.numerify('####/####'),
                    'cobrador': faker.company(),
                    'cliente': faker.name(),
                    'acordo': faker.boolean(),
                    'bloqueio': faker.boolean(),
                    'promessa': faker.boolean(),
                    'tipoAcordo': faker.random_element(['Renegociação', 'Parcelamento', 'Quitação'])
                }
            ],
            'production_date': faker.date_this_year(),
        }
        data['contrato'].append(criar_Contrato_faker)

    jsonl_data(data=data)

    return data


num_records = 10
generated_data = Datagen_pfs_risco_raw_tivea(num_records)
