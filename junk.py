import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")


quotes = soup.find_all("span", class_="text")
for quote in quotes[:25]:
    print(quote)