from faker import Faker


from jsonl_convert import input_num_linhas, jsonl_data

faker = Faker('pt_BR')

def function_pfs_raw_pix(num_records):
    data = {'v_dict_direto': []}

    for _ in range(num_records):
        criar_account = {
            'branch': faker.word(),
            'accountNumber': faker.iban(),
            'accountType': faker.word(),
            'openingDate': faker.date_object().strftime('%Y-%m-%d')


        }

        criar_holder = {
            'name': faker.name(),
            'tradeName': faker.company(),
            'taxId': faker.bothify(text='########')
        }

        criar_key = {
            'id': str(faker.random_number(digits=10, fix_len=True)),
            'value': faker.uuid4(),
            'type': faker.word()
        }

        criar_newstatus = {
            'id': faker.random_int(),
            'description': faker.word()
        }

        criar_pfs_raw_pix = {
            'production_date': faker.date_this_year().strftime('%Y-%m-%d'),
            'account': criar_account,
            'clearingAcknowledgeTimestampUtc': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'clearingEndClaimTimestampUtc': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'confirmationToken': faker.uuid4(),
            'holder': criar_holder,
            'key': criar_key,
            'newStatus': criar_newstatus,
            'newStatusUtcTimestamp': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'reason': faker.paragraph()
        }
        data['v_dict_direto'].append(criar_pfs_raw_pix)

    jsonl_data(data=data)
    return data

num_records = input_num_linhas()
function_pfs_raw_pix(num_records)

