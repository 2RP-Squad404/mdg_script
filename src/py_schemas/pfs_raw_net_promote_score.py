from google.cloud import bigquery

cliente_iteracoes_nps = [
    bigquery.SchemaField('NUM_SEQ_ITERACAO', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('NUM_SEQ_PESQUISA', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('ID_TIPO_ITERACAO', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('DAT_ITERACAO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('TIP_ITERACAO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DES_RESPOSTA', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('VAL_SCORE', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('ID_REGISTRO_WHATSAPP', 'INTEGER', 'NULLABLE'),
]
from google.cloud import bigquery

cliente_nota_nps = [
    bigquery.SchemaField('NUM_SEQ_NOTA', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('NUM_SEQ_ITERACAO', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('VAL_NOTA', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('DAT_NOTA', 'TIMESTAMP', 'NULLABLE'),
]
from google.cloud import bigquery

cliente_pesquisa_nps = [
    bigquery.SchemaField('NUM_SEQ_PESQUISA', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('ID_PESQUISA', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('NUM_CPF', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('COD_ESTABELECIMENTO', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('DES_EMAIL', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NUM_CELULAR', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('DAT_CRIACAO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DAT_FINALIZACAO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('FLG_STATUS', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NUM_REGISTRO_EVENTO', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('FLG_PRIM_ITERACAO', 'STRING', 'NULLABLE'),
]
