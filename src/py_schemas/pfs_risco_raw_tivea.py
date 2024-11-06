from google.cloud import bigquery

# Dataset: pfs_risco_raw_tivea, Table: acordo
acordo = [
bigquery.SchemaField('source', 'STRING', 'NULLABLE', description="Origem da informação do acordo"),
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="Identificador único do acordo"),
    bigquery.SchemaField('cliente', 'STRING', 'NULLABLE', description="Nome ou identificador do cliente associado ao acordo"),
    bigquery.SchemaField('cobrador', 'STRING', 'NULLABLE', description="Identificador ou nome do cobrador responsável"),
    bigquery.SchemaField('tipo', 'STRING', 'NULLABLE', description="Tipo de acordo estabelecido"),
    bigquery.SchemaField('numeroAcordo', 'STRING', 'NULLABLE', description="Número específico do acordo"),
    bigquery.SchemaField('numeroParcelas', 'STRING', 'NULLABLE', description="Número de parcelas do acordo"),
    bigquery.SchemaField('dataOperacao', 'STRING', 'NULLABLE', description="Data da operação do acordo"),
    bigquery.SchemaField('dataEmissao', 'STRING', 'NULLABLE', description="Data de emissão do acordo"),
    bigquery.SchemaField('dataProcessamento', 'STRING', 'NULLABLE', description="Data de processamento do acordo"),
    bigquery.SchemaField('dataHoraInclusao', 'STRING', 'NULLABLE', description="Data e hora de inclusão do acordo"),
    bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE', description="Data e hora da última modificação do acordo"),
    bigquery.SchemaField('dataVencimento', 'STRING', 'NULLABLE', description="Data de vencimento do acordo"),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE', description="Situação atual do acordo"),
    bigquery.SchemaField('taxaOperacao', 'STRING', 'NULLABLE', description="Taxa aplicada à operação do acordo"),
    bigquery.SchemaField('valorPagoTributo', 'STRING', 'NULLABLE', description="Valor pago referente a tributos no acordo"),
    bigquery.SchemaField('valorPrincipal', 'STRING', 'NULLABLE', description="Valor principal do acordo"),
    bigquery.SchemaField('valorJuros', 'STRING', 'NULLABLE', description="Valor de juros incluído no acordo"),
    bigquery.SchemaField('valorTarifa', 'STRING', 'NULLABLE', description="Valor de tarifa aplicado no acordo"),
    bigquery.SchemaField('valorTributo', 'STRING', 'NULLABLE', description="Valor de tributo cobrado no acordo"),
    bigquery.SchemaField('valorAdicionado', 'STRING', 'NULLABLE', description="Valor adicional inserido no acordo"),
    bigquery.SchemaField('valorTotal', 'STRING', 'NULLABLE', description="Valor total do acordo"),
    bigquery.SchemaField('saldoPrincipal', 'STRING', 'NULLABLE', description="Saldo principal do acordo"),
    bigquery.SchemaField('saldoTotal', 'STRING', 'NULLABLE', description="Saldo total atual do acordo"),
    bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE', description="Saldo atualizado do acordo"),
    bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE', description="Dias de atraso no acordo"),
    bigquery.SchemaField('motivoCancelamento', 'STRING', 'NULLABLE', description="Motivo do cancelamento do acordo"),

    bigquery.SchemaField('negociacao', 'RECORD', 'NULLABLE', description="Detalhes da negociação associada ao acordo", fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="ID da negociação"),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description="Nome da negociação"),
    bigquery.SchemaField('descricao', 'STRING', 'NULLABLE', description="Descrição da negociação"),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE', description="Situação da negociação"),
    bigquery.SchemaField('tipo', 'STRING', 'NULLABLE', description="Tipo de negociação"),
    bigquery.SchemaField('gestao', 'STRING', 'NULLABLE', description="Gestão da negociação"),
    bigquery.SchemaField('cor', 'STRING', 'NULLABLE', description="Cor associada à negociação"),
    bigquery.SchemaField('icone', 'STRING', 'NULLABLE', description="Ícone que representa a negociação"),
    bigquery.SchemaField('tipoDesconto', 'STRING', 'NULLABLE', description="Tipo de desconto aplicado na negociação"),

        bigquery.SchemaField('modalidade', 'RECORD', 'NULLABLE', description="Modalidade da negociação", fields=[
        bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="ID da modalidade"),
        bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description="Nome da modalidade"),
        bigquery.SchemaField('tipo', 'STRING', 'NULLABLE', description="Tipo de modalidade"),
        bigquery.SchemaField('situacao', 'STRING', 'NULLABLE', description="Situação da modalidade"),
        bigquery.SchemaField('gestao', 'STRING', 'NULLABLE', description="Gestão da modalidade"),
        bigquery.SchemaField('cor', 'STRING', 'NULLABLE', description="Cor da modalidade"),
        bigquery.SchemaField('valorDistorcao', 'STRING', 'NULLABLE', description="Valor da distorção na modalidade"),
        bigquery.SchemaField('percentualDistorcao', 'STRING', 'NULLABLE', description="Percentual de distorção na modalidade"),
        bigquery.SchemaField('atrasoMaximo', 'STRING', 'NULLABLE', description="Máximo atraso permitido na modalidade"),
        bigquery.SchemaField('atrasoEntrada', 'STRING', 'NULLABLE', description="Atraso na entrada da modalidade"),
        bigquery.SchemaField('acaoOrigemLiquidacao', 'STRING', 'NULLABLE', description="Ação de origem de liquidação da modalidade")])]),

    bigquery.SchemaField('criterioTributo', 'STRING', 'NULLABLE', description="Critério para aplicação de tributo no acordo"),

    bigquery.SchemaField('produto', 'RECORD', 'NULLABLE', description="Produto associado ao acordo", fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="ID do produto"),
    bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE', description="ID externo do produto"),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description="Nome do produto"),
    bigquery.SchemaField('descricao', 'STRING', 'NULLABLE', description="Descrição do produto")]),

    bigquery.SchemaField('tributo', 'RECORD', 'NULLABLE', description="Tributo associado ao acordo", fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="ID do tributo"),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description="Nome do tributo"),
    bigquery.SchemaField('percentual', 'STRING', 'NULLABLE', description="Percentual de tributo"),
    bigquery.SchemaField('percentualFixo', 'STRING', 'NULLABLE', description="Percentual fixo do tributo"),
    bigquery.SchemaField('percentualMaximo', 'STRING', 'NULLABLE', description="Percentual máximo do tributo"),
    bigquery.SchemaField('arredondamento', 'STRING', 'NULLABLE', description="Método de arredondamento do tributo"),
    bigquery.SchemaField('dataCalculo', 'STRING', 'NULLABLE', description="Data de cálculo do tributo")]),

    bigquery.SchemaField('meioPagamento', 'RECORD', 'NULLABLE', description="Meio de pagamento associado ao acordo", fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="ID do meio de pagamento"),
    bigquery.SchemaField('tipo', 'STRING', 'NULLABLE', description="Tipo do meio de pagamento"),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description="Nome do meio de pagamento"),
        bigquery.SchemaField('cobrador', 'RECORD', 'NULLABLE', description="Informações do cobrador", fields=[
        bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="ID do cobrador"),
        bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description="Nome do cobrador"),
        bigquery.SchemaField('banco', 'STRING', 'NULLABLE', description="Banco associado ao cobrador")])]),

    bigquery.SchemaField('usuario', 'RECORD', 'NULLABLE', description="Informações do usuário associado ao acordo", fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="ID do usuário"),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description="Nome do usuário")]),

    bigquery.SchemaField('assessoria', 'RECORD', 'NULLABLE', description="Assessoria responsável pelo acordo", fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="ID da assessoria"),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description="Nome da assessoria")]),

    bigquery.SchemaField('parcelas', 'RECORD', 'REPEATED', fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('acordo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('numeroParcela', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataVencimento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nossoNumero', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorPrincipal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorJuros', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorTarifa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorAdicionado', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorTotal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorTributo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorBaseTributo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorPermanencia', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorMora', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorMulta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoPrincipal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoTotal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('registrado', 'BOOLEAN', 'NULLABLE')]),

    bigquery.SchemaField('pagamentos', 'RECORD', 'REPEATED', fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataProcessamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataLiquidacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataCredito', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataCnab', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataOperacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dataHoraInclusao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('formaLiquidacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorRecebido', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorDesconto', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorEncargos', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorDistorcao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valorSobra', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('integracao', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('agrupador', 'RECORD', 'NULLABLE', fields=[
        bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('nome', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('cic', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('codigo', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('nomeFantasia', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('situacao', 'STRING', 'NULLABLE')]),
            bigquery.SchemaField('abatimentos', 'RECORD', 'REPEATED', fields=[
            bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('origem', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valorPrincipal', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valorTotal', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valorPermanencia', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valorMora', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valorMulta', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valorOutros', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valorDesconto', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valorJuros', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valorTarifa', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valorTributo', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valorAdicionado', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valorAtual', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('percentual', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('tipo', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('integracao', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('mensagemIntegracao', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('dataHoraIntegracao', 'STRING', 'NULLABLE')]),
                bigquery.SchemaField('liquidacoes', 'RECORD', 'REPEATED', fields=[
                bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
                bigquery.SchemaField('parcela', 'STRING', 'NULLABLE'),
                bigquery.SchemaField('valorPrincipal', 'STRING', 'NULLABLE'),
                bigquery.SchemaField('valorTotal', 'STRING', 'NULLABLE'),
                bigquery.SchemaField('valorJuros', 'STRING', 'NULLABLE'),
                bigquery.SchemaField('valorEncargos', 'STRING', 'NULLABLE'),
                bigquery.SchemaField('valorDesconto', 'STRING', 'NULLABLE'),
                bigquery.SchemaField('valorDistorcao', 'STRING', 'NULLABLE'),
                bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE'),
                bigquery.SchemaField('numeroParcela', 'STRING', 'NULLABLE'),
                bigquery.SchemaField('tipo', 'STRING', 'NULLABLE')])]),

    bigquery.SchemaField('origens', 'RECORD', 'REPEATED', fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="Identificador único da origem"),
    bigquery.SchemaField('valorContabil', 'STRING', 'NULLABLE', description="Valor contabilizado associado à origem"),
    bigquery.SchemaField('descontoContabil', 'STRING', 'NULLABLE', description="Valor do desconto contabilizado"),
    bigquery.SchemaField('saldoContabil', 'STRING', 'NULLABLE', description="Saldo total contabilizado da origem"),
    bigquery.SchemaField('contrato', 'STRING', 'NULLABLE', description="Descrição do contrato associado à origem"),
    bigquery.SchemaField('contratoId', 'STRING', 'NULLABLE', description="ID do contrato relacionado"),
    bigquery.SchemaField('numeroContrato', 'STRING', 'NULLABLE', description="Número específico do contrato"),
    bigquery.SchemaField('parcela', 'STRING', 'NULLABLE', description="Informação sobre a parcela associada"),
    bigquery.SchemaField('parcelaId', 'STRING', 'NULLABLE', description="ID da parcela"),
    bigquery.SchemaField('numeroParcela', 'STRING', 'NULLABLE', description="Número da parcela"),
    bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE', description="Número de dias em atraso"),
    bigquery.SchemaField('ordem', 'STRING', 'NULLABLE', description="Ordem ou posição da origem"),
    bigquery.SchemaField('dataVencimento', 'STRING', 'NULLABLE', description="Data de vencimento da origem"),
    bigquery.SchemaField('nossoNumero', 'STRING', 'NULLABLE', description="Número de controle interno"),
    bigquery.SchemaField('notaFiscal', 'STRING', 'NULLABLE', description="Número da nota fiscal associada"),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE', description="Situação atual da origem"),
    bigquery.SchemaField('valorPrincipal', 'STRING', 'NULLABLE', description="Valor principal da origem"),
    bigquery.SchemaField('valorTotal', 'STRING', 'NULLABLE', description="Valor total da origem"),
    bigquery.SchemaField('valorPermanencia', 'STRING', 'NULLABLE', description="Valor de permanência da origem"),
    bigquery.SchemaField('valorMora', 'STRING', 'NULLABLE', description="Valor de mora associado"),
    bigquery.SchemaField('valorMulta', 'STRING', 'NULLABLE', description="Valor da multa aplicada"),
    bigquery.SchemaField('valorOutros', 'STRING', 'NULLABLE', description="Outros valores relacionados"),
    bigquery.SchemaField('valorDesconto', 'STRING', 'NULLABLE', description="Valor do desconto concedido"),
    bigquery.SchemaField('valorJuros', 'STRING', 'NULLABLE', description="Valor de juros aplicados"),
    bigquery.SchemaField('valorTarifa', 'STRING', 'NULLABLE', description="Valor da tarifa aplicada"),
    bigquery.SchemaField('valorAdicionado', 'STRING', 'NULLABLE', description="Valor adicionado ao saldo"),
    bigquery.SchemaField('valorAtual', 'STRING', 'NULLABLE', description="Valor atual da origem"),
    bigquery.SchemaField('saldoPrincipal', 'STRING', 'NULLABLE', description="Saldo principal da origem"),
    bigquery.SchemaField('saldoTotal', 'STRING', 'NULLABLE', description="Saldo total da origem"),
    bigquery.SchemaField('saldoPermanencia', 'STRING', 'NULLABLE', description="Saldo de permanência"),
    bigquery.SchemaField('saldoMora', 'STRING', 'NULLABLE', description="Saldo de mora"),
    bigquery.SchemaField('saldoMulta', 'STRING', 'NULLABLE', description="Saldo da multa"),
    bigquery.SchemaField('saldoOutros', 'STRING', 'NULLABLE', description="Saldo de outros valores"),
    bigquery.SchemaField('saldoDesconto', 'STRING', 'NULLABLE', description="Saldo do desconto"),
    bigquery.SchemaField('saldoJuros', 'STRING', 'NULLABLE', description="Saldo de juros"),
    bigquery.SchemaField('saldoTarifa', 'STRING', 'NULLABLE', description="Saldo de tarifas"),
    bigquery.SchemaField('saldoAdicionado', 'STRING', 'NULLABLE', description="Saldo adicionado"),
    bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE', description="Saldo atual"),
    bigquery.SchemaField('descontoPrincipal', 'STRING', 'NULLABLE', description="Desconto sobre o valor principal"),
    bigquery.SchemaField('descontoJuros', 'STRING', 'NULLABLE', description="Desconto sobre juros"),
    bigquery.SchemaField('descontoMora', 'STRING', 'NULLABLE', description="Desconto sobre mora"),
    bigquery.SchemaField('descontoMulta', 'STRING', 'NULLABLE', description="Desconto sobre multa"),
    bigquery.SchemaField('descontoOutros', 'STRING', 'NULLABLE', description="Desconto sobre outros valores"),
    bigquery.SchemaField('descontoPermanencia', 'STRING', 'NULLABLE', description="Desconto de permanência"),
    bigquery.SchemaField('descontoTotal', 'STRING', 'NULLABLE', description="Desconto total aplicado")]),

        bigquery.SchemaField('pendencias', 'RECORD', 'REPEATED', fields=[
        bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="Identificador único da pendência"),
        bigquery.SchemaField('dataGeracao', 'STRING', 'NULLABLE', description="Data de geração da pendência"),
        bigquery.SchemaField('dataProcessamento', 'STRING', 'NULLABLE', description="Data de processamento da pendência"),
        bigquery.SchemaField('dataParecer', 'STRING', 'NULLABLE', description="Data do parecer sobre a pendência"),
        bigquery.SchemaField('situacao', 'STRING', 'NULLABLE', description="Situação atual da pendência"),
        bigquery.SchemaField('tipo', 'STRING', 'NULLABLE', description="Tipo da pendência"),
        bigquery.SchemaField('observacao', 'STRING', 'NULLABLE', description="Observações sobre a pendência"),

        bigquery.SchemaField('pareceres', 'RECORD', 'REPEATED', fields=[
        bigquery.SchemaField('situacao', 'STRING', 'NULLABLE', description="Situação do parecer"),
        bigquery.SchemaField('observacao', 'STRING', 'NULLABLE', description="Observações sobre o parecer"),
            bigquery.SchemaField('usuario', 'RECORD', 'NULLABLE', fields=[
            bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE', description="ID externo do usuário"),
            bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description="Nome do usuário"),
            bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="ID interno do usuário")],
            description="Informações do usuário que fez o parecer"),

        bigquery.SchemaField('id', 'STRING', 'NULLABLE', description="ID do parecer"),

        bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE', description="Data e hora da última modificação do parecer")])]),
        bigquery.SchemaField('production_date', 'DATE', 'NULLABLE', description="Data de produção do registro")]


# Dataset: pfs_risco_raw_tivea, Table: cliente
cliente = [
    bigquery.SchemaField('source', 'STRING', 'NULLABLE', description='Fonte dos dados do cliente'),
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description='ID do cliente'),
    bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE', description='ID externo do cliente'),
    bigquery.SchemaField('tipoPessoa', 'STRING', 'NULLABLE', description='Tipo de pessoa (física ou jurídica)'),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE', description='Situação do cliente'),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description='Nome do cliente'),
    bigquery.SchemaField('cic', 'STRING', 'NULLABLE', description='CIC do cliente'),
    bigquery.SchemaField('codigo', 'STRING', 'NULLABLE', description='Código do cliente'),
    bigquery.SchemaField('sexo', 'STRING', 'NULLABLE', description='Sexo do cliente'),
    bigquery.SchemaField('dataNascimento', 'STRING', 'NULLABLE', description='Data de nascimento do cliente'),
    bigquery.SchemaField('dataConta', 'STRING', 'NULLABLE', description='Data de abertura da conta do cliente'),
    bigquery.SchemaField('naturalidade', 'STRING', 'NULLABLE', description='Naturalidade do cliente'),
    bigquery.SchemaField('estadoCivil', 'STRING', 'NULLABLE', description='Estado civil do cliente'),
    bigquery.SchemaField('rg', 'STRING', 'NULLABLE', description='RG do cliente'),
    bigquery.SchemaField('rating', 'STRING', 'NULLABLE', description='Rating do cliente'),
    bigquery.SchemaField('lp', 'STRING', 'NULLABLE', description='LP do cliente'),
    bigquery.SchemaField('propensaoPagamento', 'STRING', 'NULLABLE', description='Propensão ao pagamento do cliente'),
    bigquery.SchemaField('historicoPagamento', 'STRING', 'NULLABLE', description='Histórico de pagamento do cliente'),
    bigquery.SchemaField('numeroDiasMaiorAtraso', 'STRING', 'NULLABLE', description='Número de dias do maior atraso do cliente'),
    bigquery.SchemaField('dataMaiorAtraso', 'STRING', 'NULLABLE', description='Data do maior atraso do cliente'),
    bigquery.SchemaField('rendaTitular', 'STRING', 'NULLABLE', description='Renda do titular da conta'),
    bigquery.SchemaField('rendaConjuge', 'STRING', 'NULLABLE', description='Renda do cônjuge'),
    bigquery.SchemaField('outrasRendas', 'STRING', 'NULLABLE', description='Outras rendas do cliente'),
    bigquery.SchemaField('profissao', 'STRING', 'NULLABLE', description='Profissão do cliente'),
    bigquery.SchemaField('categoriaProfissao', 'STRING', 'NULLABLE', description='Categoria da profissão do cliente'),
    bigquery.SchemaField('tipoResidencia', 'STRING', 'NULLABLE', description='Tipo de residência do cliente'),
    bigquery.SchemaField('saldoAtraso', 'STRING', 'NULLABLE', description='Saldo em atraso do cliente'),
    bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE', description='Saldo atual do cliente'),
    bigquery.SchemaField('saldoContabil', 'STRING', 'NULLABLE', description='Saldo contábil do cliente'),
    bigquery.SchemaField('saldoProvisao', 'STRING', 'NULLABLE', description='Saldo de provisão do cliente'),
    bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE', description='Dias em atraso do cliente'),
    bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE', description='Data e hora da última modificação'),

    bigquery.SchemaField('emails', 'RECORD', 'REPEATED', description='Emails do cliente', fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description='ID do email'),
    bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE', description='ID externo do email'),
    bigquery.SchemaField('email', 'STRING', 'NULLABLE', description='Endereço de email'),
    bigquery.SchemaField('principal', 'BOOLEAN', 'NULLABLE', description='Email principal'),
    bigquery.SchemaField('ranking', 'STRING', 'NULLABLE', description='Ranking do email'),
    bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE', description='Data e hora da última modificação do email')]),

    bigquery.SchemaField('enderecos', 'RECORD', 'REPEATED', description='Endereços do cliente', fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description='ID do endereço'),
    bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE', description='ID externo do endereço'),
    bigquery.SchemaField('cep', 'STRING', 'NULLABLE', description='CEP do endereço'),
    bigquery.SchemaField('codigoDne', 'STRING', 'NULLABLE', description='Código DNE do endereço'),
    bigquery.SchemaField('complemento', 'STRING', 'NULLABLE', description='Complemento do endereço'),
    bigquery.SchemaField('logradouro', 'STRING', 'NULLABLE', description='Logradouro do endereço'),
    bigquery.SchemaField('bairro', 'STRING', 'NULLABLE', description='Bairro do endereço'),
    bigquery.SchemaField('cidade', 'STRING', 'NULLABLE', description='Cidade do endereço'),
    bigquery.SchemaField('numero', 'STRING', 'NULLABLE', description='Número do endereço'),
    bigquery.SchemaField('tipo', 'STRING', 'NULLABLE', description='Tipo do endereço'),
    bigquery.SchemaField('tipoLogradouro', 'STRING', 'NULLABLE', description='Tipo de logradouro do endereço'),
    bigquery.SchemaField('uf', 'STRING', 'NULLABLE', description='UF do endereço'),
    bigquery.SchemaField('principal', 'BOOLEAN', 'NULLABLE', description='Endereço principal'),
    bigquery.SchemaField('ranking', 'STRING', 'NULLABLE', description='Ranking do endereço'),
    bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE', description='Data e hora da última modificação do endereço')]),

    bigquery.SchemaField('telefones', 'RECORD', 'REPEATED', description='Telefones do cliente', fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description='ID do telefone'),
    bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE', description='ID externo do telefone'),
    bigquery.SchemaField('ddd', 'STRING', 'NULLABLE', description='DDD do telefone'),
    bigquery.SchemaField('telefone', 'STRING', 'NULLABLE', description='Número do telefone'),
    bigquery.SchemaField('ramal', 'STRING', 'NULLABLE', description='Ramal do telefone'),
    bigquery.SchemaField('tipo', 'STRING', 'NULLABLE', description='Tipo do telefone'),
    bigquery.SchemaField('observacao', 'STRING', 'NULLABLE', description='Observação do telefone'),
    bigquery.SchemaField('principal', 'BOOLEAN', 'NULLABLE', description='Telefone principal'),
    bigquery.SchemaField('ranking', 'STRING', 'NULLABLE', description='Ranking do telefone'),
    bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE', description='Data e hora da última modificação do telefone')]),

    bigquery.SchemaField('informacoesAdicionais', 'RECORD', 'REPEATED', description='Informações adicionais do cliente', fields=[
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description='Nome da informação adicional'),
    bigquery.SchemaField('linha', 'STRING', 'NULLABLE', description='Linha da informação adicional'),
    bigquery.SchemaField('coluna', 'STRING', 'NULLABLE', description='Coluna da informação adicional'),
    bigquery.SchemaField('valor', 'STRING', 'NULLABLE', description='Valor da informação adicional'),
    bigquery.SchemaField('tipo', 'STRING', 'NULLABLE', description='Tipo da informação adicional'),
    bigquery.SchemaField('tamanho', 'STRING', 'NULLABLE', description='Tamanho da informação adicional')]),

    bigquery.SchemaField('assessorias', 'RECORD', 'REPEATED', description='Assessorias do cliente', fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description='ID da assessoria'),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description='Nome da assessoria'),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE', description='Situação da assessoria'),
    bigquery.SchemaField('cic', 'STRING', 'NULLABLE', description='CIC da assessoria'),
    bigquery.SchemaField('cep', 'STRING', 'NULLABLE', description='CEP da assessoria'),
    bigquery.SchemaField('complemento', 'STRING', 'NULLABLE', description='Complemento da assessoria'),
    bigquery.SchemaField('logradouro', 'STRING', 'NULLABLE', description='Logradouro da assessoria'),
    bigquery.SchemaField('bairro', 'STRING', 'NULLABLE', description='Bairro da assessoria'),
    bigquery.SchemaField('cidade', 'STRING', 'NULLABLE', description='Cidade da assessoria'),
    bigquery.SchemaField('numero', 'STRING', 'NULLABLE', description='Número da assessoria'),
    bigquery.SchemaField('uf', 'STRING', 'NULLABLE', description='UF da assessoria'),
    bigquery.SchemaField('alterarInformacoesCadastrais', 'BOOLEAN', 'NULLABLE', description='Permitir alterar informações cadastrais da assessoria')
    ]),
    bigquery.SchemaField('marcadores', 'RECORD', 'REPEATED', description='Marcadores do cliente', fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description='ID do marcador'),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description='Nome do marcador'),
    bigquery.SchemaField('cor', 'STRING', 'NULLABLE', description='Cor do marcador')
    ]),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE', description='Data de produção dos dados')
]


# Dataset: pfs_risco_raw_tivea, Table: contrato
contrato = [
    bigquery.SchemaField('SOURCE', 'STRING', 'NULLABLE', description='Fonte dos dados do contrato'),
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description='ID do contrato'),
    bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE', description='ID externo do contrato'),
    bigquery.SchemaField('numeroContrato', 'STRING', 'NULLABLE', description='Número do contrato'),
    bigquery.SchemaField('numeroParcelas', 'STRING', 'NULLABLE', description='Número de parcelas do contrato'),
    bigquery.SchemaField('dataEmissao', 'STRING', 'NULLABLE', description='Data de emissão do contrato'),
    bigquery.SchemaField('dataOperacao', 'STRING', 'NULLABLE', description='Data da operação do contrato'),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE', description='Situação do contrato'),
    bigquery.SchemaField('tipo', 'STRING', 'NULLABLE', description='Tipo do contrato'),
    bigquery.SchemaField('taxaOperacao', 'STRING', 'NULLABLE', description='Taxa da operação do contrato'),
    bigquery.SchemaField('valorDevolucao', 'STRING', 'NULLABLE', description='Valor da devolução do contrato'),
    bigquery.SchemaField('valorIof', 'STRING', 'NULLABLE', description='Valor do IOF do contrato'),
    bigquery.SchemaField('valorLiquido', 'STRING', 'NULLABLE', description='Valor líquido do contrato'),
    bigquery.SchemaField('valorTarifa', 'STRING', 'NULLABLE', description='Valor da tarifa do contrato'),

    bigquery.SchemaField('produto', 'RECORD', 'NULLABLE', description='Produto do contrato', fields=[
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description='Nome do produto'),
    bigquery.SchemaField('descricao', 'STRING', 'NULLABLE', description='Descrição do produto')]),

    bigquery.SchemaField('valorTotal', 'STRING', 'NULLABLE', description='Valor total do contrato'),
    bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE', description='Saldo atual do contrato'),
    bigquery.SchemaField('saldoTotal', 'STRING', 'NULLABLE', description='Saldo total do contrato'),
    bigquery.SchemaField('saldoContabil', 'STRING', 'NULLABLE', description='Saldo contábil do contrato'),
    bigquery.SchemaField('saldoAtraso', 'STRING', 'NULLABLE', description='Saldo em atraso do contrato'),
    bigquery.SchemaField('gestao', 'STRING', 'NULLABLE', description='Gestão do contrato'),
    bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE', description='Dias em atraso do contrato'),
    bigquery.SchemaField('dataVencimento', 'STRING', 'NULLABLE', description='Data de vencimento do contrato'),
    bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE', description='Data e hora da última modificação do contrato'),
    bigquery.SchemaField('lp', 'BOOLEAN', 'NULLABLE', description='Indica se o contrato possui LP'),
    bigquery.SchemaField('dataLp', 'STRING', 'NULLABLE', description='Data da LP do contrato'),
    bigquery.SchemaField('siglaAtraso', 'STRING', 'NULLABLE', description='Sigla do atraso do contrato'),

    bigquery.SchemaField('cliente', 'RECORD', 'NULLABLE', description='Cliente do contrato', fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description='ID do cliente'),
    bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE', description='ID externo do cliente'),
    bigquery.SchemaField('tipoPessoa', 'STRING', 'NULLABLE', description='Tipo de pessoa do cliente'),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE', description='Situação do cliente'),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description='Nome do cliente'),
    bigquery.SchemaField('cic', 'STRING', 'NULLABLE', description='CIC do cliente'),
    bigquery.SchemaField('codigo', 'STRING', 'NULLABLE', description='Código do cliente'),
    bigquery.SchemaField('sexo', 'STRING', 'NULLABLE', description='Sexo do cliente'),
    bigquery.SchemaField('dataNascimento', 'STRING', 'NULLABLE', description='Data de nascimento do cliente'),
    bigquery.SchemaField('dataConta', 'STRING', 'NULLABLE', description='Data da conta do cliente'),
    bigquery.SchemaField('naturalidade', 'STRING', 'NULLABLE', description='Naturalidade do cliente'),
    bigquery.SchemaField('estadoCivil', 'STRING', 'NULLABLE', description='Estado civil do cliente'),
    bigquery.SchemaField('rg', 'STRING', 'NULLABLE', description='RG do cliente'),
    bigquery.SchemaField('rating', 'STRING', 'NULLABLE', description='Rating do cliente'),
    bigquery.SchemaField('lp', 'STRING', 'NULLABLE', description='LP do cliente'),
    bigquery.SchemaField('propensaoPagamento', 'STRING', 'NULLABLE', description='Propensão ao pagamento do cliente'),
    bigquery.SchemaField('historicoPagamento', 'STRING', 'NULLABLE', description='Histórico de pagamento do cliente'),
    bigquery.SchemaField('numeroDiasMaiorAtraso', 'STRING', 'NULLABLE', description='Número de dias do maior atraso do cliente'),
    bigquery.SchemaField('dataMaiorAtraso', 'STRING', 'NULLABLE', description='Data do maior atraso do cliente'),
    bigquery.SchemaField('rendaTitular', 'STRING', 'NULLABLE', description='Renda do titular do cliente'),
    bigquery.SchemaField('rendaConjuge', 'STRING', 'NULLABLE', description='Renda do cônjuge do cliente'),
    bigquery.SchemaField('outrasRendas', 'STRING', 'NULLABLE', description='Outras rendas do cliente'),
    bigquery.SchemaField('profissao', 'STRING', 'NULLABLE', description='Profissão do cliente'),
    bigquery.SchemaField('categoriaProfissao', 'STRING', 'NULLABLE', description='Categoria da profissão do cliente'),
    bigquery.SchemaField('tipoResidencia', 'STRING', 'NULLABLE', description='Tipo de residência do cliente'),
    bigquery.SchemaField('saldoAtraso', 'STRING', 'NULLABLE', description='Saldo em atraso do cliente'),
    bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE', description='Saldo atual do cliente'),
    bigquery.SchemaField('saldoContabil', 'STRING', 'NULLABLE', description='Saldo contábil do cliente'),
    bigquery.SchemaField('saldoProvisao', 'STRING', 'NULLABLE', description='Saldo de provisão do cliente'),
    bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE', description='Dias em atraso do cliente'),
    bigquery.SchemaField('dataHoraModificacao', 'STRING', 'NULLABLE', description='Data e hora da última modificação do cliente')]),

    bigquery.SchemaField('parcelas', 'RECORD', 'REPEATED', description='Parcelas do contrato', fields=[
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description='ID da parcela'),
    bigquery.SchemaField('idExterno', 'STRING', 'NULLABLE', description='ID externo da parcela'),
    bigquery.SchemaField('contrato', 'STRING', 'NULLABLE', description='ID do contrato da parcela'),
    bigquery.SchemaField('numeroContrato', 'STRING', 'NULLABLE', description='Número do contrato da parcela'),
    bigquery.SchemaField('numeroParcela', 'STRING', 'NULLABLE', description='Número da parcela'),
    bigquery.SchemaField('dataVencimento', 'STRING', 'NULLABLE', description='Data de vencimento da parcela'),
    bigquery.SchemaField('diasAtraso', 'STRING', 'NULLABLE', description='Dias em atraso da parcela'),
    bigquery.SchemaField('saldoPrincipal', 'STRING', 'NULLABLE', description='Saldo principal da parcela'),
    bigquery.SchemaField('saldoTotal', 'STRING', 'NULLABLE', description='Saldo total da parcela'),
    bigquery.SchemaField('saldoAtual', 'STRING', 'NULLABLE', description='Saldo atual da parcela'),
    bigquery.SchemaField('saldoContabil', 'STRING', 'NULLABLE', description='Saldo contábil da parcela'),
    bigquery.SchemaField('valorPrincipal', 'STRING', 'NULLABLE', description='Valor principal da parcela'),
    bigquery.SchemaField('valorTotal', 'STRING', 'NULLABLE', description='Valor total da parcela'),
    bigquery.SchemaField('valorMulta', 'STRING', 'NULLABLE', description='Valor da multa da parcela'),
    bigquery.SchemaField('valorPermanencia', 'STRING', 'NULLABLE', description='Valor da permanência da parcela'),
    bigquery.SchemaField('valorMora', 'STRING', 'NULLABLE', description='Valor da mora da parcela'),
    bigquery.SchemaField('valorOutros', 'STRING', 'NULLABLE', description='Valor de outros da parcela'),
    bigquery.SchemaField('valorDesconto', 'STRING', 'NULLABLE', description='Valor do desconto da parcela'),
    bigquery.SchemaField('valorDespesa', 'STRING', 'NULLABLE', description='Valor da despesa da parcela'),
    bigquery.SchemaField('valorBoleto', 'STRING', 'NULLABLE', description='Valor do boleto da parcela'),
    bigquery.SchemaField('valorBaseTributo', 'STRING', 'NULLABLE', description='Valor base do tributo da parcela'),
    bigquery.SchemaField('valorPrincipalAberto', 'STRING', 'NULLABLE', description='Valor principal aberto da parcela'),
    bigquery.SchemaField('situacao', 'STRING', 'NULLABLE', description='Situação da parcela'),
    bigquery.SchemaField('agencia', 'STRING', 'NULLABLE', description='Agência da parcela'),
    bigquery.SchemaField('banco', 'STRING', 'NULLABLE', description='Banco da parcela'),
    bigquery.SchemaField('conta', 'STRING', 'NULLABLE', description='Conta da parcela'),
    bigquery.SchemaField('digito', 'STRING', 'NULLABLE', description='Dígito da parcela'),
    bigquery.SchemaField('numeroNossoNumero', 'STRING', 'NULLABLE', description='Número do nosso número da parcela'),
    bigquery.SchemaField('nossoNumero', 'STRING', 'NULLABLE', description='Nosso número da parcela'),
    bigquery.SchemaField('digitoNossoNumero', 'STRING', 'NULLABLE', description='Dígito do nosso número da parcela'),
    bigquery.SchemaField('numeroDocumento', 'STRING', 'NULLABLE', description='Número do documento da parcela'),
    bigquery.SchemaField('notaFiscal', 'STRING', 'NULLABLE', description='Nota fiscal da parcela'),
    bigquery.SchemaField('cobrador', 'STRING', 'NULLABLE', description='Cobrador da parcela'),
    bigquery.SchemaField('cliente', 'STRING', 'NULLABLE', description='ID do cliente da parcela'),
    bigquery.SchemaField('acordo', 'BOOLEAN', 'NULLABLE', description='Indica se a parcela possui acordo'),
    bigquery.SchemaField('bloqueio', 'BOOLEAN', 'NULLABLE', description='Indica se a parcela está bloqueada'),
    bigquery.SchemaField('promessa', 'BOOLEAN', 'NULLABLE', description='Indica se a parcela possui promessa de pagamento'),
    bigquery.SchemaField('tipoAcordo', 'STRING', 'NULLABLE', description='Tipo de acordo da parcela')]),

    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE', description='Data de produção dos dados do contrato')
]
