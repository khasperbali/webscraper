import urllib.request
from bs4 import BeautifulSoup
import csv 
from datetime import datetime

def scraper():
	quote_page = "https://coinmarketcap.com/currencies/bitcoin/"
	page = urllib.request.urlopen(quote_page0)
	soup = BeautifulSoup(page, "html.parser")
	name_box = soup.find("h1", attrs={"class" : "text-large2"})
	text = name_box(encode)
	name = name_box.text.strip()
	print (name)
	price_box = soup.find("div", attrs={"class" : "text-large2"})
	price = price_box.text
	text = price_box(encode)
	print (price)
	writer = csv.writer(csv_file)
	writer.writerow ([name, price, datetime.now()])
	f= open("guru99.txt","w+")
	for i in range(10):
		f.write("This is line %d\r\n" % (i+1))
	f.close() 
