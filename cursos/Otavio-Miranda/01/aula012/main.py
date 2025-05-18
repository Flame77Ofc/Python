# Tuplas
tupla = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla = tupla + tupla2
print(tupla)


tupla = 'Miguel', 'Pedro', 'Paulo'
print(tupla[2])
for nome in tupla:
    print(nome)


tupla = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
n1, n2, *n = tupla
print(n1, n2, n)


tupla = 'Maria', 'José'
print(tupla * 2)