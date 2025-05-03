# pesquisar sobre a função key em listas
# Listas: São mutáveis, ou seja, podem ser modificadas.
lista = [1,5,9,2,4,9,1,3,0,2]
print(lista)

# funções de listas
# len: Retorna o tamanho da lista
len(lista) 
# min: Retorna o menor valor da lista
min(lista)
# max: Retorna o maior valor da lista
max(lista)
# sum: Retorna a soma dos valores da lista
sum(lista)
# append: Adiciona um elemento no final(último índice) da lista
lista.append(8)

# pop: Remove o último elemento da lista
lista.pop()

# remove('elemento'): Remove o elemento especificado
lista.remove('exemplo')

# del: Deleta a lista ou elemento da lista
"del lista"
"del lista[3]"

# in, not in: Verifica se um valor pertence à lista.
'Melancia' in lista
'Abacate' in lista
'Leopardo' not in lista

# sort: Ordena os elementos da lista em ordem crescente
lista.sort()

# reverse: inverte os elementos de uma lista
lista.reverse()


# Concatenação
a = [0,1,2]
b = [3,4,5]
c = a + b # [0,1,2,3,4,5]

# Repetição
a = [1,2,3]
repeticao = 3
a * repeticao # [1, 2, 3, 1, 2, 3, 1, 2, 3]



# listas com range
lista = list(range(5)) # [0, 1, 2, 3, 4]
print(lista)

# Exercicio
# Gere uma lista de contendo os múltiplos de 3 entre 1 e 50.
lista = list(range(1,50,3))
print(lista)