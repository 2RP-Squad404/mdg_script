from google.cloud import bigquery

# Dataset: pfs_raw_unicom, Table: funcionarios
funcionarios = [
    bigquery.SchemaField('num_chapa', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('func_type', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('nom_funcionario', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dat_ult_atu', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('nom_user_atu', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('cod_estabelecimento', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('cod_depto', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('cod_secao', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('cod_cargo', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('flg_situacao', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('num_cpf', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('num_rg', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dat_admissao', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dat_demissao', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dat_inic_afastamento', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dat_term_afastamento', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('des_depto', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('des_cargo', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('email', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('flg_ponto', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('flg_acesso', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('cod_uniorg', 'STRING', 'NULLABLE', description='None')
]