from google.cloud import bigquery

# Dataset: raw_dock, Table: debit_account
debit_account = [
    bigquery.SchemaField('next_due_date', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('delivery_address', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('product', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('issuer_account_number', 'STRING', 'NULLABLE'), bigquery.SchemaField('issuer_bank_number', 'INTEGER', 'NULLABLE'), bigquery.SchemaField('issuer_branch_number', 'STRING', 'NULLABLE'), bigquery.SchemaField('product_id', 'INTEGER', 'NULLABLE'), bigquery.SchemaField('product_type', 'STRING', 'NULLABLE'), bigquery.SchemaField('produto_description', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('status_description', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('account_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('due_day', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('status_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('next_real_due_date', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('create_date', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('properties', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('cmd_seq', 'INTEGER', 'NULLABLE'), bigquery.SchemaField('dt_capture', 'STRING', 'NULLABLE'), bigquery.SchemaField('dt_publish', 'STRING', 'NULLABLE'), bigquery.SchemaField('dt_sync', 'STRING', 'NULLABLE'), bigquery.SchemaField('dt_transaction', 'STRING', 'NULLABLE'), bigquery.SchemaField('issuer_id', 'INTEGER', 'NULLABLE'), bigquery.SchemaField('issuer_name', 'STRING', 'NULLABLE'), bigquery.SchemaField('operation', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('person_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
]


# Dataset: raw_dock, Table: debit_person
debit_person = [
<<<<<<< HEAD
    bigquery.SchemaField('bank_account', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('bank_agency', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('bank_code', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('birth_date', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('birth_place', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('document_id', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('document_issuer', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('email', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('father', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('gender', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('graduation_degree', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('mother', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('name', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nationality', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('occupation', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('person_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('person_type', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('politically_exposed', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('properties', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('cmd_seq', 'INTEGER', 'NULLABLE'), bigquery.SchemaField('dt_capture', 'STRING', 'NULLABLE'), bigquery.SchemaField('dt_publish', 'STRING', 'NULLABLE'), bigquery.SchemaField('dt_sync', 'STRING', 'NULLABLE'), bigquery.SchemaField('dt_transaction', 'STRING', 'NULLABLE'), bigquery.SchemaField('issuer_id', 'INTEGER', 'NULLABLE'), bigquery.SchemaField('issuer_name', 'STRING', 'NULLABLE'), bigquery.SchemaField('operation', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('salary', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('spouse_name', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('spouse_salary', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('tax_identification_number', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
=======
    bigquery.SchemaField('bank_account', 'STRING', 'NULLABLE', description='Conta bancária'),
    bigquery.SchemaField('bank_agency', 'STRING', 'NULLABLE', description='Agência bancária'),
    bigquery.SchemaField('bank_code', 'INTEGER', 'NULLABLE', description='Código do banco'),
    bigquery.SchemaField('birth_date', 'STRING', 'NULLABLE', description='Data de nascimento'),
    bigquery.SchemaField('birth_place', 'STRING', 'NULLABLE', description='Local de nascimento'),
    bigquery.SchemaField('document_id', 'STRING', 'NULLABLE', description='ID do documento'),
    bigquery.SchemaField('document_issuer', 'STRING', 'NULLABLE', description='Emissor do documento'),
    bigquery.SchemaField('email', 'STRING', 'NULLABLE', description='Email'),
    bigquery.SchemaField('father', 'STRING', 'NULLABLE', description='Nome do pai'),
    bigquery.SchemaField('gender', 'STRING', 'NULLABLE', description='Gênero'),
    bigquery.SchemaField('graduation_degree', 'STRING', 'NULLABLE', description='Grau de escolaridade'),
    bigquery.SchemaField('mother', 'STRING', 'NULLABLE', description='Nome da mãe'),
    bigquery.SchemaField('name', 'STRING', 'NULLABLE', description='Nome'),
    bigquery.SchemaField('nationality', 'STRING', 'NULLABLE', description='Nacionalidade'),
    bigquery.SchemaField('occupation', 'STRING', 'NULLABLE', description='Ocupação'),
    bigquery.SchemaField('person_id', 'INTEGER', 'NULLABLE', description='ID da pessoa'),
    bigquery.SchemaField('person_type', 'STRING', 'NULLABLE', description='Tipo de pessoa'),
    bigquery.SchemaField('politically_exposed', 'BOOLEAN', 'NULLABLE', description='Exposto politicamente'),

    bigquery.SchemaField('properties', 'RECORD', 'NULLABLE', description='Propriedades adicionais', fields=[
    bigquery.SchemaField('cmd_seq', 'INTEGER', 'NULLABLE', description='Sequência do comando'),
    bigquery.SchemaField('dt_capture', 'STRING', 'NULLABLE', description='Data de captura'),
    bigquery.SchemaField('dt_publish', 'STRING', 'NULLABLE', description='Data de publicação'),
    bigquery.SchemaField('dt_sync', 'STRING', 'NULLABLE', description='Data de sincronização'),
    bigquery.SchemaField('dt_transaction', 'STRING', 'NULLABLE', description='Data da transação'),
    bigquery.SchemaField('issuer_id', 'INTEGER', 'NULLABLE', description='ID do emissor'),
    bigquery.SchemaField('issuer_name', 'STRING', 'NULLABLE', description='Nome do emissor'),
    bigquery.SchemaField('operation', 'STRING', 'NULLABLE', description='Operação')]),

    bigquery.SchemaField('salary', 'FLOAT', 'NULLABLE', description='Salário'),
    bigquery.SchemaField('spouse_name', 'STRING', 'NULLABLE', description='Nome do cônjuge'),
    bigquery.SchemaField('spouse_salary', 'FLOAT', 'NULLABLE', description='Salário do cônjuge'),
    bigquery.SchemaField('tax_identification_number', 'STRING', 'NULLABLE', description='Número de identificação fiscal'),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE', description='Data de produção dos dados')
>>>>>>> a292a1809c41d2cb7f6eba509ea28d7807aea6f5
]
