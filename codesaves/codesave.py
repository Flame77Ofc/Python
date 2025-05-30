from random import randint
lista = []

while True:
    numero = randint(1, 10)
    if len(lista) == 10:
        break
    if numero in lista:
        continue
    lista.append(numero)
    lista.sort()
    print(lista)