from sqlalchemy import Column, Integer, Float, Date

from database_connection import Base


class CurrencyRates(Base):
    '''
    CurrencyRates model for storing currency exchange rates.
    '''

    __tablename__ = 'currency_rates'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, unique=True)

    usd = Column(Float)    # United States Donnar
    eur = Column(Float)    # Euro
    pln = Column(Float)    # Polish zloty
    gbp = Column(Float)    # Pound
    cny = Column(Float)    # Chinese yuan
    jpy = Column(Float)    # Japanese yen
    chf = Column(Float)    # Swiss franc
    cad = Column(Float)    # Canadian dollar
    aud = Column(Float)    # Australian dollar
    czk = Column(Float)    # Czech crown
    sek = Column(Float)    # Swedish króna
    nok = Column(Float)    # Norwegian Krone
    huf = Column(Float)    # Hungarian forint