from google.cloud import bigquery

# Dataset: pfs_unificacao_cliente, Table: cliente_complemento
cliente_complemento = [
    bigquery.SchemaField('id_cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tip_pessoa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_cnpj_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_nacionalidade', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_nacionalidade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_naturalidade_cidade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_naturalidade_estado', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_pessoa_politicamente_exposta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_deficiente_visual', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('val_outra_renda_cliente', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('nom_pai_cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_rg', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_emissao_rg', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('cod_orgao_expedicao_rg', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_estado_emissao_rg', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_cnh', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_validade_cnh', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('num_seguranca_cnh', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_validacao_cnh', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_emissao_cnh', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('val_patrimonio_total', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('cod_profissao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_profissao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tip_origem_principal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_ult_atu_so', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao_reg', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('cod_nacionalidade_iso', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_nacionalidade_iso', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_profissao_isco08', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_profissao_isco08', 'STRING', 'NULLABLE'),
]


# Dataset: pfs_unificacao_cliente, Table: cliente_item_perfil
cliente_item_perfil = [
    bigquery.SchemaField('id_cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_primeiro_evento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_ultimo_evento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_ult_atu_cli', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('tip_origem', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_cliente_so', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('flg_evento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_evento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('qtd_evento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('val_evento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_item_perfil', 'INTEGER', 'NULLABLE'),
]


# Dataset: pfs_unificacao_cliente, Table: de_para_num_pfj_id_cdt_cpf
de_para_num_pfj_id_cdt_cpf = [
    bigquery.SchemaField('num_pfj', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cpf', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_pessoa_cdt', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('tip_origem_cdt', 'STRING', 'NULLABLE'),
]
