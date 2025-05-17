# Dicionários
semana = {
    1: 'Segunda-feira',
    2: 'Terça-feira',
    4: 'Quinta-feira',
    5: 'Sexta-feira',
    6: 'Sábado',
    7: 'Domingo'
}

semana[3] = 'Quarta-feira'
print(semana)

# del: Apaga um elmento do dicionário ou apaga todo o dicionário
"""del semana
del semana[3]
print(semana)"""

# get: Retorna o valor de um elemento do dicionário
print(semana.get(1))
print(semana.get(8))

# setdefault: Retorna o valor de um elemento do dicionário, se ele não existir, ele cria um novo
print(semana.setdefault(1))
semana.setdefault(8, 'Domingo')
print(semana.setdefault(8))

# keys: Retorna as chaves do dicionário
print(semana.keys())

# values: Retorna os valores do dicionário
print(semana.values())

# items: Retorna as chaves e os valores do dicionário
print(semana.items())

# for com items: Retorna as chaves e os valores do dicionário
for x, y in semana.items():
    print(x, y)

# pop: Remove um elemento do dicionário
semana.pop(5)
print(semana)

# copy: Copia o dicionário
semanacopy = semana.copy()
print(semanacopy)





SuperGMs = {
    2831: 'Magnus Carlsen',
    2802: 'Hikaru Nakamura',
    2801: 'Arjun Erigaisi'
}
# Acessando pelo índice
SuperGMs[2831]
SuperGMs[2802]

# len: Retorna a quantidade de itens
len(SuperGMs)

# Alterando o elemento de um dicionário
SuperGMs[2754] = 'Ian Nepomniachtchi'

# Deletando um elemento
del SuperGMs[2801]

'Alireza' in SuperGMs # True
'Carlsen' not in SuperGMs # False


# keys(): A chave que identifica os valores
for chave in SuperGMs.keys():
    pass # print(chave)

# values(): O elemento/valor depois da chave
for elemento in SuperGMs.values():
    pass # print(elemento)

# items(): É a junção entre chave e valor
for chave_valor in SuperGMs.items():
    pass # print(chave_valor)


# utilizando o zip :)
for chave, valor in zip(SuperGMs.keys(), SuperGMs.values()):
    pass # print(chave, valor)


# pop: Remove pela chave especificada
SuperGMs.pop(2802)


# clear: Remove todos os itens do dicionário
SuperGMs.clear()







# Os dicionários não possuem índice, apenas chave: valor. A chave é semelhante a um índice, pois identifica o elemento
Ranking = {
    1: 'Pedro Luiz',
    2: 'José Gaúcho Costa',
    3: 'Matheus Henrique',
    4: 'Rafael Moto'
#   chave: 'valor'
}
# Acessando seus valores
print(Ranking[1])
# print(Ranking[1:3]) Fatiamento não é possível em dicionários

Ranking.keys() # => Retorna as chaves do dicionário: 1, 2, 3, 4
Ranking.values() # => Retorna os elementos/valores do dicionário: 'Pedro Luiz', 'José Gaúcho Costa', 'Matheus Henrique', 'Rafael Moto'
Ranking.items() # => Retorna a chave e o valor

# Alterando seus valores
Ranking[1] = 'Maria de Moura'
print(Ranking)

# Imprime a chave e o valor do dicionário com uma visualização melhor
for chave, valor in Ranking.items():
    print(chave, valor)

# del: deleta um elemento ou o próprio dicionário
"""del Ranking[1]
del Ranking"""

# clear: Limpa todo o dicionário
"Ranking.clear()"











frutas = {  
    'Maçã': 3.99,  
    'Laranja': 4.59,  
    'Banana': 2.99,  
    'Morango': 6.49,  
    'Uva': 8.99,  
    'Abacaxi': 5.89,  
    'Melancia': 7.49
#   'chave': valor
}
# Acessando um valor pela chave
frutas['Melancia']

# len: Retorna a quantidade de par chave-valor possui
quantidade = len(frutas)

# Alterando um valor pela chave
frutas['Abacaxi'] = 6.59

# Atualiza uma chave e um valor, se não existir, então é criado
frutas.update({'Melancia': 9.99})

# pop('chave'): Remove a chave e o valor
frutas.pop('Melancia')

# get('chave'): Retorna o valor da chave, se não existir, não acontece nada
print(frutas.get('Uva'))

# Remove o último par chave-valor
frutas.popitem()

# clear: limpa todo o dicionário
frutas.clear()

chaves = frutas.keys()
valores = frutas.values()
itens = frutas.items()

for chave, valor in itens:
    print(f'{chave}: {valor}')

