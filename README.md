# Mock-Data for BigQuery 

![Python](https://img.shields.io/badge/Python-3.12.6-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.114.1-teal?logo=fastapi)
![Pytest](https://img.shields.io/badge/Pytest-8.3.3-yellow?logo=pytest)
![Ruff](https://img.shields.io/badge/Ruff-0.6.5-blue?logo=python)
![Taskipy](https://img.shields.io/badge/Taskipy-1.13.0-green?logo=taskipy)

![logo](/img/applogo.png)


 Esta aplicação gera e dispara eventos com dados 'mockados' para seram usados na pipeline analítica BigQuery/Dataform

 ****

### Arquitetura

```mermaid
graph LR

    o1[Mock-Data App]

    subgraph Mock Tables
        o3[BigQuery]
        o4[Dataform]
    end

    o1 --> o3
    o3 --> o4
```
****

### Funcionamento 

**Publicação:**

A aplicação Mock-Data gera dados e os envia para o `Tópico` existente. Esses dados podem ser de qualquer tipo, desde eventos simples até grandes volumes de dados estruturados.

**Distribuição:**

Quando uma nova mensagem é publicada no `Tópico`, o sistema de `Pub/Sub` a distribui para todos os `Subscribers` inscritos.

**Assinatura:**

O `Dataform` e o `BigQuery` se inscrevem no mesmo `Tópico`, indicando que vão receber as mensagens publicadas. Cada um pode ter suas próprias lógicas e regras de negócios para o processamento e filtros para os dados.


**Consumo:**

Cada `Subscriber` processa a mensagem de forma independente. O `Dataform` pode, por exemplo, armazenar os dados em um data warehouse, enquanto o `BigQuery` pode realizar análises complexas e criar views sobre os dados obtidos.
