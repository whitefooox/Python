import requests
from bs4 import BeautifulSoup

html_text = requests.get('http://olympus.realpython.org/profiles').text
soup = BeautifulSoup(html_text, "html.parser")

for link in soup.find_all("a", href=True):
    print('http://olympus.realpython.org' + link['href'])