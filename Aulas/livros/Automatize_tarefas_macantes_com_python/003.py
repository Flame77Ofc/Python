# Dicionários
produtos = {
    'lanterna': 15.90,
    'abajur': 13.99,
    'fone de ouvido': 23.99,
    'celular': 2950.99
#   'chave': valor
}

# alterando a chave de um valor
produtos['celular'] = 'tablet'

chaves = produtos.keys()
valores = produtos.values()
par_chave_valor = produtos.items()

print(chaves)
print(valores)
print(par_chave_valor)

for chave, valor in produtos.items():
    print(chave, valor)