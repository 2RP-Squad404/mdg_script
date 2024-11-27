from google.cloud import bigquery

# Dataset: pfs_seguros_ssa, Table: adesao_participacao
adesao_participacao = [
    bigquery.SchemaField('id_AdesaoSeguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_Participante', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_Operacao', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('data_cdcBI', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='None')
]

# Dataset: pfs_seguros_ssa, Table: adesao_seguro
adesao_seguro = [
    bigquery.SchemaField('id_adesaoseguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_emissor', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_cliente', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_produtoseguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_planoseguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_estabelecimento', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_emissao', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_iniciovigencia', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_terminovigencia', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_certificado', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_objetoseguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_produtovenda', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_objetoseguro', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_vendaproduto', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_franquia', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_localrisco', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_situacaoseguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_situacaoseguro', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_premioliquido', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_iof', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_premiototal', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_situacaotransferencia', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_restituido', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_cancelamento', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_ultimaparcelaemitida', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_motivocancelamento', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('cd_canalvenda', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_prolabore', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_observacaocancelamento', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_parcelas', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_notafiscal', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_serieprodutovenda', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_bilhete', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_adesao', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_iofrestituido', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_documentosafedoc', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_estabelecimentocancelamento', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_emissaoproxparcela', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_emissaoultparcela', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_pin', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_comissaosegurada', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_canalvenda', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_canalvenda', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_cancelamentofimvigencia', 'DATE', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_safedocassinatura', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('cd_planoenquadramento', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_arquivoexportacaodados', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_statusintegracaogs', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_observacaostatus', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_seguroquitado', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_restituidoviacartao', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_contrato', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_mesescarencia', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_emissaohora', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_documentosafedoc_new', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_safedocassinatura_new', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_safedocassinatura_old', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_documentosafedoc_old', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_emissaohorareal', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('data_cdcbi', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='None')
]

# Dataset: pfs_seguros_ssa, Table: adesao_seguro_item
adesao_seguro_item = [
    bigquery.SchemaField('id_AdesaoSeguroItem', 'INTEGER', 'NULLABLE', description='ID único do item da adesão ao seguro.'),
    bigquery.SchemaField('id_AdesaoSeguro', 'INTEGER', 'NULLABLE', description='ID da adesão ao seguro.'),
    bigquery.SchemaField('id_Pessoa', 'INTEGER', 'NULLABLE', description='ID da pessoa associada à adesão.'),
    bigquery.SchemaField('cd_Item', 'INTEGER', 'NULLABLE', description='Código do item do seguro.'),
    bigquery.SchemaField('dt_InicioVigencia', 'TIMESTAMP', 'NULLABLE', description='Data e hora do início da vigência do seguro.'),
    bigquery.SchemaField('dt_TerminoVigencia', 'TIMESTAMP', 'NULLABLE', description='Data e hora do término da vigência do seguro.'),
    bigquery.SchemaField('fl_Titular', 'BOOLEAN', 'NULLABLE', description='Indica se o item é do titular (true/false).'),
    bigquery.SchemaField('tp_statusIntegracao', 'INTEGER', 'NULLABLE', description='Status da integração.'),
    bigquery.SchemaField('dt_Exclusao', 'TIMESTAMP', 'NULLABLE', description='Data e hora da exclusão do item (se aplicável).'),
    bigquery.SchemaField('dt_Adesao', 'TIMESTAMP', 'NULLABLE', description='Data e hora da adesão ao item do seguro.'),
    bigquery.SchemaField('id_IntegracaoParceiro', 'STRING', 'NULLABLE', description='ID da integração com o parceiro.'),
    bigquery.SchemaField('data_cdcBI', 'TIMESTAMP', 'NULLABLE', description='Data e hora do CDC BI.'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='Data de produção do registro.')
]

# Dataset: pfs_seguros_ssa, Table: agrupamento_produto_seguro
agrupamento_produto_seguro = [
    bigquery.SchemaField('id_AgrupamentoProdutoSeguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('nm_Agrupamento', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_TermoAceite', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_OrdemApresentacao', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_Emissor', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_Ativo', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='None')
]

# Dataset: pfs_seguros_ssa, Table: canal_venda
canal_venda = [
    bigquery.SchemaField('id_CanalVenda', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('cd_CanalVenda', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('nm_CanalVenda', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_CanalPadrao', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_Emissor', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='None')
]

# Dataset: pfs_seguros_ssa, Table: cliente
cliente = [
    bigquery.SchemaField('id_cliente', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_emissor', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_cliente', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_conta', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_cartao', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_diavencimento', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_titularidade', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_pessoa', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_statusintegracaocliente', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_contacredito', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_grade', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('data_cdcbi', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='None')
]

# Dataset: pfs_seguros_ssa, Table: endereco
endereco = [
    bigquery.SchemaField('id_Endereco', 'INTEGER', 'NULLABLE', description='ID único do endereço.'),
    bigquery.SchemaField('nm_Logradouro', 'STRING', 'NULLABLE', description='Nome do logradouro (ex: Rua, Avenida).'),
    bigquery.SchemaField('no_Logradouro', 'STRING', 'NULLABLE', description='Número do logradouro.'),
    bigquery.SchemaField('dc_Complemento', 'STRING', 'NULLABLE', description='Complemento do endereço.'),
    bigquery.SchemaField('nm_Bairro', 'STRING', 'NULLABLE', description='Nome do bairro.'),
    bigquery.SchemaField('nm_Municipio', 'STRING', 'NULLABLE', description='Nome do município.'),
    bigquery.SchemaField('cd_UF', 'STRING', 'NULLABLE', description='Sigla da UF.'),
    bigquery.SchemaField('no_CEP', 'STRING', 'NULLABLE', description='CEP.'),
    bigquery.SchemaField('data_cdcBI', 'TIMESTAMP', 'NULLABLE', description='Data e hora do CDC BI.'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='Data de produção do registro.')
]

# Dataset: pfs_seguros_ssa, Table: estabelecimento
estabelecimento = [
    bigquery.SchemaField('id_Estabelecimento', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_Emissor', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_CNPJ', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('cd_Estabelecimento', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('nm_Estabelecimento', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_Endereco', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_Contato', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_Ativo', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_SerieNFE', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('cd_Servico', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='None')
]

# Dataset: pfs_seguros_ssa, Table: objeto_seguro
objeto_seguro = [
    bigquery.SchemaField('id_ObjetoSeguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_PlanoSeguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_ObjetoSeguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_CategoriaProduto', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_InicioVigencia', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_TerminoVigencia', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_FaixaPrecoInicial', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_FaixaPrecoFinal', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_PremioLiquido', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_IOF', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_PremioTotal', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('pc_Franquia', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_ProLabore', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('data_cdcBI', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='None')
]

# Dataset: pfs_seguros_ssa, Table: parcela_seguro
parcela_seguro = [
    bigquery.SchemaField('id_ParcelaSeguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_AdesaoSeguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_Parcela', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_Vencimento', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_Parcela', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_Situacao', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_Situacao', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_Emissao', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_SituacaoCobranca', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_SituacaoTransferencia', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_TituloCapitalizacao', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_PagamentoPDV', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_EnvioCobranca', 'DATE', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_PostagemParcela', 'DATE', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_Liquidacao', 'DATE', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_FormaPagamento', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_SituacaoCobranca', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_SituacaoTransferencia', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_TentativasLancamentosContaDigital', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_ArquivoExportacaoDados', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_ParcelaPIN', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_StatusIntegracaoParcelaGS', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_RetornoProcessadora', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_AjusteLancado', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_LiquidacaoHoraReal', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('data_cdcBI', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='None')
]

# Dataset: pfs_seguros_ssa, Table: participante
participante = [
    bigquery.SchemaField('id_Participante', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_Participante', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('cd_Participante', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_Estabelecimento', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('nm_Participante', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('data_cdcBI', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='None')
]

# Dataset: pfs_seguros_ssa, Table: pessoa
pessoa = [
    bigquery.SchemaField('id_Pessoa', 'INTEGER', 'NULLABLE', description='ID único da pessoa.'),
    bigquery.SchemaField('nm_Pessoa', 'STRING', 'NULLABLE', description='Nome completo da pessoa.'),
    bigquery.SchemaField('no_CPF', 'STRING', 'NULLABLE', description='CPF da pessoa.'),
    bigquery.SchemaField('dt_Nascimento', 'TIMESTAMP', 'NULLABLE', description='Data e hora de nascimento da pessoa.'),
    bigquery.SchemaField('tp_Sexo', 'INTEGER', 'NULLABLE', description='Sexo da pessoa (código).'),
    bigquery.SchemaField('nm_Mae', 'STRING', 'NULLABLE', description='Nome da mãe da pessoa.'),
    bigquery.SchemaField('no_RG', 'STRING', 'NULLABLE', description='Número do RG da pessoa.'),
    bigquery.SchemaField('dt_EmissaoRG', 'TIMESTAMP', 'NULLABLE', description='Data e hora de emissão do RG.'),
    bigquery.SchemaField('cd_UF_RG', 'STRING', 'NULLABLE', description='UF de emissão do RG.'),
    bigquery.SchemaField('no_PIS', 'STRING', 'NULLABLE', description='Número do PIS da pessoa.'),
    bigquery.SchemaField('no_CNS', 'STRING', 'NULLABLE', description='Número do CNS da pessoa.'),
    bigquery.SchemaField('no_DeclaracaoNascidoVivo', 'STRING', 'NULLABLE', description='Número da Declaração de Nascido Vivo.'),
    bigquery.SchemaField('tp_EstadoCivil', 'INTEGER', 'NULLABLE', description='Estado civil da pessoa (código).'),
    bigquery.SchemaField('tp_GrauParentesco', 'INTEGER', 'NULLABLE', description='Grau de parentesco (código).'),
    bigquery.SchemaField('id_Endereco', 'INTEGER', 'NULLABLE', description='ID do endereço da pessoa.'),
    bigquery.SchemaField('id_Contato', 'INTEGER', 'NULLABLE', description='ID do contato da pessoa.'),
    bigquery.SchemaField('tp_Pessoa', 'STRING', 'NULLABLE', description='Tipo de pessoa (física ou jurídica).'),
    bigquery.SchemaField('fl_ApenasResponsavelFinanceiro', 'BOOLEAN', 'NULLABLE', description='Apenas responsável financeiro (true/false).'),
    bigquery.SchemaField('id_IntegracaoParceiro', 'INTEGER', 'NULLABLE', description='ID da integração com o parceiro.'),
    bigquery.SchemaField('data_cdcBI', 'TIMESTAMP', 'NULLABLE', description='Data e hora do CDC BI.'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='Data de produção do registro.')
]

# Dataset: pfs_seguros_ssa, Table: plano_seguro
plano_seguro = [
    bigquery.SchemaField('id_PlanoSeguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_ProdutoSeguro', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('cd_PlanoEmissor', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('nm_PlanoSeguro', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_PlanoSeguro', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('nm_ProdutoPlano', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_InicioVigencia', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_TerminoVigencia', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_MesesVigencia', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_InformarMesesVigencia', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_PrefixoCertificado', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_MascaraCertificado', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('qt_TitulosCapitalizacao', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_InformarQtdNumerosSorte', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_InformarNumerosSorte', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_MascaraNumeroSorte', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('qt_LoteNumerosSorte', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_EmissaoTituloCapitalizacaoMensal', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_CobrancaRepasse', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_VigenciaFutura', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_DiasVigenciaFutura', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_ConjuntoTituloCapitalizacao', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_OperacaoCobranca', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_OperacaoEstorno', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_Completa', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_RiscosExcluidos', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_TermoAdesao', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_ExtratoIncondicional', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_DebitoIncondicional', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_Garantia', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_RenovacaoAutomatica', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_ReenviarEmail', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('dt_InicioVigenciaRenovacaoAutomatica', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_Plano', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_TipoAjusteDebito', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_TipoAjusteEstorno', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_AceitaLancamentoNaAdesao', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_ConjuntoPIN', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_MascaraPIN', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_RecebeInfoPinAdesao', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_MascaraSeriePIN', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_MascaraLotePIN', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_AceitaItem', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_ObtemValorNoPlano', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_AjusteRestituicaoCredito', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_AjusteRestituicaoDebito', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_mesesCarencia', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('destaque', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('tp_Complemento', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_mesesCarencia', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('Total_Dependentes', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_OperacaoCobranca', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_OperacaoEstorno', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_AjusteCobranca', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dc_AjusteEstorno', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='None')
]

# Dataset: pfs_seguros_ssa, Table: produto_seguro
produto_seguro = [
    bigquery.SchemaField('id_ProdutoSeguro', 'INTEGER', 'NULLABLE', description='ID único do produto de seguro.'),
    bigquery.SchemaField('id_Emissor', 'INTEGER', 'NULLABLE', description='ID do emissor do seguro.'),
    bigquery.SchemaField('cd_ProdutoSeguro', 'STRING', 'NULLABLE', description='Código do produto de seguro.'),
    bigquery.SchemaField('nm_ProdutoSeguro', 'STRING', 'NULLABLE', description='Nome do produto de seguro.'),
    bigquery.SchemaField('dc_ProdutoSeguro', 'STRING', 'NULLABLE', description='Descrição do produto de seguro.'),
    bigquery.SchemaField('id_Seguradora', 'INTEGER', 'NULLABLE', description='ID da seguradora.'),
    bigquery.SchemaField('fl_SeguroMensal', 'BOOLEAN', 'NULLABLE', description='Seguro mensal (true/false).'),
    bigquery.SchemaField('fl_PagamentoAntecipado', 'BOOLEAN', 'NULLABLE', description='Pagamento antecipado (true/false).'),
    bigquery.SchemaField('qt_ParcelasBonificacao', 'INTEGER', 'NULLABLE', description='Quantidade de parcelas de bonificação.'),
    bigquery.SchemaField('tp_BonificacaoMensal', 'INTEGER', 'NULLABLE', description='Tipo de bonificação mensal.'),
    bigquery.SchemaField('tp_DevolucaoCancelamento', 'INTEGER', 'NULLABLE', description='Tipo de devolução em caso de cancelamento.'),
    bigquery.SchemaField('no_DiasDevolucaoCancelamento', 'INTEGER', 'NULLABLE', description='Número de dias para devolução em caso de cancelamento.'),
    bigquery.SchemaField('fl_ValidacaoAdesao', 'BOOLEAN', 'NULLABLE', description='Validação de adesão (true/false).'),
    bigquery.SchemaField('fl_Excluido', 'BOOLEAN', 'NULLABLE', description='Excluído (true/false).'),
    bigquery.SchemaField('fl_PossuiItem', 'INTEGER', 'NULLABLE', description='Possui item (1 para sim, 0 para não).'),
    bigquery.SchemaField('no_Itens', 'INTEGER', 'NULLABLE', description='Número de itens.'),
    bigquery.SchemaField('id_AgrupamentoProdutoSeguro', 'INTEGER', 'NULLABLE', description='ID do agrupamento do produto de seguro.'),
    bigquery.SchemaField('fl_AceitaParcelamento', 'BOOLEAN', 'NULLABLE', description='Aceita parcelamento (true/false).'),
    bigquery.SchemaField('no_MaximoParcelas', 'INTEGER', 'NULLABLE', description='Número máximo de parcelas.'),
    bigquery.SchemaField('no_NOP', 'STRING', 'NULLABLE', description='NOP.'),
    bigquery.SchemaField('dc_TextoNotaFiscal', 'STRING', 'NULLABLE', description='Texto da nota fiscal.'),
    bigquery.SchemaField('cd_IntegracaoAP', 'STRING', 'NULLABLE', description='Código de integração AP.'),
    bigquery.SchemaField('tp_IntegracaoAP', 'STRING', 'NULLABLE', description='Tipo de integração AP.'),
    bigquery.SchemaField('cd_GrupoPagamento', 'STRING', 'NULLABLE', description='Código do grupo de pagamento.'),
    bigquery.SchemaField('dc_GrupoPagamento', 'STRING', 'NULLABLE', description='Descrição do grupo de pagamento.'),
    bigquery.SchemaField('cd_ContaContabil', 'STRING', 'NULLABLE', description='Código da conta contábil.'),
    bigquery.SchemaField('qt_ParcelasCancelamento', 'INTEGER', 'NULLABLE', description='Quantidade de parcelas em caso de cancelamento.'),
    bigquery.SchemaField('fl_NaoEstornarParcelasNaoPagas', 'BOOLEAN', 'NULLABLE', description='Não estornar parcelas não pagas (true/false).'),
    bigquery.SchemaField('fl_PostagemParcelaCorte', 'BOOLEAN', 'NULLABLE', description='Postagem de parcela no corte (true/false).'),
    bigquery.SchemaField('fl_EnvioSeguradoraMensal', 'BOOLEAN', 'NULLABLE', description='Envio para seguradora mensal (true/false).'),
    bigquery.SchemaField('dc_SMS', 'STRING', 'NULLABLE', description='Mensagem SMS.'),
    bigquery.SchemaField('fl_EnvioSMS', 'BOOLEAN', 'NULLABLE', description='Envio de SMS (true/false).'),
    bigquery.SchemaField('fl_permitePrimeiraParcelaPaga', 'BOOLEAN', 'NULLABLE', description='Permite primeira parcela paga (true/false).'),
    bigquery.SchemaField('fl_PermiteResponsavelFinanceiro', 'BOOLEAN', 'NULLABLE', description='Permite responsável financeiro (true/false).'),
    bigquery.SchemaField('fl_PermiteMultiplasAdesoes', 'BOOLEAN', 'NULLABLE', description='Permite múltiplas adesões (true/false).'),
    bigquery.SchemaField('fl_ValidaProdutoVenda', 'BOOLEAN', 'NULLABLE', description='Valida produto de venda (true/false).'),
    bigquery.SchemaField('fl_ValidaNumeroSerieProdutoVenda', 'BOOLEAN', 'NULLABLE', description='Valida número de série do produto de venda (true/false).'),
    bigquery.SchemaField('fl_RestituicaoCancelamento', 'BOOLEAN', 'NULLABLE', description='Restituição em caso de cancelamento (true/false).'),
    bigquery.SchemaField('fl_CalculaParcelaPorItem', 'BOOLEAN', 'NULLABLE', description='Calcula parcela por item (true/false).'),
    bigquery.SchemaField('no_MinimoItens', 'INTEGER', 'NULLABLE', description='Número mínimo de itens.'),
    bigquery.SchemaField('fl_IntegracaoServicoGS', 'BOOLEAN', 'NULLABLE', description='Integração com serviço GS (true/false).'),
    bigquery.SchemaField('id_ProdutoAssociado', 'INTEGER', 'NULLABLE', description='ID do produto associado.'),
    bigquery.SchemaField('fl_PermiteAssociacao', 'BOOLEAN', 'NULLABLE', description='Permite associação (true/false).'),
    bigquery.SchemaField('fl_IntegracaoServicoGSRecorrencia', 'BOOLEAN', 'NULLABLE', description='Integração com serviço GS recorrência (true/false).'),
    bigquery.SchemaField('fl_BonificacaoAntesDoCorte', 'BOOLEAN', 'NULLABLE', description='Bonificação antes do corte (true/false).'),
    bigquery.SchemaField('no_DiasBonificacao', 'INTEGER', 'NULLABLE', description='Número de dias de bonificação.'),
    bigquery.SchemaField('fl_PermiteEstCancSolicitacao', 'BOOLEAN', 'NULLABLE', description='Permite estorno/cancelamento da solicitação (true/false).'),
    bigquery.SchemaField('id_Parceiro', 'INTEGER', 'NULLABLE', description='ID do parceiro.'),
    bigquery.SchemaField('fl_ProdutoNovo', 'BOOLEAN', 'NULLABLE', description='Produto novo (true/false).'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='Data de produção do registro.')
]

# Dataset: pfs_seguros_ssa, Table: produto_venda
produto_venda = [
    bigquery.SchemaField('id_ProdutoVenda', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_Emissor', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('cd_ProdutoVenda', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('nm_ProdutoVenda', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('fl_Ativo', 'BOOLEAN', 'NULLABLE', description='None'),
    bigquery.SchemaField('no_MesesGarantiaFabricante', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('id_NivelProduto', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('nm_Marca', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('nm_Modelo', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('vl_PremioRisco', 'NUMERIC', 'NULLABLE', description='None'),
    bigquery.SchemaField('data_cdcBI', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='None')
]

# Dataset: pfs_seguros_ssa, Table: seguradora
seguradora = [
    bigquery.SchemaField('id_Seguradora', 'INTEGER', 'NULLABLE', description='ID único da seguradora.'),
    bigquery.SchemaField('nm_Seguradora', 'STRING', 'NULLABLE', description='Nome da seguradora.'),
    bigquery.SchemaField('id_Endereco', 'INTEGER', 'NULLABLE', description='ID do endereço da seguradora.'),
    bigquery.SchemaField('fl_Ativo', 'BOOLEAN', 'NULLABLE', description='Ativa (true/false).'),
    bigquery.SchemaField('no_CNPJ', 'STRING', 'NULLABLE', description='CNPJ da seguradora.'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED', description='Data de produção do registro.')
]
