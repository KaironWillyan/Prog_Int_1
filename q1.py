import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.youtube.com/rogerio410")
soup = BeautifulSoup(response.text, 'html.parser')
links = []
for link in soup.find_all("a"):
    href = link.get('href')
    print(" - ", href)