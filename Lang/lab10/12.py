import requests
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

counter = {}

for elem in authors:
    counter[elem.text] = counter.get(elem.text, 0) + 1

list_counter = list(counter.items())
list_counter.sort(key=lambda i: i[1], reverse=True)

for author_count in list_counter:
    print(author_count[0], author_count[1], sep=' - ')