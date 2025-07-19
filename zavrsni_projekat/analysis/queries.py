from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine("mssql+pyodbc://armin:123456@HP-VICTUS-16\\SQLEXPRESS/housing_price_data?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes")  # zamijeni ako koristiš drugu bazu

queries = {
    "1. Svi podaci": "SELECT * FROM housing_price_data",
    "2. Prosječna cijena": "SELECT AVG(price) AS average_price FROM housing_price_data",
    "3. Top 5 najskupljih kuća": "SELECT TOP 5 * FROM housing_price_data ORDER BY price DESC",
    "4. Broj kuća sa podrumom": "SELECT COUNT(*) AS houses_with_basement FROM housing_price_data WHERE sqm_basement > 0",
    "5. Broj kuća na vodi": "SELECT COUNT(*) AS waterfront_properties FROM housing_price_data WHERE waterfront > 0",
    "6. Broj kuća po deceniji": """
        SELECT 
            (yr_built / 10) * 10 AS decade_built, 
            COUNT(*) AS properties_built 
        FROM housing_price_data 
        GROUP BY (yr_built / 10) * 10 
        ORDER BY decade_built
    """,
    "7. Najnovija godina izgradnje": "SELECT MAX(yr_built) AS newest_year_built FROM housing_price_data"
}


with engine.connect() as conn:
    for description, query in queries.items():
        print(f"\n🔹 {description}")
        if query is None:
            print("Preskočeno (nije primjenjivo).")
            continue

        result = pd.read_sql(text(query), conn)
        print(result)
