# split: divide uma string em partes, usando um separador, e devolve uma lista com essas partes.
texto = 'Estou=Aprendendo=Python'
texto = texto.split('=') # ['Estou', 'Aprendendo', 'Python']
print(texto)

texto = 'Macacos2Gostam2De2Comer2Banana'
print(texto.split('2')) # ['Macacos', 'Gostam', 'De', 'Comer', 'Banana']

texto = 'Python é uma linguagem muito legal!'
print(texto.split()) # ['Python', 'é', 'uma', 'linguagem', 'muito', 'legal!']



# join: junta os itens de uma lista (ou outro iterável) em uma string, colocando um separador entre eles.
lista = ['Maria', 'Pedro', 'João']
frase = ', '.join(lista) # Maria, Pedro, João
print(frase)

frutas = ['Maçã', 'Banana', 'Uva']
print(' '.join(frutas)) # Maçã Banana Uva