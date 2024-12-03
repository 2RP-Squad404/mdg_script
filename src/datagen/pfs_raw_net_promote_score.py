from faker import Faker

from jsonl_convert import input_num_linhas, jsonl_data

faker = Faker('pt_BR')

def function_pfs_raw_net_promote_score(num_records):
    data = {'cliente_iteracoes_nps': [], 'cliente_nota_nps': [], 'cliente_pesquisa_nps': []}
    for _ in range(num_records):
        criar_cliente_iteracoes_nps = {
            'NUM_SEQ_ITERACAO': faker.random_int(),
            'NUM_SEQ_PESQUISA': faker.random_int(),
            'ID_TIPO_ITERACAO': faker.random_int(),
            'DAT_ITERACAO': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'TIP_ITERACAO': faker.word(),
            'DES_RESPOSTA': faker.paragraph(),
            'VAL_SCORE': faker.pyfloat(left_digits=7),
            'ID_REGISTRO_WHATSAPP': faker.random_int()
        }
        data['cliente_iteracoes_nps'].append(criar_cliente_iteracoes_nps)

        criar_cliente_nota_nps = {
            'NUM_SEQ_NOTA': faker.random_int(),
            'NUM_SEQ_ITERACAO': faker.random_int(),
            'VAL_NOTA': faker.pyfloat(left_digits=2),
            'DAT_NOTA': faker.date_time().strftime('%Y-%m-%d %H:%M:%S')
        }
        data['cliente_nota_nps'].append(criar_cliente_nota_nps)

        criar_cliente_pesquisa_nps = {
            'NUM_SEQ_PESQUISA': faker.random_int(),
            'ID_PESQUISA': faker.random_int(),
            'NUM_CPF': faker.bothify(text='###########'),
            'COD_ESTABELECIMENTO': faker.random_int(),
            'DES_EMAIL': faker.email(),
            'NUM_CELULAR': faker.random_number(digits=11, fix_len=True),
            'DAT_CRIACAO': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'DAT_FINALIZACAO': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'FLG_STATUS': faker.random_element(elements=('Ativo', 'Inativo')),
            'NUM_REGISTRO_EVENTO': faker.random_int(),
            'FLG_PRIM_ITERACAO': faker.random_element(elements=('Sim', 'Nao'))
        }
        data['cliente_pesquisa_nps'].append(criar_cliente_pesquisa_nps)
    jsonl_data(data=data)
    return data

num_records = input_num_linhas()
function_pfs_raw_net_promote_score(num_records)
