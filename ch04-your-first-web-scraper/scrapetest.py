from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

# try:
#     html = urlopen("http://pythonscraping.com/pages/page1.html")
# except HTTPError as e:
#     print(e)
# except URLError as e:
#     print("The server could not be found!")
# else:
#     print("It worked")

#     bs = BeautifulSoup(html, 'html.parser')
#     print(bs)

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
    # this could also be without the e as we are not using the value for anything now
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://pythonscraping.com/pages/page1.html")
if title is None:
    print('Title could not be found')
else:
    print(title)

