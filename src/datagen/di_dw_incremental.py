
from faker import Faker
import random

from utils import input_num_linhas

faker = Faker('pt_BR')

def function_di_dw_funcionarios(num_registros):
    dados = {'dw_funcionario': []}
    for _ in range(num_registros):
        registro = {
            'sk_funcionario': faker.random_int(),
            'num_chapa_so': faker.random_int(),
            'nom_funcionario': faker.name(),
            'sk_local': faker.random_int(),
            'sk_cargo': faker.random_int(),
            'dat_dia_admissao': faker.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d %H:%M:%S'),
            'dat_dia_demissao': faker.date_between(start_date='today', end_date='+1y').strftime('%Y-%m-%d %H:%M:%S') if random.random() < 0.2 else None,
            'dat_dia_ini_afastamento': faker.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d %H:%M:%S') if random.random() < 0.1 else None,
            'dat_dia_fim_afastamento': faker.date_between(start_date='today', end_date='+1y').strftime('%Y-%m-%d %H:%M:%S') if random.random() < 0.1 else None,
            'des_email': faker.email(),
            'dat_inc_dw': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_ult_alt_dw': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_exc_dw': faker.date_time().strftime('%Y-%m-%d %H:%M:%S') if random.random() < 0.05 else None,
            'sk_situacao_funcionario': faker.random_int(),
            'num_cpf': faker.cpf(),
            'num_rg': faker.bothify(text='########-#')
        }
        dados['dw_funcionario'].append(registro)
    return dados

num_records = input_num_linhas()
function_dw_funcionarios(num_records)