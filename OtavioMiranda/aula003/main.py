# O laço de repetição while
"""
while True:
    nome = input('Qual é seu nome? ')
    nome = nome.lower()
    if nome == 'flame':
        print(f'Olá, {nome}')
        break
    print('Ops, não é a pessoa certa!')
"""

x = 1
while x <= 5:
    print(x)
    x += 1

print()

# while else
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
else:
    print('Acabou\n')


# O laço de repetição for
texto = 'Oi'
for index in texto:
    print(index)

print()
 

# for else
amigo = 'João'
for elementos in amigo:
    print(elementos)
else:
    print('Acabou\n')


# for range
for n in range(1, 11):
    print(n)