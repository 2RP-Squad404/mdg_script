import random
from datetime import date

from faker import Faker
from models import Account, Card, Person

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


def generate_card():
    account = random.sample(accounts, 1)[0]

    card = Card(
        card_id=fake.unique.random_int(min=1, max=5002, step=1),
        card_number=fake.credit_card_number(),
        account_id=account.account_id,
        status_id=fake.random_int(min=0, max=10),
        limit=fake.random_number(digits=3),
        expiration_date=fake.credit_card_expire()
    )

    return card


cards = [generate_card() for _ in range(3500)]


for _ in range(10):
    person = random.sample(persons, 1)[0]
    print(person.model_dump_json())
    account = random.sample(accounts, 1)[0]
    print(account.model_dump_json())
    card = random.sample(cards, 1)[0]
    print(card.model_dump_json())
    print("\n")
