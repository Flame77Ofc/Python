# Listas
notas1 = [3, 7, 9, 5]
notas2 = [8, 9, 3, 1]

# Juntando as listas
notas = notas1 + notas2
print(notas)


# Acessando um elemento pelo índice
print(notas[0]) # O primeiro elemento da lista
print(notas[-1]) # O último elemento da lista
print(notas[2:5]) # Fatiando

# Substituindo um elemento por outro pelo índice
notas[0] = 5
print(notas)

# Acessando a quantidade de elementos
print(len(notas))

# Ordenando
print(sorted(notas)) # Ordem crescente
print(sorted(notas, reverse=True)) # Ordem decrescente

# Somando todos os valores da lista
print(sum(notas))

# Encontrando o valor minimo e máximo
print(min(notas))
print(max(notas))

# -----------------------------------------------
nomes = ['João', 'Maria', 'Pedro', 'Osvaldo']

# append: Adiciona um elemento no final da lista
nomes.append('Mario')
print(nomes)

# pop: Remove o último elemento da lista
nomes.pop() # ou: nomes.pop(indice)
print(nomes)

# insert: Adiciona um valor no índice especificado
nomes.insert(0, 'Roberto')
print(nomes)

# in: Verifica se tal elemento está na lista
print('Emanuel' in nomes) # 'Mario' está na lista nomes?