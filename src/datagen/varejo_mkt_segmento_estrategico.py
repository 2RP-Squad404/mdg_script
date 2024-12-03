from faker import Faker

from jsonl_convert import input_num_linhas, jsonl_data

fake = Faker('pt_BR')

def function_varejo_mkt_segmento_estrategico(num_records):
    data = {'segmentacao_cliente': []}
    for _ in range(num_records):
        criar_segmentacao_cliente = {
            'data_processamento': fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'id_cliente': str(fake.random_number(digits=10, fix_len=True)),
            'num_cpf': fake.random_number(digits=11, fix_len=True),
            'ind_comprou_03m': fake.random_int(min=0, max=1),
            'ind_comprou_06m': fake.random_int(min=0, max=1),
            'ind_comprou_12m': fake.random_int(min=0, max=1),
            'ind_comprou_24m': fake.random_int(min=0, max=1),
            'qtd_compras_ult_24m': fake.random_int(min=0, max=100),
            'ticket_medio_ult_24m': str(fake.random_number(digits=6, fix_len=True)),
            'r': fake.random_int(min=1, max=5),
            'f': fake.random_int(min=1, max=5),
            'v': fake.random_int(min=1, max=5),
            'cod_segmento_rfv': fake.random_int(min=1, max=10),
            'segmento_rfv': fake.word(),
            'mes_processamento': fake.date_this_year().strftime('%Y-%m-%d')
        }
        data['segmentacao_cliente'].append(criar_segmentacao_cliente)

    jsonl_data(data=data)
    return data

num_records = input_num_linhas()
function_varejo_mkt_segmento_estrategico(num_records)


