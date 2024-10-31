import json
import os

from faker import Faker

faker = Faker('pt_BR')

# As funções abaixo são responsáveis por criar dados mock para o dataset pfs_risco_raw_tivea
# observe que as funções correspondem a tabelas presentes no dataset.


def DataGen(num_records, output_dir="src/mock_data"):

    data = {'acordo': [], 'cliente': []}

    for _ in range(num_records):

        criar_Emails = {
                "id": str(str(faker.random_number(digits=19, fix_len=True))),
                "idExterno": faker.uuid4(),
                "email": faker.email(),
                "principal": faker.boolean(),
                "ranking": faker.word(),
                "dataHoraModificacao": faker.date_time().strftime('%Y-%m-%d %H:%M:%S')
            }

        criar_Enderecos = {
                "id": str(str(faker.random_number(digits=19, fix_len=True))),
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

        criar_Telefones = {
                "id": str(str(faker.random_number(digits=19, fix_len=True))),
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

        criar_Informacoesadicionais = {
                "id": str(faker.random_number(digits=19, fix_len=True)),
                "nome": faker.word(),
                "linha": faker.word(),
                "coluna": faker.word(),
                "valor": faker.word(),
                "tipo": faker.word(),
                "tamanho": faker.word(),
            }

        criar_Assessorias = {
                "id": str(str(faker.random_number(digits=19, fix_len=True))),
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

        criar_marcadores = {
                "id": str(str(faker.random_number(digits=19, fix_len=True))),
                "nome": faker .word(),
                "cor": faker .color_name()
            }

        criar_Cliente_faker = {
                "source": faker.word(),
                "id": str(str(faker.random_number(digits=19, fix_len=True))),
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
                "emails": criar_Emails,
                "enderecos": criar_Enderecos,
                "telefones": criar_Telefones,
                "informacoesAdicionais": criar_Informacoesadicionais,
                "assessorias": criar_Assessorias,
                "marcadores": criar_marcadores,
                "production_date": faker.date_time().strftime('%Y-%m-%d %H:%M:%S')
            }
        data['cliente'].append(criar_Cliente_faker)

        criar_Acordo_faker = {
                "source": faker.url(),
                "id": str(str(faker.random_number(digits=19, fix_len=True))),
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
                    "id": str(str(faker.random_number(digits=19, fix_len=True))),
                    "nome": faker.word(),
                    "descricao": faker.sentence(),
                    "situacao": faker.word(),
                    "tipo": faker.word(),
                    "gestao": faker.word(),
                    "cor": "#" + ''.join([faker.random_element(elements='0123456789abcdef') for _ in range(6)]),
                    "icone": faker.word(),
                    "tipoDesconto": faker.word(),
                    "modalidade": {
                        "id": str(str(faker.random_number(digits=19, fix_len=True))),
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
                "produto": {
                    "id": str(str(faker.random_number(digits=19, fix_len=True))),
                    "idExterno": faker.word(),
                    "nome": faker.word(),
                    "descricao": faker.sentence()
                },
                "tributo": {
                    "id": str(str(faker.random_number(digits=19, fix_len=True))),
                    "nome": faker.word(),
                    "percentual": str(faker.pyfloat(left_digits=2, right_digits=4)),
                    "percentualFixo": str(faker.pyfloat(left_digits=2, right_digits=4)),
                    "percentualMaximo": str(faker.pyfloat(left_digits=2, right_digits=4)),
                    "arredondamento": faker.word(),
                    "dataCalculo": faker.word()
                },
                "meioPagamento": {
                    "id": str(str(faker.random_number(digits=19, fix_len=True))),
                    "tipo": faker.word(),
                    "nome": faker.word(),
                    "cobrador": {
                        "id": str(str(faker.random_number(digits=19, fix_len=True))),
                        "nome": faker.word(),
                        "banco": faker.random_number(digits=3)
                    }
                },
                "usuario": {
                    "id": str(str(faker.random_number(digits=19, fix_len=True))),
                    "nome": faker.word()
                },
                "assessoria": {
                    "id": str(str(faker.random_number(digits=19, fix_len=True))),
                    "nome": faker.word()
                },
                "parcelas": [{
                    "id": str(str(faker.random_number(digits=19, fix_len=True))),
                    "acordo": str(str(faker.random_number(digits=19, fix_len=True))),
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
                "pagamentos": [],
                "origens": [],
                "pendencias": [],
                "production_date": faker.date_this_year().strftime('%Y-%m-%d %H:%M:%S')
            }
        data['acordo'].append(criar_Acordo_faker)

    # Obtendo o nome do dataset
    dataset_name = os.path.splitext(os.path.basename(__file__))[0]

    # Obtendo o caminho absoluto do diretório raiz do projeto
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    output_path = os.path.join(project_root, output_dir, dataset_name)

    os.makedirs(output_path, exist_ok=True)

    # Salvando os dados
    for array_name, array_data in data.items():
        filename = f"{array_name}.jsonl"
        filepath = os.path.join(output_path, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            for item in array_data:
                json.dump(item, f, ensure_ascii=False)
                f.write('\n')

    return data


num_records = 100
generated_data = DataGen(num_records)
