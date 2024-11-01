from google.cloud import bigquery

# Dataset: pfs_risco_tivea, Table: cartao
cartao = [
    bigquery.SchemaField('id_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_produto_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cartao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_seq_via_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_tip_portador', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_bin', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_loja_emis_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_cliente_so', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_emis_cartao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_embs_cartao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_valid_cartao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_desbloqueio', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('cod_sit_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_sit_cartao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_sit_cartao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('cod_estagio_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_estagio_cartao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_estagio_cartao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('flg_embs_loja', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_cartao_cancelado', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_cartao_provisorio', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_conta_cancelada', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_ult_atu_so', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('num_seq_ult_alteracao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao_reg', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('num_anomes_emis_cartao', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobranca_acordo
cobranca_acordo = [
    bigquery.SchemaField('id_acordo_cobranca', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_cliente_externo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_cnpj_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_cobrador', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_cobrador', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tip_modalidade_acordo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_acordo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_parcelas', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_operacao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_emissao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_processamento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao_origem', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_alteracao_origem', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_vencimento', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('ind_situacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('val_taxa_operacao', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_principal', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_juros', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_atributo', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_total', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_desconto', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_principal', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_total', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_atual', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('qtd_dias_atraso', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_atraso_orig_acordo', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('id_acordo_usuario', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_acordo_usuario', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_acordo_assessoria', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_acordo_assessoria', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_acordo_negociacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_acordo_negociacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tip_acordo_meio_pagto', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobranca_assessoria
cobranca_assessoria = [
    bigquery.SchemaField('id_assessoria', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_assessoria', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_cliente_cobranca', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobranca_campo_customizavel
cobranca_campo_customizavel = [
    bigquery.SchemaField('id_cliente_cobranca', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_campo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('val_campo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobranca_cliente
cobranca_cliente = [
    bigquery.SchemaField('id_cliente_cobranca', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_cliente_externo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tip_pessoa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tip_situacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_cnpj_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_uf', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_rating', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_marcador', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_dias_maior_atraso', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_maior_atraso', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_atraso', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_atual', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_contabil', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_provisao', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('qtd_dias_atraso', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_total', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_total_atraso', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('dth_modificacao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('num_ddd_cel', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_tel_cel', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_ddd_res', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_tel_res', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_ddd_com', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_tel_com', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_email', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobranca_email_cliente
cobranca_email_cliente = [
    bigquery.SchemaField('id_cliente_cobranca', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_email', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobranca_endereco_cliente
cobranca_endereco_cliente = [
    bigquery.SchemaField('id_cliente_cobranca', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_cliente_externo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_endereco_cobranca', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('tip_endereco_princ', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('nom_logradouro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_logradouro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_complemento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_cep', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_bairro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_cidade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_uf', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('ind_tipo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobranca_liquidacao_parc_acordo
cobranca_liquidacao_parc_acordo = [
    bigquery.SchemaField('id_liqd_parc_acordo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_parcela_acordo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_parcela_acordo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('val_principal', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_total', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_juros', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_encargos', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_desconto', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_distorcao', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('ind_tipo_liqd', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_pagto_acordo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobranca_origem_acordo
cobranca_origem_acordo = [
    bigquery.SchemaField('id_origem_acordo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_acordo_cobranca', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_contrato', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_ordem_contrato', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_parcela', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_parcela', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_vencimento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('id_situacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('qtd_dias_atr_cont', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('val_principal', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_total', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_permanencia', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_multa', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_juros', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_tarifa', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_adicionado', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_atual', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_desconto', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_desc_principal', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_desc_juros', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_desc_multa', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_desc_permanencia', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_desconto_total', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobranca_pagamento_acordo
cobranca_pagamento_acordo = [
    bigquery.SchemaField('id_pagto_acordo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_acordo_cobranca', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_processamento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_liquidacao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_credito', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_cnab', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_operacao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_horainclusao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('ind_forma_liquidacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('val_recebido', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_desconto', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_encargos', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_distorcao', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('ind_situacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('ind_integracao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobranca_parcela_acordo
cobranca_parcela_acordo = [
    bigquery.SchemaField('id_parcela_acordo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_acordo_cobranca', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_parcela_acordo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_vencimento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('ind_situacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_nossonumero', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('val_principal', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_juros', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_tarifa', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_adicionado', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_total', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_tributo', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_base_tributo', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_permanencia', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_principal', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_total', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_atual', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('ind_registrado', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobranca_telefone
cobranca_telefone = [
    bigquery.SchemaField('id_cliente_cobranca', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_telefone_cobranca', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_telefone_externo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_cnpj_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_ddd', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_telefone', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('tip_telefone', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_principal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_obsercacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_ranking', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_modificacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_inclusao_reg', 'INTEGER', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobranca_telefone_cliente
cobranca_telefone_cliente = [
    bigquery.SchemaField('id_cliente_cobranca', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_ddd_celular', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_tel_celular', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_ddd_residencial', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_tel_residencial', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_ddd_comercial', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_tel_comercial', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: cobr_cliente_atraso
cobr_cliente_atraso = [
    bigquery.SchemaField('num_cpf_cnpj_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_cliente_so', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cartao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_produto_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tip_pessoa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tip_situacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_uf', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_rating', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_marcador', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_atual', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_atraso', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_contabil', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_provisao', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_total', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_total_atraso', 'NUMERIC', 'NULLABLE'),
    bigquery.SchemaField('qtd_dias_atraso', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('qtd_parcela_aberta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_modificacao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('nom_assessoria', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_ddd_cel', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_tel_cel', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_ddd_res', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_tel_res', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_ddd_com', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_tel_com', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_email', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_loja', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_colmar', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_colchao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_contr_orig', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_dist_assessoria', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_dist_assess_mar', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_dist_escob', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_estrategia1', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_estrategia2', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_estrategia3', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_estrategia4', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_estrategia5', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_fpd', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_var_aux', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_faixa_atraso_b', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_tivea, Table: conta
conta = [
    bigquery.SchemaField('id_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_produto_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('tip_produto', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_loja_ads_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_canal_ads_conta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_politica', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_mod_score', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('val_score_aprov_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_operacao_proposta_so', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_proposta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_colab_proposta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_chapa_colab_proposta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_origem_entrada_proposta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_cliente_so', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_ori_comercial', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_ads_conta', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_prim_ads_conta', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_prim_ads_cred', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('cod_sit_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_sit_conta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_sit_conta', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('num_dia_vencto_fatura', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_prox_vencto_real', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_prox_vencto_padrao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_ult_alt_vencto', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('flg_conta_bloqueada', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_conta_cancelada', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_produto_cartao_ant', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_ult_grade_produto_cartao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('cod_banco', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_agencia', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dv_agencia', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_conta_corrente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dv_conta_corrente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_adesao_prod_flex', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_cancel_adesao_prod_flex', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('id_adesao_carteira_digital_so', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dt_adesao_carteira_digital', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dt_cancelamento_carteira_digital', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('nm_usr_adesao_carteira_digital', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nm_usr_cancelamento_carteira_digital', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_overlimit_disp', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_indicacao_amigo_revendedor', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_conta_revendedor', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_indicador', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_ult_atu_so', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('num_seq_ult_alteracao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao_reg', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('num_anomes_ads_conta', 'DATE', 'NULLABLE'),
]
