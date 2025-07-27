import httpx


url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'


TARGET_CURRENCIES = {
    'USD': 'usd',
    'EUR': 'eur',
    'PLN': 'pln',
    'GBP': 'gbp',
    'CNY': 'cny',
    'JPY': 'jpy',
    'CHF': 'chf',
    'CAD': 'cad',
    'AUD': 'aud',
    'CZK': 'czk',
    'SEK': 'sek',
    'NOK': 'nok',
    'HUF': 'huf',
}


async def fetch_currency_rates():
    '''
    Fetch currency exchange rates from the National Bank of Ukraine API.
    :return:
        A dictionary containing currency exchange rates.
    '''

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

        rates = {}
        for item in data:
            if item['cc'] in TARGET_CURRENCIES:
                field_name = TARGET_CURRENCIES[item['cc']]
                rates[field_name] = item['rate']
                rate_date = datetime.strptime(item['exchangedate'], '%d.%m.%Y').date()

        # Creting session in database
        db: Session = SessionLocal()

        # Checking if rates for this date already exist
        existing = db.query(CurrencyRates).filter_by(date=rate_date).first()
        if existing:
            db.close()
            return {'message': 'Courses for this date already exist.'}

        # Creating a new entry in the database
        new_entry = CurrencyRates(date=rate_date, **rates)
        db.add(new_entry)
        db.commit()
        db.close()

        return {'message': 'Courses saved successfully', 'date': str(rate_date)}

