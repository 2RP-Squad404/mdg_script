import random

import pytz
from faker import Faker
from models import CardEvent

fake = Faker(['pt_BR'])


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
        dth_valid_cartao=str(fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')),  # timestamp fied
        dth_desbloqueio=str(fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')),  # timestamp field
        cod_sit_cartao=str(random.randint(1, 5)),
        des_sit_cartao=random.choice(["ATIVO", "BLOQUEADO", "CANCELADO"]),
        dth_sit_cartao=str(fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')),  # timestamp field
        cod_estagio_cartao=str(random.randint(1, 5)),
        des_estagio_cartao=random.choice(["ENCAMINHADO", "FINALIZADO"]),
        dth_estagio_cartao=str(fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')),  # timestamp field
        flg_embs_loja=random.choice(["S", "N"]),
        flg_cartao_cancelado=random.choice(["S", "N"]),
        flg_cartao_provisorio=random.choice(["S", "N"]),
        flg_conta_cancelada=random.choice(["S", "N"]),
        dth_ult_atu_so=str(fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')),  # timestamp field
        num_seq_ult_alteracao=str(random.randint(1, 100)),
        dth_inclusao_reg=str(fake.date_time_between(start_date='-30d', end_date='now', tzinfo=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')),  # timestamp field
        pt_nomeplastico=fake.name(),
        ca_arquivolote=fake.lexify(text="CPEM??????"),
        ca_id_imagem=fake.uuid4(),
        bc_responsavel=fake.lexify(text="[IRIS]_????"),
        ca_codigocancelamento=fake.uuid4(),
        ca_flaggeracartasenha=str(random.randint(0, 1)),
        pt_id_imagem=fake.uuid4()
    )
    card_event_dict = card_event.__dict__

    return card_event_dict
