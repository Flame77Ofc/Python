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