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