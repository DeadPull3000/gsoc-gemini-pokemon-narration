# Ecosystem Database Schema

Although the entry task utilizes a simple JSON structure, a production-ready application will require a normalized relational database schema. 

## Entity Relationship Diagram
We use Mermaid.js to visualize the underlying ecosystem relationships.

```mermaid
erDiagram
    TRAINER {
        int id PK
        string name
        string region
    }
    POKEMON {
        int id PK
        string species
        string type
    }
    LOCATION {
        int id PK
        string name
        string environment_type
    }
    EVENT {
        int id PK
        timestamp occurred_at
        int trainer_id FK
        int pokemon_id FK
        int location_id FK
        string action
        string outcome
    }

    TRAINER ||--o{ EVENT : "participates in"
    POKEMON ||--o{ EVENT : "involved in"
    LOCATION ||--o{ EVENT : "hosts"