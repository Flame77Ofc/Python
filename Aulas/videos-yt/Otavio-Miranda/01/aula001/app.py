# while
i = 1
while i < 5:
    print(i)
    i += 1
# print(1)
# print(1)
# print(1)
# print(1)
# print(1)
# print(1)
# print(1)


# Pular uma iteração
# a = 1
# while a < 5:
#     if a == 3:
#         continue
#     print(a)
#     a += 1


# # Quebrar uma iteração
# y = 1
# while y < 10:
#     if y == 3:
#         break
#     print(y)


# while, else: executará o else após a condição do while ser falsa.
foguete = 0
while foguete <= 3:
    print(f'Contagem regressiva: {foguete}')
    foguete += 1
else:
    print('Lançar!')


# quando é acionado o break, o else não será executado!
contador = 1
while contador < 10:
    print(contador)
    if contador == 5:
        break
    contador += 1
else:
    print('Não será executado')
print('Isso será executado')



# Iterando com o loop while
string = 'o rato roeu a roupa do rei de roma'

contador = 0
while contador < len(string):
    print(string[contador], end='')
    contador += 1