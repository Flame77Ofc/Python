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

