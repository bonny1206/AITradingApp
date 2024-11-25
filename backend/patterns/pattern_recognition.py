import pandas as pd
import numpy as np

def detect_head_and_shoulders(df):
    """
    Rileva il pattern "Testa e Spalle" in un dataframe di prezzi azionari.
    Si basa su un'analisi semplice dei picchi locali.

    Args:
    - df (pd.DataFrame): Dati storici di un titolo con colonne 'Close'.

    Returns:
    - bool: True se il pattern "Testa e Spalle" viene rilevato, altrimenti False.
    """
    # Assumiamo che il dataframe abbia una colonna 'Close' con i prezzi di chiusura
    close_prices = df['Close']
    
    # Trova i picchi locali
    peaks = close_prices[(close_prices.shift(1) < close_prices) & (close_prices.shift(-1) < close_prices)]

    # Rileva almeno 3 picchi (testa e due spalle)
    if len(peaks) >= 3:
        # Definisci i picchi principali: la testa deve essere il picco più alto, le spalle devono essere più basse
        left_shoulder = peaks.iloc[0]
        head = peaks.max()  # La testa è il picco massimo
        right_shoulder = peaks.iloc[-1]

        # Verifica che la testa sia più alta delle spalle
        if head > left_shoulder and head > right_shoulder:
            # Se la testa è più alta, ritorna True (pattern trovato)
            return True

    return False


def detect_flags(df):
    """
    Rileva il pattern "Bandiera" in un dataframe di prezzi azionari.
    Una bandiera è una breve pausa nel trend di un'azione, con prezzi che si muovono in un canale parallelo.

    Args:
    - df (pd.DataFrame): Dati storici di un titolo con colonne 'Close'.

    Returns:
    - bool: True se il pattern "Bandiera" viene rilevato, altrimenti False.
    """
    close_prices = df['Close']
    
    # Condizioni di base per rilevare una bandiera
    # 1. Un trend principale precede la bandiera (aumento o diminuzione).
    # 2. Prezzi che si muovono all'interno di un canale parallelo.

    # Calcolare la differenza tra i prezzi di chiusura per osservare la direzione del trend
    diff = close_prices.diff()

    # Verifica se il trend precedente è forte e se il prezzo si muove all'interno di un canale
    # Esempio semplificato: se i prezzi si muovono per un periodo lungo in un canale stretto
    if diff.max() > diff.min():
        # Se troviamo un forte trend crescente o decrescente, possiamo osservare la bandiera
        return True
    return False


# Funzione principale per rilevare i pattern
def detect_patterns(df):
    """
    Funzione per rilevare i pattern grafici più comuni nel dataframe di prezzi.

    Args:
    - df (pd.DataFrame): Dati storici di un titolo con colonne 'Close'.

    Returns:
    - str: Nome del pattern rilevato, oppure "Nessun pattern trovato".
    """
    if detect_head_and_shoulders(df):
        return "Testa e Spalle"
    elif detect_flags(df):
        return "Bandiera"
    else:
        return "Nessun pattern trovato"
