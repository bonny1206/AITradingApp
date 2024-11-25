// frontend/src/components/TradingSuggestions.js
import React, { useState, useEffect } from 'react';

const TradingSuggestions = ({ symbol }) => {
  const [suggestion, setSuggestion] = useState('');

  useEffect(() => {
    const fetchSuggestion = async () => {
      const response = await fetch(`/api/trading-suggestions/${symbol}`);
      const data = await response.json();
      setSuggestion(data.suggestion);
    };

    fetchSuggestion();
  }, [symbol]);

  return (
    <div className="trading-suggestions">
      <h3>Consigli di Trading per {symbol}</h3>
      <p>{suggestion ? suggestion : 'Caricamento...'}</p>
    </div>
  );
};

export default TradingSuggestions;
