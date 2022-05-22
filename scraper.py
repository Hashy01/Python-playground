import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.de/Sony-DigitalKamera-Touch-Display-Vollformatsensor-Kartenslosts/dp/B07B4L1PQ8/ref=sr_1_3?keywords=sony_a7&qid=1561393494&s-gateway&sr-8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}

page = requests.get(URL, headers=headers) #returns all the data from the website

soup = BeautifulSoup(page.content, 'html.passer')

print(soup.prettyify())
