# Tuplas
# Toda variável é um espaço na memória
lanche = 'hot dog'
lanche = 'suco de laranja'
print(lanche)
# Agora lanche é suco de laranja e não hot dog

lanche = 'hot dog', 'suco'
print(lanche)
# Agora lanche guarda hot dog e suco

animais = 'gato', 'cachorro', 'urso'
print(len(animais))

# Iterando sobre cada elemento
for animal in animais:
    print(animal)


lanche = ('Burguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[0])
print(lanche[1])
print(lanche[-1])
# lanche[3] = 'Bolo'


for i in range(0, len(lanche)):
    print(lanche[i])


tup1 = (1, 4, 8)
tup2 = (6, 2, 5, 4, 5)
tupla = tup1 + tup2
print(tupla.count(4))
print(tupla.index(4))
print(tupla.index(4, 2)) # tupla.index(numero, inicio)