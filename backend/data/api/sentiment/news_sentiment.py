from textblob import TextBlob
import requests

# Funzione per analizzare il sentiment delle notizie
def analyze_sentiment(news_text):
    """
    Analizza il sentiment del testo delle notizie.
    Ritorna il sentiment come positivo, negativo o neutro.
    
    Args:
        news_text (str): Il testo della notizia da analizzare.

    Returns:
        str: 'Positivo', 'Negativo' o 'Neutro'
    """
    # Crea un oggetto TextBlob
    blob = TextBlob(news_text)
    
    # Calcola il polarità del sentiment (-1 è negativo, +1 è positivo)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        return "Positivo"
    elif polarity < 0:
        return "Negativo"
    else:
        return "Neutro"

# Funzione per ottenere le notizie tramite un'API (ad esempio, NewsAPI)
def get_news_for_symbol(symbol, api_key):
    """
    Ottiene le notizie più recenti per un simbolo specifico tramite NewsAPI.
    
    Args:
        symbol (str): Il simbolo del titolo (es. 'AAPL', 'GOOGL').
        api_key (str): La chiave API per NewsAPI.
    
    Returns:
        list: Una lista di notizie (ogni notizia è un dizionario con titolo e contenuto).
    """
    url = f'https://newsapi.org/v2/everything?q={symbol}&apiKey={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json()['articles']
        news_data = []
        
        for article in articles:
            news_item = {
                'title': article['title'],
                'description': article['description'],
                'content': article['content']
            }
            news_data.append(news_item)
        
        return news_data
    else:
        raise Exception(f"Errore nel recupero delle notizie: {response.status_code}")

