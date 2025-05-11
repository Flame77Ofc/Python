<!-- Concluídos -->
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

# Implementar uma função que receba um dicionário e retorne a soma, a média e a variação dos valores.
notas = {
    'João Alberto': 6.70,
    'Maria Carvalho': 9.68,
    'Luiz Paulo Costa': 4.76
}

total = 0
for value in notas.values():
    total += value

 
media = round(total / len(notas.values()), 2)
print(media)
print(total)