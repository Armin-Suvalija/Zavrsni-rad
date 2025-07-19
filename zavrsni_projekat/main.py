from etl.extract.extractor import load_dataset
from etl.transform.transformer import full_transform
from etl.load.loader import load_to_mssql
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os
import subprocess

dataset_path = "data/house_data.csv"
table_name = "housing_price_data"
connection_string = "mssql+pyodbc://armin:123456@HP-VICTUS-16\\SQLEXPRESS/housing_price_data?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

df = load_dataset(dataset_path)
df_clean = full_transform(df)
load_to_mssql(df_clean, table_name, connection_string)

def run_notebook(notebook_path):
    print(f"Running notebook: {notebook_path} ...")

    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name="venv")
    try:
        ep.preprocess(nb, {"metadata": {"path": os.path.dirname(notebook_path)}})
    except Exception as e:
        print(f"Error executing {notebook_path}: {e}")
        raise

    with open(notebook_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    print(f"Finished notebook: {notebook_path}")

run_notebook("analysis/eda.ipynb")
run_notebook("ml/train_model.ipynb")

print("📊 Running queries...")
subprocess.run(["python", "analysis/queries.py"], check=True)

print("✅ All steps completed successfully.")
