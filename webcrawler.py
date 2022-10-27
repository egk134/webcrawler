import requests
from bs4 import BeautifulSoup

def web_crawler(max_pages):
    pages = 1
    while pages <= max_pages:
        pages += 1
        url = "quotes.toscrape.com/page/" + str(pages)
        code = requests.get(url)
        plain_text = code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('span'):
            quote = link.string
            print(quote)

web_crawler(1)
