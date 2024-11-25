// frontend/src/App.js
import React, { useState } from 'react';
import StockChart from './components/StockChart';
import NewsFeed from './components/NewsFeed';
import TradingSuggestions from './components/TradingSuggestions';

const App = () => {
  const [symbol, setSymbol] = useState('AAPL'); // Impostiamo un simbolo di default (Apple)

  const handleSymbolChange = (e) => {
    setSymbol(e.target.value); // Funzione per cambiare il simbolo da monitorare
  };

  return (
    <div>
      <header>
        <h1>AI Trading App</h1>
        <input
          type="text"
          value={symbol}
          onChange={handleSymbolChange}
          placeholder="Inserisci simbolo (es. AAPL)"
        />
      </header>

      <main>
        <StockChart symbol={symbol} />
        <NewsFeed symbol={symbol} />
        <TradingSuggestions symbol={symbol} />
      </main>
    </div>
  );
};

export default App;
