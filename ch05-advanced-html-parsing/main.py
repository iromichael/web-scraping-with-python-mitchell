from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.find_all('span', {'class': 'green'})
# for name in nameList:
#     print(name.get_text())

text_num = bs.find_all(text='the prince')
print(len(text_num))