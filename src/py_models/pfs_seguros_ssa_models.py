from datetime import date, datetime

from pydantic import BaseModel


# Dataset: pfs_seguros_ssa, Table: adesao_seguro_item
class Adesao_seguro_item(BaseModel):
    id_AdesaoSeguroItem: int
    id_AdesaoSeguro: int
    id_Pessoa: int
    cd_Item: int
    dt_InicioVigencia: datetime
    dt_TerminoVigencia: datetime
    fl_Titular: bool
    tp_statusIntegracao: int
    dt_Exclusao: datetime
    dt_Adesao: datetime
    id_IntegracaoParceiro: str
    data_cdcBI: datetime
    production_date: date


# Dataset: pfs_seguros_ssa, Table: endereco
class Endereco(BaseModel):
    id_Endereco: int
    nm_Logradouro: str
    no_Logradouro: str
    dc_Complemento: str
    nm_Bairro: str
    nm_Municipio: str
    cd_UF: str
    no_CEP: str
    data_cdcBI: datetime
    production_date: date


# Dataset: pfs_seguros_ssa, Table: pessoa
class Pessoa(BaseModel):
    id_Pessoa: int
    nm_Pessoa: str
    no_CPF: str
    dt_Nascimento: datetime
    tp_Sexo: int
    nm_Mae: str
    no_RG: str
    dt_EmissaoRG: datetime
    cd_UF_RG: str
    no_PIS: str
    no_CNS: str
    no_DeclaracaoNascidoVivo: str
    tp_EstadoCivil: int
    tp_GrauParentesco: int
    id_Endereco: int
    id_Contato: int
    tp_Pessoa: str
    fl_ApenasResponsavelFinanceiro: bool
    id_IntegracaoParceiro: int
    data_cdcBI: datetime
    production_date: date


# Dataset: pfs_seguros_ssa, Table: produto_seguro
class Produto_seguro(BaseModel):
    id_ProdutoSeguro: int
    id_Emissor: int
    cd_ProdutoSeguro: str
    nm_ProdutoSeguro: str
    dc_ProdutoSeguro: str
    id_Seguradora: int
    fl_SeguroMensal: bool
    fl_PagamentoAntecipado: bool
    qt_ParcelasBonificacao: int
    tp_BonificacaoMensal: int
    tp_DevolucaoCancelamento: int
    no_DiasDevolucaoCancelamento: int
    fl_ValidacaoAdesao: bool
    fl_Excluido: bool
    fl_PossuiItem: int
    no_Itens: int
    id_AgrupamentoProdutoSeguro: int
    fl_AceitaParcelamento: bool
    no_MaximoParcelas: int
    no_NOP: str
    dc_TextoNotaFiscal: str
    cd_IntegracaoAP: str
    tp_IntegracaoAP: str
    cd_GrupoPagamento: str
    dc_GrupoPagamento: str
    cd_ContaContabil: str
    qt_ParcelasCancelamento: int
    fl_NaoEstornarParcelasNaoPagas: bool
    fl_PostagemParcelaCorte: bool
    fl_EnvioSeguradoraMensal: bool
    dc_SMS: str
    fl_EnvioSMS: bool
    fl_permitePrimeiraParcelaPaga: bool
    fl_PermiteResponsavelFinanceiro: bool
    fl_PermiteMultiplasAdesoes: bool
    fl_ValidaProdutoVenda: bool
    fl_ValidaNumeroSerieProdutoVenda: bool
    fl_RestituicaoCancelamento: bool
    fl_CalculaParcelaPorItem: bool
    no_MinimoItens: int
    fl_IntegracaoServicoGS: bool
    id_ProdutoAssociado: int
    fl_PermiteAssociacao: bool
    fl_IntegracaoServicoGSRecorrencia: bool
    fl_BonificacaoAntesDoCorte: bool
    no_DiasBonificacao: int
    fl_PermiteEstCancSolicitacao: bool
    id_Parceiro: int
    fl_ProdutoNovo: bool
    production_date: date


# Dataset: pfs_seguros_ssa, Table: seguradora
class Seguradora(BaseModel):
    id_Seguradora: int
    nm_Seguradora: str
    id_Endereco: int
    fl_Ativo: bool
    no_CNPJ: str
    production_date: date
