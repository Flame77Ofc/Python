# Sets: Não são ordernados, e ignoram elementos repetidos, aceitando apenas um valor que não seja igual.
cesta = {'maçã', 'banana', 'uva', 'melancia', 'maçã', 'banana', 'banana'}
print(cesta)

# add: Adiciona um elemento ao set
cesta.add('abacaxi')
print(cesta)

# remove: Remove um elemento do set
cesta.remove('banana')
print(cesta)

# clear: Limpa o set
cesta.clear()
print(cesta)

# in, not in: Verifica se um elemento pertence ao set
print('banana' in cesta)
print('banana' not in cesta)

# len: Retorna o tamanho do set
print(len(cesta))

# union: Junta dois sets
cesta1 = {1,2,3}
cesta2 = {4,5,6}
cesta3 = cesta1.union(cesta2)
print(cesta3)

# update: Junta dois sets
cesta1.update(cesta2)
print(cesta1)

# intersection: Retorna os elementos em comum de dois sets
cesta1 = {1,2,3}
cesta2 = {3,4,5}
cesta3 = cesta1.intersection(cesta2)
print(cesta3)

# difference: Retorna os elementos diferentes de dois sets
cesta1 = {1,2,3}
cesta2 = {3,4,5}
cesta3 = cesta1.difference(cesta2)
print(cesta3)





# Sets são conjuntos que são desordenados, ou seja, não possuem uma ordenação especifica, a ordem de seus elementos sempre variam
precos = {50, 35, 15, 125, 490, 340}
vendas = {120, 45, 180, 450, 390, 875, 365, 985, 260, 410}

# union: Une duas listas
uniao = precos.union(vendas)
uniao = precos | vendas # Também é possível unir utilizando a barra vertical
print(len(uniao))

# add: adiciona um elemento no último índice
igredientes = {'Farinha', 'Trigo'}
igredientes.add('Fermento')
print(igredientes)

# remove o elemento especificado
igredientes.remove('Farinha')
print(igredientes)

# pop: remove um elemento(remove o último elemento, mas como um set é desordenado, remove um elemento aleatório)
igredientes.pop()
print(igredientes)

# clear: limpa todos os elementos da lista
igredientes.clear()
print(igredientes)

