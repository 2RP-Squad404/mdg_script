from pydantic import BaseModel
from datetime import date, datetime


# Dataset: pfs_risco_tivea, Table: cartao
class Cartao(BaseModel):
    id_cartao: int
    id_produto_cartao: int
    num_cartao: str
    num_seq_via_cartao: int
    id_conta: int
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
    cod_estagio_cartao: int
    des_estagio_cartao: str
    dth_estagio_cartao: datetime
    flg_embs_loja: str
    flg_cartao_cancelado: str
    flg_cartao_provisorio: str
    flg_conta_cancelada: str
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: int
    dth_inclusao_reg: datetime
    num_anomes_emis_cartao: date




# Dataset: pfs_risco_tivea, Table: cobranca_acordo
class Cobranca_acordo(BaseModel):
    id_acordo_cobranca: int
    id_cliente_externo: int
    num_cpf_cnpj_cliente: int
    id_cobrador: str
    nom_cobrador: str
    tip_modalidade_acordo: str
    num_acordo: int
    num_parcelas: int
    dat_operacao: datetime
    dat_emissao: datetime
    dth_processamento: datetime
    dth_inclusao_origem: datetime
    dth_alteracao_origem: datetime
    dat_vencimento: date
    ind_situacao: str
    val_taxa_operacao: Any
    val_principal: Any
    val_juros: Any
    val_atributo: Any
    val_total: Any
    val_desconto: Any
    val_saldo_principal: Any
    val_saldo_total: Any
    val_saldo_atual: Any
    qtd_dias_atraso: int
    dat_atraso_orig_acordo: date
    id_acordo_usuario: int
    nom_acordo_usuario: str
    id_acordo_assessoria: int
    nom_acordo_assessoria: str
    id_acordo_negociacao: int
    nom_acordo_negociacao: str
    tip_acordo_meio_pagto: str
    dat_referencia: date




# Dataset: pfs_risco_tivea, Table: cobranca_assessoria
class Cobranca_assessoria(BaseModel):
    id_assessoria: str
    nom_assessoria: str
    id_cliente_cobranca: str
    dat_referencia: date




# Dataset: pfs_risco_tivea, Table: cobranca_campo_customizavel
class Cobranca_campo_customizavel(BaseModel):
    id_cliente_cobranca: int
    nom_campo: str
    val_campo: str
    dat_referencia: date




# Dataset: pfs_risco_tivea, Table: cobranca_cliente
class Cobranca_cliente(BaseModel):
    id_cliente_cobranca: int
    id_cliente_externo: str
    tip_pessoa: str
    tip_situacao: str
    nom_cliente: str
    num_cpf_cnpj_cliente: int
    nom_uf: str
    cod_rating: str
    des_marcador: str
    num_dias_maior_atraso: int
    dat_maior_atraso: datetime
    val_saldo_atraso: Any
    val_saldo_atual: Any
    val_saldo_contabil: Any
    val_saldo_provisao: Any
    qtd_dias_atraso: int
    val_saldo_total: Any
    val_saldo_total_atraso: Any
    dth_modificacao: datetime
    num_ddd_cel: int
    num_tel_cel: int
    num_ddd_res: int
    num_tel_res: int
    num_ddd_com: int
    num_tel_com: int
    nom_email: str
    dat_referencia: date




# Dataset: pfs_risco_tivea, Table: cobranca_email_cliente
class Cobranca_email_cliente(BaseModel):
    id_cliente_cobranca: int
    nom_email: str
    dat_referencia: date




# Dataset: pfs_risco_tivea, Table: cobranca_endereco_cliente
class Cobranca_endereco_cliente(BaseModel):
    id_cliente_cobranca: int
    id_cliente_externo: str
    id_endereco_cobranca: int
    tip_endereco_princ: bool
    nom_logradouro: str
    num_logradouro: str
    nom_complemento: str
    num_cep: int
    nom_bairro: str
    nom_cidade: str
    nom_uf: str
    ind_tipo: str
    dat_referencia: date




# Dataset: pfs_risco_tivea, Table: cobranca_liquidacao_parc_acordo
class Cobranca_liquidacao_parc_acordo(BaseModel):
    id_liqd_parc_acordo: int
    id_parcela_acordo: int
    num_parcela_acordo: int
    val_principal: Any
    val_total: Any
    val_juros: Any
    val_encargos: Any
    val_desconto: Any
    val_distorcao: Any
    ind_tipo_liqd: str
    id_pagto_acordo: int
    dat_referencia: date




# Dataset: pfs_risco_tivea, Table: cobranca_origem_acordo
class Cobranca_origem_acordo(BaseModel):
    id_origem_acordo: str
    id_acordo_cobranca: int
    num_contrato: str
    num_ordem_contrato: str
    id_parcela: str
    num_parcela: int
    dat_vencimento: datetime
    id_situacao: str
    qtd_dias_atr_cont: int
    val_principal: Any
    val_total: Any
    val_permanencia: Any
    val_multa: Any
    val_juros: Any
    val_tarifa: Any
    val_adicionado: Any
    val_atual: Any
    val_desconto: Any
    val_desc_principal: Any
    val_desc_juros: Any
    val_desc_multa: Any
    val_desc_permanencia: Any
    val_desconto_total: Any
    dat_referencia: date




# Dataset: pfs_risco_tivea, Table: cobranca_pagamento_acordo
class Cobranca_pagamento_acordo(BaseModel):
    id_pagto_acordo: int
    id_acordo_cobranca: int
    dat_processamento: datetime
    dat_liquidacao: datetime
    dat_credito: datetime
    dat_cnab: datetime
    dat_operacao: datetime
    dth_horainclusao: datetime
    ind_forma_liquidacao: str
    val_recebido: Any
    val_desconto: Any
    val_encargos: Any
    val_distorcao: Any
    ind_situacao: str
    ind_integracao: str
    dat_referencia: date




# Dataset: pfs_risco_tivea, Table: cobranca_parcela_acordo
class Cobranca_parcela_acordo(BaseModel):
    id_parcela_acordo: int
    id_acordo_cobranca: int
    num_parcela_acordo: int
    dat_vencimento: datetime
    ind_situacao: str
    num_nossonumero: str
    val_principal: Any
    val_juros: Any
    val_tarifa: Any
    val_adicionado: Any
    val_total: Any
    val_tributo: Any
    val_base_tributo: Any
    val_permanencia: Any
    val_saldo_principal: Any
    val_saldo_total: Any
    val_saldo_atual: Any
    ind_registrado: str
    dat_referencia: date




# Dataset: pfs_risco_tivea, Table: cobranca_telefone
class Cobranca_telefone(BaseModel):
    id_cliente_cobranca: int
    id_telefone_cobranca: int
    id_telefone_externo: int
    num_cpf_cnpj_cliente: int
    num_ddd: int
    num_telefone: int
    tip_telefone: str
    flg_principal: str
    des_obsercacao: str
    num_ranking: int
    dat_modificacao: int
    dat_inclusao_reg: int




# Dataset: pfs_risco_tivea, Table: cobranca_telefone_cliente
class Cobranca_telefone_cliente(BaseModel):
    id_cliente_cobranca: int
    num_ddd_celular: int
    num_tel_celular: int
    num_ddd_residencial: int
    num_tel_residencial: int
    num_ddd_comercial: int
    num_tel_comercial: int
    dat_referencia: date




# Dataset: pfs_risco_tivea, Table: cobr_cliente_atraso
class Cobr_cliente_atraso(BaseModel):
    num_cpf_cnpj_cliente: int
    id_conta: int
    id_cliente_so: int
    num_cartao: str
    id_produto_cartao: int
    nom_cliente: str
    tip_pessoa: str
    tip_situacao: str
    nom_uf: str
    cod_rating: str
    des_marcador: str
    val_saldo_atual: Any
    val_saldo_atraso: Any
    val_saldo_contabil: Any
    val_saldo_provisao: Any
    val_saldo_total: Any
    val_saldo_total_atraso: Any
    qtd_dias_atraso: int
    qtd_parcela_aberta: int
    dth_modificacao: datetime
    nom_assessoria: str
    num_ddd_cel: int
    num_tel_cel: int
    num_ddd_res: int
    num_tel_res: int
    num_ddd_com: int
    num_tel_com: int
    nom_email: str
    cod_loja: str
    cod_colmar: str
    cod_colchao: str
    cod_contr_orig: str
    cod_dist_assessoria: str
    cod_dist_assess_mar: str
    cod_dist_escob: str
    cod_estrategia1: str
    cod_estrategia2: str
    cod_estrategia3: str
    cod_estrategia4: str
    cod_estrategia5: str
    cod_fpd: str
    cod_var_aux: str
    cod_faixa_atraso_b: str
    dat_referencia: date




# Dataset: pfs_risco_tivea, Table: conta
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
    dat_referencia: int
    dth_inclusao_reg: datetime
    num_anomes_ads_conta: date


