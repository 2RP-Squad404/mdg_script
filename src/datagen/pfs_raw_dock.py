from faker import Faker
from jsonl_convert import input_num_linhas, jsonl_data

faker = Faker()

def generate_properties():
    """Gera propriedades comuns para todos os registros."""
    return {
        'cmd_seq': faker.random_int(),
        'dt_capture': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        'dt_publish': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        'dt_transaction': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
        'issuer_id': faker.random_int(),
        'issuer_name': faker.word(),
        'operation': faker.word()
    }

def generate_product():
    """Gera os dados de produto para `v_debit_account`."""
    return {
        'product_id': faker.random_int(),
        'product_description': faker.word(),
        'product_type': faker.word(),
        'issuer_bank_number': faker.random_int(),
        'issuer_branch_number': faker.random_number(digits=5),
        'issuer_account_number': faker.iban()
    }

def function_pfs_raw_dock(num_records):
    data = {'v_credit_card': [],'v_credit_limit': [],'v_credit_person': [],'v_debit_account': [],'v_debit_person': []}

    for _ in range(num_records):
        properties = generate_properties()

        # v_credit_card
        v_credit_card = {
            'production_date': faker.date_this_year(),
            'card_id': faker.random_int(),
            'account_id': faker.random_int(),
            'person_id': faker.random_int(),
            'pan': faker.credit_card_number(),
            'bin': faker.random_int(),
            'name_on_card': faker.name(),
            'status_id': faker.random_int(),
            'status_description': faker.word(),
            'status_allow_approve': faker.boolean(),
            'expiration_date': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'issue_date': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'status_upd_date': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'stage_id': faker.random_int(),
            'stage_description': faker.word(),
            'embossing_date': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'embossing_file': faker.word(),
            'owner': faker.name(),
            'is_temporary_card': faker.boolean(),
            'card_sequence_number': faker.random_int(),
            'card_hash': faker.sha256(),
            'brand': faker.credit_card_provider(),
            'incorrect_password_attempts': faker.random_int(),
            'properties': properties
        }
        data['v_credit_card'].append(v_credit_card)

        # v_credit_limit
        v_credit_limit = {
            'production_date': faker.date_this_year(),
            'account_id': faker.random_int(),
            'credit_limit': faker.pyfloat(),
            'installment_limit': faker.pyfloat(),
            'tranche_limit': faker.pyfloat(),
            'withdrawal_limit': faker.pyfloat(),
            'international_purchase_limit': faker.pyfloat(),
            'international_withdrawal_limit': faker.pyfloat(),
            'maximum_limit': faker.pyfloat(),
            'available_balance': faker.pyfloat(),
            'installment_available_balance': faker.pyfloat(),
            'tranche_available_balance': faker.pyfloat(),
            'withdrawal_available_balance': faker.pyfloat(),
            'international_available_balance': faker.pyfloat(),
            'international_withdrawal_available': faker.pyfloat(),
            'available_point': faker.pyfloat(),
            'properties': properties
        }
        data['v_credit_limit'].append(v_credit_limit)

        # v_credit_person
        v_credit_person = {
            'production_date': faker.date_this_year(),
            'bank_account': faker.iban(),
            'bank_agency': faker.random_number(digits=5),
            'bank_code': faker.random_int(),
            'birth_date': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'birth_place': faker.city(),
            'document_id': faker.ssn(),
            'document_issuer': faker.word(),
            'email': faker.email(),
            'father': faker.name(),
            'gender': faker.random_element(elements=('Male', 'Female')),
            'graduation_degree': faker.word(),
            'marital_status': faker.word(),
            'mother': faker.name(),
            'name': faker.name(),
            'nationality': faker.word(),
            'occupation': faker.word(),
            'person_id': faker.random_int(),
            'person_type': faker.word(),
            'politically_exposed': faker.word(),
            'properties': properties,
            'salary': faker.pyfloat(),
            'spouse_name': faker.name(),
            'spouse_salary': faker.pyfloat(),
            'tax_identification_number': faker.ssn()
        }
        data['v_credit_person'].append(v_credit_person)

        # v_debit_account
        product = generate_product()
        v_debit_account = {
            'production_date': faker.date_this_year(),
            'account_id': faker.random_int(),
            'person_id': faker.random_int(),
            'status_id': faker.random_int(),
            'status_description': faker.word(),
            'create_date': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'due_day': faker.random_int(min=1, max=28),
            'status_date': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'delivery_address': faker.address(),
            'charge_date': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'properties': properties,
            'product': product
        }
        data['v_debit_account'].append(v_debit_account)

        # v_debit_person
        v_debit_person = {
            'production_date': faker.date_this_year(),
            'person_id': faker.random_int(),
            'person_type': faker.word(),
            'name': faker.name(),
            'tax_identification_number': faker.ssn(),
            'birth_date': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'gender': faker.random_element(elements=('Male', 'Female')),
            'document_id': faker.ssn(),
            'document_issuer': faker.word(),
            'mother': faker.name(),
            'father': faker.name(),
            'marital_status': faker.word(),
            'birth_place': faker.city(),
            'nationality': faker.word(),
            'salary': faker.pyfloat(),
            'spouse_name': faker.name(),
            'spouse_salary': faker.pyfloat(),
            'graduation_degree': faker.word(),
            'occupation': faker.word(),
            'bank_code': faker.random_int(),
            'bank_agency': faker.random_number(digits=5),
            'bank_account': faker.iban(),
            'email': faker.email(),
            'politically_exposed': faker.boolean(),
            'properties': properties
        }
        data['v_debit_person'].append(v_debit_person)

    jsonl_data(data=data)
    return data

num_records = input_num_linhas()
function_pfs_raw_dock(num_records)
