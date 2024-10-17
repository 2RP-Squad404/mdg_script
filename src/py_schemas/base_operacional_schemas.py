from google.cloud import bigquery

# Dataset: base_operacional, Table: conta_cartao_cliente
conta_cartao_cliente_schema = [
    bigquery.SchemaField('id_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_produto_cartao_atual', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_cliente_so', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_loja_ads_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_ads_conta', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_prim_ads_conta', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('nom_canal_ads_conta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_sit_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_sit_conta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_sit_conta', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('num_dia_vencto_fatura', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('flg_conta_bloqueada', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_conta_cancelada', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_ult_grade_produto_cartao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('id_produto_ult_grade', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_ult_atu_so_conta', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('num_anomes_ads_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_chapa_colab_proposta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_origem_entrada_proposta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_produto_atual', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_prim_cancelamento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('des_motivo_prim_cancelamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_ult_cancelamento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('des_motivo_ult_cancelamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_pl_flex', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_indicacao_amigo_revendedor', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_conta_revendedor', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_indicador', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cartao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_bin', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_seq_via_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_sit_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_sit_cartao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_sit_cartao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('flg_cartao_cancelado', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_cancelamento_cartao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_valid_cartao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('num_anomes_emis_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('flg_titular', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_anomes_valid_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('tip_origem_principal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_loja_pref', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_cadastro_cliente', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_nascimento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('cod_sexo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_estado_civil', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_cep_res', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nom_mae_cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_funcionario', 'STRING', 'NULLABLE'),
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
    bigquery.SchemaField('id_produto_cartao_inicial', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_prim_grade', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('id_produto_prim_grade', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_estab_prim_grade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_chapa_colab_prim_grade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_estab_ult_grade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_chapa_colab_ult_grade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_ativacao_conta', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('flg_trans_ofs', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao_reg', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('des_origem', 'STRING', 'NULLABLE'),
]


# Dataset: base_operacional, Table: emprestimo_pessoal_processado
emprestimo_pessoal_processado_schema = [
    bigquery.SchemaField('id_evento_ep', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_cartao_credito_so', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cartao_credito', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_conta_cartao_credito', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_colab_proposta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_chapa_colab_proposta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_loja_ads_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_cliente_so', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_tipo_operacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_tipo_operacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_estab_so', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_estab', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_status', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_status', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_trans', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('val_trans', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('qtd_parcela', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('val_parcela', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('per_taxa_juro', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_trans_origem', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_trans_destino', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('cod_origem', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_origem', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_ori_resolucao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_ori_resolucao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_vencto_prim_par_ep', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_estimada_vencto_ult_par_ep', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('id_autorizacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_autorizacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('val_tac', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_iof', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_juro', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_financiado', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_taxa', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('des_tipo_transacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_origem_informacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_seq_ult_alteracao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_ult_atu_so', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao_reg', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_cancelamento_ep', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('nom_canal_aprovacao_ep', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_loja_ads_ep', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_modelo_score', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_sistema_origem', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_anomes_ep', 'DATE', 'NULLABLE'),
]


# Dataset: base_operacional, Table: faturamento_conta_digital
faturamento_conta_digital_schema = [
    bigquery.SchemaField('id_conta_ccred_transacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cartao_credito', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_titularidade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_pl_flex', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_cartao_mutiplo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_produto_ccred_transacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_transacao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_origem', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('cod_status_transacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_status_transacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_tipo_trans_cred_deb', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_estab_transacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_estab_transacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_mcc_estab_exter', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_mcc_estab_exter', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_transacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_tipo_trans_on_off_us', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('val_transacao', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('cod_tipo_transacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_tipo_transacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_agrupamento_transacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_atual_conta', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('flg_trans_carteira_digital', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_qr_code', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_cliente_funcionario', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_trans_isencao_tarifa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_trans_cashback', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao_reg', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_anomes_transacao', 'DATE', 'NULLABLE'),
]


# Dataset: base_operacional, Table: fatura_fechada
fatura_fechada_schema = [
    bigquery.SchemaField('id_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_sit_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_sit_conta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_produto_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_fatura', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_fatura_anterior', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_vencto_padrao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_vencto_real_ant', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('val_pagamento_anterior', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_atual_ftura', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_saldo_anterior_fatura', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_minimo_atual', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_minimo_anterior', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_pagamento_realizado', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('flg_adesao_parcelamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_tipo_parcelamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_tipo_pagamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_canal_pagamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_cliente_cobranca', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_emite_extrato', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_pl_flex', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_corte_fatura', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('val_cotacao_dolar_corte', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao_reg', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('des_origem', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_anomes_vencto_fatura', 'DATE', 'NULLABLE'),
]


# Dataset: base_operacional, Table: limite_disponibilidade_pos_mensal
limite_disponibilidade_pos_mensal_schema = [
    bigquery.SchemaField('id_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_produto_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cpf_cliente_titular', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_tip_portador', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_sit_conta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_conta_cancelada', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_cadastro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dia_vencto_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('val_disp_global_credito', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_disp_parcela_nac', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_disp_saque_nac_global', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_limite_global_credito', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_limite_maximo', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_limite_parcelas_nac', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_limite_saque_nac_global', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_lim_util_max', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_lim_util_global', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_lim_util_parc', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_lim_util_saque', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('perc_iu_max', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('perc_iu_global', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('perc_iu_parc', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('perc_iu_saque', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('dth_ult_atu_so', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('num_seq_ult_alteracao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao_reg', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('num_anomes_posicao_limite', 'DATE', 'NULLABLE'),
]


# Dataset: base_operacional, Table: pagamento_consolidado
pagamento_consolidado_schema = [
    bigquery.SchemaField('num_cpf_cliente', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_conta', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_produto_cartao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_pagamento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('val_pagamento', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('des_tipo_pagamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_canal_pagamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_meio_pagamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_loja_pagamento', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('qtde_dias_atraso_padrao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('qtde_dias_atraso_real', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_fatura', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dth_vencto_padrao_fatura', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dth_vencto_real_fatura', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('val_min_fatura', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('val_tot_fatura', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('flg_adesao_parcelamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('des_tipo_parcelamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_estorno', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_estorno', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('id_pagamento', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_origem_informacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('flg_emite_extrato', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao_reg', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_referencia', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('des_origem', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_anomes_pagto', 'DATE', 'NULLABLE'),
]