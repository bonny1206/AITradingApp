// frontend/src/components/PatternDisplay.js
import React from 'react';

const PatternDisplay = ({ patterns }) => {
  return (
    <div className="pattern-display">
      <h3>Pattern Grafici Rilevati</h3>
      <ul>
        {patterns.map((pattern, index) => (
          <li key={index}>{pattern}</li>
        ))}
      </ul>
    </div>
  );
};

export default PatternDisplay;
