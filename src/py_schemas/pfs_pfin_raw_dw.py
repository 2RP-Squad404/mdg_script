from google.cloud import bigquery

# Dataset: pfs_pfin_raw_dw, Table: dw_funcionario
dw_funcionario = [
    bigquery.SchemaField('sk_funcionario', 'INTEGER', 'NULLABLE', description='Chave Surrogate do funcionário'),
    bigquery.SchemaField('num_chapa_so', 'INTEGER', 'NULLABLE', description='Número da chapa do funcionário'),
    bigquery.SchemaField('nom_funcionario', 'STRING', 'NULLABLE', description='Nome do funcionário'),
    bigquery.SchemaField('sk_local', 'INTEGER', 'NULLABLE', description='Chave Surrogate do local de trabalho'),
    bigquery.SchemaField('sk_cargo', 'INTEGER', 'NULLABLE', description='Chave Surrogate do cargo do funcionário'),
    bigquery.SchemaField('dat_dia_admissao', 'TIMESTAMP', 'NULLABLE', description='Data de admissão do funcionário'),
    bigquery.SchemaField('dat_dia_demissao', 'TIMESTAMP', 'NULLABLE', description='Data de demissão do funcionário'),
    bigquery.SchemaField('dat_dia_ini_afastamento', 'TIMESTAMP', 'NULLABLE', description='Data de início do afastamento'),
    bigquery.SchemaField('dat_dia_fim_afastamento', 'TIMESTAMP', 'NULLABLE', description='Data de fim do afastamento'),
    bigquery.SchemaField('des_email', 'STRING', 'NULLABLE', description='Endereço de e-mail do funcionário'),
    bigquery.SchemaField('dat_inc_dw', 'TIMESTAMP', 'NULLABLE', description='Data de inclusão no Data Warehouse'),
    bigquery.SchemaField('dat_ult_alt_dw', 'TIMESTAMP', 'NULLABLE', description='Data da última atualização no Data Warehouse'),
    bigquery.SchemaField('dat_exc_dw', 'TIMESTAMP', 'NULLABLE', description='Data de excecução no Data Warehouse'),
    bigquery.SchemaField('sk_situacao_funcionario', 'INTEGER', 'NULLABLE', description='Chave Surrogate da situação do funcionário'),
    bigquery.SchemaField('num_cpf', 'STRING', 'NULLABLE', description='Número do CPF do funcionário'),
    bigquery.SchemaField('num_rg', 'STRING', 'NULLABLE', description='Número do RG do funcionário'),
]
