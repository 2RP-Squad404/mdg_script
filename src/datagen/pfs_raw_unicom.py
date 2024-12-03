from faker import Faker
from jsonl_convert import input_num_linhas, jsonl_data


faker = Faker('pt_BR')


def datagen_funcionarios(num_records):
    
    dados = {'funcionarios': []}
    for _ in range(num_records):
        criar_funcionarios = {
            'num_chapa': faker.random_int(min=1000, max=9999),
            'func_type': faker.random_element(elements=['CLT', 'PJ']),
            'nom_funcionario': faker.name(),
            'dat_ult_atu': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'nom_user_atu': faker.user_name(),
            'cod_estabelecimento': faker.random_int(min=1, max=100),
            'cod_depto': faker.random_int(min=1, max=100),
            'cod_secao': faker.random_int(min=1, max=100),
            'cod_cargo': faker.random_int(min=1, max=100),
            'flg_situacao': faker.random_element(
                elements=['Ativo', 'Inativo']
            ),
            'num_cpf': faker.cpf(),
            'num_rg': faker.bothify(text='??########'),
            'dat_admissao': faker.date_between(
                start_date='-20y', end_date='today'
            ).strftime('%Y-%m-%d %H:%M:%S'),
            'dat_demissao': faker.date_between(
                start_date='today', end_date='+1y'
            ).strftime('%Y-%m-%d %H:%M:%S'),
            'dat_inic_afastamento': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'dat_term_afastamento': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'des_depto': faker.word(),
            'des_cargo': faker.job(),
            'email': faker.email(),
            'flg_ponto': faker.random_element(elements=['Sim', 'Nao']),
            'flg_acesso': faker.random_element(elements=['Sim', 'Nao']),
            'cod_uniorg': faker.bothify(text='??####'),
        }
        dados['funcionarios'].append(criar_funcionarios)

    jsonl_data(data=dados)

    return dados

num_records = input_num_linhas()
datagen_funcionarios(num_records)
