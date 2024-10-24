from pydantic import BaseModel
from datetime import date, datetime


# Dataset: pfs_risco_raw_neurotech, Table: proposta
class Proposta(BaseModel):
    hash_key: str
    source: str
    codigooperacao: str
    codigoproposta: str
    nomepolitica: str
    resultado: str
    instante_data: datetime
    mensagem: str
    sucesso: str
    versaopolitica: str
    dth_inclusao: datetime
    tempo_execucao_msec: float
    instantefim: datetime
    instanceinicio: datetime
    production_date: date




# Dataset: pfs_risco_raw_neurotech, Table: proposta_consultas
class Proposta_consultas(BaseModel):
    hash_key: str
    source: str
    codigooperacao: str
    status: str
    retornos: Any
    datarealizacao: datetime
    dhfim: datetime
    entradas: Any
    id: str
    nome: str
    idlog: str
    origem: str
    dhinicio: datetime
    descricao: str
    instante_data: datetime
    production_date: date




# Dataset: pfs_risco_raw_neurotech, Table: proposta_detalhe
class Proposta_detalhe(BaseModel):
    hash_key: str
    source: str
    codigooperacao: str
    entradas: Any
    calculadas: Any
    outros: Any
    retornos: Any
    variaveis: Any
    fluxo_regras: Any
    banco: Any
    instante_data: datetime
    production_date: date


