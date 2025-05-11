# Dicionários possuem chave e valor, onde as chaves são identificadores(tipo índices em listas) para os valores/elementos.
frutas = {
    'Maçã': 3.50,
    'Laranja': 2.99,
    'Abacaxi': 4.50,
    'Goiaba': 2.99,
    'Uva': 1.99
#   chave: valor
}

print(frutas['Maçã']) # Imprime o valor da chave
frutas['Goiaba'] = 5.99
print(frutas)

quantidade = len(frutas)
print(quantidade)

chaves = frutas.keys()
# print(chaves)
valores = frutas.values()
# print(valores)
itens = frutas.items()
# print(itens)

for chave, valor in itens: # Imprime os itens em um efeito visual melhor
    print(chave, valor)

# deleta um elemento
del frutas['Uva'], frutas['Abacaxi']
print(frutas)

# popitem: remove o último elemento do dicionário
frutas.popitem()
print(frutas)

# pop: remove um item pela chave
frutas.pop('Maçã')

print(frutas)
# get('valor', 'valor se não for encontrado'): Retorna o valor da chave
print(frutas.get('Abacaxi', 'Fruta não foi encontrada'))


# limpa todos os valores
frutas.clear()