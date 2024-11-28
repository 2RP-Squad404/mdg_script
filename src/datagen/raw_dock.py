from faker import Faker
from datetime import date, datetime
from pydantic import BaseModel

from jsonl_convert import input_num_linhas, jsonl_data

fake = Faker()
def criar_properties():
        return {
            'cmd_seq': fake.random_int(),
            'dt_capture': fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dt_publish': fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dt_sync': fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dt_transaction': fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'issuer_id': fake.random_int(),
            'issuer_name': fake.company(),
            'operation': fake.word(),
        }

def function_raw_dock(num_records):
    data = {'debit_account': [],'debit_person':[]}
    for _ in range(num_records):
        criar_product = {
            'issuer_account_number': fake.pystr(min_chars=10, max_chars=10),
            'issuer_bank_number': fake.random_int(min=1000, max=9999),
            'issuer_branch_number': fake.pystr(min_chars=10, max_chars=10),
            'product_id': fake.random_int(),
            'product_type': fake.word(),
            'produto_description': fake.paragraph(),
        }

        criar_debit_account = {
            'next_due_date': fake.date_object().strftime('%Y-%m-%d'),
            'delivery_address': fake.address(),
            'product': criar_product,
            'status_description': fake.word(),
            'account_id': fake.random_int(),
            'due_day': fake.random_int(min=1, max=31),
            'status_id': fake.random_int(),
            'next_real_due_date': fake.date_object().strftime('%Y-%m-%d'),
            'create_date': fake.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'properties': criar_properties(),
            'person_id': fake.random_int(),
            'production_date': fake.date(),
        }
        data['debit_account'].append(criar_debit_account)

        criar_debit_person = {
            'bank_account': fake.pystr(min_chars=10, max_chars=10),
            'bank_agency': fake.pystr(min_chars=10, max_chars=10),
            'bank_code': fake.random_int(min=1000, max=9999),
            'birth_date': fake.date_object().strftime('%Y-%m-%d'),
            'birth_place': fake.city(),
            'document_id': fake.ssn(),
            'document_issuer': fake.word(),
            'email': fake.email(),
            'father': fake.name(),
            'gender': fake.random_element(elements=('Male', 'Female')),
            'graduation_degree': fake.word(),
            'mother': fake.name(),
            'name': fake.name(),
            'nationality': fake.country(),
            'occupation': fake.job(),
            'person_id': fake.random_int(),
            'person_type': fake.random_element(elements=('Fisica', 'Juridica')),
            'politically_exposed': fake.boolean(),
            'properties': criar_properties(),
            'salary': fake.random_int(min=1000, max=100000),
            'spouse_name': fake.name(),
            'spouse_salary': fake.random_int(min=1000, max=100000),
            'tax_identification_number': fake.ssn(),
            'production_date': fake.date(),
        }
        data['debit_person'].append(criar_debit_person)

    jsonl_data(data=data)
    return data

num_records = input_num_linhas()
function_raw_dock(num_records)


