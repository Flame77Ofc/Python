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














# Listas COMPLETAS ;/
nomes = ['Pedro', 'João', 'Fernando',' Carlos', 'Bruno', 'Henrique']
# Acessando pelo índice
nomes[0]
nomes[1:5]

# Alterando o elemento 3 que possui o índice 2
nomes[2] = 'Maria'

# Retorna a quantidade de elementos de uma lista
quantidade = len(nomes)

# max: Retorna o maior valor da lista
numeros = [12, 45, 23, 27, 9]
maior = max(numeros)

# menor: Retorna o menor valor da lista
numeros = [-2, 15, 90, 23, 0]
menor = min(numeros)

# append('elemento'): Adiciona um novo elemento no último índice
nomes.append('Alberto')

# insert('indice', 'elemento'): Adiciona um elemento em determinado índice
nomes.insert(2, 'Luiz')

# remove('elemento'): Remove um elemento desejado
nomes.remove('Pedro')

# pop(): Retira elementos
nomes.pop() # remove o último elemento
nomes.pop(2) # remove o elemento do índice 2

# count('elemento'): Retorna o número de vezes que um elemento aparece numa lista
nomes.count('Felipe')

# index('elemento'): Retorna qual o índice em que um elemento está
nomes.index('João')

# copy: Permite que outra lista tenha o mesmo valor que a original
nomes2 = nomes.copy()

# reverse: Inverte a ordem de todos os valores da lista
nomes.reverse()

# sort: Ordena os valores da lista em ordem alfabética ou númerica(se a lista for números)
nomes.sort()

# del: Deleta um elemento ou a própria lista
"del nomes[1]" # deleta o elemento do índice 1
"del nomes" # deleta toda a lista

# clear: Limpa todos os elementos de uma lista, deixando-a vazia.
nomes.clear()

# extend: Junta duas listas
alunos = ['João', 'Letícia', 'Pedro']
notas = [6, 4, 9]
alunos.extend(notas)