# While e for
i = 1
while i <= 10:
    print(i)
    i += 1


# for
nomes = ['Julia', 'Alberto', 'Gabriel']
for nome in nomes:
    print(nome)

palavra = 'Flame'
for letra in palavra:
    print(letra)


# for in range
for i in range(0, 21, 5):
    print(i)


# Mostrar quantos itens há em uma lista
frutas = ['Abacaxi', 'Uva', 'Maçã']
for index in range(len(frutas)):
    print(frutas[index], index)

# Aninhamento de loops while e for
matrixNums = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
]

for linha in matrixNums:
    for coluna in linha:
        print(coluna)