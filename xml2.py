import requests
from bs4 import BeautifulSoup

r = requests.get('https://edition.metro.news/endpoint.xml')
soup = BeautifulSoup(r.content)

d =soup.find_all("id")
print(len(d))