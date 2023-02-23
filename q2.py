import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.youtube.com/rogerio410")
soup = BeautifulSoup(response.text, 'html.parser')
tagEsc = input("Tag desejada: ")
tags = []

links = soup.find_all(tagEsc)
for link in links:
    texto = link.getText()
    print(texto)