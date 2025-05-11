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