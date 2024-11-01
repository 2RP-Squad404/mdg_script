from datetime import date

from pydantic import BaseModel


# Dataset: pfs_risco_raw_tivea, Table: acordo
class Acordo(BaseModel):
    source: str
    id: str
    cliente: str
    cobrador: str
    tipo: str
    numeroAcordo: str
    numeroParcelas: str
    dataOperacao: str
    dataEmissao: str
    dataProcessamento: str
    dataHoraInclusao: str
    dataHoraModificacao: str
    dataVencimento: str
    situacao: str
    taxaOperacao: str
    valorPagoTributo: str
    valorPrincipal: str
    valorJuros: str
    valorTarifa: str
    valorTributo: str
    valorAdicionado: str
    valorTotal: str
    saldoPrincipal: str
    saldoTotal: str
    saldoAtual: str
    diasAtraso: str
    motivoCancelamento: str
    negociacao: 'Negociacao'
    criterioTributo: str
    produto: 'Produto'
    tributo: 'Tributo'
    meioPagamento: 'Meiopagamento'
    usuario: 'Usuario'
    assessoria: 'Assessoria'
    parcelas: 'Parcelas'
    pagamentos: 'Pagamentos'
    origens: 'Origens'
    pendencias: 'Pendencias'
    production_date: date


class Negociacao(BaseModel):
    id: str
    nome: str
    descricao: str
    situacao: str
    tipo: str
    gestao: str
    cor: str
    icone: str
    tipoDesconto: str
    modalidade: dict


class Produto(BaseModel):
    id: str
    idExterno: str
    nome: str
    descricao: str


class Tributo(BaseModel):
    id: str
    nome: str
    percentual: str
    percentualFixo: str
    percentualMaximo: str
    arredondamento: str
    dataCalculo: str


class Meiopagamento(BaseModel):
    id: str
    tipo: str
    nome: str
    cobrador: dict


class Usuario(BaseModel):
    id: str
    nome: str


class Assessoria(BaseModel):
    id: str
    nome: str


class Parcelas(BaseModel):
    id: str
    acordo: str
    numeroParcela: str
    dataVencimento: str
    situacao: str
    nossoNumero: str
    valorPrincipal: str
    valorJuros: str
    valorTarifa: str
    valorAdicionado: str
    valorTotal: str
    valorTributo: str
    valorBaseTributo: str
    valorPermanencia: str
    valorMora: str
    valorMulta: str
    saldoPrincipal: str
    saldoTotal: str
    saldoAtual: str
    registrado: bool


class Pagamentos(BaseModel):
    id: str
    dataProcessamento: str
    dataLiquidacao: str
    dataCredito: str
    dataCnab: str
    dataOperacao: str
    dataHoraInclusao: str
    formaLiquidacao: str
    valorRecebido: str
    valorDesconto: str
    valorEncargos: str
    valorDistorcao: str
    valorSobra: str
    situacao: str
    integracao: str
    agrupador: dict
    abatimentos: dict
    liquidacoes: dict


class Origens(BaseModel):
    id: str
    valorContabil: str
    descontoContabil: str
    saldoContabil: str
    contrato: str
    contratoId: str
    numeroContrato: str
    parcela: str
    parcelaId: str
    numeroParcela: str
    diasAtraso: str
    ordem: str
    dataVencimento: str
    nossoNumero: str
    notaFiscal: str
    situacao: str
    valorPrincipal: str
    valorTotal: str
    valorPermanencia: str
    valorMora: str
    valorMulta: str
    valorOutros: str
    valorDesconto: str
    valorJuros: str
    valorTarifa: str
    valorAdicionado: str
    valorAtual: str
    saldoPrincipal: str
    saldoTotal: str
    saldoPermanencia: str
    saldoMora: str
    saldoMulta: str
    saldoOutros: str
    saldoDesconto: str
    saldoJuros: str
    saldoTarifa: str
    saldoAdicionado: str
    saldoAtual: str
    descontoPrincipal: str
    descontoJuros: str
    descontoMora: str
    descontoMulta: str
    descontoOutros: str
    descontoPermanencia: str
    descontoTotal: str


class Pendencias(BaseModel):
    id: str
    dataGeracao: str
    dataProcessamento: str
    dataParecer: str
    situacao: str
    tipo: str
    observacao: str
    pareceres: dict


# Dataset: pfs_risco_raw_tivea, Table: cliente
class Cliente(BaseModel):
    source: str
    id: str
    idExterno: str
    tipoPessoa: str
    situacao: str
    nome: str
    cic: str
    codigo: str
    sexo: str
    dataNascimento: str
    dataConta: str
    naturalidade: str
    estadoCivil: str
    rg: str
    rating: str
    lp: str
    propensaoPagamento: str
    historicoPagamento: str
    numeroDiasMaiorAtraso: str
    dataMaiorAtraso: str
    rendaTitular: str
    rendaConjuge: str
    outrasRendas: str
    profissao: str
    categoriaProfissao: str
    tipoResidencia: str
    saldoAtraso: str
    saldoAtual: str
    saldoContabil: str
    saldoProvisao: str
    diasAtraso: str
    dataHoraModificacao: str
    emails: 'Emails'
    enderecos: 'Enderecos'
    telefones: 'Telefones'
    informacoesAdicionais: 'Informacoesadicionais'
    assessorias: 'Assessorias'
    marcadores: 'Marcadores'
    production_date: date


class Emails(BaseModel):
    id: str
    idExterno: str
    email: str
    principal: bool
    ranking: str
    dataHoraModificacao: str


class Enderecos(BaseModel):
    id: str
    idExterno: str
    cep: str
    codigoDne: str
    complemento: str
    logradouro: str
    bairro: str
    cidade: str
    numero: str
    tipo: str
    tipoLogradouro: str
    uf: str
    principal: bool
    ranking: str
    dataHoraModificacao: str


class Telefones(BaseModel):
    id: str
    idExterno: str
    ddd: str
    telefone: str
    ramal: str
    tipo: str
    observacao: str
    principal: bool
    ranking: str
    dataHoraModificacao: str


class Informacoesadicionais(BaseModel):
    nome: str
    linha: str
    coluna: str
    valor: str
    tipo: str
    tamanho: str


class Assessorias(BaseModel):
    id: str
    nome: str
    situacao: str
    cic: str
    cep: str
    complemento: str
    logradouro: str
    bairro: str
    cidade: str
    numero: str
    uf: str
    alterarInformacoesCadastrais: bool


class Marcadores(BaseModel):
    id: str
    nome: str
    cor: str


# Dataset: pfs_risco_raw_tivea, Table: contrato
class Contrato(BaseModel):
    SOURCE: str
    id: str
    idExterno: str
    numeroContrato: str
    numeroParcelas: str
    dataEmissao: str
    dataOperacao: str
    situacao: str
    tipo: str
    taxaOperacao: str
    valorDevolucao: str
    valorIof: str
    valorLiquido: str
    valorTarifa: str
    produto: 'Produto'
    valorTotal: str
    saldoAtual: str
    saldoTotal: str
    saldoContabil: str
    saldoAtraso: str
    gestao: str
    diasAtraso: str
    dataVencimento: str
    dataHoraModificacao: str
    lp: bool
    dataLp: str
    siglaAtraso: str
    cliente: 'Cliente'
    parcelas: 'Parcelas'
    production_date: date


class Produto(BaseModel):
    nome: str
    descricao: str


class Cliente(BaseModel):
    id: str
    idExterno: str
    tipoPessoa: str
    situacao: str
    nome: str
    cic: str
    codigo: str
    sexo: str
    dataNascimento: str
    dataConta: str
    naturalidade: str
    estadoCivil: str
    rg: str
    rating: str
    lp: str
    propensaoPagamento: str
    historicoPagamento: str
    numeroDiasMaiorAtraso: str
    dataMaiorAtraso: str
    rendaTitular: str
    rendaConjuge: str
    outrasRendas: str
    profissao: str
    categoriaProfissao: str
    tipoResidencia: str
    saldoAtraso: str
    saldoAtual: str
    saldoContabil: str
    saldoProvisao: str
    diasAtraso: str
    dataHoraModificacao: str


class Parcelas(BaseModel):
    id: str
    idExterno: str
    contrato: str
    numeroContrato: str
    numeroParcela: str
    dataVencimento: str
    diasAtraso: str
    saldoPrincipal: str
    saldoTotal: str
    saldoAtual: str
    saldoContabil: str
    valorPrincipal: str
    valorTotal: str
    valorMulta: str
    valorPermanencia: str
    valorMora: str
    valorOutros: str
    valorDesconto: str
    valorDespesa: str
    valorBoleto: str
    valorBaseTributo: str
    valorPrincipalAberto: str
    situacao: str
    agencia: str
    banco: str
    conta: str
    digito: str
    numeroNossoNumero: str
    nossoNumero: str
    digitoNossoNumero: str
    numeroDocumento: str
    notaFiscal: str
    cobrador: str
    cliente: str
    acordo: bool
    bloqueio: bool
    promessa: bool
    tipoAcordo: str
