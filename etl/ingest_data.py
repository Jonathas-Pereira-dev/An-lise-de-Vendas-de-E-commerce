import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("postgresql://user:password@localhost:5432/ecommerce")


df_orders = pd.read_csv("data/orders.csv")
df_customers = pd.read_csv("data/customers.csv")


df_orders.to_sql("orders_raw", engine, if_exists="replace", index=False)
df_customers.to_sql("customers_raw", engine, if_exists="replace", index=False)


print("Dados carregados com sucesso")