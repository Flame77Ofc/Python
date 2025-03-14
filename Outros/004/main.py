# Dicionários
dicionario = {
    'Indice 1': 'Gabriel',  'idade': 12, 
    'Indice 2': 'Lucas',
    'Indice 3': 12,
    'Indice 4': True,
}

print(f"{dicionario['Indice 1']}, {dicionario['idade']}")
dict2 = {
    'str': 'Valor 1',
    123: 'Valor 2',
    'Tupla': (1, 3, 7 )
}
print(dict2['Tupla'])

"""
dict2['naoexiste'] = 'agora existe'
if 'naoexiste' in dict2:
    print(dict2['naoexiste'])

if 'naoexiste' not in dict2:
    print(dict2['naoexiste'])
"""