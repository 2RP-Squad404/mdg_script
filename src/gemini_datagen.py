from faker import Faker
import pytz
import itertools

fake = Faker('pt_BR')
id_serial = itertools.count(start=0)
    
# Função gerada por GenIA:

# def criar_adesao_debito_automatico():
#     fake = Faker('pt_BR')
#     return {
#         "hash_key": fake.uuid4(),
#         "source": fake.word() --!!--,
#         "id": fake.random_int() --!!--,
#         "dataadesao": fake.date_time_this_year(),
#         "id_contadigital": fake.random_int(),
#         "id_contacredito": fake.random_int(),
#         "id_tipodebitoautomatico": fake.random_int(),
#         "descricaotipodebitoautomatico": fake.sentence() --!!--,
#         "responsavel": fake.name(),
#         "datacancelamento": fake.date_time_this_year(),
#         "responsavelcancelamento": fake.name(),
#         "dh_relatorio": fake.date_time_this_year(),
#         "operation": fake.word() --!!--,
#         "operation_sequence": fake.random_int(),
#         "production_date": fake.date_this_year()
#     }


# Função ajustada:

def criar_adesao_debito_automatico():
    fake = Faker('pt_BR')
    return {
        "hash_key": fake.uuid4(),
        "source": fake.random_element(elements=['FATURAMENTO', 'BANCO']),
        "id": next(id_serial),
        "dataadesao": fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S'),
        "id_contadigital": next(id_serial),
        "id_contacredito": next(id_serial),
        "id_tipodebitoautomatico": next(id_serial),
        "descricaotipodebitoautomatico": fake.random_element(elements=['Fatura Cartão de Crédito Múltiplo', 'Fatura Cartão de Crédito']),
        "responsavel": fake.random_element(elements=['app', 'Realização Grade de Produto']),
        "datacancelamento": fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S'),
        "responsavelcancelamento": fake.random_element(elements=['app', 'null', 'Realização Grade de Produto']),
        "dh_relatorio": fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S'),
        "operation": fake.random_element(elements=['INSERT', 'A_UPDATE']),
        "operation_sequence": next(id_serial),
        "production_date": fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')
    }


# print(json.dumps(criar_adesao_debito_automatico(fake), default=str))```python


