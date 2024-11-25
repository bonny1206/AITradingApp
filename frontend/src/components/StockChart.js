// frontend/src/components/StockChart.js
import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend } from 'chart.js';

// Registrazione dei componenti necessari per Chart.js
ChartJS.register(CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend);

const StockChart = ({ chartData }) => {
  const options = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Grafico Prezzi Azioni'
      },
      tooltip: {
        mode: 'index',
        intersect: false,
      },
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Data'
        }
      },
      y: {
        title: {
          display: true,
          text: 'Prezzo'
        }
      }
    }
  };

  return (
    <div className="stock-chart">
      <Line data={chartData} options={options} />
    </div>
  );
};

export default StockChart;
