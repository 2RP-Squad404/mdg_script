from datetime import date, datetime

from pydantic import BaseModel


# Dataset: pfs_unificacao_cliente, Table: cliente_complemento
class Cliente_complemento(BaseModel):
    id_cliente: str
    tip_pessoa: str
    num_cpf_cnpj_cliente: int
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
    tip_origem_principal: str
    dth_ult_atu_so: datetime
    dth_inclusao_reg: datetime
    cod_nacionalidade_iso: str
    des_nacionalidade_iso: str
    cod_profissao_isco08: int
    nom_profissao_isco08: str


# Dataset: pfs_unificacao_cliente, Table: cliente_item_perfil
class Cliente_item_perfil(BaseModel):
    id_cliente: str
    dth_primeiro_evento: datetime
    dth_ultimo_evento: datetime
    dth_ult_atu_cli: datetime
    dth_inclusao: datetime
    tip_origem: str
    id_cliente_so: int
    flg_evento: str
    des_evento: str
    qtd_evento: str
    val_evento: str
    cod_item_perfil: int


# Dataset: pfs_unificacao_cliente, Table: de_para_num_pfj_id_cdt_cpf
class De_para_num_pfj_id_cdt_cpf(BaseModel):
    num_pfj: int
    num_cpf: int
    id_pessoa_cdt: int
    tip_origem_cdt: str
