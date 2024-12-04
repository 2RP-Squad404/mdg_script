from google.cloud import bigquery

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
    bigquery.SchemaField('cod_uniorg', 'STRING', 'NULLABLE', description='None'),
]
from google.cloud import bigquery

gerencia_geral_vendas = [
    bigquery.SchemaField('cod_regional', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_corporacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_ger_geral_venda_so', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_ger_geral_venda', 'STRING', 'NULLABLE'),
]
from google.cloud import bigquery

vendedores = [
    bigquery.SchemaField('COD_ESTABELECIMENTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_VENDEDOR', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NOM_VENDEDOR', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('STA_ATIVO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DAT_INCL', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('COD_CARGO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_ULT_ATU', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('NOM_USER_ATU', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NUM_CHAPA', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_VENDEDOR_CHEFE', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('COD_ESTABELECIMENTO_CHEFE', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_EXCL', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_inc', 'TIMESTAMP', 'NULLABLE'),
]
