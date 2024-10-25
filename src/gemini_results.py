
"""
from datetime import datetime, timedelta, date
from faker import Faker
from pydantic import BaseModel, ValidationError
import random

fake = Faker('pt_BR')

class Adesao_debito_automatico(BaseModel):
    hash_key: str
    source: str
    id: int
    dataadesao: datetime
    id_contadigital: int
    id_contacredito: int
    id_tipodebitoautomatico: int
    descricaotipodebitoautomatico: str
    responsavel: str
    datacancelamento: datetime
    responsavelcancelamento: str
    dh_relatorio: datetime
    operation: str
    operation_sequence: int
    production_date: date


def criar_adesao_debito_automatico() -> dict:
    Cria um objeto Adesao_debito_automatico com dados Faker e retorna como dicionário.

    try:
        data_adesao = fake.date_between(start_date='-2y', end_date='today')
        data_cancelamento = fake.date_between(start_date=data_adesao, end_date=data_adesao + timedelta(days=365))

        adesao = Adesao_debito_automatico(
            hash_key=fake.hexify(text='32'),
            source=fake.word(),
            id=fake.random_int(min=1, max=1000),
            dataadesao=datetime(data_adesao.year, data_adesao.month, data_adesao.day),
            id_contadigital=fake.random_int(min=1, max=1000),
            id_contacredito=fake.random_int(min=1, max=1000),
            id_tipodebitoautomatico=random.choice([1, 2, 3]),  # Assinatura, Cartão, Boleto
            descricaotipodebitoautomatico=fake.sentence(nb_words=5),
            responsavel=fake.name(),
            datacancelamento=datetime(data_cancelamento.year, data_cancelamento.month, data_cancelamento.day),
            responsavelcancelamento=fake.name(),
            dh_relatorio=fake.date_time_this_year(),
            operation=fake.word(),
            operation_sequence=fake.random_int(min=1, max=1000),
            production_date=date.today()
        )
        return adesao.model_dump()

    except ValidationError as e:
        print(f"Erro na validação do modelo Pydantic: {e}")
        return {}


#Exemplo de uso
adesao_dict = criar_adesao_debito_automatico()
print(adesao_dict)
"""