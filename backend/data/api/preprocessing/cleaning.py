import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def clean_data(df):
    """
    Pulisce i dati rimuovendo i valori nulli e i duplicati.
    
    Args:
        df (pandas.DataFrame): Dati da pulire.
    
    Returns:
        pandas.DataFrame: Dati puliti.
    """
    # Rimuove i duplicati
    df = df.drop_duplicates()

    # Rimuove le righe con valori nulli
    df = df.dropna()

    # Restituisce il dataframe pulito
    return df

def normalize_data(df):
    """
    Normalizza i dati (scalando i valori tra 0 e 1).
    
    Args:
        df (pandas.DataFrame): Dati da normalizzare.
    
    Returns:
        pandas.DataFrame: Dati normalizzati.
    """
    # Seleziona le colonne numeriche per la normalizzazione
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Inizializza il MinMaxScaler
    scaler = MinMaxScaler()
    
    # Applica la normalizzazione
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df

def fill_missing_data(df):
    """
    Compensa i dati mancanti con la media della colonna.
    
    Args:
        df (pandas.DataFrame): Dati da processare.
    
    Returns:
        pandas.DataFrame: Dati con valori mancanti riempiti.
    """
    # Riempi i valori mancanti con la media della colonna
    df = df.fillna(df.mean())
    
    return df

