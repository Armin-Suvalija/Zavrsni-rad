# 🏡 Housing Price Analysis & Prediction

Ovaj projekat predstavlja **krajni ETL + Data Science pipeline** za analizu i predikciju cijena kuća korištenjem **housing\_data** skupa podataka. Kombinuje **ETL obradu**, **eksploratornu analizu**, **treniranje modela mašinskog učenja**, i **SQL analize**.

---

## 📁 Struktura Projekta

```
zavrsni_projekat/
├── data/                          # Ulazni CSV fajlovi
├── etl/                           # ETL moduli (Extract, Transform, Load)
│   ├── extract/
│   │   └── extractor.py
│   ├── transform/
│   │   └── transformer.py
│   └── load/
│       └── loader.py
├── analysis/                      
│   ├── eda.ipynb                  # Exploratory Data Analysis u Jupyteru
│   └── queries.py                 # SQL upiti za analizu iz baze
├── ml/                            
│   └── train_model.ipynb          # Treniranje ML modela za predikciju cijene
├── requirements.txt              # Lista Python biblioteka
├── main.py                        # Glavna skripta koja pokreće pipeline
└── README.md                      # Dokumentacija projekta
```

---

## ✅ Funkcionalnosti

- ✔️ **ETL pipeline**: Učitavanje CSV fajla, čišćenje i transformacija podataka, i učitavanje u SQL Server.
- ✔️ **EDA**: Vizualizacije i statistička analiza u `eda.ipynb`.
- ✔️ **Machine Learning**: Treniranje modela za predikciju cijena kuća u `train_model.ipynb`.
- ✔️ **SQL analize**: Automatsko pokretanje ključnih SQL upita kroz `queries.py`.

---

## 🚀 Pokretanje projekta

### 1. Kloniraj repozitorij

```bash
git clone https://github.com/Armin-Suvalija/Zavrsni-rad.git
cd Zavrsni-rad
```

### 2. Kreiraj virtuelno okruženje

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
# ili
source .venv/bin/activate      # Linux/macOS
```

### 3. Instaliraj biblioteke

```bash
pip install -r requirements.txt
```

### 4. Provjeri da SQL Server radi

Projekat koristi MSSQL Express. Provjeri da ti lokalni SQL Server radi i da imaš odgovarajući **ODBC drajver 18** instaliran.

### 5. Pokreni glavnu skriptu

```bash
python main.py
```

Skripta će automatski:

1. Učitati podatke iz `data/house_data.csv`
2. Očistiti i transformisati ih
3. Učitati podatke u SQL Server (`housing_price_data` tabela)
4. Pokrenuti `eda.ipynb` i `train_model.ipynb`
5. Izvršiti SQL upite iz `analysis/queries.py`

---

## 🧪 Primer SQL upita

U `analysis/queries.py` definišu se upiti poput:

- Prosječna cijena kuće
- Broj kuća sa podrumom
- Broj kuća na vodi
- Broj izgrađenih kuća po deceniji
- Top 5 najskupljih kuća

---
