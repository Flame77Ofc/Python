# Collections, lists, tuples
comidas = ['maçã', 'banana', 'batata', 'arroz', 'macarrão', 'feijão', 'farinha', 'alface']
print(comidas[3:6]) #Selecionar índice até outro índice
print(comidas[2]) # Selecionar pelo índice

comidas.append('abóbora') # Adicionar no último elemento da lista
print(comidas)
comidas.insert(2, 'melão')  # Adicionar um elemento pela posição (Não substitui por outro elemento, apenas adiciona)
print(comidas)
comidas.pop() # Remover o último elemento da lista
print(comidas)
comidas.remove('arroz') # Remover pelo nome
print(comidas)

# Ordernar os items da lista em ordem crescente:
comidas.sort()
print(comidas)

# Limpar todo os valores da lista:
comidas.clear()
print(comidas)


# Um pouco sobre tuples(Não é possível modificar) ⇒
coordenadas = (49, 56)
print(coordenadas)