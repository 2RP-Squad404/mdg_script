# Mock-Data for BigQuery 

![Python](https://img.shields.io/badge/Python-3.12.6-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.114.1-teal?logo=fastapi)
![Static Badge](https://img.shields.io/badge/Pub%2FSub-1.7.0-blue?style=flat)
![Pytest](https://img.shields.io/badge/Pytest-8.3.3-yellow?logo=pytest)
![Ruff](https://img.shields.io/badge/Ruff-0.6.5-blue?logo=python)
![Taskipy](https://img.shields.io/badge/Taskipy-1.13.0-green?logo=taskipy)

![logo](/img/applogo.png)


 Esta aplicação gera e dispara eventos com dados 'mockados' para seram usados na pipeline analítica BigQuery/Dataform

 ****

### Arquitetura

```mermaid
graph LR

    subgraph Publisher
        o1[Mock-Data App]
    end

    o2[Topic]
    o5[Subscriptions 1]
    o6[Subscriptions 2]
    o7(Schema)

    subgraph Subscriber
        o3[BigQuery]
        o4[Dataform]
    end

    o1 --> o2
    o2 --> o5
    o2 --> o6

    o5 --> o4
    o5 --> o3
    o6 --> o3
    o2 <-.-> o7
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
