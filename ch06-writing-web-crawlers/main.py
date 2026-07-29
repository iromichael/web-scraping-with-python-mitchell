from bs4 import BeautifulSoup
import requests
import re
import datetime
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# get all internal links

def getLinks(articleUrl):
    base_url = 'http://en.wikipedia.org'
    url = f"{base_url}{articleUrl}"
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.content, 'html.parser')

    links = soup.find_all('a', {'rel': 'mw:WikiLink'})
    for link in links:
        print(link['href'])
        # return href

links = getLinks('/wiki/Kevin_Bacon')
print(links)