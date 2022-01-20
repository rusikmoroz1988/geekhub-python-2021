import scrapy
import datetime

from bs4 import BeautifulSoup

class VikkaDbSpyder(scrapy.Spider):

    """
    class to scraping site vikka.ua.
    ...
    Attributes
    --------
    name : str
        spider name
    date : str
        date of news  
    
    Methods
    ------
    start_requests():
        start start_requests of spider.
    
    get_tags():
        get tags of block

    parse():
        parsing of site 
    """
    
    name = 'vikkadb'

    def __init__(self):
        self.date = input("Enter a date in the format 'year/month/day':")
        try:
            datetime.datetime.strptime(self.date, '%Y/%m/%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    def start_requests(self):
        urls = ['https://www.vikka.ua/' + self.date]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def get_tags(self, list_tags):
        unique_numbers = set(list_tags)
        return ','.join('#' + i for i in unique_numbers)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.find_all('ul', {'class': 'cat-posts-wrap bg-white white-blocks-decor margin-b-40'})

        for item in content:
            for item_1 in item.find_all('li'):
                yield {
                    "title": item_1.select('.title-cat-post')[0].text,
                    "text": item_1.select('.content-cat-post')[0].text,
                    "tags": self.get_tags([element.name for element in item_1.descendants if element.name is not None]),
                    "URL": item_1.select('.more-link-style')[0].get('href')}