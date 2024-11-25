import pandas as pd
import numpy as np

def calculate_rsi(df, period=14):
    """
    Calcola il Relative Strength Index (RSI) per i dati del titolo.
    
    Args:
        df (pandas.DataFrame): Dati storici del titolo (deve includere una colonna 'Close').
        period (int): Periodo per il calcolo del RSI, default 14.
    
    Returns:
        pandas.Series: RSI calcolato.
    """
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

def calculate_macd(df, short_period=12, long_period=26, signal_period=9):
    """
    Calcola il MACD (Moving Average Convergence Divergence) per i dati del titolo.
    
    Args:
        df (pandas.DataFrame): Dati storici del titolo (deve includere una colonna 'Close').
        short_period (int): Periodo della media mobile corta, default 12.
        long_period (int): Periodo della media mobile lunga, default 26.
        signal_period (int): Periodo della media mobile di segnale, default 9.
    
    Returns:
        pandas.DataFrame: MACD, Signal e Histogram.
    """
    short_ema = df['Close'].ewm(span=short_period, adjust=False).mean()
    long_ema = df['Close'].ewm(span=long_period, adjust=False).mean()
    
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_period, adjust=False).mean()
    histogram = macd - signal
    
    return pd.DataFrame({'MACD': macd, 'Signal': signal, 'Histogram': histogram})

def calculate_sma(df, window=50):
    """
    Calcola la media mobile semplice (SMA) per i dati del titolo.
    
    Args:
        df (pandas.DataFrame): Dati storici del titolo (deve includere una colonna 'Close').
        window (int): Periodo per il calcolo della SMA, default 50.
    
    Returns:
        pandas.Series: SMA calcolato.
    """
    sma = df['Close'].rolling(window=window).mean()
    return sma

def create_features(df):
    """
    Crea nuove feature per il modello di trading aggiungendo gli indicatori tecnici.
    
    Args:
        df (pandas.DataFrame): Dati storici del titolo.
    
    Returns:
        pandas.DataFrame: Dati con le nuove feature.
    """
    # Calcola gli indicatori tecnici
    df['RSI'] = calculate_rsi(df)
    df['MACD'], df['Signal'], df['Histogram'] = calculate_macd(df).T
    df['SMA_50'] = calculate_sma(df, window=50)
    df['SMA_200'] = calculate_sma(df, window=200)
    
    # Restituisce il DataFrame con le nuove feature
    return df
