
# Mapeamento dos tipos do schema para os tipos Python
TYPE_MAPPING = {
    "STRING": "str",
    "TIMESTAMP": "datetime",
    # Adicione outros tipos conforme necessário
}


def create_class_code(schema: dict, class_name: str) -> str:
    # importações e configurações iniciais do arquivo 
    class_code = "from pydantic import BaseModel\nfrom datetime import datetime\n\n"
    class_code += f"class {class_name}(BaseModel):\n"

    # construção da classe com Pydantic e BaseModel
    for field_name, field_type in schema.items():
        python_type = TYPE_MAPPING.get(field_type)
        class_code += f"    {field_name}: {python_type}\n"

    return class_code


def write_class_to_file(schema: dict, class_name: str, file_path: str):
    # Gerar o código da classe
    class_code = create_class_code(schema, class_name)

    # Escrever o código da classe no arquivo models.py
    with open(file_path, "w") as file:
        file.write(class_code)


# Exemplo de schema
schema =     {
        "id_cartao": "STRING",
        "id_produto_cartao": "STRING",
        "num_cartao": "STRING",
        "num_seq_via_cartao": "STRING",
        "id_conta": "STRING",
        "num_cpf_cliente": "STRING",
        "cod_tip_portador": "STRING",
        "num_bin": "STRING",
        "cod_loja_emis_cartao": "STRING",
        "id_cliente_so": "STRING",
        "dth_emis_cartao": "TIMESTAMP",
        "dth_embs_cartao": "TIMESTAMP",
        "dth_valid_cartao": "TIMESTAMP",
        "dth_desbloqueio": "TIMESTAMP",
        "cod_sit_cartao": "STRING",
        "des_sit_cartao": "STRING",
        "dth_sit_cartao": "TIMESTAMP",
        "cod_estagio_cartao": "STRING",
        "des_estagio_cartao": "STRING",
        "dth_estagio_cartao": "TIMESTAMP",
        "flg_embs_loja": "STRING",
        "flg_cartao_cancelado": "STRING",
        "flg_cartao_provisorio": "STRING",
        "flg_conta_cancelada": "STRING",
        "dth_ult_atu_so": "TIMESTAMP",
        "num_seq_ult_alteracao": "STRING",
        "dth_inclusao_reg": "TIMESTAMP",
        "pt_nomeplastico": "STRING",
        "ca_arquivolote": "STRING",
        "ca_id_imagem": "STRING",
        "bc_responsavel": "STRING",
        "ca_codigocancelamento": "STRING",
        "ca_flaggeracartasenha": "STRING",
        "pt_id_imagem": "STRING"
    }

# Nome da classe e caminho do arquivo
class_name = "CartaoModel"
file_path = "models.py"

# Gerar e escrever a classe no arquivo models.py
write_class_to_file(schema, class_name, file_path)
