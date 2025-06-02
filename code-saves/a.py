# Exercicio 1: Criar uma função que recebe um número e faz uma contagem regressiva desse número:
def contador(numero):
    for i in range(numero, 0, -1):
        print(i)
contador(15)
contador(5)


# Exercício 2: Criar uma função que recebe uma lista e retorna o maior número dessa lista:
def maior_numero(lista):
    maior = -1
    for i in lista:
        if i > maior:
            maior = i
    print(maior)
maior_numero([17, -5, 45, 9, 92, 64, 56])
maior_numero([-9, -12, -5, -8])