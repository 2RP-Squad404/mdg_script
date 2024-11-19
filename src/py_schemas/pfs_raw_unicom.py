from google.cloud import bigquery

# Dataset: pfs_raw_unicom, Table: funcionarios
funcionarios = [
    bigquery.SchemaField('num_chapa', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('func_type', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_funcionario', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_ult_atu', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('nom_user_atu', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_estabelecimento', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_depto', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_secao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_cargo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('flg_situacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_cpf', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_rg', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_admissao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_demissao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_inic_afastamento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_term_afastamento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('des_depto', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_cargo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('email', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_ponto', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_acesso', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_uniorg', 'STRING', 'NULLABLE')
]
