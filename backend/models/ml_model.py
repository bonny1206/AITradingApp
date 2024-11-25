import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Funzione per preparare i dati (normalizzazione e creazione delle feature)
def prepare_data(data, time_step=60):
    """
    Prepara i dati per l'addestramento del modello, creando sequenze temporali.
    
    Args:
        data (pd.DataFrame): Dati storici delle azioni.
        time_step (int): Numero di giorni da considerare come sequenza (default 60 giorni).
        
    Returns:
        X (np.array): Caratteristiche (features) per il modello.
        y (np.array): Etichette (labels) per il modello.
    """
    # Normalizza i dati (solo la colonna 'Close' per la previsione del prezzo)
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data[['Close']])
    
    # Crea le sequenze di dati per addestrare il modello
    X, y = [], []
    for i in range(time_step, len(data_scaled)):
        X.append(data_scaled[i-time_step:i, 0])  # Sequenze temporali di X
        y.append(data_scaled[i, 0])  # Valore futuro di y
    
    X, y = np.array(X), np.array(y)
    
    # Reshape X per la rete neurale (samples, time_steps, features)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    
    return X, y, scaler


# Funzione per creare il modello di rete neurale
def create_model(input_shape):
    """
    Crea e compila il modello di rete neurale per la previsione del prezzo.
    
    Args:
        input_shape (tuple): Forma dei dati di input (time_steps, features).
        
    Returns:
        model (tf.keras.Model): Il modello di rete neurale.
    """
    model = Sequential()
    model.add(tf.keras.layers.LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(tf.keras.layers.LSTM(units=50, return_sequences=False))
    model.add(tf.keras.layers.Dense(units=25))
    model.add(tf.keras.layers.Dense(units=1))  # Previsione del prezzo futuro
    
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')
    
    return model


# Funzione per addestrare il modello
def train_model(data, time_step=60, epochs=10, batch_size=32):
    """
    Addestra il modello sui dati storici.
    
    Args:
        data (pd.DataFrame): Dati storici delle azioni.
        time_step (int): Numero di giorni da considerare per ogni sequenza (default 60).
        epochs (int): Numero di epoche per l'addestramento (default 10).
        batch_size (int): Dimensione del batch per l'addestramento (default 32).
        
    Returns:
        model (tf.keras.Model): Il modello addestrato.
        scaler (StandardScaler): Il trasformatore per la normalizzazione.
    """
    X, y, scaler = prepare_data(data, time_step)
    
    # Suddividi i dati in training e test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    # Crea il modello
    model = create_model((X_train.shape[1], X_train.shape[2]))
    
    # Addestra il modello
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_test, y_test))
    
    # Salva il modello addestrato
    model.save('stock_price_predictor.h5')
    
    return model, scaler


# Funzione per fare previsioni
def predict(model, scaler, data, time_step=60):
    """
    Esegui previsioni sui dati storici.
    
    Args:
        model (tf.keras.Model): Il modello addestrato.
        scaler (StandardScaler): Il trasformatore per la normalizzazione.
        data (pd.DataFrame): Dati storici per fare le previsioni.
        time_step (int): Numero di giorni da considerare per ogni sequenza (default 60).
        
    Returns:
        predictions (np.array): Le previsioni del prezzo futuro.
    """
    # Prepara i dati per la previsione
    data_scaled = scaler.transform(data[['Close']])
    X = []
    for i in range(time_step, len(data_scaled)):
        X.append(data_scaled[i-time_step:i, 0])
    
    X = np.array(X)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    
    # Prevedi i prezzi
    predictions = model.predict(X)
    predictions = scaler.inverse_transform(predictions)  # Ripristina i valori originali
    
    return predictions


# Funzione per caricare un modello già addestrato
def load_trained_model(model_path='stock_price_predictor.h5'):
    """
    Carica un modello addestrato salvato.
    
    Args:
        model_path (str): Percorso del modello addestrato salvato.
        
    Returns:
        model (tf.keras.Model): Il modello caricato.
    """
    model = tf.keras.models.load_model(model_path)
    return model
