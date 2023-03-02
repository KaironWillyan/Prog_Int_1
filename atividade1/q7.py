import requests

cep = input("Digite o cep: ")
link = f'https://viacep.com.br/ws/{cep}/json/'
endereco= requests.get(link)
print(endereco.json())