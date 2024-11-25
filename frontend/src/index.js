// frontend/src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Aggiungi il tuo file di stile, se esiste
import App from './App'; // Importa il componente principale App
import reportWebVitals from './reportWebVitals'; // Per il monitoraggio delle prestazioni (opzionale)

ReactDOM.render(
  <React.StrictMode>
    <App /> {/* Renderizza il componente principale dell'app */}
  </React.StrictMode>,
  document.getElementById('root') // Attacca l'app al div con id 'root' nel file HTML
);

// Questo è un codice opzionale per misurare le performance della tua app.
reportWebVitals();
