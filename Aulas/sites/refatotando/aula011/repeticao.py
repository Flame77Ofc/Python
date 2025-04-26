# Estruturas de repetição
# while

i = 1
while i <= 10:
    print(i)
    i += 1



# for 
pessoas = ['Mario', 'Beto', 'Maria'] # Iteração com listas

for pessoa in pessoas:
    print(pessoa)


canal = 'Refatorando' # Iteração com letras

for letra in canal:
    print(letra)



# for range(começo, fim, pulos)

for index in range(1, 11, 1):
    print(index)


for pessoa in range(len(pessoas)):
    print(pessoas[pessoa], pessoa)




matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
]

for linha in matriz:
    # print(linha)
    print("---")
    for coluna in linha:
        print(coluna)