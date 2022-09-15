import requests
import random
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/page/1/'

quotes = []
authors = []
new_url = url

while new_url:
    response = requests.get(new_url)
    soup = BeautifulSoup(response.text, "html.parser")
    authors += soup.find_all('small', class_='author')
    quotes += soup.find_all('span', class_='text')
    next = soup.find('li', class_='next')
    if next:
        next_url = next.find('a', href=True)['href']
        new_url = url.replace('/page/1/', next_url)
    else:
        new_url = None

result = random.sample(quotes, 5)
for quote in result:
    print(quote.text, end='\n\n')