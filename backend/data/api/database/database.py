# database.py
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Definiamo la base per la nostra classe di modello
Base = declarative_base()

# Definiamo il modello per il database
class StockData(Base):
    __tablename__ = 'stock_data'

    id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)

    def __repr__(self):
        return f"<StockData(symbol={self.symbol}, date={self.date}, close={self.close})>"

# Funzione per creare il database
def create_database(db_url='sqlite:///stocks.db'):
    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)

# Funzione per salvare i dati nel database
def save_to_database(db_url='sqlite:///stocks.db', data=None):
    if data is None:
        raise ValueError("I dati non possono essere nulli.")
    
    engine = create_engine(db_url, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Salvare i dati nel database
    for record in data:
        stock_data = StockData(
            symbol=record['symbol'],
            date=datetime.strptime(record['date'], "%Y-%m-%d"),
            open=record['open'],
            high=record['high'],
            low=record['low'],
            close=record['close'],
            volume=record['volume']
        )
        session.add(stock_data)
    
    session.commit()
    session.close()
    print(f"{len(data)} record salvati nel database.")
