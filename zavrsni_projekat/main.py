from src.extract.extractor import load_dataset
from src.transform.transformer import clean_dataset
from src.load.loader import load_to_mssql

dataset_path = "data/students_performance.csv"
table_name = "students"
connection_string = "mssql+pyodbc://USERNAME:PASSWORD@HOSTNAME/DBNAME?driver=ODBC+Driver+17+for+SQL+Server"

df = load_dataset(dataset_path)
df_clean = clean_dataset(df)
load_to_mssql(df_clean, table_name, connection_string)