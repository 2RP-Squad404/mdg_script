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


###### Mock-Data App:

Esta aplicação gera dados mockados para alimentar as tabelas já existentes, seguindo o mesmo `schema`. O dados são gerados a partir da biblioteca `Faker` que possui opções diversificadas para geração de dados conforme a necessidade da aplicação. 

