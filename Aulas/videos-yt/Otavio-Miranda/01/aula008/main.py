# Desempacotamento de listas
lista = ['Pedro', 'Maria', 'João']
n1, n2, n3 = lista # Cada variável é um elemento da lista
print(n1, n2, n3)

# Exemplo com *
lista = ['Melancia', 'Cáqui', 'Uva', 'Laranja', 'Maçã', 'Limão']
n1, n2, *n = lista # n agora contém o resto da lista
print(n1, n2, n)

lista = ['Artur', 'Pedro', 'Luiz', 'Marcos']
*n, n1 = lista # n contém os primeiros itens da lista
print(n, n1)