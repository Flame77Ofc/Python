# Dicionários
elemento = {
    'Z': 3,
    'nome': 'Lítio', 
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}
print(elemento)
print(elemento['nome'])
print(len(elemento))

# Atualizar uma entrada/ Substituir
elemento['grupo'] = 'Alcalinos'
print(elemento)

# Adicionar uma entrada
elemento['periodo'] = 1
print(elemento)
# Se atribuir um valor que ainda não existe, será criado, se não, será substituido


# Exclusão de itens
del elemento['densidade']
print(elemento)

elemento.clear()
print(elemento)

# deletar todo o dicionário ⇒
del elemento
print(elemento) # Dará erro, pois elemento não existe mais.