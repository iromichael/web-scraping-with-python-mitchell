from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import time
import random


headers={
    'User-Agent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }


def getSoup(url):
    response = requests.get(url, headers=headers)
    time.sleep(random.uniform(1, 3))
    return BeautifulSoup(response.text, 'html.parser')

# bs = getSoup('https://en.wikipedia.org/wiki/Kevin_Bacon')

# Function 1: gets all internal links
def getInternalLinks(bs, url):
    netloc = urlparse(url).netloc
    scheme = urlparse(url).scheme
    internalLinks = set()
    for link in bs.find_all('a'):
        if not link.attrs.get('href'):
            continue
        parsed = urlparse(link.attrs['href'])
        if parsed.netloc == '':
            l = f'{scheme}://{netloc}/{link.attrs["href"].strip("/")}'
            internalLinks.add(l)
        elif parsed.netloc == netloc:
            internalLinks.add(link.attrs['href'])
    return list(internalLinks)

# Function 1: gets external links, looks one page only
def getExternalLinks(bs, url):
    internal_netloc = urlparse(url).netloc
    externalLinks = set()
    for link in bs.find_all('a'):
        if not link.attrs.get('href'):
            continue
        parsed = urlparse(link.attrs['href'])
        if parsed.netloc != '' and parsed.netloc != internal_netloc:
            externalLinks.add(link.attrs['href'])
    return list(externalLinks)

allExtLinks = {}
allIntLinks = []

# crawls and entire site and checks for external links
def getAllExternalLinks(url, max_pages=20):
    if url not in allIntLinks:
        allIntLinks.append(url)

    if len(allIntLinks) >= max_pages:
        return
    
    bs = getSoup(url)
    internalLinks = getInternalLinks(bs, url)
    externalLinks = getExternalLinks(bs, url)

    for link in externalLinks:
        if link not in allExtLinks:
            # allExtLinks.append(link)
            # print(link)
            allExtLinks[link] = url
            print(f"{link} (found on {url})")
    for link in internalLinks:
        if len(allIntLinks) >= max_pages:
            break
        if link not in allIntLinks:
            allIntLinks.append(link)
            print(f"Int link: {link}, found on {url}")
            getAllExternalLinks(link, max_pages)


getAllExternalLinks('https://www.litfinadvisors.com/')