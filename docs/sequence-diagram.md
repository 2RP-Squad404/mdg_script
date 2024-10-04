# **Diagrama de sequência**:

```mermaid
sequenceDiagram
    participant App as MDG Script
    participant SM as Secret Manager API
    participant BQ as BigQuery API
    participant Tables as Tabelas do BigQuery

    App->>SM: Autentica conta de serviço
    SM-->>App: Retorna secret_id autenticado 

    App->>BQ: Importa schemas
    BQ-->>App: Retorna mapeamento dos schemas em JSON

    App->>App: Gera classes automaticamente a partir dos schemas

    App->>App: Gera e retorna dados mock utilizando Faker simulando dados reais

    App->>Tables: Envia dados mock para as tabelas no BigQuery
    Tables-->>App: Confirma envio dos dados

```

----

### [**> Voltar página.**](/README.md)