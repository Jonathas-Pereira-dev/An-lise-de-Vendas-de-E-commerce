import subprocess

def run_etl():
    print("Executando ETL...")
    subprocess.run(["python", "etl/ingest_data.py"], check=True)

def run_dbt():
    print("Executando dbt...")
    subprocess.run(["dbt", "run"], check=True)
    subprocess.run(["dbt", "test"], check=True)

if __name__ == "__main__":
    try:
        run_etl()
        run_dbt()
        print("Pipeline executado com sucesso!")
    except Exception as e:
        print(f"Erro no pipeline: {e}")