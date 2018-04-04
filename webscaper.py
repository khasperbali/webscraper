from bs4 import BeautifulSoup
import urllib.request

def scrapePrice():
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    name_box = strftime("As Of " + "%m/%d/%Y %H:%M", gmtime()) + ", the Bitcoin price is" + " $" + soup.find(attrs={"class": "text-large2"}).get_text()
    text = name_box.encode()
    print(text)
    f = open('bitcoinPrice.txt', 'wb')
    f.write(text)
    f.close()
    print('Price saved to bitcoinPrice.txt')
    
