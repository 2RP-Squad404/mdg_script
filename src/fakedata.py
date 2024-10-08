import random
from datetime import date

import pytz
from faker import Faker

from mdg_script.old_models import Account, CardEvent, Person

fake = Faker(['pt_BR'])


def generate_person():
    person = Person(
        person_id=fake.unique.random_int(min=1, max=5002, step=1),
        name=fake.unique.name(),
        email=fake.unique.email(),
        gender=fake.passport_gender(),
        birth_date=fake.date(
            end_datetime=date(day=1, month=1, year=2000)),
        address=fake.address(),
        salary=fake.random_number(digits=4),
        cpf=fake.cpf()
    )
    return person


persons = [generate_person() for _ in range(1000)]


fake.unique.clear()


def generate_account():
    person = random.sample(persons, 1)[0]

    account = Account(
        account_id=fake.unique.random_int(min=1, max=5002, step=1),
        status_id=fake.random_int(min=0, max=10),
        due_day=fake.random_int(min=1, max=30),
        person_id=person.person_id,
        balance=fake.random_number(digits=4),
        avaliable_balance=fake.random_number(digits=3)
    )
    return account


accounts = [generate_account() for _ in range(2000)]

fake.unique.clear()


# def generate_card():
#     account = random.sample(accounts, 1)[0]

#     card = Card(
#         card_id=fake.unique.random_int(min=1, max=5002, step=1),
#         card_number=fake.credit_card_number(),
#         account_id=account.account_id,
#         status_id=fake.random_int(min=0, max=10),
#         limit=fake.random_number(digits=3),
#         expiration_date=fake.credit_card_expire()
#     )

#     return card

def generate_card():
    account = random.sample(accounts, 1)[0]

    card_event = CardEvent(
        id_cartao=fake.uuid4(),
        id_produto_cartao=fake.uuid4(),
        num_cartao=fake.credit_card_number(card_type="mastercard"),
        num_seq_via_cartao=str(random.randint(1, 10)),
        id_conta=account.account_id,
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


cards = [generate_card() for _ in range(3500)]


# for _ in range(10):
#     person = random.sample(persons, 1)[0]
#     print(person.model_dump_json())
#     account = random.sample(accounts, 1)[0]
#     print(account.model_dump_json())
#     card = random.sample(cards, 1)[0]
#     print(card.model_dump_json())
#     print("\n")
