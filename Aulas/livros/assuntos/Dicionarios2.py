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