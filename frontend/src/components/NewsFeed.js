// frontend/src/components/NewsFeed.js
import React, { useEffect, useState } from 'react';

const NewsFeed = ({ symbol }) => {
  const [news, setNews] = useState([]);

  useEffect(() => {
    const fetchNews = async () => {
      const response = await fetch(`/api/news/${symbol}`);
      const data = await response.json();
      setNews(data);
    };

    fetchNews();
  }, [symbol]);

  return (
    <div className="news-feed">
      <h3>Ultime notizie per {symbol}</h3>
      <ul>
        {news.map((item, index) => (
          <li key={index}>
            <a href={item.url} target="_blank" rel="noopener noreferrer">
              {item.title}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NewsFeed;
