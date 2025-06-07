# Criar uma função que recebe uma lista e retorna o maior número dessa lista:
def maior_numero(lista):
    maior = -1
    for i in lista:
        if i > maior:
            maior = i
    return maior
print(maior_numero([17, -5, 45, 9, 92, 64, 56]))
