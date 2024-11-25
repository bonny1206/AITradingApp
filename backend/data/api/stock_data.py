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
        pd.DataFrame: DataFrame con i dati storici (Open, High, Low, Close, Volume, Dividendi, Stock Splits).
    """
    if end_date is None:
        end_date = datetime.today().strftime('%Y-%m-%d')
    
    # Scarica i dati storici
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


def save_stock_data_to_csv(symbol, start_date="2000-01-01", end_date=None, file_name=None):
    """
    Ottiene i dati storici di un titolo e li salva in un file CSV.
    
    Args:
        symbol (str): Il simbolo del titolo (es. "AAPL").
        start_date (str): La data di inizio per i dati storici (formato YYYY-MM-DD).
        end_date (str): La data finale per i dati storici (formato YYYY-MM-DD).
        file_name (str): Il nome del file CSV dove salvare i dati. Se None, usa il simbolo del titolo.
    """
    stock_data = get_historical_data(symbol, start_date, end_date)
    
    if file_name is None:
        file_name = f"{symbol}_historical_data.csv"
    
    # Salva i dati in un file CSV
    stock_data.to_csv(file_name)
    print(f"Dati per {symbol} salvati in {file_name}")


def load_stock_data_from_csv(file_name):
    """
    Carica i dati storici da un file CSV in un DataFrame.
    
    Args:
        file_name (str): Il nome del file CSV da caricare.
        
    Returns:
        pd.DataFrame: DataFrame con i dati storici letti dal CSV.
    """
    stock_data = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return stock_data


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
