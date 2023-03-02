from googlesearch import search

q = input("Valor a ser buscado: ")

for resul in search(q):
    print(resul)