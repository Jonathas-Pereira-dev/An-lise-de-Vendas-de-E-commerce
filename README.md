# Pipeline de dados automatizado para análise de vendas

## Contexto do Negócio

Este projeto simula um cenário real de uma empresa de e-commerce que necessita estruturar e automatizar o processamento de dados de vendas para apoiar a tomada de decisão.

O foco não é apenas análise, mas a construção de um pipeline de dados confiável, capaz de transformar dados brutos em informações analíticas consistentes e reutilizáveis.

Principais perguntas respondidas:

- Como as vendas evoluem ao longo do tempo?
- Quais produtos e categorias geram mais receita?
- Quem são os clientes mais valiosos?
- Qual é o ticket médio das vendas?

## Objetivo Técnico

- Estruturar um pipeline de dados (ETL) completo
- Automatizar o fluxo de ingestão e transformação
- Garantir qualidade e confiabilidade dos dados
- Criar uma base analítica escalável

## Stack Utilizada

* **Python**: ingestão e tratamento inicial dos dados (ETL)
* **PostgreSQL**: banco de dados analítico
* **SQL**: consultas e análises
* **dbt Core**: modelagem de dados, testes e documentação

## Arquitetura do Projeto
O pipeline foi estruturado de forma modular, permitindo execução automatizada e fácil manutenção.

![pics](https://github.com/Jonathas-Pereira-dev/An-lise-de-Vendas-de-E-commerce/blob/main/pics/arquitetura.png)

Os dados são carregados inicialmente no PostgreSQL em formato bruto. Em seguida, o dbt Core é utilizado para transformar esses dados em modelos analíticos confiáveis, seguindo boas práticas de engenharia analítica.

## Pipeline de Dados

O fluxo de dados segue as seguintes etapas:

1. Ingestão de dados brutos via scripts Python
2. Armazenamento inicial no PostgreSQL
3. Transformação e limpeza com dbt (camada staging)
4. Modelagem analítica (camada marts)
5. Validação e testes de qualidade

## Modelagem de Dados

A modelagem segue o padrão analítico com separação entre staging e marts.

### Staging

Camada responsável pela limpeza e padronização dos dados:

* `stg_orders`
* `stg_customers`
* `stg_products`
* `stg_payments`

Principais tratamentos:

* Padronização de nomes e tipos de dados
* Remoção de duplicidades
* Tratamento de valores nulos

### Marts

Camada focada em negócio, com tabelas prontas para análise:

**Dimensões**

* `dim_customers`
* `dim_products`
* `dim_date`

**Fato**

* `fact_sales`

*A documentação completa da modelagem pode ser visualizada através do `dbt docs`, conforme exemplo abaixo.*

> **Print do dbt docs**: *(inserir aqui imagem gerada pelo comando `dbt docs generate`)*

## Métricas Geradas

As principais métricas de negócio calculadas neste projeto são:

* Receita total
* Receita mensal
* Quantidade de pedidos
* Ticket médio
* Top 10 produtos por faturamento
* Faturamento por categoria
* Top clientes por valor gasto

Essas métricas permitem analisar o desempenho do e-commerce e identificar oportunidades de crescimento.

## Qualidade e Testes de Dados

Foram implementados testes de qualidade utilizando o **dbt**, como:

* `not_null`
* `unique`

Exemplos:

* `order_id` não pode ser nulo
* `customer_id` deve ser único
* Valor do pedido maior que zero

---

## Como Rodar o Projeto

### Pré-requisitos

* Python 3.10+
* PostgreSQL
* dbt Core
* Git

### 2️⃣ Criar e ativar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

### 3️⃣ Instalar dependências

```bash
poetry install -r requirements.txt
```

### 4️⃣ Executar ETL (Python)

```bash
python etl/ingest_data.py
```

### 5️⃣ Rodar transformações com dbt

```bash
dbt run
dbt test
dbt docs generate
dbt docs serve
```

### 6️⃣ Consultar métricas

As consultas SQL estão disponíveis na pasta `sql/` e podem ser executadas diretamente no PostgreSQL.

## 7️⃣ Considerações Finais

Ele demonstra habilidades em SQL, modelagem de dados, dbt Core, organização de projetos e entendimento de métricas de negócio.

## Automação e Escalabilidade

O projeto foi pensado para evolução em ambientes reais, com possibilidade de:

- Execução automatizada do pipeline
- Monitoramento de falhas- Integração com ferramentas de orquestração (ex: n8n, Airflow)