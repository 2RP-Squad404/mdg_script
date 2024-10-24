from google.cloud import bigquery

# Dataset: pfs_risco_raw_tivea, Table: acordo
acordo = [
    bigquery.SchemaField('source', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cobrador', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tipo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('numeroAcordo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('numeroParcelas', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataOperacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataEmissao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataProcessamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataHoraInclusao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataVencimento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('taxaOperacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorPagoTributo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorPrincipal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorJuros', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorTarifa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorTributo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorAdicionado', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorTotal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoPrincipal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoTotal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('motivoCancelamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('negociacao', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('nome', 'STRING', 'NULLABLE'), bigquery.SchemaField('descricao', 'STRING', 'NULLABLE'), bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('tipo', 'STRING', 'NULLABLE'), bigquery.SchemaField('gestao', 'STRING', 'NULLABLE'), bigquery.SchemaField('cor', 'STRING', 'NULLABLE'), bigquery.SchemaField('icone', 'STRING', 'NULLABLE'), bigquery.SchemaField('tipoDesconto', 'STRING', 'NULLABLE'), bigquery.SchemaField('modalidade', 'RECORD', 'NULLABLE')]),
    bigquery.SchemaField('criterioTributo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('produto', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE'), bigquery.SchemaField('nome', 'STRING', 'NULLABLE'), bigquery.SchemaField('descricao', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('tributo', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('nome', 'STRING', 'NULLABLE'), bigquery.SchemaField('percentual', 'STRING', 'NULLABLE'), bigquery.SchemaField('percentualFixo', 'STRING', 'NULLABLE'), bigquery.SchemaField('percentualMaximo', 'STRING', 'NULLABLE'), bigquery.SchemaField('arredondamento', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataCalculo', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('meioPagamento', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('tipo', 'STRING', 'NULLABLE'), bigquery.SchemaField('nome', 'STRING', 'NULLABLE'), bigquery.SchemaField('cobrador', 'RECORD', 'NULLABLE')]),
    bigquery.SchemaField('usuario', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('nome', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('assessoria', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('nome', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('parcelas', 'RECORD', 'REPEATED', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('acordo', 'STRING', 'NULLABLE'), bigquery.SchemaField('numeroParcela', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataVencimento', 'STRING', 'NULLABLE'), bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('nossoNumero', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorPrincipal', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorJuros', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorTarifa', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorAdicionado', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorTotal', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorTributo', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorBaseTributo', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorPermanencia', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorMora', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorMulta', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoPrincipal', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoTotal', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE'), bigquery.SchemaField('registrado', 'BOOLEAN', 'NULLABLE')]),
    bigquery.SchemaField('pagamentos', 'RECORD', 'REPEATED', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataProcessamento', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataLiquidacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataCredito', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataCnab', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataOperacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataHoraInclusao', 'STRING', 'NULLABLE'), bigquery.SchemaField('formaLiquidacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorRecebido', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorDesconto', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorEncargos', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorDistorcao', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorSobra', 'STRING', 'NULLABLE'), bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('integracao', 'STRING', 'NULLABLE'), bigquery.SchemaField('agrupador', 'RECORD', 'NULLABLE'), bigquery.SchemaField('abatimentos', 'RECORD', 'REPEATED'), bigquery.SchemaField('liquidacoes', 'RECORD', 'REPEATED')]),
    bigquery.SchemaField('origens', 'RECORD', 'REPEATED', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorContabil', 'STRING', 'NULLABLE'), bigquery.SchemaField('descontoContabil', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoContabil', 'STRING', 'NULLABLE'), bigquery.SchemaField('contrato', 'STRING', 'NULLABLE'), bigquery.SchemaField('contratoId', 'STRING', 'NULLABLE'), bigquery.SchemaField('numeroContrato', 'STRING', 'NULLABLE'), bigquery.SchemaField('parcela', 'STRING', 'NULLABLE'), bigquery.SchemaField('parcelaId', 'STRING', 'NULLABLE'), bigquery.SchemaField('numeroParcela', 'STRING', 'NULLABLE'), bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE'), bigquery.SchemaField('ordem', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataVencimento', 'STRING', 'NULLABLE'), bigquery.SchemaField('nossoNumero', 'STRING', 'NULLABLE'), bigquery.SchemaField('notaFiscal', 'STRING', 'NULLABLE'), bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorPrincipal', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorTotal', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorPermanencia', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorMora', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorMulta', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorOutros', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorDesconto', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorJuros', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorTarifa', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorAdicionado', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorAtual', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoPrincipal', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoTotal', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoPermanencia', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoMora', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoMulta', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoOutros', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoDesconto', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoJuros', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoTarifa', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoAdicionado', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE'), bigquery.SchemaField('descontoPrincipal', 'STRING', 'NULLABLE'), bigquery.SchemaField('descontoJuros', 'STRING', 'NULLABLE'), bigquery.SchemaField('descontoMora', 'STRING', 'NULLABLE'), bigquery.SchemaField('descontoMulta', 'STRING', 'NULLABLE'), bigquery.SchemaField('descontoOutros', 'STRING', 'NULLABLE'), bigquery.SchemaField('descontoPermanencia', 'STRING', 'NULLABLE'), bigquery.SchemaField('descontoTotal', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('pendencias', 'RECORD', 'REPEATED', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataGeracao', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataProcessamento', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataParecer', 'STRING', 'NULLABLE'), bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('tipo', 'STRING', 'NULLABLE'), bigquery.SchemaField('observacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('pareceres', 'RECORD', 'REPEATED')]),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_raw_tivea, Table: cliente
cliente = [
    bigquery.SchemaField('source', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tipoPessoa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cic', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('codigo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('sexo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataNascimento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataConta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('naturalidade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('estadoCivil', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('rg', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('rating', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('lp', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('propensaoPagamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('historicoPagamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('numeroDiasMaiorAtraso', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataMaiorAtraso', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('rendaTitular', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('rendaConjuge', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('outrasRendas', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('profissao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('categoriaProfissao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tipoResidencia', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoAtraso', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoContabil', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoProvisao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('emails', 'RECORD', 'REPEATED', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE'), bigquery.SchemaField('email', 'STRING', 'NULLABLE'), bigquery.SchemaField('principal', 'BOOLEAN', 'NULLABLE'), bigquery.SchemaField('ranking', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('enderecos', 'RECORD', 'REPEATED', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE'), bigquery.SchemaField('cep', 'STRING', 'NULLABLE'), bigquery.SchemaField('codigoDne', 'STRING', 'NULLABLE'), bigquery.SchemaField('complemento', 'STRING', 'NULLABLE'), bigquery.SchemaField('logradouro', 'STRING', 'NULLABLE'), bigquery.SchemaField('bairro', 'STRING', 'NULLABLE'), bigquery.SchemaField('cidade', 'STRING', 'NULLABLE'), bigquery.SchemaField('numero', 'STRING', 'NULLABLE'), bigquery.SchemaField('tipo', 'STRING', 'NULLABLE'), bigquery.SchemaField('tipoLogradouro', 'STRING', 'NULLABLE'), bigquery.SchemaField('uf', 'STRING', 'NULLABLE'), bigquery.SchemaField('principal', 'BOOLEAN', 'NULLABLE'), bigquery.SchemaField('ranking', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('telefones', 'RECORD', 'REPEATED', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE'), bigquery.SchemaField('ddd', 'STRING', 'NULLABLE'), bigquery.SchemaField('telefone', 'STRING', 'NULLABLE'), bigquery.SchemaField('ramal', 'STRING', 'NULLABLE'), bigquery.SchemaField('tipo', 'STRING', 'NULLABLE'), bigquery.SchemaField('observacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('principal', 'BOOLEAN', 'NULLABLE'), bigquery.SchemaField('ranking', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('informacoesAdicionais', 'RECORD', 'REPEATED', fields=[bigquery.SchemaField('nome', 'STRING', 'NULLABLE'), bigquery.SchemaField('linha', 'STRING', 'NULLABLE'), bigquery.SchemaField('coluna', 'STRING', 'NULLABLE'), bigquery.SchemaField('valor', 'STRING', 'NULLABLE'), bigquery.SchemaField('tipo', 'STRING', 'NULLABLE'), bigquery.SchemaField('tamanho', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('assessorias', 'RECORD', 'REPEATED', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('nome', 'STRING', 'NULLABLE'), bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('cic', 'STRING', 'NULLABLE'), bigquery.SchemaField('cep', 'STRING', 'NULLABLE'), bigquery.SchemaField('complemento', 'STRING', 'NULLABLE'), bigquery.SchemaField('logradouro', 'STRING', 'NULLABLE'), bigquery.SchemaField('bairro', 'STRING', 'NULLABLE'), bigquery.SchemaField('cidade', 'STRING', 'NULLABLE'), bigquery.SchemaField('numero', 'STRING', 'NULLABLE'), bigquery.SchemaField('uf', 'STRING', 'NULLABLE'), bigquery.SchemaField('alterarInformacoesCadastrais', 'BOOLEAN', 'NULLABLE')]),
    bigquery.SchemaField('marcadores', 'RECORD', 'REPEATED', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('nome', 'STRING', 'NULLABLE'), bigquery.SchemaField('cor', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_raw_tivea, Table: contrato
contrato = [
    bigquery.SchemaField('SOURCE', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('numeroContrato', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('numeroParcelas', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataEmissao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataOperacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tipo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('taxaOperacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorDevolucao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorIof', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorLiquido', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorTarifa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('produto', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('nome', 'STRING', 'NULLABLE'), bigquery.SchemaField('descricao', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('valorTotal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoTotal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoContabil', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoAtraso', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('gestao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataVencimento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('lp', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('dataLp', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('siglaAtraso', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cliente', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE'), bigquery.SchemaField('tipoPessoa', 'STRING', 'NULLABLE'), bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('nome', 'STRING', 'NULLABLE'), bigquery.SchemaField('cic', 'STRING', 'NULLABLE'), bigquery.SchemaField('codigo', 'STRING', 'NULLABLE'), bigquery.SchemaField('sexo', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataNascimento', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataConta', 'STRING', 'NULLABLE'), bigquery.SchemaField('naturalidade', 'STRING', 'NULLABLE'), bigquery.SchemaField('estadoCivil', 'STRING', 'NULLABLE'), bigquery.SchemaField('rg', 'STRING', 'NULLABLE'), bigquery.SchemaField('rating', 'STRING', 'NULLABLE'), bigquery.SchemaField('lp', 'STRING', 'NULLABLE'), bigquery.SchemaField('propensaoPagamento', 'STRING', 'NULLABLE'), bigquery.SchemaField('historicoPagamento', 'STRING', 'NULLABLE'), bigquery.SchemaField('numeroDiasMaiorAtraso', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataMaiorAtraso', 'STRING', 'NULLABLE'), bigquery.SchemaField('rendaTitular', 'STRING', 'NULLABLE'), bigquery.SchemaField('rendaConjuge', 'STRING', 'NULLABLE'), bigquery.SchemaField('outrasRendas', 'STRING', 'NULLABLE'), bigquery.SchemaField('profissao', 'STRING', 'NULLABLE'), bigquery.SchemaField('categoriaProfissao', 'STRING', 'NULLABLE'), bigquery.SchemaField('tipoResidencia', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoAtraso', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoContabil', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoProvisao', 'STRING', 'NULLABLE'), bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('parcelas', 'RECORD', 'REPEATED', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE'), bigquery.SchemaField('contrato', 'STRING', 'NULLABLE'), bigquery.SchemaField('numeroContrato', 'STRING', 'NULLABLE'), bigquery.SchemaField('numeroParcela', 'STRING', 'NULLABLE'), bigquery.SchemaField('dataVencimento', 'STRING', 'NULLABLE'), bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoPrincipal', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoTotal', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE'), bigquery.SchemaField('saldoContabil', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorPrincipal', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorTotal', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorMulta', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorPermanencia', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorMora', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorOutros', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorDesconto', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorDespesa', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorBoleto', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorBaseTributo', 'STRING', 'NULLABLE'), bigquery.SchemaField('valorPrincipalAberto', 'STRING', 'NULLABLE'), bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'), bigquery.SchemaField('agencia', 'STRING', 'NULLABLE'), bigquery.SchemaField('banco', 'STRING', 'NULLABLE'), bigquery.SchemaField('conta', 'STRING', 'NULLABLE'), bigquery.SchemaField('digito', 'STRING', 'NULLABLE'), bigquery.SchemaField('numeroNossoNumero', 'STRING', 'NULLABLE'), bigquery.SchemaField('nossoNumero', 'STRING', 'NULLABLE'), bigquery.SchemaField('digitoNossoNumero', 'STRING', 'NULLABLE'), bigquery.SchemaField('numeroDocumento', 'STRING', 'NULLABLE'), bigquery.SchemaField('notaFiscal', 'STRING', 'NULLABLE'), bigquery.SchemaField('cobrador', 'STRING', 'NULLABLE'), bigquery.SchemaField('cliente', 'STRING', 'NULLABLE'), bigquery.SchemaField('acordo', 'BOOLEAN', 'NULLABLE'), bigquery.SchemaField('bloqueio', 'BOOLEAN', 'NULLABLE'), bigquery.SchemaField('promessa', 'BOOLEAN', 'NULLABLE'), bigquery.SchemaField('tipoAcordo', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
]
