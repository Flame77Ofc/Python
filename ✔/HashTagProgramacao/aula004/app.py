# Dicionários
lista_produtor = ['airpod', 'iphone', 'samsung']
dicionario = {
    'airpod': 300,
    'iphone': 9800,
    'samsung': 2300,
}
print(dicionario)

# Manipular um elemento
print(dicionario['iphone'])

# Editar um elemento
dicionario['iphone'] = dicionario['iphone'] * 1.3
print(dicionario)

# Quantidade de itens ⇒começa do 0
print(len(dicionario))

# Remover um elemento
dicionario.pop("airpod")
print(dicionario)


# Adicionar um elemento
dicionario['apple watch'] = 350
print(dicionario)