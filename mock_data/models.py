from pydantic import BaseModel
from datetime import datetime

class CartaoModel(BaseModel):
    id_cartao: str
    id_produto_cartao: str
    num_cartao: str
    num_seq_via_cartao: str
    id_conta: str
    num_cpf_cliente: str
    cod_tip_portador: str
    num_bin: str
    cod_loja_emis_cartao: str
    id_cliente_so: str
    dth_emis_cartao: datetime
    dth_embs_cartao: datetime
    dth_valid_cartao: datetime
    dth_desbloqueio: datetime
    cod_sit_cartao: str
    des_sit_cartao: str
    dth_sit_cartao: datetime
    cod_estagio_cartao: str
    des_estagio_cartao: str
    dth_estagio_cartao: datetime
    flg_embs_loja: str
    flg_cartao_cancelado: str
    flg_cartao_provisorio: str
    flg_conta_cancelada: str
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: str
    dth_inclusao_reg: datetime
    pt_nomeplastico: str
    ca_arquivolote: str
    ca_id_imagem: str
    bc_responsavel: str
    ca_codigocancelamento: str
    ca_flaggeracartasenha: str
    pt_id_imagem: str
