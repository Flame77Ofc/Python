# Criar uma função que recebe um número e faz uma contagem regressiva desse número
def contador(numero):
    contagem = [i for i in range(numero, 0, -1)]
    return contagem
print(contador(15))
print(contador(5))


# Exercício 2: Criar uma função que recebe uma lista e retorna o maior número dessa lista:
def maior_numero(lista):
    maior = -1
    for i in lista:
        if i > maior:
            maior = i
    return maior
print(maior_numero([17, -5, 45, 9, 92, 64, 56]))

# Faça um programa que leia uma frase e exiba o número de palavras.
frase = input('Digite uma frase ou um texto: ').strip()
frase = frase.split()
print(f"Há {len(frase)} palavras na sua frase/texto")
