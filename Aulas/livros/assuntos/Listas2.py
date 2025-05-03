# Listas: Cada elemento de uma lista é acessado pelo seu índice. O primeiro elemento começa o índice como 0, o segundo no índice 1 e assim por diante. O último elemento tem a quantidade de elementos - 1 (Se a lista tem 50 elementos, o primeiro índice é o 0 e o último é o índice 49). Uma lista pode conter elementos com múltiplos tipos de dados. As listas são formadas por uma sequência de elementos separados por vírgulas e envolvidos por um par de colchetes.
"ESTRUTURA: <lista> = [<elemento 1>, <elemento 2>, <elemento N>]"

# lista vazia
idades = []

# lista com elementos
idades = [12, 34, 25, 67]
#índices:  0   1   2   3

# Há duas formas de imprimir os elementos dentro de uma lista
print(idades) # Imprimindo todos os seus elementos: <nome da lista>
print(idades[2]) # Imprimindo um elemento baseado no seu índice: lista[<índice>]

# exemplo
frutas = ['Laranja', 'Maçã', 'Abacaxi', 'Abacate']
nomes = ['João', 'Maria', 'Pedro', 'Luiz']
numeros = [34, 12, 38, 24, 56, 4]

# Manipulando elementos com funções
# append: adiciona um elemento no final da lista: lista.append(<elemento>)
numeros.append(15) # resultado: [34, 12, 38, 24, 56, 4, 15]

# insert: adiciona um elemento no índice especificado: lista.insert(<índice>, <elemento>)
numeros.insert(3, 100) # resultado: [34, 12, 38, 100, 24, 56, 4, 15]

# sort: ordena os elementos em ordem crescente: lista.sort()
numeros.sort() # resultado: [4, 12, 15, 24, 34, 38, 56, 100]

# remove: remove um elemento especificando um elemento: lista.remove(<elemento>)
numeros.remove(24) # resultado: [4, 12, 15, 24, 34, 38, 56, 100]

# pop: remove o último elemento: lista.pop()
numeros.pop() # resultado: [4, 12, 15, 34, 38, 56]

# del: remove a lista toda ou pelo índice: del lista/ del lista[<índice>]
"""del numeros
del numeros[0]"""

# extend: junta duas listas: lista1.extend(lista2)
lista1 = ['Maçã']
lista2 = ['Beterraba']
lista1.extend(lista2)

# len: retorna a quantidade de elementos de uma lista: len(lista)
lista = ['Pedro', 'Joaquim', 'Maria']
len(lista) # resultado: 3

# index: retorna o índice de um elemento: lista.index(elemento)
lista.index('Pedro') # resultado: 0

# in: verifica se algum elemento está na lista. <elemento> in lista
'Mario' in lista # Mario está na lista? False
'Lucas' not in lista # Lucas não está na lista? True

# Iterando sobre uma lista: retornando cada elemento da lista
for i in lista:
    print(i)

# Retornando cada elemento e índice
for indice, name in enumerate(lista):
    print(name, indice)


