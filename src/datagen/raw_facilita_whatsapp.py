from faker import Faker

from jsonl_convert import input_num_linhas, jsonl_data

fake = Faker('pt_BR')

def function_raw_facilita_whatsapp(num_records):
    data = {'revendedor': []}
    for _ in range(num_records):
        criar_revendedor = {
            'id_revendedor': fake.random_int(),
            'nome_revendedor': fake.company(),
            'cpf_cnpj_revendedor': fake.bothify(text='###########'),
            'telefone_revendedor': fake.phone_number(),
            'email_revendedor': fake.email(),
            'datahora_cadastro': fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'datahora_aceite': fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'cep': fake.postcode(),
            'cod_loja': fake.random_number(digits=5, fix_len=True),
            'dth_inc': fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'source': fake.word(),
            'production_date': fake.date_object().strftime('%Y-%m-%d')
        }
        data['revendedor'].append(criar_revendedor)
        
    jsonl_data(data=data)
    return data

num_records = input_num_linhas()
function_raw_facilita_whatsapp(num_records)


