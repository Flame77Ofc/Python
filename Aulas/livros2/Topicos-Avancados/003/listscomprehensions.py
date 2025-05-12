lista = [1, 2, 3, 4, 5]

# utilizando o for
for i in lista:
    print(i * 2)


lista_nova = [x*2 for x in lista]
print(lista_nova) # Retorna outra lista



lista = [1, 2, 3, 4, 5]
duplicacao = [x*2 for x in lista]
par = [x for x in lista if x % 2 == 0]
print(par)


texto = 'Python'
separar = [x.strip() for x in texto]
print(separar)