import urllib.request

url = input("Digite a url da imagem: ")

urllib.request.urlretrieve(url, "foto.png")