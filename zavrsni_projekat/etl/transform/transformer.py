from sklearn.preprocessing import StandardScaler

def prices_above_50000(df):
    
    return df[df["price"] > 50000]

def convert_living_sqft_to_sqm(df, column="sqft_living", new_column="sqm_living"):
    
    df[new_column] = df[column] * 0.092903
    return df

def convert_lot_sqft_to_sqm(df, column="sqft_lot", new_column="sqm_lot"):
    
    df[new_column] = df[column] * 0.092903
    return df

def convert_above_sqft_to_sqm(df, column="sqft_above", new_column="sqm_above"):
    
    df[new_column] = df[column] * 0.092903
    return df

def convert_basement_sqft_to_sqm(df, column="sqft_basement", new_column="sqm_basement"):
    
    df[new_column] = df[column] * 0.092903
    return df

def round_sqm_living(df, column="sqm_living"):
   
    df[column] = df[column].round(2)
    return df

def round_sqm_lot(df, column="sqm_lot"):
   
    df[column] = df[column].round(2)
    return df

def round_sqm_above(df, column="sqm_above"):
   
    df[column] = df[column].round(2)
    return df

def round_sqm_basement(df, column="sqm_basement"):
   
    df[column] = df[column].round(2)
    return df

def drop_column(df, columns):
    return df.drop(columns=columns)

def select_round_rows(df):
    return df[
        (df['bedrooms'] % 1 == 0) &
        (df['bathrooms'] % 1 == 0) &
        (df['floors'] % 1 == 0)
    ]

def full_transform(df):
    df = prices_above_50000(df)
    df = convert_living_sqft_to_sqm(df)
    df = convert_lot_sqft_to_sqm(df)
    df = convert_above_sqft_to_sqm(df)
    df = convert_basement_sqft_to_sqm(df)
    df = round_sqm_living(df)
    df = round_sqm_lot(df)
    df = round_sqm_above(df)
    df = round_sqm_basement(df)
    df = drop_column(df, ["id", "date", "sqft_living", "sqft_lot", "sqft_above", "sqft_basement", "zipcode", "lat", "long", "sqft_living15", "sqft_lot15"])
    df = select_round_rows(df)
    return df
