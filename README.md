# Mock-Data for BigQuery 

![Python](https://img.shields.io/badge/Python-3.12.6-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.114.1-teal?logo=fastapi)
![Static Badge](https://img.shields.io/badge/Pub%2FSub-1.7.0-blue?style=flat)
![Pytest](https://img.shields.io/badge/Pytest-8.3.3-yellow?logo=pytest)
![Ruff](https://img.shields.io/badge/Ruff-0.6.5-blue?logo=python)
![Taskipy](https://img.shields.io/badge/Taskipy-1.13.0-green?logo=taskipy)

![logo](/img/applogo.png)


#### Esta aplicação gera e dispara eventos com dados 'mockados' para seram usados na pipeline analítica BigQuery/Dataform


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

