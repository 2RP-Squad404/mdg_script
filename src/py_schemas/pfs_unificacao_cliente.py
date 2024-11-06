from google.cloud import bigquery

# Dataset: pfs_unificacao_cliente, Table: cliente_complemento
cliente_complemento = [
    bigquery.SchemaField('id_cliente', 'STRING', 'NULLABLE', description='ID do cliente.'),
    bigquery.SchemaField('tip_pessoa', 'STRING', 'NULLABLE', description='Tipo de pessoa (Física ou Jurídica).'),
    bigquery.SchemaField('num_cpf_cnpj_cliente', 'INTEGER', 'NULLABLE', description='CPF ou CNPJ do cliente.'),
    bigquery.SchemaField('cod_nacionalidade', 'INTEGER', 'NULLABLE', description='Código da nacionalidade do cliente.'),
    bigquery.SchemaField('des_nacionalidade', 'STRING', 'NULLABLE', description='Descrição da nacionalidade do cliente.'),
    bigquery.SchemaField('des_naturalidade_cidade', 'STRING', 'NULLABLE', description='Cidade de naturalidade do cliente.'),
    bigquery.SchemaField('cod_naturalidade_estado', 'STRING', 'NULLABLE', description='Código do estado de naturalidade do cliente.'),
    bigquery.SchemaField('flg_pessoa_politicamente_exposta', 'STRING', 'NULLABLE', description='Indicador se o cliente é pessoa politicamente exposta (S/N).'),
    bigquery.SchemaField('flg_deficiente_visual', 'STRING', 'NULLABLE', description='Indicador se o cliente é deficiente visual (S/N).'),
    bigquery.SchemaField('val_outra_renda_cliente', 'FLOAT', 'NULLABLE', description='Valor de outras rendas do cliente.'),
    bigquery.SchemaField('nom_pai_cliente', 'STRING', 'NULLABLE', description='Nome do pai do cliente.'),
    bigquery.SchemaField('num_rg', 'STRING', 'NULLABLE', description='Número do RG do cliente.'),
    bigquery.SchemaField('dat_emissao_rg', 'DATE', 'NULLABLE', description='Data de emissão do RG.'),
    bigquery.SchemaField('cod_orgao_expedicao_rg', 'STRING', 'NULLABLE', description='Código do órgão expedidor do RG.'),
    bigquery.SchemaField('cod_estado_emissao_rg', 'STRING', 'NULLABLE', description='Código do estado de emissão do RG.'),
    bigquery.SchemaField('num_cnh', 'STRING', 'NULLABLE', description='Número da CNH do cliente.'),
    bigquery.SchemaField('dat_validade_cnh', 'DATE', 'NULLABLE', description='Data de validade da CNH.'),
    bigquery.SchemaField('num_seguranca_cnh', 'STRING', 'NULLABLE', description='Número de segurança da CNH.'),
    bigquery.SchemaField('cod_validacao_cnh', 'STRING', 'NULLABLE', description='Código de validação da CNH.'),
    bigquery.SchemaField('dat_emissao_cnh', 'DATE', 'NULLABLE', description='Data de emissão da CNH.'),
    bigquery.SchemaField('val_patrimonio_total', 'FLOAT', 'NULLABLE', description='Valor total do patrimônio do cliente.'),
    bigquery.SchemaField('cod_profissao', 'INTEGER', 'NULLABLE', description='Código da profissão do cliente.'),
    bigquery.SchemaField('nom_profissao', 'STRING', 'NULLABLE', description='Nome da profissão do cliente.'),
    bigquery.SchemaField('tip_origem_principal', 'STRING', 'NULLABLE', description='Tipo de origem principal do cliente.'),
    bigquery.SchemaField('dth_ult_atu_so', 'TIMESTAMP', 'NULLABLE', description='Data e hora da última atualização no sistema.'),
    bigquery.SchemaField('dth_inclusao_reg', 'TIMESTAMP', 'NULLABLE', description='Data e hora de inclusão do registro.'),
    bigquery.SchemaField('cod_nacionalidade_iso', 'STRING', 'NULLABLE', description='Código ISO da nacionalidade.'),
    bigquery.SchemaField('des_nacionalidade_iso', 'STRING', 'NULLABLE', description='Descrição da nacionalidade (ISO).'),
    bigquery.SchemaField('cod_profissao_isco08', 'INTEGER', 'NULLABLE', description='Código da profissão (ISCO-08).'),
    bigquery.SchemaField('nom_profissao_isco08', 'STRING', 'NULLABLE', description='Nome da profissão (ISCO-08).')
]


# Dataset: pfs_unificacao_cliente, Table: cliente_item_perfil
cliente_item_perfil = [
    bigquery.SchemaField('id_cliente', 'STRING', 'NULLABLE', description='ID do cliente.'),
    bigquery.SchemaField('dth_primeiro_evento', 'TIMESTAMP', 'NULLABLE', description='Data e hora do primeiro evento.'),
    bigquery.SchemaField('dth_ultimo_evento', 'TIMESTAMP', 'NULLABLE', description='Data e hora do último evento.'),
    bigquery.SchemaField('dth_ult_atu_cli', 'TIMESTAMP', 'NULLABLE', description='Data e hora da última atualização do cliente.'),
    bigquery.SchemaField('dth_inclusao', 'TIMESTAMP', 'NULLABLE', description='Data e hora de inclusão do registro.'),
    bigquery.SchemaField('tip_origem', 'STRING', 'NULLABLE', description='Tipo de origem.'),
    bigquery.SchemaField('id_cliente_so', 'INTEGER', 'NULLABLE', description='ID do cliente no sistema.'),
    bigquery.SchemaField('flg_evento', 'STRING', 'NULLABLE', description='Flag do evento.'),
    bigquery.SchemaField('des_evento', 'STRING', 'NULLABLE', description='Descrição do evento.'),
    bigquery.SchemaField('qtd_evento', 'STRING', 'NULLABLE', description='Quantidade do evento.'),
    bigquery.SchemaField('val_evento', 'STRING', 'NULLABLE', description='Valor do evento.'),
    bigquery.SchemaField('cod_item_perfil', 'INTEGER', 'NULLABLE', description='Código do item do perfil.')
]


# Dataset: pfs_unificacao_cliente, Table: de_para_num_pfj_id_cdt_cpf
de_para_num_pfj_id_cdt_cpf = [
    bigquery.SchemaField('num_pfj', 'INTEGER', 'NULLABLE', description='Número de pessoa física ou jurídica.'),
    bigquery.SchemaField('num_cpf', 'INTEGER', 'NULLABLE', description='Número do CPF.'),
    bigquery.SchemaField('id_pessoa_cdt', 'INTEGER', 'NULLABLE', description='ID da pessoa no CDT.'),
    bigquery.SchemaField('tip_origem_cdt', 'STRING', 'NULLABLE', description='Tipo de origem do CDT.')
]
