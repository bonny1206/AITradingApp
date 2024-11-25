import yfinance as yf
import pandas as pd
from datetime import datetime

def get_historical_data(symbol, start_date="2000-01-01", end_date=None):
    """
    Ottiene i dati storici di un titolo da Yahoo Finance.
    
    Args:
        symbol (str): Il simbolo del titolo (es. "AAPL").
        start_date (str): La data di inizio per i dati storici (formato YYYY-MM-DD).
        end_date (str): La data finale per i dati storici (formato YYYY-MM-DD). Se None, usa la data corrente.
        
    Returns:
        pd.DataFrame: Dataframe con i dati storici (Open, High, Low, Close, Volume, Dividendi, Stock Splits).
    """
    if end_date is None:
        end_date = datetime.today().strftime('%Y-%m-%d')
    
    # Recupera i dati dal simbolo specificato
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    
    # Rinomina le colonne per uniformità
    stock_data.rename(columns={
        "Open": "Open",
        "High": "High",
        "Low": "Low",
        "Close": "Close",
        "Adj Close": "Adjusted Close",
        "Volume": "Volume"
    }, inplace=True)
    
    return stock_data

def get_all_symbols():
    """
    Recupera una lista di simboli azionari da Yahoo Finance.
    
    Returns:
        list: Una lista di simboli (ad esempio, ["AAPL", "GOOGL", "MSFT"]).
    """
    # Esempio di lista di simboli. Questo potrebbe essere esteso in base alla tua logica.
    symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
    return symbols

def get_stock_info(symbol):
    """
    Recupera informazioni di base su un'azione, come il nome e il settore.
    
    Args:
        symbol (str): Il simbolo del titolo.
        
    Returns:
        dict: Un dizionario con informazioni sul titolo.
    """
    stock = yf.Ticker(symbol)
    info = stock.info
    return {
        "symbol": symbol,
        "name": info.get("longName", "N/A"),
        "sector": info.get("sector", "N/A"),
        "industry": info.get("industry", "N/A"),
        "marketCap": info.get("marketCap", "N/A")
    }
