# Listas
animais = ['Panda', 'Gato', 'Urso', 'Gorila', 'Macaco']
# positivos:  0        1       2         3         4
# negativos: -5       -4      -3        -2        -1

# Índices positivos
print(animais[1])
print(animais[1:4])

# Índices negativos
print(animais[-1])
print(animais[-4:])


lista = ['Peixe', 'Sapo', 'Rinoceronte', 'Porco', 'Guaxinim', 'Raposa']
duplicar = lista * 2 # Vai duplicar os elementos, ou seja, terá 2 peixes, 2 sapos, etc: ['Peixe', 'Sapo', 'Rinoceronte', 'Porco', 'Guaxinim', 'Raposa', 'Peixe', 'Sapo', 'Rinoceronte', 'Porco', 'Guaxinim', 'Raposa']

# deletando elementos
del lista[1]

# adicionando elementos
lista.append('Tartaruga')
lista.insert(1, 'Hipopótamo')

# removendo elementos
lista.remove('Tartaruga')
lista.pop()
lista.pop(0)

# ordenando elementos em ordem alfabética (funciona com números também)
lista.sort()