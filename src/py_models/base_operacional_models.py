from pydantic import BaseModel
from datetime import date, datetime


# Dataset: base_operacional, Table: conta_cartao_cliente
class Conta_cartao_cliente(BaseModel):
    id_conta: int
    id_produto_cartao_atual: int
    num_cpf_cliente: int
    id_cliente_so: int
    cod_loja_ads_conta: int
    dth_ads_conta: datetime
    dth_prim_ads_conta: datetime
    nom_canal_ads_conta: str
    cod_sit_conta: int
    des_sit_conta: str
    dth_sit_conta: datetime
    num_dia_vencto_fatura: int
    flg_conta_bloqueada: str
    flg_conta_cancelada: str
    dth_ult_grade_produto_cartao: datetime
    id_produto_ult_grade: int
    dth_ult_atu_so_conta: datetime
    num_anomes_ads_conta: int
    id_chapa_colab_proposta: str
    des_origem_entrada_proposta: str
    dth_produto_atual: datetime
    dth_prim_cancelamento: datetime
    des_motivo_prim_cancelamento: str
    dth_ult_cancelamento: datetime
    des_motivo_ult_cancelamento: str
    flg_pl_flex: str
    flg_indicacao_amigo_revendedor: str
    flg_conta_revendedor: str
    num_cpf_indicador: int
    id_cartao: int
    num_cartao: str
    num_bin: int
    num_seq_via_cartao: int
    cod_sit_cartao: int
    des_sit_cartao: str
    dth_sit_cartao: datetime
    flg_cartao_cancelado: str
    dth_cancelamento_cartao: datetime
    dth_valid_cartao: datetime
    num_anomes_emis_cartao: int
    flg_titular: str
    num_anomes_valid_cartao: int
    tip_origem_principal: str
    cod_loja_pref: int
    nom_cliente: str
    dth_cadastro_cliente: datetime
    dat_nascimento: datetime
    cod_sexo: str
    cod_estado_civil: str
    cod_cep_res: str
    nom_mae_cliente: str
    flg_funcionario: str
    cod_nacionalidade: int
    des_nacionalidade: str
    des_naturalidade_cidade: str
    cod_naturalidade_estado: str
    flg_pessoa_politicamente_exposta: str
    flg_deficiente_visual: str
    val_outra_renda_cliente: float
    nom_pai_cliente: str
    num_rg: str
    dat_emissao_rg: date
    cod_orgao_expedicao_rg: str
    cod_estado_emissao_rg: str
    num_cnh: str
    dat_validade_cnh: date
    num_seguranca_cnh: str
    cod_validacao_cnh: str
    dat_emissao_cnh: date
    val_patrimonio_total: float
    cod_profissao: int
    nom_profissao: str
    id_produto_cartao_inicial: int
    dth_prim_grade: datetime
    id_produto_prim_grade: int
    id_estab_prim_grade: str
    id_chapa_colab_prim_grade: str
    id_estab_ult_grade: str
    id_chapa_colab_ult_grade: str
    dth_ativacao_conta: datetime
    flg_trans_ofs: str
    dth_inclusao_reg: datetime
    des_origem: str




# Dataset: base_operacional, Table: emprestimo_pessoal_processado
class Emprestimo_pessoal_processado(BaseModel):
    id_evento_ep: str
    id_cartao_credito_so: int
    num_cartao_credito: str
    id_conta_cartao_credito: int
    nom_colab_proposta: str
    id_chapa_colab_proposta: str
    cod_loja_ads_conta: int
    id_cliente_so: str
    num_cpf_cliente: int
    cod_tipo_operacao: str
    des_tipo_operacao: str
    id_estab_so: int
    cod_estab: int
    cod_status: int
    des_status: str
    dth_trans: datetime
    val_trans: float
    qtd_parcela: int
    val_parcela: float
    per_taxa_juro: float
    val_trans_origem: float
    val_trans_destino: float
    cod_origem: str
    des_origem: str
    cod_ori_resolucao: str
    des_ori_resolucao: str
    dth_vencto_prim_par_ep: datetime
    dth_estimada_vencto_ult_par_ep: datetime
    id_autorizacao: int
    cod_autorizacao: str
    val_tac: float
    val_iof: float
    val_juro: float
    val_financiado: float
    val_taxa: float
    des_tipo_transacao: str
    des_origem_informacao: str
    num_seq_ult_alteracao: int
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    dat_referencia: int
    dat_cancelamento_ep: datetime
    nom_canal_aprovacao_ep: str
    cod_loja_ads_ep: int
    nom_modelo_score: str
    des_sistema_origem: str
    num_anomes_ep: date




# Dataset: base_operacional, Table: faturamento_conta_digital
class Faturamento_conta_digital(BaseModel):
    id_conta_ccred_transacao: int
    id_cliente: str
    num_cpf_cliente: int
    num_cartao_credito: str
    flg_titularidade: str
    flg_pl_flex: str
    flg_cartao_mutiplo: str
    id_produto_ccred_transacao: int
    dth_transacao: datetime
    dth_origem: datetime
    cod_status_transacao: int
    des_status_transacao: str
    des_tipo_trans_cred_deb: str
    cod_estab_transacao: int
    des_estab_transacao: str
    cod_mcc_estab_exter: int
    des_mcc_estab_exter: str
    id_transacao: int
    des_tipo_trans_on_off_us: str
    val_transacao: float
    cod_tipo_transacao: int
    des_tipo_transacao: str
    cod_agrupamento_transacao: int
    val_saldo_atual_conta: float
    flg_trans_carteira_digital: str
    flg_qr_code: str
    flg_cliente_funcionario: str
    flg_trans_isencao_tarifa: str
    flg_trans_cashback: str
    dth_inclusao_reg: datetime
    dat_referencia: int
    num_anomes_transacao: date




# Dataset: base_operacional, Table: fatura_fechada
class Fatura_fechada(BaseModel):
    id_conta: int
    id_cliente: str
    num_cpf_cliente: int
    cod_sit_conta: int
    des_sit_conta: str
    id_produto_cartao: int
    id_fatura: int
    id_fatura_anterior: int
    dth_vencto_padrao: str
    dat_vencto_real_ant: datetime
    val_pagamento_anterior: float
    val_saldo_atual_ftura: float
    val_saldo_anterior_fatura: float
    val_minimo_atual: float
    val_minimo_anterior: float
    val_pagamento_realizado: float
    flg_adesao_parcelamento: str
    des_tipo_parcelamento: str
    cod_tipo_pagamento: str
    des_canal_pagamento: str
    flg_cliente_cobranca: str
    flg_emite_extrato: str
    flg_pl_flex: str
    dth_corte_fatura: datetime
    val_cotacao_dolar_corte: float
    dat_referencia: int
    dth_inclusao_reg: datetime
    des_origem: str
    num_anomes_vencto_fatura: date




# Dataset: base_operacional, Table: limite_disponibilidade_pos_mensal
class Limite_disponibilidade_pos_mensal(BaseModel):
    id_conta: int
    id_produto_cartao: int
    num_cpf_cliente: int
    num_cpf_cliente_titular: int
    cod_tip_portador: int
    des_sit_conta: str
    flg_conta_cancelada: str
    dat_cadastro: str
    dia_vencto_cartao: int
    val_disp_global_credito: float
    val_disp_parcela_nac: float
    val_disp_saque_nac_global: float
    val_limite_global_credito: float
    val_limite_maximo: float
    val_limite_parcelas_nac: float
    val_limite_saque_nac_global: float
    val_lim_util_max: float
    val_lim_util_global: float
    val_lim_util_parc: float
    val_lim_util_saque: float
    perc_iu_max: float
    perc_iu_global: float
    perc_iu_parc: float
    perc_iu_saque: float
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    num_anomes_posicao_limite: date




# Dataset: base_operacional, Table: pagamento_consolidado
class Pagamento_consolidado(BaseModel):
    num_cpf_cliente: int
    id_conta: int
    id_produto_cartao: int
    dth_pagamento: datetime
    val_pagamento: float
    des_tipo_pagamento: str
    des_canal_pagamento: str
    des_meio_pagamento: str
    cod_loja_pagamento: int
    qtde_dias_atraso_padrao: int
    qtde_dias_atraso_real: int
    id_fatura: int
    dth_vencto_padrao_fatura: datetime
    dth_vencto_real_fatura: datetime
    val_min_fatura: float
    val_tot_fatura: float
    flg_adesao_parcelamento: str
    des_tipo_parcelamento: str
    flg_estorno: str
    dth_estorno: datetime
    id_pagamento: int
    des_origem_informacao: str
    flg_emite_extrato: str
    dth_inclusao_reg: datetime
    dat_referencia: int
    des_origem: str
    num_anomes_pagto: date


