from pydantic import BaseModel
from datetime import date, datetime


# Dataset: pfs_unificacao_pefisa, Table: adesao_deb_automatico
class Adesao_deb_automatico(BaseModel):
    id_adesao_deb_automatico: int
    dth_data_adesao: datetime
    id_conta_digital: int
    id_conta_credito: int
    num_cpf_cliente: int
    id_tipo_deb_automatico: int
    nom_tipo_deb_automatico: str
    nom_user_adesao_deb_automatico: str
    dth_canc_deb_automatico: datetime
    nom_user_canc_deb_automatico: str
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    des_origem: str
    num_anomes_ads_deb_autm: date




# Dataset: pfs_unificacao_pefisa, Table: adesao_pacote_tarifa_hist
class Adesao_pacote_tarifa_hist(BaseModel):
    id_conta: int
    id_produto_conta: int
    id_pacote_tarifa: int
    des_pacote_tarifa: str
    val_tarifa: float
    dth_ativacao: datetime
    dth_desativacao: datetime
    dth_fim_ciclo: datetime
    dth_adesao_conta_ccred: datetime
    num_cpf_cliente: int
    id_cliente_so: int
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    num_anomes_ads_conta: int
    dat_referencia: date




# Dataset: pfs_unificacao_pefisa, Table: agpr_transacao_txn
class Agpr_transacao_txn(BaseModel):
    cod_tipo_transacao: int
    des_tipo_transacao: str
    flg_credito: str
    cod_agrupamento_txn: int
    des_agrupamento_txn: str




# Dataset: pfs_unificacao_pefisa, Table: ajuste_debito
class Ajuste_debito(BaseModel):
    id_conta_debito_so: int
    id_ajuste_debito: int
    dth_inclusao_ajuste_debito: datetime
    dth_origem_ajuste_debito: datetime
    dth_val_ajuste_debito: float
    cod_sit_ajuste_debito: int
    des_sit_ajuste_debito: str
    cod_tipo_ajuste_debito: int
    des_tipo_ajuste_debito: str
    flg_ajuste_credito: str
    des_user: str
    des_estabelecimento_externo: str
    id_conta_multiplo: int
    id_produto_cartao: int
    num_cpf_cliente: int
    id_cartao_multiplo_titular: int
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: int
    num_anomes_ajuste_debito: date




# Dataset: pfs_unificacao_pefisa, Table: autorizacao_cartao_credito
class Autorizacao_cartao_credito(BaseModel):
    id_autorizacao_ccred: int
    dth_autoriz_ccred: datetime
    id_cartao_autoriz_ccred: int
    des_funcao_cartao: str
    num_cartao_autoriz_ccred: str
    cod_estab_autoriz_ccred: int
    num_estab_autoriz_ccred_so: int
    nom_estab_exter_autoriz_ccred: str
    cod_canal_autoriz_ccred: int
    des_canal_autoriz_ccred: str
    cod_tipo_trans_autoriz_ccred: str
    cod_proc_autoriz_ccred: str
    des_tipo_transacao: str
    id_tip_terminal_autoriz_ccred: int
    des_tip_terminal_autoriz_ccred: str
    id_band_modo_entrada: int
    cod_modo_entrada_autoriz_ccred: str
    des_modo_entrada_autoriz_ccred: str
    val_autorizacao_ccred: float
    qtd_parcela_autoriz_ccred: int
    cod_resp_terml_autoriz_ccred: str
    cod_resp_autoriz_ccred: str
    des_resp_autoriz_ccred: str
    des_status_autoriz_ccred: str
    des_categoria_autorizacao: str
    cod_motivo_neg_autoriz_ccred: str
    des_motivo_neg_autoriz_ccred: str
    cod_autorizacao_ccred: str
    id_autorizacao_ccred_so: int
    num_nsuhost_autoriz_ccred: int
    cod_tipo_estab_mcc_autoriz: int
    des_tipo_estab_mcc_autoriz: str
    cod_moeda_autoriz_ccred: str
    des_moeda_autoriz_ccred: str
    id_conta_ccred: int
    flg_autoriz_ons: str
    num_cpf_cliente: int
    id_cliente_so: int
    cod_instituicao_autoriz_ccred: str
    nom_adquirente: str
    id_transacao_uuid: str
    cod_resp_autorizador_antigo: str
    des_resp_autorizador_antigo: str
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    dat_referencia: int
    des_origem: str
    num_anomes_autoriz_ccred: date




# Dataset: pfs_unificacao_pefisa, Table: autorizacao_cartao_credito_hist
class Autorizacao_cartao_credito_hist(BaseModel):
    id_autorizacao_ccred: int
    dth_autoriz_ccred: datetime
    id_cartao_autoriz_ccred: int
    des_funcao_cartao: str
    num_cartao_autoriz_ccred: str
    cod_estab_autoriz_ccred: int
    num_estab_autoriz_ccred_so: int
    nom_estab_exter_autoriz_ccred: str
    cod_canal_autoriz_ccred: int
    des_canal_autoriz_ccred: str
    cod_tipo_trans_autoriz_ccred: str
    cod_proc_autoriz_ccred: str
    des_tipo_transacao: str
    id_tip_terminal_autoriz_ccred: int
    des_tip_terminal_autoriz_ccred: str
    id_band_modo_entrada: int
    cod_modo_entrada_autoriz_ccred: str
    des_modo_entrada_autoriz_ccred: str
    val_autorizacao_ccred: float
    qtd_parcela_autoriz_ccred: int
    cod_resp_terml_autoriz_ccred: str
    cod_resp_autoriz_ccred: str
    des_resp_autoriz_ccred: str
    des_status_autoriz_ccred: str
    des_categoria_autorizacao: str
    cod_motivo_neg_autoriz_ccred: str
    des_motivo_neg_autoriz_ccred: str
    cod_autorizacao_ccred: str
    id_autorizacao_ccred_so: int
    num_nsuhost_autoriz_ccred: int
    cod_tipo_estab_mcc_autoriz: int
    des_tipo_estab_mcc_autoriz: str
    cod_moeda_autoriz_ccred: str
    des_moeda_autoriz_ccred: str
    id_conta_ccred: int
    flg_autoriz_ons: str
    num_cpf_cliente: int
    id_cliente_so: int
    cod_instituicao_autoriz_ccred: str
    nom_adquirente: str
    id_transacao_uuid: str
    cod_resp_autorizador_antigo: str
    des_resp_autorizador_antigo: str
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    num_anomes_autoriz_ccred: int




# Dataset: pfs_unificacao_pefisa, Table: autorizacao_detalhes
class Autorizacao_detalhes(BaseModel):
    id_aut_detalhe_so: int
    id_transacao_uuid: str
    cod_estab_autoriz_ccred: int
    nom_razao_social: str
    nom_estab_exter_autoriz_ccred: str
    cod_estab: int
    cod_estab_cdt: int
    num_cpf_cliente: int
    flg_autoriz_ons: str
    val_score_conductor: int
    val_score_bandeira: int
    val_score_regra: int
    cod_aut_detalhe_1: int
    cod_aut_detalhe_2: int
    cod_aut_detalhe_3: int
    nom_cidade_evento: str
    cod_pais_evento: str
    cod_cep_evento: str
    cod_token_evento: str
    id_token_evento: int
    dth_evento_autorizacao: str
    des_com_eletronico: str
    dat_referencia: date




# Dataset: pfs_unificacao_pefisa, Table: cadastro_chave_pix
class Cadastro_chave_pix(BaseModel):
    num_cpf_cnpj_cliente: int
    num_conta_corrente: str
    dth_cad_conta: datetime
    id_chave_pix: str
    des_tipo_chave_pix: str
    val_chave_pix: str
    cod_status_chave_pix: int
    des_status_chave_pix: str
    dth_status_chave_pix: datetime
    nome_cliente: str
    num_ano_mes_status: int
    dat_referencia: date




# Dataset: pfs_unificacao_pefisa, Table: cartao
class Cartao(BaseModel):
    id_cartao: int
    id_produto_cartao: int
    num_cartao: str
    num_seq_via_cartao: int
    des_modo_cartao: str
    flg_cartao_atual: str
    id_conta: int
    id_conta_debito: int
    id_produto_cartao_debito: int
    num_cpf_cliente: int
    cod_tip_portador: int
    num_bin: int
    cod_loja_emis_cartao: int
    id_cliente_so: int
    dth_emis_cartao: datetime
    dth_embs_cartao: datetime
    dth_valid_cartao: datetime
    dth_desbloqueio: datetime
    cod_sit_cartao: int
    des_sit_cartao: str
    dth_sit_cartao: datetime
    cod_agrp_sit_cartao: int
    des_agrp_sit_cartao: str
    cod_estagio_cartao: int
    des_estagio_cartao: str
    dth_estagio_cartao: datetime
    flg_embs_loja: str
    flg_cartao_cancelado: str
    flg_cartao_provisorio: str
    flg_conta_cancelada: str
    flg_conta_debito_cancelada: str
    pt_nomeplastico: str
    ca_arquivolote: str
    ca_id_imagem: int
    bc_responsavel: str
    ca_codigocancelamento: str
    ca_flaggeracartasenha: int
    pt_id_imagem: int
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    id_cartao_hist_dock: int
    id_conta_hist_dock: int
    id_cliente_hist_dock: int
    flg_cartao_migrado: str
    dth_cartao_migrado: datetime
    des_origem: str
    num_anomes_emis_cartao: date




# Dataset: pfs_unificacao_pefisa, Table: cartao_debito
class Cartao_debito(BaseModel):
    id_conta_debito_so: int
    id_cartao_debito_so: int
    dth_emissao: datetime
    dth_embossing: datetime
    dth_validade: datetime
    cod_sit_cartao_debito: int
    des_sit_cartao_debito: str
    dth_sit_cartao_debito: datetime
    cod_estagio: int
    des_stagio: str
    flg_status_allow_approve: str
    des_portador: str
    num_cartao: str
    cod_bin: int
    nom_bandeira: str
    cod_hash_cartao: str
    qtd_pasword_incorreta: int
    flg_cartao_temporario: str
    nom_cliente_cartao: str
    id_cliente_debito_so: int
    id_conta_multiplo: int
    id_produto_cartao: int
    num_cpf_cliente: int
    id_cartao_multiplo_titular: int
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: int
    num_anomes_emiss_cartao_debito: date




# Dataset: pfs_unificacao_pefisa, Table: conta
class Conta(BaseModel):
    id_conta: int
    id_produto_cartao: int
    tip_produto: str
    num_cpf_cliente: int
    cod_loja_ads_conta: int
    nom_canal_ads_conta: str
    nom_politica: str
    nom_mod_score: str
    val_score_aprov_conta: int
    cod_operacao_proposta_so: str
    id_proposta: int
    nom_colab_proposta: str
    id_chapa_colab_proposta: str
    des_origem_entrada_proposta: str
    id_cliente_so: int
    id_ori_comercial: int
    dth_ads_conta: datetime
    dth_prim_ads_conta: datetime
    dth_prim_ads_cred: datetime
    cod_loja_ativacao_credito: int
    nm_user_ativacao_credito: str
    cod_sit_conta: int
    des_sit_conta: str
    dth_sit_conta: datetime
    cod_agrp_sit_conta: int
    des_agrp_sit_conta: str
    cod_sit_financeiro_conta: int
    des_sit_financeiro_conta: str
    cod_overall_status_conta: int
    des_overall_status_conta: str
    cod_overall_reason_conta: int
    des_overall_reason_conta: str
    num_dia_vencto_fatura: int
    dth_prox_vencto_real: datetime
    dth_prox_vencto_padrao: datetime
    dth_ult_alt_vencto: datetime
    flg_conta_bloqueada: str
    flg_conta_cancelada: str
    id_produto_cartao_ant: int
    dth_ult_grade_produto_cartao: datetime
    id_conta_debito: int
    id_produto_conta_debito: int
    cod_sit_conta_debito: int
    des_sit_conta_debito: str
    dth_sit_conta_debito: datetime
    cod_agrp_sit_conta_debito: int
    des_agrp_sit_conta_debito: str
    cod_sit_financeiro_conta_debito: int
    des_sit_financeiro_conta_debito: str
    cod_overall_status_conta_debito: int
    des_overall_status_conta_debito: str
    cod_overall_reason_conta_debito: int
    des_overall_reason_conta_debito: str
    cod_banco: int
    cod_agencia: int
    dv_agencia: int
    cod_conta_corrente: str
    dv_conta_corrente: str
    flg_conta_debito_bloqueada: str
    flg_conta_debito_cancelada: str
    dth_adesao_prod_flex: datetime
    dth_cancel_adesao_prod_flex: datetime
    cod_loja_ads_prod_flex: int
    nm_usr_adesao_prod_flex: str
    nm_usr_cancelamento_prod_flex: str
    id_adesao_carteira_digital_so: int
    dt_adesao_carteira_digital: datetime
    dt_cancelamento_carteira_digital: datetime
    nm_usr_adesao_carteira_digital: str
    nm_usr_cancelamento_carteira_digital: str
    flg_overlimit_disp: str
    flg_indicacao_amigo_revendedor: str
    flg_conta_revendedor: str
    num_cpf_indicador: int
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    id_conta_hist_dock: int
    id_cliente_hist_dock: int
    flg_conta_migrada: str
    dth_migracao: datetime
    dat_referencia: int
    dth_inclusao_reg: datetime
    des_origem: str
    num_anomes_ads_conta: date




# Dataset: pfs_unificacao_pefisa, Table: conta_debito
class Conta_debito(BaseModel):
    id_conta_multiplo: int
    id_produto_cartao: int
    num_cpf_cliente: int
    id_conta_debito_so: int
    dth_ads_conta_debito: datetime
    des_sit_conta_debito: str
    cod_sit_conta_debito: int
    num_conta_corrente: str
    dv_conta_corrente: str
    cod_banco: int
    num_agencia_conta_corrente: int
    dv_agencia_conta_corrente: int
    num_dia_vencimento: int
    dth_prox_vencto_padrao: datetime
    dth_prox_vencto_real: datetime
    id_cliente_debito_so: int
    id_cliente_multiplo_so: int
    flg_conta_saldo_apartado: str
    id_pacote_tarifa_debito: int
    des_tipo_pacote_tarifa_debito: str
    des_pacote_tarifa_debito: str
    des_tipo_endereco_entrega: str
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: int
    num_anomes_ads_conta_debito: date




# Dataset: pfs_unificacao_pefisa, Table: conta_hist
class Conta_hist(BaseModel):
    id_conta: int
    id_produto_cartao: int
    tip_produto: str
    num_cpf_cliente: int
    cod_loja_ads_conta: int
    nom_canal_ads_conta: str
    nom_politica: str
    nom_mod_score: str
    val_score_aprov_conta: int
    cod_operacao_proposta_so: str
    id_proposta: int
    nom_colab_proposta: str
    id_chapa_colab_proposta: str
    des_origem_entrada_proposta: str
    id_cliente_so: int
    id_ori_comercial: int
    dth_ads_conta: datetime
    dth_prim_ads_conta: datetime
    dth_prim_ads_cred: datetime
    cod_sit_conta: int
    des_sit_conta: str
    dth_sit_conta: datetime
    num_dia_vencto_fatura: int
    dth_prox_vencto_real: datetime
    dth_prox_vencto_padrao: datetime
    dth_ult_alt_vencto: datetime
    flg_conta_bloqueada: str
    flg_conta_cancelada: str
    id_produto_cartao_ant: int
    dth_ult_grade_produto_cartao: datetime
    cod_banco: int
    cod_agencia: int
    dv_agencia: int
    cod_conta_corrente: str
    dv_conta_corrente: str
    dth_adesao_prod_flex: datetime
    dth_cancel_adesao_prod_flex: datetime
    id_adesao_carteira_digital_so: int
    dt_adesao_carteira_digital: datetime
    dt_cancelamento_carteira_digital: datetime
    nm_usr_adesao_carteira_digital: str
    nm_usr_cancelamento_carteira_digital: str
    flg_overlimit_disp: str
    flg_indicacao_amigo_revendedor: str
    flg_conta_revendedor: str
    num_cpf_indicador: int
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    num_anomes_ads_conta: int




# Dataset: pfs_unificacao_pefisa, Table: contestacoes
class Contestacoes(BaseModel):
    num_cpf_cliente: int
    num_cartao: str
    id_conta: int
    id_produto_cartao: int
    des_sit_cartao: str
    id_cartao: int
    flg_cartao_virtual: str
    num_anomes_emis_cartao: int
    data_transacao: datetime
    val_trans: float
    val_financiado: float
    des_tipo_operacao: str
    data_contestacao: datetime
    status_contestacao: str
    razaocb: str
    cc_id_compracontestada: int
    dataenviocb: datetime
    motivo2reapresentacao: str
    trc_tiporesolucaocontestacao: str
    cc_historico: str
    cc_parcelapedida: int
    dataalteracao: datetime
    tipo_contestacao: str
    modo_entrada: str
    des_modo_entrada_autoriz_ccred: str
    mcc: int
    reference_number: str
    bandeira: str
    des_tipo_produto: str
    uuid: str
    val_score_conductor: int
    val_score_bandeira: int
    modalidade: str
    nom_estab: str
    cod_autorizacao: str
    id_evento_compra_saque: int
    id_eventocompra: int
    id_autorizacao: int
    id_autorizacao_ccred: int
    safra_trans: int
    anomesdia_trans: int
    anomesdia_contest: int
    safra_alt: int
    anomesdia_alt: int
    dat_referencia: int
    des_origem: str
    safra_contest: date




# Dataset: pfs_unificacao_pefisa, Table: contrato_emprestimo
class Contrato_emprestimo(BaseModel):
    id_contrato_so: str
    num_contrato_so: str
    id_cliente_so: str
    num_cpf_cliente: int
    dth_solicitacao_emprestimo: datetime
    des_status_contrato: str
    dth_alteracao_status: datetime
    dth_prim_vencto: datetime
    dth_ult_vencto: datetime
    dth_efetivacao_emprestimo: datetime
    dth_credito_cliente: datetime
    dth_geracao_contrato_so: datetime
    nom_financeira: str
    id_proposta_so: str
    cod_ip_assinatura: str
    dth_assinatura: datetime
    des_browser_assinatura: str
    per_taxa_permanencia: float
    per_juros_nominal: float
    per_taxa_interna_retorno: float
    per_taxa_custo_efetivo_mes: float
    per_taxa_iof: float
    per_taxa_iof_complementar: float
    per_taxa_multa: float
    qtde_dia_cobranca_multa: int
    val_liberado_cliente: float
    val_financiado: float
    val_saldo_devedor: float
    val_depositado_cliente: float
    val_iof: float
    val_tarifa: float
    val_juro: float
    val_recebivel: float
    val_seguro: float
    val_parcela: float
    qtde_parcela: int
    des_modalidade_contrato: str
    cod_banco_pagto: int
    nom_banco_pagto: str
    num_agencia_pagto: int
    num_dv_agencia_pagto: int
    des_tipo_conta_pagto: str
    des_class_conta_pagto: str
    num_conta_pagto: str
    num_dv_conta_pagto: str
    num_cpf_responsavel_pagto: int
    nom_titular_pagto: str
    dth_cliente_desde_bco_pagto: datetime
    des_origem_contrato: str
    des_canal_emprestimo: str
    num_cpf_operador: int
    num_chapa_operador: int
    cod_loja_operador: int
    num_chapa_usuario_logado: int
    qtde_parcela_atraso: int
    qtde_parcela_pendente: int
    qtde_parcela_paga: int
    id_conta_debito: int
    id_conta_multiplo: int
    id_produto_cartao: int
    des_origem_informacao: str
    dth_ult_atu_so: datetime
    dat_referencia: int
    dth_inclusao_reg: datetime
    num_ano_mes_sol_empr: date




# Dataset: pfs_unificacao_pefisa, Table: estabelecimento_externo
class Estabelecimento_externo(BaseModel):
    id_estabelecimento_externo: int
    nom_estabelecimento_externo: str
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    dat_referencia: date




# Dataset: pfs_unificacao_pefisa, Table: evento_ajuste
class Evento_ajuste(BaseModel):
    id_evento_ajuste: int
    id_movimento_ajuste: int
    id_tipo_ajuste: str
    des_tipo_ajuste: str
    dth_ajuste: datetime
    val_ajuste: float
    dth_origem: datetime
    dth_movimento: datetime
    id_conta: int
    num_seq_via_cartao: int
    id_cartao: int
    num_cartao: str
    des_funcao_cartao: str
    num_cpf_cliente: int
    dth_vencimento_padrao: datetime
    dth_vencimento_real: datetime
    id_estabelecimento: int
    id_transacao_original: int
    cod_status: int
    des_status: str
    des_categoria_autorizacao: str
    nom_responsavel_inclusao: str
    dth_processamento_lojista: datetime
    id_borderaux: int
    dth_processamento_lojista_dois: datetime
    id_evento_externo_original: int
    tip_evento_externo_original: str
    cod_status_lojista: int
    id_estabelecimento_visa: int
    val_destino: float
    id_incoming: int
    num_parcela_pedida_incoming: int
    cod_origem_resolucao: str
    dth_debito_conta: datetime
    des_estabelecimento_externo: str
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: int




# Dataset: pfs_unificacao_pefisa, Table: evento_compra_saque
class Evento_compra_saque(BaseModel):
    id_evento_compra_saque: int
    id_cartao_credito_so: int
    des_funcao_cartao: str
    num_cartao_credito: str
    id_conta_cartao_credito: int
    id_cliente_so: int
    num_cpf_cliente: int
    cod_tipo_operacao: str
    des_tipo_operacao: str
    id_estab_so: int
    cod_estab: int
    flg_trans_ofs: str
    cod_status: int
    des_status: str
    des_categoria_autorizacao: str
    dth_trans: datetime
    val_trans: float
    qtd_parcela: int
    val_parcela: float
    cod_moeda: int
    des_moeda: str
    per_taxa_juro: float
    val_trans_origem: float
    val_trans_destino: float
    cod_moeda_dest: int
    des_moeda_dest: str
    cod_origem: str
    des_origem: str
    cod_ori_resolucao: str
    des_ori_resolucao: str
    id_estab_exter: int
    nom_estab_exter: str
    cod_tipo_estab_mcc: int
    des_tipo_estab_mcc: str
    dth_vencto_prim_par_ep: datetime
    dth_estimada_vencto_ult_par_ep: datetime
    id_autorizacao: int
    cod_autorizacao: str
    val_tac: float
    val_iof: float
    val_juro: float
    val_financiado: float
    val_taxa: float
    dth_vencimento_padrao: datetime
    des_tipo_transacao: str
    des_origem_informacao: str
    id_evento_original: int
    id_transacao_uuid: str
    cod_reference_number: str
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: int
    des_sistema_origem: str
    num_anomes_compra_saque: date




# Dataset: pfs_unificacao_pefisa, Table: evento_pagamento
class Evento_pagamento(BaseModel):
    id_evento_pagamento: int
    id_cartao_credito_so: int
    des_funcao_cartao: str
    num_cartao_credito: str
    id_conta_cartao_credito: int
    id_cliente_so: int
    num_cpf_cliente: int
    cod_tipo_operacao: str
    des_tipo_operacao: str
    id_estab_so: int
    cod_estab: int
    cod_status: int
    des_status: str
    des_categoria_autorizacao: str
    dth_pagamento: datetime
    val_pago: float
    cod_moeda: int
    des_moeda: str
    cod_origem: str
    des_origem: str
    cod_ori_resolucao: str
    des_ori_resolucao: str
    id_estab_exter: int
    nom_estab_exter: str
    cod_tipo_estab_mcc: int
    des_tipo_estab_mcc: str
    num_banco: int
    dth_vencto_padrao: datetime
    dth_vencto_real: datetime
    id_autorizacao: int
    cod_autorizacao: str
    des_tipo_transacao: str
    id_evento_original: int
    id_fatura_paga: int
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: int
    des_sistema_origem: str
    num_anomes_pagamento: date




# Dataset: pfs_unificacao_pefisa, Table: fatura_ccred
class Fatura_ccred(BaseModel):
    id_fatura_hist: int
    id_conta: int
    id_produto_cartao: int
    id_pessoa_cdt_tit_cta: int
    num_cpf_tit_cta: int
    dat_vencto_real: datetime
    dat_vencto_real_ant: datetime
    dat_vencto_padrao: datetime
    dat_vencto_padrao_ant: datetime
    dth_ini_periodo_faturado: datetime
    dth_fim_periodo_faturado: datetime
    num_documento: int
    cod_situacao: int
    des_situacao: str
    num_ciclo: int
    val_saldo_anterior_final: float
    val_saldo_atual_final: float
    val_saldo_extrato_anterior: float
    val_min_extrato_ant: float
    val_min_extrato: float
    val_base_multa_cobrada: float
    val_multa_extrato: float
    val_multa: float
    flg_multa: str
    val_encargo_financiamento: float
    val_encargo_atraso: float
    val_pagamento: float
    flg_pagamento: str
    dat_vencto_cobranca: datetime
    dat_fechto_prox_fatura: datetime
    val_parcelado_futuro: float
    val_credito_pagto_minimo: float
    val_correcao_credito_minimo: float
    qtd_vencimento: int
    qtd_portador: int
    dth_atualizacao_so: datetime
    cod_canal_envio: int
    des_canal_envio: str
    val_compra_nacional: float
    val_compra_internacional: float
    val_saque_nacional: float
    val_saque_internacional: float
    val_tarifa_nacional: float
    val_seguro: float
    val_encargo_pagto_min: float
    val_encargo_rot_periodo: float
    val_encargo_rot_prox_periodo: float
    val_parcelado_periodo: float
    val_parcelado_prox_periodo: float
    val_encargo_saque_periodo: float
    val_encargo_saque_prox_peri: float
    val_cotacao_dolar: float
    flg_emite_extrato: str
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: int
    des_origem: str
    num_anomes_vencto_fatura: date




# Dataset: pfs_unificacao_pefisa, Table: grade_produto
class Grade_produto(BaseModel):
    id_grade_produto: str
    id_conta_cartao_credito: int
    num_cpf_cliente: int
    id_produto_ccred_origem: int
    id_produto_ccred_destino: int
    id_estabelecimento_grade: str
    nom_estabelecimento_grade: str
    id_chapa_colaborador_grade: str
    nom_colaborador_grade: str
    cod_status_grade_produto: int
    des_status_grade_produto: str
    dth_solicitacao_grade_produto: datetime
    dth_migracao_grade_produto: datetime
    val_limite_anterior_ccred: float
    val_limite_novo_ccred: float
    flg_origem_web_service: str
    des_responsavel: str
    flg_grade_automatico: str
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    des_origem: str
    num_anomes_mig_grade: date




# Dataset: pfs_unificacao_pefisa, Table: grade_produto_hist
class Grade_produto_hist(BaseModel):
    id_grade_produto: str
    id_conta_cartao_credito: int
    num_cpf_cliente: int
    id_produto_ccred_origem: int
    id_produto_ccred_destino: int
    id_estabelecimento_grade: str
    nom_estabelecimento_grade: str
    id_chapa_colaborador_grade: str
    nom_colaborador_grade: str
    cod_status_grade_produto: int
    des_status_grade_produto: str
    dth_solicitacao_grade_produto: datetime
    dth_migracao_grade_produto: datetime
    val_limite_anterior_ccred: float
    val_limite_novo_ccred: float
    flg_origem_web_service: str
    des_responsavel: str
    flg_grade_automatico: str
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    num_anomes_mig_grade: int
    des_origem: str
    dat_referencia: date




# Dataset: pfs_unificacao_pefisa, Table: limite_disponibilidade
class Limite_disponibilidade(BaseModel):
    id_conta: int
    id_produto_cartao: int
    num_cpf_cliente: int
    num_cpf_cliente_titular: int
    cod_tip_portador: int
    val_limite_saque_nac_global: float
    val_limite_global_credito: float
    val_disp_saque_nac_global: float
    val_disp_parcela_nac: float
    val_disp_global_credito: float
    val_limite_parcelas_nac: float
    val_limite_maximo: float
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    des_origem: str
    num_anomes_posicao_limite: date




# Dataset: pfs_unificacao_pefisa, Table: limite_disponibilidade_hist
class Limite_disponibilidade_hist(BaseModel):
    id_conta: int
    id_produto_cartao: int
    num_cpf_cliente: int
    num_cpf_cliente_titular: int
    cod_tip_portador: int
    val_limite_saque_nac_global: float
    val_limite_global_credito: float
    val_disp_saque_nac_global: float
    val_disp_parcela_nac: float
    val_disp_global_credito: float
    val_limite_parcelas_nac: float
    val_limite_maximo: float
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    num_anomes_posicao_limite: date
    des_origem: str
    dat_referencia: date




# Dataset: pfs_unificacao_pefisa, Table: meta_dia_pfin
class Meta_dia_pfin(BaseModel):
    dat_dia: datetime
    cod_estabelecimento: int
    cod_produto_financeiro: int
    qtd_prev_venda: float
    qtd_real_venda: float
    val_prev_venda: float
    val_real_venda: float
    qtd_prev_receb: float
    qtd_real_receb: float
    val_prev_receb: float
    val_real_receb: float
    per_prev_receb: float
    per_real_receb: float
    per_real_receb_acm: float
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: date




# Dataset: pfs_unificacao_pefisa, Table: parcelamento_fatura_ccred
class Parcelamento_fatura_ccred(BaseModel):
    id_parcelamento_fatura: str
    id_conta: int
    dth_vencimento_fatura: datetime
    dth_efetivacao_adesao: datetime
    id_regra_campanha: int
    des_regra_campanha: str
    cod_status_adesao: int
    des_status_adesao: str
    id_servico_tipo: int
    des_tipo_servico: str
    val_total_parcelamento: float
    val_saldo_atual_fatura: float
    dth_geracao_parcelamento: datetime
    qtd_parcela: int
    val_parcela: float
    per_taxa_refinanciamento: float
    per_custo_efetivo_total: float
    val_iof: float
    val_tac: float
    val_total_refinanciamento: float
    num_cpf_cliente_titular: int
    id_fatura_ccred: int
    id_evento_compra: int
    val_entrada_parcelamento: float
    flg_com_entrada: str
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    dat_referencia: int
    des_origem: str
    num_anomes_geracao_parcel: date




# Dataset: pfs_unificacao_pefisa, Table: produto_cartao
class Produto_cartao(BaseModel):
    nom_processadora: str
    nom_parceiro: str
    id_produto_cartao: int
    nom_produto_cartao: str
    id_band_produto_cartao: int
    des_band_produto_cartao: str
    num_bin: int
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime




# Dataset: pfs_unificacao_pefisa, Table: produto_financeiro
class Produto_financeiro(BaseModel):
    id_produto_financeiro: int
    cod_produto_financeiro_so: int
    des_tip_origem: str
    nom_produto_financeiro: str
    des_produto_financeiro: str
    flg_seguro_mensal: str
    qtd_parcelas_bonificacao: int
    cod_tip_bonificacao_mensal: int
    des_tip_bonificacao_mensal: str
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: date




# Dataset: pfs_unificacao_pefisa, Table: refinanciamento_fatura_ccred
class Refinanciamento_fatura_ccred(BaseModel):
    id_refinanciamento_fatura: int
    id_conta: int
    num_cpf_cliente_titular: int
    id_evento_compra: int
    cod_tipo_operacao: int
    des_tipo_operacao: str
    dth_refinanciamento: datetime
    val_rotativo_paga_juro: float
    val_debito_faturado_prox: float
    val_total_pos_prox: float
    val_total_refinanciado: float
    qtde_parcela: int
    val_parcela: float
    val_taxa_juro: float
    val_iof: float
    per_cet: float
    nm_responsavel: str
    cd_status: int
    des_status: str
    val_antecipacao_pendente: float
    val_parcela_futura: float
    val_abatimento_juro: float
    flg_saldo_total: str
    val_total_refinanciar: float
    cd_status_cashback: int
    des_status_cashback: str
    per_cashback: float
    val_cashback: float
    id_parcelamento_fatura: int
    id_fatura: int
    dth_vencimento_fatura: datetime
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    dat_referencia: int
    des_origem: str
    num_anomes_refinanciamento: date




# Dataset: pfs_unificacao_pefisa, Table: saldo_conta
class Saldo_conta(BaseModel):
    id_conta: int
    id_produto_cartao: int
    num_cpf_cliente: int
    val_saldo_atual_final: float
    dth_saldo: datetime
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    dat_referencia: date
    des_origem: str
    num_anomes_posicao_saldo: date




# Dataset: pfs_unificacao_pefisa, Table: saldo_conta_debito
class Saldo_conta_debito(BaseModel):
    id_conta_debito_so: int
    val_saldo_conta_debito: float
    id_conta_multiplo: int
    id_produto_cartao: int
    num_cpf_cliente: int
    flg_conta_saldo_apartado: str
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: int
    des_origem: str
    num_anomes_pos_saldo_debito: date




# Dataset: pfs_unificacao_pefisa, Table: saldo_conta_hist
class Saldo_conta_hist(BaseModel):
    id_conta: int
    id_produto_cartao: int
    num_cpf_cliente: int
    val_saldo_atual_final: float
    dth_saldo: datetime
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    num_anomes_posicao_saldo: date
    des_origem: str
    dat_referencia: date




# Dataset: pfs_unificacao_pefisa, Table: seguradora
class Seguradora(BaseModel):
    id_seguradora: int
    nom_seguradora: str
    num_cnpj_seguradora: str
    cod_seguradora_origem: int
    nom_seguradora_origem: str
    des_tip_origem_sgrd: str
    dth_inclusao_reg: datetime
    dat_referencia: date




# Dataset: pfs_unificacao_pefisa, Table: seguro_adesao
class Seguro_adesao(BaseModel):
    id_adesao_seguro_so: int
    des_tip_origem: str
    dth_adesao: datetime
    id_produto_financeiro: int
    nom_produto_financeiro: str
    des_tip_origem_pfin: str
    cod_tip_adesao: int
    des_tip_adesao: str
    cod_canal_venda: int
    des_canal_venda: str
    cod_tip_canal_venda: int
    des_tip_canal_venda: str
    cod_estabelecimento_adesao: int
    cod_estabelecimento_cancel: int
    cod_tip_situacao_seguro: int
    des_tip_situacao_seguro: str
    dth_situacao_seguro: datetime
    cod_tip_cancelamento: int
    des_tip_cancelamento: str
    cod_motivo_cancelamento: int
    des_motivo_cancelamento: str
    dth_cancelamento: datetime
    id_conta: int
    num_cpf_cliente: int
    cod_tip_titularidade: int
    des_tip_titularidade: str
    cod_seguradora: int
    nom_seguradora: str
    des_tip_origem_sgrd: str
    dth_inicio_vigencia_seguro: datetime
    dth_termino_vigencia_seguro: datetime
    num_meses_vigencia_seguro: int
    val_premio_total: float
    id_cliente_so: int
    id_cliente: str
    num_chapa_adesao: int
    num_chapa_cancel: int
    id_produto_cartao: int
    cod_artigo: int
    cod_cor: int
    cod_tamanho: int
    cod_sortimento: int
    nom_artigo: str
    cod_sku_produto: str
    val_venda_artigo: float
    num_apolice_seguro: str
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: int
    flg_conta_credito: str
    num_anomes_adesao: date




# Dataset: pfs_unificacao_pefisa, Table: seguro_adesao_item
class Seguro_adesao_item(BaseModel):
    id_adesao_seguro_so: int
    id_adesao_seguro_item_so: int
    dth_adesao_seguro_item: datetime
    id_produto_financeiro: int
    nom_produto_financeiro: str
    id_cliente_adesao: int
    num_cpf_cliente_adesao: int
    id_pessoa_adesao_item: int
    num_cpf_adesao_item: int
    cod_item_seguro: int
    dth_ini_vigencia: datetime
    dth_fim_vigencia: datetime
    flg_titular: str
    flg_apenas_resp_financeiro: str
    tp_status_integracao: int
    dth_exclusao: datetime
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: int
    des_tip_origem: str
    num_anomes_adesao_item: date




# Dataset: pfs_unificacao_pefisa, Table: seguro_dependente
class Seguro_dependente(BaseModel):
    id_pessoa_so: int
    num_cpf_cnpj: int
    tip_pessoa: str
    cod_sexo: str
    des_sexo: str
    nm_dependente: str
    dat_nascimento: datetime
    nom_mae: str
    cod_estado_civil: int
    des_estado_civil: str
    cod_grau_parentesco: int
    des_grau_parentesco: str
    num_rg: str
    cod_uf_rg: str
    dat_emissao_rg: datetime
    num_pis: str
    num_cns: str
    num_doc_nascido_vivo: str
    flg_apenas_resp_financeiro: str
    nom_lograd_end: str
    num_lograd_end: str
    des_compl_end: str
    nom_bairro_end: str
    nom_municipio_end: str
    cod_estado_end: str
    cod_cep_end: str
    dth_ult_atu_so: datetime
    dt_referencia: int
    dth_inclusao_reg: datetime
    des_tip_origem: str
    num_anomes_referencia: date




# Dataset: pfs_unificacao_pefisa, Table: seguro_parcela
class Seguro_parcela(BaseModel):
    id_adesao_seguro: int
    id_produto_financeiro: int
    nom_produto_financeiro: str
    des_tip_origem_pfin: str
    num_parcela: int
    val_parcela: float
    dth_vencimento_parcela: datetime
    cod_tip_situacao: int
    des_tip_situacao: str
    dth_situacao: datetime
    dth_emissao_parcela: datetime
    dth_cancelamento: datetime
    des_motivo_cancelamento: str
    cod_tip_situacao_cobranca: int
    des_tip_situacao_cobranca: str
    cod_tip_situacao_transferencia: int
    des_tip_situacao_transferencia: str
    dth_liquidacao: datetime
    dth_real_liquidacao: datetime
    dth_envio_cobranca: datetime
    dth_postagem_parcela: datetime
    num_cpf_cliente: int
    num_apolice_seguro: str
    cod_canal_venda: int
    des_canal_venda: str
    num_seq_recebe_bau: int
    num_serie_bau: str
    num_carne_bau: str
    ind_serie_pnb_bau: str
    tipo_operacao_bau: str
    nm_local_pagamento_bau: str
    cod_estabelecimento_lote: int
    nm_estabelecimento_lote: str
    tip_recebimento_lote: str
    dat_lote: datetime
    num_lote: int
    num_seq_lote: int
    cod_operador: str
    num_bordero: int
    tip_negociacao: int
    dat_ano_mes_apuracao: datetime
    dth_atualizacao_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    dat_referencia: int
    des_tip_origem_adesao: str
    cod_forma_pagto: int
    des_forma_pagto: str
    num_anomes_vencimento: date




# Dataset: pfs_unificacao_pefisa, Table: transacao_contabilizada
class Transacao_contabilizada(BaseModel):
    id_transacao: int
    id_conta_ccred_transacao: int
    id_produto_ccred_transacao: int
    id_fatura: int
    id_autorizacao: int
    cod_processamento: str
    des_processamento: str
    num_sequencial_ccred_transacao: int
    cod_portador_transacao: int
    id_cliente_so: int
    num_cpf_cliente: int
    cod_tipo_transacao: int
    des_tipo_transacao: str
    id_estab_transacao_so: int
    cod_estab_transacao: int
    id_estab_exter_transacao: int
    des_estab_exter_transacao: str
    cod_status_contabil_trans: int
    des_status_contabil_trans: str
    cod_status_gerencial_trans: int
    des_status_gerencial_trans: str
    cod_status_conta_transacao: int
    des_status_conta_transacao: str
    dth_origem_transacao: datetime
    dth_geracao_transacao: datetime
    val_transacao: float
    dth_vencto_real_transacao: datetime
    dth_vencto_padrao_transacao: str
    dth_faturamento_transacao: datetime
    dth_vencto_padrao_trans: datetime
    des_historico_transacao: str
    id_evento_exter_trans_so: int
    flg_extrato: str
    flg_credito: str
    flg_faturado: str
    flg_estornado: str
    id_transacao_estorno: int
    des_complemento_transacao: str
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    des_funcao_cartao: str
    dth_inclusao_reg: datetime
    dat_referencia: int
    des_origem: str
    num_anomes_geracao_trans: date




# Dataset: pfs_unificacao_pefisa, Table: transacao_debito
class Transacao_debito(BaseModel):
    id_conta_debito_so: int
    id_cartao_debito_so: int
    id_transacao_debito: int
    dth_transacao_debito: datetime
    dth_origem_transacao_debito: datetime
    val_transacao_debito: float
    nom_tipo_transacao_debito: str
    cod_tipo_transacao_debito: int
    des_tipo_transacao_debito: str
    flg_transacao_credito: str
    cod_categoria_comerciante: int
    des_categoria_comerciante: str
    id_evento_debito: int
    num_parcela_atual: int
    qtde_parcela: int
    id_conta_multiplo: int
    id_produto_cartao: int
    num_cpf_cliente: int
    id_cartao_multiplo_titular: int
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: int
    num_anomes_trans_debito: date


