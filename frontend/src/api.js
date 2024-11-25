// frontend/src/api.js
const API_BASE_URL = "http://localhost:5000";  // Indica l'URL del tuo backend (assumendo che il backend sia in esecuzione su localhost:5000)

// Funzione per ottenere i dati delle azioni da un endpoint API
export const getStockData = async (symbol) => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/stock-data/${symbol}`);
    if (!response.ok) {
      throw new Error('Errore nel recupero dei dati delle azioni');
    }
    const data = await response.json();
    return data; // Ritorna i dati delle azioni
  } catch (error) {
    console.error("Errore:", error);
    throw error; // Propaga l'errore
  }
};

// Funzione per ottenere le notizie (se necessario)
export const getNews = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/news`);
    if (!response.ok) {
      throw new Error('Errore nel recupero delle notizie');
    }
    const newsData = await response.json();
    return newsData;  // Ritorna le notizie
  } catch (error) {
    console.error("Errore:", error);
    throw error; // Propaga l'errore
  }
};
