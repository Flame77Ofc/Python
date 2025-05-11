# Listas
lista = ['Maria', 'Pedro', 'Fernando', 'João']
print(lista)

tamanho = len(lista) # len: Retorna a quantidade de elementos numa lista

# Alterando elementos de uma lista
lista[2] = 'Amanda'

# insert(indice, elemento): adiciona um elemento no índice especificado
lista.insert(1, 'Carlos')

# pop(índice opcional): remove um elemento
lista.pop() # Remove o último elemento
lista.pop(0) # Remove o primeiro elemento

# remove(elemento): remove pelo elemento
lista.remove('Pedro')

# sort: ordena uma lista em ordem crescente.
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letras.sort()