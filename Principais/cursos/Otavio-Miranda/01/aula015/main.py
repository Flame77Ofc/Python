# List Comprehensions
lista = [1, 2, 3, 4, 5, 6, 7, 8]

# Duplicar cada valor da lista
dobrar = [i*2 for i in lista]
print(dobrar)

# Verificar quais números são pares na lista
pares = [i for i in lista if i % 2 == 0]
print(pares)