
from faker import Faker
from datetime import datetime, date

faker = Faker('pt_BR')

def criar_transacao_corrente_faker():
    return {
        "hash_key": faker.uuid4(),
        "source": faker.random_number(digits=12),
        "tc_id_transacao": faker.random_int(),
        "tc_id_tipotransacao": faker.random_int(),
        "tc_id_emissor": faker.random_int(),
        "tc_id_produto": faker.random_int(),
        "tc_id_conta": faker.random_int(),
        "tc_portador": faker.random_int(),
        "tc_sequencialcartao": faker.random_int(),
        "tc_datavencimentoreal": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "tc_datavencimentopadrao": faker.date_this_year().strftime('%d/%m/%Y'),
        "tc_datageracao": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "tc_valor": faker.pyfloat(left_digits=2, right_digits=2, positive=True),
        "tc_historico": faker.sentence(),
        "tc_statuscontabil": faker.random_int(),
        "tc_statusgerencial": faker.random_int(),
        "tc_id_eventoexterno": faker.random_int(),
        "tc_dataorigem": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "tc_statusconta": faker.random_int(),
        "tc_faturado": faker.random_int(),
        "tc_id_estabelecimento": faker.random_int(),
        "tc_datafaturamento": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "tc_complemento": faker.sentence(),
        "tc_id_transacaoestorno": faker.random_int(),
        "tc_flagestornado": faker.random_int(),
        "tc_parcela": faker.random_int(),
        "tc_plano": faker.random_int(),
        "tc_id_estabelecimento_visa": faker.random_int(),
        "tc_id_planocredito": faker.random_int(),
        "tc_id_processoprocedure": faker.random_int(),
        "tc_datavencpadrao": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "tc_id_taxajurosapropriacao": faker.random_int(),
        "dh_relatorio": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "operation": faker.word(),
        "operation_sequence": faker.random_int(),
        "production_date": faker.date_this_year().strftime('%Y-%m-%d')
    }

def datagen_cliente(num_records):
    data = {'cliente': []}
    for _ in range(num_records):
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
            'codigoDne': faker.ean13(),
            'complemento': faker.street_suffix(),
            'logradouro': faker.street_address(),
            'bairro': faker.street_name(),
            'cidade': faker.city(),
            'numero': faker.building_number(),
            'tipo': faker.random_element(elements=('Residencial', 'Comercial')),
            'tipoLogradouro': faker.random_element(elements=('Rua', 'Avenida', 'Praça')),
            'uf': faker.state_abbr(),
            'principal': faker.boolean(),
            'ranking': faker.word(),
            'dataHoraModificacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        }

        criar_Telefones = {
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'idExterno': faker.uuid4(),
            'ddd': faker.random_number(digits=2, fix_len=True),
            'telefone': faker.phone_number(),
            'ramal': faker.random_number(digits=4, fix_len=True),
            'tipo': faker.random_element(elements=('Residencial', 'Comercial', 'Celular')),
            'observacao': faker.sentence(),
            'principal': faker.boolean(),
            'ranking': faker.word(),
            'dataHoraModificacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        }

        criar_Informacoesadicionais = {
            'nome': faker.word(),
            'linha': faker.random_number(digits=2, fix_len=True),
            'coluna': faker.random_number(digits=2, fix_len=True),
            'valor': faker.word(),
            'tipo': faker.word(),
            'tamanho': faker.random_number(digits=2, fix_len=True),
        }

        criar_Assessorias = {
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'nome': faker.company(),
            'situacao': faker.random_element(elements=('Ativo', 'Inativo')),
            'cic': faker.bothify(text='??########'),
            'cep': faker.postcode(),
            'complemento': faker.street_suffix(),
            'logradouro': faker.street_address(),
            'bairro': faker.street_name(),
            'cidade': faker.city(),
            'numero': faker.building_number(),
            'uf': faker.state_abbr(),
            'alterarInformacoesCadastrais': faker.boolean(),
        }

        criar_Marcadores = {
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'nome': faker.word(),
            'cor': faker.color_name(),
        }

        criar_cliente = {
            'source': faker.word(),
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'idExterno': faker.uuid4(),
            'tipoPessoa': faker.random_element(elements=('Física', 'Jurídica')),
            'situacao': faker.random_element(elements=('Ativo', 'Inativo')),
            'nome': faker.name(),
            'cic': faker.bothify(text='??########'),
            'codigo': faker.random_number(digits=10, fix_len=True),
            'sexo': faker.random_element(elements=('Masculino', 'Feminino')),
            'dataNascimento': faker.date_of_birth().strftime('%Y-%m-%d %H:%M:%S'),
            'dataConta': faker.date_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'naturalidade': faker.city(),
            'estadoCivil': faker.random_element(elements=('Solteiro', 'Casado', 'Divorciado', 'Viuvo')),
            'rg': faker.bothify(text='??########'),
            'rating': faker.random_number(digits=3, fix_len=True),
            'lp': faker.boolean(),
            'propensaoPagamento': faker.random_element(elements=('Alta', 'Media', 'Baixa')),
            'historicoPagamento': faker.paragraph(),
            'numeroDiasMaiorAtraso': faker.random_number(digits=3, fix_len=True),
            'dataMaiorAtraso': faker.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'rendaTitular': faker.random_number(digits=8, fix_len=True),
            'rendaConjuge': faker.random_number(digits=8, fix_len=True),
            'outrasRendas': faker.random_number(digits=8, fix_len=True),
            'profissao': faker.job(),
            'categoriaProfissao': faker.word(),
            'tipoResidencia': faker.random_element(elements=('Propria', 'Alugada', 'Cedida')),
            'saldoAtraso': faker.random_number(digits=8, fix_len=True),
            'saldoAtual': faker.random_number(digits=8, fix_len=True),
            'saldoContabil': faker.random_number(digits=8, fix_len=True),
            'saldoProvisao': faker.random_number(digits=8, fix_len=True),
            'diasAtraso': faker.random_number(digits=3, fix_len=True),
            'dataHoraModificacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'emails': criar_Emails,
            'enderecos': criar_Enderecos,
            'telefones': criar_Telefones,
            'informacoesAdicionais': criar_Informacoesadicionais,
            'assessorias': criar_Assessorias,
            'marcadores': criar_Marcadores,
            'production_date': faker.date_this_year(),
        }
        data['cliente'].append(criar_cliente)
    return data