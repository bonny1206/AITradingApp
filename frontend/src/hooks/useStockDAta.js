// frontend/src/hooks/useStockData.js
import { useState, useEffect } from 'react';

const useStockData = (symbol) => {
  const [data, setData] = useState(null); // Stato per memorizzare i dati delle azioni
  const [loading, setLoading] = useState(true); // Stato per il caricamento dei dati
  const [error, setError] = useState(null); // Stato per errori durante il recupero dei dati

  useEffect(() => {
    // Funzione per ottenere i dati delle azioni
    const fetchStockData = async () => {
      setLoading(true); // Imposta lo stato di caricamento
      setError(null); // Resetta eventuali errori precedenti

      try {
        // Fai la richiesta API per ottenere i dati delle azioni
        const response = await fetch(`/api/stock-data/${symbol}`);
        if (!response.ok) {
          throw new Error('Errore nel recupero dei dati delle azioni');
        }
        const result = await response.json();
        setData(result); // Memorizza i dati nel nostro stato
      } catch (err) {
        setError(err.message); // Memorizza eventuali errori
      } finally {
        setLoading(false); // Imposta lo stato di caricamento a falso
      }
    };

    // Chiamata alla funzione di fetch ogni volta che cambia il simbolo
    fetchStockData();
  }, [symbol]); // Rieffettua la chiamata ogni volta che il simbolo cambia

  return { data, loading, error }; // Ritorna i dati, il caricamento e gli errori
};

export default useStockData;
