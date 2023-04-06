import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.meutimao.com.br/tabela-de-classificacao/campeonato_brasileiro/')

soup = BeautifulSoup(url.text, 'html.parser')
tabela = soup.find('table')

print(tabela)