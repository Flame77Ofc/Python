# Lista: listas são mutáveis, ou seja, podem ser modificadas
pessoas = ['Pedro', 'João', 'Maria', 'Bernardo', 'Roberto', 'Micael']
print(pessoas)

# Imprime um elemento pelo índice
print(pessoas[3], pessoas[5])

# Imprime o último elemento da lista
ultimo_elemento = pessoas[-1]
print(ultimo_elemento)

# Fatia a lista
fatia_elementos = pessoas[0:2]
print(fatia_elementos)

# append: Adiciona um elemento no último índice
pessoas.append('Spock')
print(pessoas)

# insert: Adiciona elementos no índice especificado
pessoas.insert(1, 'Amanda')
print(pessoas)

# pop: Remove o último elemento
pessoas.pop()
print(pessoas)

# remove: Remove um elemento pelo nome especificado
pessoas.remove('Pedro')
print(pessoas)

# index: Retorna o índice do nome especificado
print(pessoas.index("Bernardo"))

# count: Conta quantos elementos iguais tem em uma lista
salario = [3400, 6900, 3200, 5400, 12000, 3400, 3200]
print(salario.count(3400))

# Ordenar uma lista
numeros = [4, 8, 1, 9, 2, 5, 12, 8, -0, 0, -1]
letras = ['Z', 'D', 'I', 'W', 'A', 'O', 'R']
nomes = ['Pedro', 'João', 'Maria', 'Leonardo']
numeros.sort() # Em ordem crescente
print(numeros)
letras.sort(reverse=True) # Em ordem decrescente
print(letras)
nomes.reverse() # Inversão
print(nomes)

# clear: Remove todos os elementos de uma lista
pessoas.clear()
print(pessoas)