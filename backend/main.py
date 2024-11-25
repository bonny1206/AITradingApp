import os
import pandas as pd
from backend.data.api.api import get_historical_data, get_all_symbols
from backend.data.api.sentiment.news_sentiment import get_sentiment_analysis
from backend.data.api.preprocessing.cleaning import clean_data
from backend.data.api.preprocessing.feature_engineering import add_technical_indicators
from backend.patterns.pattern_recognition import detect_patterns
from backend.models.ml_model import train_model, make_prediction
from backend.data.api.database.database import create_database, save_to_database
from datetime import datetime


def main():
    # Configura il database (se necessario)
    database_url = os.getenv("DATABASE_URL", "sqlite:///trading_data.db")
    create_database(database_url)

    # Recupera simboli dei titoli (per esempio, scegliamo solo alcuni simboli per testare)
    symbols = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
    all_data = {}

    for symbol in symbols:
        print(f"Recuperando i dati storici per {symbol}...")
        try:
            # Ottieni i dati storici da Yahoo Finance
            df = get_historical_data(symbol)
            print(f"Dati storici per {symbol} recuperati con successo.")

            # Pulisci i dati
            cleaned_data = clean_data(df)

            # Aggiungi indicatori tecnici (RSI, MACD, SMA, etc.)
            data_with_indicators = add_technical_indicators(cleaned_data)

            # Rileva pattern grafici
            pattern = detect_patterns(data_with_indicators)
            print(f"Pattern rilevato per {symbol}: {pattern}")

            # Recupera l'analisi del sentiment delle notizie relative al simbolo
            sentiment = get_sentiment_analysis(symbol)
            print(f"Sentiment per {symbol}: {sentiment}")

            # Salva i dati nel database
            save_to_database(symbol, data_with_indicators)

            # Aggiungi i dati al dizionario
            all_data[symbol] = {
                'data': data_with_indicators,
                'pattern': pattern,
                'sentiment': sentiment
            }

            # Allenamento del modello di previsione (se necessario)
            # (Nota: potresti voler eseguire questa parte solo una volta al giorno)
            model = train_model(all_data)

            # Fare una previsione
            prediction = make_prediction(model, symbol)
            print(f"Previsione per {symbol}: {prediction}")

        except Exception as e:
            print(f"Errore durante il trattamento del simbolo {symbol}: {e}")
    
    # Termina il processo
    print("Flusso di lavoro completato.")


if __name__ == "__main__":
    main()
