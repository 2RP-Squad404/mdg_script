# Este arquivo estabelece a comunicação com o Gemini IA do GCP
from google.cloud import aiplatform

project_id = "big-maxim-430019-g7"
location = "us-central1"  
model_id = "gemini-1.5-flash-002"  

aiplatform.init(project=project_id, location=location)

def send_prompt(prompt):
    model = aiplatform.TextGenerationModel.from_pretrained(model_id)
    response = model.predict(prompt)
    return response


contexto = "contexto"

prompt = f"""Implemente uma função em python semelhante a funçao abaixo:
def generate_cardevent():
    card_event = CardEvent(
        id_cartao=fake.uuid4(),
        id_produto_cartao=fake.uuid4(),
        num_cartao=fake.credit_card_number(card_type="mastercard"),
        num_seq_via_cartao=str(random.randint(1, 10)),
        id_conta=str(random.randint(10000000, 99999999)),
        num_cpf_cliente=fake.ssn(),
        cod_tip_portador=str(random.randint(1, 5)),
        num_bin=fake.credit_card_number()[:6],
        cod_loja_emis_cartao=str(random.randint(1000, 9999)),
        id_cliente_so=str(random.randint(10000000, 99999999)),
        dth_emis_cartao=str(fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')),  # timestamp fied
        dth_embs_cartao=str(fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')),  # timestamp fied
        cod_sit_cartao=str(random.randint(1, 5)),
        des_sit_cartao=random.choice(["ATIVO", "BLOQUEADO", "CANCELADO"]),
        dth_sit_cartao=str(fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')),  # timestamp field
        cod_estagio_cartao=str(random.randint(1, 5)),
        des_estagio_cartao=random.choice(["ENCAMINHADO", "FINALIZADO"]),
        dth_estagio_cartao=str(fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')),  # timestamp field
        flg_embs_loja=random.choice(["S", "N"]),
        flg_conta_cancelada=random.choice(["S", "N"]),
        dth_ult_atu_so=str(fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')),  # timestamp field
        ca_flaggeracartasenha=str(random.randint(0, 1)),
        pt_id_imagem=fake.uuid4()
    )
    card_event_dict = card_event.__dict__

    return card_event_dict

porém preciso que seja para esta classe: 

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
"""

response = send_prompt(prompt)

print(response.text)


