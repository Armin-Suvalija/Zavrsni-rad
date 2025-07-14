from etl.extract.extractor import load_dataset
from etl.transform.transformer import full_transform
from etl.load.loader import load_to_mssql

dataset_path = "data/house_data.csv"
table_name = "housing_price_data"
connection_string = "mssql+pyodbc://armin:123456@HP-VICTUS-16\\SQLEXPRESS/housing_price_data?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

df = load_dataset(dataset_path)
df_clean = full_transform(df)
load_to_mssql(df_clean, table_name, connection_string)