from google.cloud import bigquery

# Dataset: pfs_raw_dock, Table: v_credit_card
v_credit_card = [
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('card_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('account_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('person_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('pan', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('bin', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('name_on_card', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('status_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('status_description', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('status_allow_approve', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('expiration_date', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('issue_date', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('status_upd_date', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('stage_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('stage_description', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('embossing_date', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('embossing_file', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('owner', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('is_temporary_card', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('card_sequence_number', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('card_hash', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('brand', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('incorrect_password_attempts', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('properties', 'RECORD', 'NULLABLE')
]

# Dataset: pfs_raw_dock, Table: v_credit_limit
v_credit_limit = [
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('account_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('credit_limit', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('installment_limit', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('tranche_limit', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('withdrawal_limit', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('international_purchase_limit', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('international_withdrawal_limit', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('maximum_limit', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('available_balance', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('installment_available_balance', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('tranche_available_balance', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('withdrawal_available_balance', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('international_available_balance', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('international_withdrawal_available', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('available_point', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('properties', 'RECORD', 'NULLABLE')
]

# Dataset: pfs_raw_dock, Table: v_credit_person
v_credit_person = [
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('bank_account', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('bank_agency', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('bank_code', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('birth_date', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('birth_place', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('document_id', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('document_issuer', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('email', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('father', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('gender', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('graduation_degree', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('marital_status', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('mother', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('name', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nationality', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('occupation', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('person_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('person_type', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('politically_exposed', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('properties', 'RECORD', 'NULLABLE'),
    bigquery.SchemaField('salary', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('spouse_name', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('spouse_salary', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('tax_identification_number', 'STRING', 'NULLABLE')
]

# Dataset: pfs_raw_dock, Table: v_debit_account
v_debit_account = [
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('account_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('person_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('status_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('status_description', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('create_date', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('due_day', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('status_date', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('delivery_address', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('charge_date', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('properties', 'RECORD', 'NULLABLE'),
    bigquery.SchemaField('product', 'RECORD', 'NULLABLE')
]

# Dataset: pfs_raw_dock, Table: v_debit_person
v_debit_person = [
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('person_id', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('person_type', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('name', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tax_identification_number', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('birth_date', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('gender', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('document_id', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('document_issuer', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('mother', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('father', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('marital_status', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('birth_place', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nationality', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('salary', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('spouse_name', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('spouse_salary', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('graduation_degree', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('occupation', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('bank_code', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('bank_agency', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('bank_account', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('email', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('politically_exposed', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('properties', 'RECORD', 'NULLABLE')
]