import requests
import datetime
import time

def do_request_PB(date, first_currency, second_currency):
    url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=' + date
    response = requests.get(url)
    dict_json = response.json()
    exchangeRate = dict_json['exchangeRate']
    if len(exchangeRate)==0:
        return tuple()
    exchangeRate.pop(0)
    first_course = list(filter(lambda item: item['currency'] == first_currency, exchangeRate))[0]
    second_course = list(filter(lambda item: item['currency'] == second_currency, exchangeRate))[0]
    
    purchaseRate = saleRate = 0
    purchaseRate = first_course['purchaseRate'] if 'purchaseRate' in first_course else first_course['purchaseRateNB']
    saleRate = second_course['saleRate'] if 'saleRate' in second_course else second_course['saleRateNB']

    return purchaseRate, saleRate
        
def currency_changes():
    currencies = ['USD', 'EUR', 'RUB', 'CHF', 'GBP', 'PLN', 'SEK', 'CAD']
    print('Available currencies:')
    print('\n'.join(currencies))
    first_curr = input('Enter the first currency: ')
    if not first_curr in currencies:
       print('First currency entered incorrectly!')
       return
    second_curr = input('Enter the second currency: ')
    if not second_curr in currencies:
       print('Second currency entered incorrectly!')
       return
    summa = float(input("Enter the summ: "))
    if summa<=0:
       print('The summa entered is not correct!')
       return
   
    today = datetime.datetime.today().date()
    while True:
        time.sleep(0.5) 
        date = today.strftime('%d.%m.%Y')
        сourses = do_request_PB(date, first_curr, second_curr)
        if len(сourses)==0:
            today -= datetime.timedelta(days=1)
            continue
        
        first_course, second_course = сourses
        in_UAH = first_course * summa
        print("Summa in", second_curr, ':', round(in_UAH / second_course, 4))
        break

currency_changes()    
