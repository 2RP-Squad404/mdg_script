from faker import Faker
from datetime import datetime, timedelta
import random
from pydantic import BaseModel # Assumindo que BaseModel é da biblioteca Pydantic

fake = Faker('pt_BR') # Define a localização para português do Brasil. Ajuste se necessário.

class Cliente_item_perfil(BaseModel):
    id_cliente: str
    dth_primeiro_evento: datetime
    dth_ultimo_evento: datetime
    dth_ult_atu_cli: datetime
    dth_inclusao: datetime
    tip_origem: str
    id_cliente_so: int
    flg_evento: str
    des_evento: str
    qtd_evento: str
    val_evento: str
    cod_item_perfil: int


def generate_cliente_item_perfil():
    # Datas aleatórias nos últimos 365 dias
    data_base = datetime.now() - timedelta(days=365)
    dth_primeiro_evento =fake .date_between(start_date=data_base, end_date='today')
    dth_ultimo_evento = fake.date_between(start_date=dth_primeiro_evento, end_date='today')
    dth_ult_atu_cli = fake.date_between(start_date=dth_ultimo_evento, end_date='today')
    dth_inclusao = fake.date_between(start_date=data_base, end_date='today')

    cliente_item = Cliente_item_perfil(
        id_cliente=fake.uuid4(),
        dth_primeiro_evento=dth_primeiro_evento,
        dth_ultimo_evento=dth_ultimo_evento,
        dth_ult_atu_cli=dth_ult_atu_cli,
        dth_inclusao=dth_inclusao,
        tip_origem=random.choice(["WEB", "APP", "TELEFONE"]),
        id_cliente_so=random.randint(10000000, 99999999),
        flg_evento=random.choice(["A", "I", "C"]), # Exemplo de flags, ajuste conforme necessário
        des_evento=fake.word(),
        qtd_evento=str(random.randint(1, 100)),
        val_evento=str(random.uniform(0, 1000)), # Valor aleatório entre 0 e 1000
        cod_item_perfil=random.randint(1, 10)
    )

    return cliente_item.dict() # Usa o método dict() do Pydantic para converter para dicionário

# Exemplo de uso:
print(generate_cliente_item_perfil())