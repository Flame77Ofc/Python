import random
# random.random: Gera um valor aleatório entre 0 e 1 com diversas casas decimais
'random.random()'
print(random.random())

# randint: Gera um número aleatório entre o número inicial e final(range especificado)
"random.randint(início, fim)"
print(random.randint(1, 10))

# randrange: Gera um número aleatório entre inicio e fim, com passos.
"random.randrange(inicio, fim, passos)"
print(random.randrange(0, 11, 2))

# choice: Escolhe um elemento de uma lista
"random.choice(['elemento 1', 'elemento2')"
lista = [1, 2, 3, 4, 5]
print(random.choice(lista))

# choices: Escolhe um número elementos numa lista 
"random.choices(lista, k=numero-de-escolhas)"
lista = ['hello', 'python', 'world']
print(random.choices(lista, k=2))

# shuffle: Embaralha os elementos de uma lista
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros)