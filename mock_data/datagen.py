import random
from datetime import date
from faker import Faker
from models import Account, BuyEvent, Card, CardEvent, Person, Mock_test

fake = Faker(['pt_BR'])


def generate_person():
    person = Person(
        person_id=fake.unique.random_int(min=1, max=1002, step=1),
        name=fake.unique.name(),
        email=fake.unique.email(),
        gender=fake.passport_gender(),
        birth_date=fake.date(
            end_datetime=date(day=1, month=1, year=2000)),
        address=fake.address(),
        salary=fake.random_number(digits=4),
        cpf=fake.cpf()
    )

    person_dict = person.__dict__

    return person_dict


def generate_account():
    account = Account(
        account_id=fake.unique.random_int(min=1, max=2002, step=1),
        status_id=fake.random_int(min=1, max=10),
        due_day=fake.random_int(min=1, max=30),
        person_id=fake.unique.random_int(min=1, max=1002, step=1),
        balance=fake.random_number(digits=4),
        available_balance=fake.random_number(digits=3)
    )

    account_dict = account.__dict__

    return account_dict


def generate_card():
    card = Card(
        card_id=fake.unique.random_int(min=1, max=4002, step=1),
        card_number=fake.credit_card_number(),
        account_id=fake.unique.random_int(min=1, max=2002, step=1),
        status_id=fake.random_int(min=0, max=10),
        limit=fake.random_number(digits=3),
        expiration_date=fake.credit_card_expire()
    )

    card_dict = card.__dict__

    return card_dict


def generate_buy():
    buy = BuyEvent(
        person_id=fake.unique.random_int(min=1, max=2002, step=1),
        name=fake.unique.name(),
        email=fake.unique.email(),
        address=fake.unique.address(),
        salary=fake.random_number(digits=4),
        cpf=fake.cpf(),
        card_id=fake.unique.random_int(min=1, max=2002, step=1),
        card_number=fake.credit_card_number(),
        account_id=fake.unique.random_int(min=1, max=2002, step=1),
        status_id=fake.random_int(min=0, max=10),
        limit=fake.random_number(digits=3),
        expiration_date=fake.credit_card_expire()
    )

    buy_dict = buy.__dict__

    return buy_dict


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
        dth_emis_cartao=fake.uuid4(),
        dth_embs_cartao=fake.uuid4(),
        dth_valid_cartao=fake.uuid4(),
        dth_desbloqueio=fake.uuid4(),
        cod_sit_cartao=str(random.randint(1, 5)),
        des_sit_cartao=random.choice(["ATIVO", "BLOQUEADO", "CANCELADO"]),
        dth_sit_cartao=fake.uuid4(),
        cod_estagio_cartao=str(random.randint(1, 5)),
        des_estagio_cartao=random.choice(["ENCAMINHADO", "FINALIZADO"]),
        dth_estagio_cartao=fake.uuid4(),
        flg_embs_loja=random.choice(["S", "N"]),
        flg_cartao_cancelado=random.choice(["S", "N"]),
        flg_cartao_provisorio=random.choice(["S", "N"]),
        flg_conta_cancelada=random.choice(["S", "N"]),
        dth_ult_atu_so=fake.uuid4(),
        num_seq_ult_alteracao=str(random.randint(1, 100)),
        dth_inclusao_reg=fake.uuid4(),
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

def generate_mock_data_test():
    mock_test = Mock_test(
        person_id = fake.unique.random_int(min=1, max=2002, step=1),
        name = fake.name()
    )
    
    mock_test_dict = mock_test.__dict__
    
    return mock_test_dict

mock_tests = [generate_mock_data_test() for i in range(10)]
print(mock_tests)


# def generate_event():
#     event_type = random.randint(1, 4)
#     if (event_type == 1):
#         event_data = generate_person()
#     elif (event_type == 2):
#         event_data = generate_card()
#     elif (event_type == 3):
#         event_data = generate_buy()
#     else:
#         event_data = generate_account()
#     return event_data

# print(generate_cardevent())
