import subprocess
import sys

def run_etl():
    print("Executando ETL...")
    subprocess.run([sys.executable, "etl/ingest_data.py"], check=True)

def run_dbt():
    print("Executando dbt...")
    subprocess.run([sys.executable, "-m", "dbt", "run"], check=True)
    subprocess.run([sys.executable, "-m", "dbt", "test"], check=True)

if __name__ == "__main__":
    try:
        run_etl()
        run_dbt()
        print("Pipeline executado com sucesso!")
    except Exception as e:
        print(f"Erro no pipeline: {e}")