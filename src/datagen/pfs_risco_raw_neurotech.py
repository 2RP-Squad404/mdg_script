import random

from faker import Faker
from jsonl_convert import input_num_linhas, jsonl_data

faker = Faker('pt_BR')


def gerar_dados_propostas(num_records):
    dados = {'proposta_consultas': [], 'proposta': [], 'proposta_detalhe': []}

    for _ in range(num_records):
        proposta_consultas = {
            'hash_key': faker.uuid4(),
            'source': faker.url(),
            'codigooperacao': faker.random_number(digits=18, fix_len=True),
            'status': faker.random_number(digits=4, fix_len=True),
            'retornos': {'key1': faker.word(), 'key2': faker.sentence()},
            'datarealizacao': faker.date_time_this_year().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'dhfim': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'entradas': {'key1': faker.word(), 'key2': faker.sentence()},
            'id': faker.uuid4(),
            'nome': faker.word(),
            'idlog': faker.random_number(digits=18, fix_len=True),
            'origem': faker.word(),
            'dhinicio': faker.date_time_this_year().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'descricao': faker.sentence(),
            'instante_data': faker.date_time_this_year().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'production_date': faker.date_this_year().strftime('%Y-%m-%d'),
        }
        dados['proposta_consultas'].append(proposta_consultas)

        proposta = {
            'hash_key': faker.uuid4(),
            'source': faker.url(),
            'codigooperacao': faker.random_number(digits=18, fix_len=True),
            'codigoproposta': faker.random_number(digits=10, fix_len=True),
            'nomepolitica': faker.word(),
            'resultado': faker.random_element(
                elements=['APROVADO', 'REPROVADO']
            ),
            'instante_data': faker.date_time_this_year().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'mensagem': faker.sentence(),
            'sucesso': faker.random_element(elements=['S', 'N']),
            'versaopolitica': faker.word(),
            'dth_inclusao': faker.date_time_this_year().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'tempo_execucao_msec': faker.random_number(
                digits=5, fix_len=False
            ),
            'instantefim': faker.date_time_this_year().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'instanceinicio': faker.date_time_this_year().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'production_date': faker.date_this_year().strftime('%Y-%m-%d'),
        }
        dados['proposta'].append(proposta)

        proposta_detalhe = {
            'hash_key': faker.uuid4(),
            'source': faker.url(),
            'codigooperacao': faker.random_number(digits=18, fix_len=True),
            'entradas': {'key1': faker.word(), 'key2': faker.sentence()},
            'calculadas': {'key1': faker.word(), 'key2': faker.sentence()},
            'outros': {'key1': faker.word(), 'key2': faker.sentence()},
            'retornos': {'key1': faker.word(), 'key2': faker.sentence()},
            'variaveis': {'key1': faker.word(), 'key2': faker.sentence()},
            'fluxo_regras': {'key1': faker.word(), 'key2': faker.sentence()},
            'banco': {'key1': faker.word(), 'key2': faker.sentence()},
            'instante_data': faker.date_time_this_year().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'production_date': faker.date_this_year().strftime('%Y-%m-%d'),
        }
        dados['proposta_detalhe'].append(proposta_detalhe)

    jsonl_data(data=dados)
    return dados


num_records = input_num_linhas()
gerar_dados_propostas(num_records)
