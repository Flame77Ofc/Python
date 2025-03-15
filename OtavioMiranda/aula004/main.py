# Listas
frutas = ['Maçã', 'Banana', 'Uva', 'Cenoura', 'Pepino', 'Brocólis', 'Batata']
print('acessando pelo índice:', frutas[1], frutas[4], frutas[6])

# fatiamento
print('fatiamento:', frutas[3:5])

# Adicionar
# append = adiciona um valor no final da lista
frutas.append('b')
print(frutas)

# insert = adiciona um valor no índice especificado (não substitui)
frutas.insert(0, 'Salada de frutas')
print(frutas)



# Remover
# pop = remove o último índice
frutas.pop()
print(frutas)

# del = remove pelo índice ou fatiamento
del(frutas[2:5])
print(frutas)


# Iterando
frutas = list(range(1, len(frutas) + 1))
print(frutas)

frutas = [0,1,2,3,4,5,6,7,8,9]
soma = 0
for valor in frutas:
    soma = soma + valor
    print(soma)