from google.cloud import bigquery

# Dataset: pfs_raw_credit, Table: adesoes_pfin
adesoes_pfin = [
    bigquery.SchemaField('NUM_SEQ_ADESAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_PRODUTO_FINANCEIRO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('PFIN_DAT_INI_VIGENCIA', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('COD_TIPO_ADESAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_ADESAO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DAT_INI_VIGENCIA', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('VAL_ADESAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_ULT_ATU', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('NOM_USER_ATU', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NUM_ADESAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_CERTIFICADO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DAT_FIM_VIGENCIA', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('VAL_REPASSE', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_CHAPA_ADESAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_COM_GERENTE', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_COM_VENDEDOR', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('QTD_PARCELAS', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_PARCELA', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_PRIM_VENCTO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DAT_PRIM_PAGTO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('COD_DOCUMENTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_DOCUMENTO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('COD_ESTAB_ADESAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_ESTAB_VENDA', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_ESTAB_ATRIB', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_TIPO_CANCELAMENTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_CANCELAMENTO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('COD_ESTAB_CANCEL', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_CHAPA_CANCEL', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_PFJ_ADESAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_PFJ_TIT', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_CARTAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_CONTRATO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_TAX_FINANCIAMENTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_PLANO_FINANCIAMENTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('TIP_VENDA_FINANCIADA', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('COD_ARTIGO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_COR', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('COD_TAMANHO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('COD_SORTIMENTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_TRIB_RECOLHIDO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_TRIB_RETIDO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_DEVOLUCAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_DEV_PERDAS', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_DEV_CLIENTE', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_DEV_CLIENTE', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('VAL_IOF', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_ISS', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_IRRF', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_SEQ_MOVTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_PDV', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_NSU_AUTORIZADOR', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_CANAL_VENDA', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_NOTA', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NUM_SERIE', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NUM_ITEM', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DES_MARCA', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DES_PRODUTO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NUM_PEDIDO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DAT_PEDIDO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DAT_APROVACAO_PEDIDO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('COD_CORPORACAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('SK_CONTRATO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_ENVIO_ADMIN', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DAT_ENVIO_CANCEL', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DAT_NASCTO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('NOM_CLIENTE', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('VAL_RENDA', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('SGL_SEXO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DES_LOGRADOURO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NUM_LOGRADOURO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DES_COMPL_LOGRADOURO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('COD_CEP', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NOM_BAIRRO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NOM_MUNICIPIO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('SGL_ESTADO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('COD_DDD_RES', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_FONE_RES', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_DDD_COM', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_FONE_COM', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_DDD_CEL', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_FONE_CEL', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DES_EMAIL', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NUM_SEQ_ITEM_ENVIO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_SEQ_ITEM_RECEB', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DES_OBSERVACAO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('COD_MOTIVO_CANCEL', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_SEQ_CCPF', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_TIPO_LOGRADOURO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('VAL_COMISSAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_DEV_REPASSE', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_BILHETE', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NUM_CONTRATO_PFIN', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_CALC_COB_DANO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_CALC_COB_ROUBO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_CALC_FRANQUIA', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('ID_VAL_GRP_FX', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_VENDA_ARTIGO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_COMERCIAL_ARTIGO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('TIP_DOC_FISCAL', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_DOC_FISCAL', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_ITEM_DOC_FISCAL', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_NIVEL_ARTIGO', 'STRING', 'NULLABLE')
]

# Dataset: pfs_raw_credit, Table: faturas_pfin
faturas_pfin = [
    bigquery.SchemaField('NUM_SEQ_ADESAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('PFIN_DAT_INI_VIGENCIA', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('COD_PRODUTO_FINANCEIRO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_VENCTO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('COD_TIPO_FATURA', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_FATURA', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_FATURA', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_ULT_ATU', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('NOM_USER_ATU', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DAT_PAGTO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('VAL_FATURA_PAGTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('VAL_CUSTO_EXTRATO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_LOTE', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('NUM_LOTE', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_ESTAB_LOTE', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('TIPO_LOTE_RECEBIMENTO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DAT_BONIFICACAO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DAT_GERACAO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('NOM_USER_GERACAO_FATURA', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DAT_ENVIO_ADMIN', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DAT_ENVIO_DB_BAND', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DAT_ENVIO_CR_BAND', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('NUM_BORDERO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_GRUPO_ECONOMICO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('TIP_NEGOCIACAO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_ANO_MES', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('NUM_BORDERO_CNC', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_GRUPO_ECONOMICO_CNC', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('TIP_NEGOCIACAO_CNC', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_ANO_MES_CNC', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('NUM_SEQ_ITEM_ENVIO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('NUM_SEQ_ITEM_RECEB', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_PROCES_EXTRATO', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DAT_BAIXA_FATURA', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('FLG_RECEBE_FATURA', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('NUM_SEQ_LOTE_RECEBIMENTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_ENVIO_DB_ROT', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DAT_ENVIO_CR_ROT', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('COD_PROCESSADORA', 'NUMERIC', 'NULLABLE')
]

# Dataset: pfs_raw_credit, Table: garantias_seguros
garantias_seguros = [
    bigquery.SchemaField('num_pfj', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_documento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_venda_garantia', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('des_endereco', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_complemento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_bairro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_municipio', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('sgl_estado', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_cep', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_ddd', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_telefone', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_ult_atu', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('cod_estabelecimento', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_documento', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_garantia', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_seguradora', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_tipo_garantia', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('qtd_meses_garantia', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('val_garantia_venda', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('dat_garantia_fabric', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_cancelamento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_movimento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('cod_estab_cancel', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_canal_venda', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_observacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_artigo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_cor', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_tamanho', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_sortimento', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('val_venda_artigo', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('des_produto', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_marca', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_chapa_vendedor', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_chapa_atu', 'INTEGER', 'NULLABLE')
]

# Dataset: pfs_raw_credit, Table: motivos_cancelamentos
motivos_cancelamentos = [
    bigquery.SchemaField('COD_MOTIVO_CANCEL', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DESC_MOTIVO_CANCEL', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('COD_CANCELAMENTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_INI_VIGENCIA', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DAT_FIM_VIGENCIA', 'TIMESTAMP', 'NULLABLE')
]

# Dataset: pfs_raw_credit, Table: produtos_financeiros
produtos_financeiros = [
    bigquery.SchemaField('COD_PRODUTO_FINANCEIRO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DAT_INI_VIGENCIA', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('DES_PRODUTO_FINANCEIRO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DAT_ULT_ATU', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('NOM_USER_ATU', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DAT_FIM_VIGENCIA', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('COD_INTERFACE', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('IND_PRIORIDADE_PAGTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_TIPO_PRODUTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_ADMIN_PFIN', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('COD_ADMIN_PFIN_TERC', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DES_PFIN_PDV', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DES_PFIN_EXTRATO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('DES_PRODUTO_FINANCEIRO_SUSEP', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('COD_SEGURO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('FLG_IND_DESCONTO', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('SEQ_OFERTA_PDV', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('FLG_IND_GRUPO', 'STRING', 'NULLABLE')
]

# Dataset: pfs_raw_credit, Table: tipos_canais
tipos_canais = [
    bigquery.SchemaField('COD_CANAL', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DES_CANAL', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('FLG_COMMIT_AUTORIZADOR', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('FLG_BANDEIRADO', 'STRING', 'NULLABLE')
]

# Dataset: pfs_raw_credit, Table: tipos_cancelamentos
tipos_cancelamentos = [
    bigquery.SchemaField('COD_CANCELAMENTO', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('DES_CANCELAMENTO', 'STRING', 'NULLABLE')
]