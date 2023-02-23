import requests
from bs4 import BeautifulSoup

url = input('url: ')
termo = input("termo: ")
resposta = requests.get(url)
soup = BeautifulSoup(resposta.content, 'html.parser')
texto = soup.get_text()

for i in range(len(texto)):
    if texto[i:i+len(termo)] == termo:
        print(texto[i-20:i]+ termo + texto[i+len(termo):i+len(termo)+20])