import requests
from bs4 import BeautifulSoup
import csv
import sqlite3
import time

PARSING_RESULT_FILE = "Parsing.csv"
PARSING_RESULT_DB = "Parsing.db"
URL = 'https://quotes.toscrape.com'

def get_info_about_author(url_author):
    response = requests.get(url_author)
    soup = BeautifulSoup(response.text, 'lxml')    
    return soup.select('.author-description')[0].text.strip()

def write_to_csv(list_info):
    with open(PARSING_RESULT_FILE, "w", encoding='utf-8') as file:
        columns = ["Quote", "Author", "AuthorInfo", "Content"]
        writer = csv.DictWriter(file, delimiter = ",", 
                                 lineterminator="\r", fieldnames=columns)
        writer.writeheader()
        writer.writerows(list_info)

def write_to_db(list_info):
    connection = sqlite3.connect(PARSING_RESULT_DB)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS info(
        quote TEXT,
        author TEXT,
        authorInfo TEXT,
        content TEXT);
        """)    
        
    cursor.execute("SELECT * FROM info LIMIT 1")
    try:
        cursor.fetchone()[0]
        cursor.execute("DELETE FROM info")
    except:
        pass
    sql = "INSERT INTO info VALUES (?, ?, ?, ?)"
    for item in list_info:
        cursor.execute(sql, (item['Quote'], item['Author'], item['AuthorInfo'], item['Content']))
    connection.commit()
    connection.close()
     
def parser():
     list_of_dict = []
     url = URL
     start_time = time.time()
     while True:
         response = requests.get(url)
         soup = BeautifulSoup(response.text, 'lxml')
         quotes = soup.find_all('div', class_='quote')        
         for element in quotes:
             dict_elements = {}
             dict_elements['Quote'] = element.select(".text")[0].text
             dict_elements['Author'] = element.select(".author")[0].text
             dict_elements['Content'] = element.select('.keywords')[0]['content']
             path_to_author = URL + element.select('span a[href]')[0]['href']
             dict_elements['AuthorInfo'] = get_info_about_author(path_to_author)     
             list_of_dict.append(dict_elements)    
         
         quotes_next = soup.find('li', class_='next')
         if quotes_next == None:
             break
         else:
             url = URL + quotes_next.select('a[href]')[0]['href']
     
     if len(list_of_dict)==0:
         print('Parsing did not give any result!')
     else:
         write_to_csv(list_of_dict)
         write_to_db(list_of_dict)
         print("Parsing is done for %s seconds" % (time.time() - start_time))
             
parser()