from datetime import datetime

from pydantic import BaseModel


# Dataset: pfs_pfin_raw_dw, Table: dw_funcionario
class Dw_funcionario(BaseModel):
    sk_funcionario: int
    num_chapa_so: int
    nom_funcionario: str
    sk_local: int
    sk_cargo: int
    dat_dia_admissao: datetime
    dat_dia_demissao: datetime
    dat_dia_ini_afastamento: datetime
    dat_dia_fim_afastamento: datetime
    des_email: str
    dat_inc_dw: datetime
    dat_ult_alt_dw: datetime
    dat_exc_dw: datetime
    sk_situacao_funcionario: int
    num_cpf: str
    num_rg: str
