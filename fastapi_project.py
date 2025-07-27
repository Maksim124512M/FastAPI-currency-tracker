from fastapi import FastAPI, Depends, HTTPException

from datetime import date

from sqlalchemy.orm import Session

from typing import Dict, List

from parsing import fetch_currency_rates

from database_connection import get_db

from models import CurrencyRates


app = FastAPI()

@app.get('/currencies/')
async def currencies_list(db: Session = Depends(get_db)) -> Dict[str, float]:
    # Get the latest currency rates from the database
    rate_obj = db.query(CurrencyRates).order_by(CurrencyRates.date.desc()).first()
    if not rate_obj:
        raise HTTPException(status_code=404, detail='Currency rates not found in the database')

    # Define the set of currencies we are interested in
    currencies = {'usd', 'eur', 'pln', 'gbp', 'cny', 'jpy', 'chf', 'cad', 'aud', 'czk', 'sek', 'nok', 'huf'}

    # For each currency, get the rate from the rate_obj
    result = {currency: getattr(rate_obj, currency) for currency in currencies}

    return result

VALID_CURRENCIES = {'usd', 'eur', 'pln', 'gbp', 'cny', 'jpy', 'chf', 'cad', 'aud', 'czk', 'sek', 'nok', 'huf'}    # List of valid currency codes


@app.get('/currency/{currency_code}/')
async def get_currency(currency_code: str, db: Session = Depends(get_db), query_date: date = None) -> float:
    '''
    Endpoint to fetch the exchange rate for a specific currency on a given date.
    :param currency_code:
        The currency code for which the exchange rate is requested.
    :param db:
        Database session dependency.
    :param query_date:
        The date for which the exchange rate is requested. If not provided, the latest rate will be returned.
    :return:
        The exchange rate for the specified currency on the given date.
    '''


    if currency_code not in VALID_CURRENCIES:
        raise HTTPException(status_code=400, detail='Unknown currency')

    if query_date is None:
        rate_obj = db.query(CurrencyRates).order_by(CurrencyRates.date.desc()).first()
    else:
        rate_obj = db.query(CurrencyRates).filter(CurrencyRates.date == query_date).first()

    if not rate_obj:
        raise HTTPException(status_code=404, detail='Currency rates for this date not found')

    rate_value = getattr(rate_obj, currency_code)
    if rate_value is None:
        raise HTTPException(status_code=404, detail='There is no exchange rate for this currency.')

    return rate_value


if __name__ == '__main__':
    import uvicorn
    from database_connection import engine
    from models import Base

    Base.metadata.create_all(bind=engine)  # Create database tables if they do not exist

    uvicorn.run('fastapi_project:app', host='127.0.0.1', port=8000, reload=True)

