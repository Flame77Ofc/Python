from random import randint
lista = []

while True:
    numero = randint(1, 10)

    lista.append(numero)

    if len(lista) >= 15:
        break


soma = 0
for i in range(1, 11):
    print(f'{i} repetiu {lista.count(i)} vezes')
    soma += lista.count(i)
print(soma)