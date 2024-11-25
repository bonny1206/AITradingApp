# Questo file rende la cartella 'api' un pacchetto Python.
# Puoi lasciare questo file vuoto, oppure aggiungere codice di inizializzazione se necessario.
from .api import get_historical_data, get_all_symbols
from .database import create_database, save_to_database
from .preprocessing.cleaning import clean_data
from .sentiment.news_sentiment import analyze_sentiment
