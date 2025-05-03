# Problema: A partir de uma lista você deve criar uma nova lista com o primeiro e último elemento. Para isso você deve criar uma função que faça essa criação automaticamente. Crie uma função que sirva para qualquer tamanho de lista.

numeros = [4, 7, 3, 9, 12, 5]

def primeiro_ultimo():
    first_last = numeros[0], numeros[-1]
    print(first_last)

primeiro_ultimo()