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

