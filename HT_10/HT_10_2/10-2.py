import requests
import datetime
import time

class DateError(Exception):
    def __init__(self, text):
        self.txt = text

def do_request_PB(date, currency):
    url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=' + date
    response = requests.get(url)
    dict_json = response.json()
    exchangeRate = dict_json['exchangeRate']
    if len(exchangeRate)==0:
        return 0
    exchangeRate.pop(0)
    result = list(filter(lambda item: item['currency'] == currency, exchangeRate));
    return result[0]['saleRateNB'] 
      
def currency_changes():
    currencies = ['USD', 'EUR', 'RUB', 'CHF', 'GBP', 'PLN', 'SEK', 'CAD']
    print('Enter currency from the list:')
    currency = input('\n'.join(currencies) + '\n')
    if not currency in currencies:
        print('Currency entered incorrectly!')
        return
    
    date = input('Enter the date in the format "day.month.year": ')
    try:
        input_date = datetime.datetime.strptime(date, '%d.%m.%Y').date()
        now_date = datetime.datetime.today().date()
        future_date = input_date > now_date
        if future_date:
            raise DateError("You can not put a future date!")
    except ValueError:
        print('Invalid format of date!')
        return
    except DateError as de:
        print(de)
        return
    
    print("Currency: ", currency)
    print('\n')
    last_course = None
    while input_date<=now_date:
         date = input_date.strftime('%d.%m.%Y')
         print('Date:', date)
         сourse = do_request_PB(date, currency)
         print('NBU: ', round(сourse, 4), '-------' if last_course==None else round(сourse - last_course, 4), '\n')
         input_date += datetime.timedelta(days=1)
         last_course = сourse
         time.sleep(0.5) 
         
currency_changes()

