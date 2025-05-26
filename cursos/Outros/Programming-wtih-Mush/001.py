# Listas
courses = ['Python', 'Math', 'Pyshics', 'Science']
print(courses[0])
print(courses[-3])


quantity = len(courses)
print(quantity)

# Modificando listas
courses.append('Biology')
courses.insert(1, 'Tecnology')

courses.pop()
courses.remove('Python')
del courses[1]

print(courses)


numeros = [4, 6, 12, 3, 89, 12, 15, 16]
numeros.sort()
print(numeros)


# Achando elementos em uma lista
lista = ['e1', 'e2', 'e3', 'e4', 'e5']
print(lista.index('e1'))
"print(lista.index('e9'))" # erro
print('e3' not in lista)



# List Comprehensions
# Oferece uma simples sintaxe quando você quer criar uma lista apartir de outra lista existente mas com alguma modificação desejada.
# Essa List Comprehension filtra todos os animais que possuem a letra a
animais = ['Urso', 'Abelha', 'Mosquito', 'Aranha', 'Centopeia', 'Crocodilo', 'Elefante']
animais_com_a = [x for x in animais if 'a' in x.lower()]
print(animais_com_a)
