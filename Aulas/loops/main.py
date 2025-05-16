# Loops
# for
for x in range(11):
    print(x)


cor = ['Verde', 'Amarelo', 'Cinza', 'Azul', 'Vermelho']
for x in cor:
    print(x)

string = 'Olá, Mundo'
for letra in string:
    print(letra)



numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(numero)
    if numero == 7:
        break


# while
num = 1
while num <= 10:
    print(num)
    num += 1

# break: para quando encontra o 5
num = 1
while num <= 10:
    if num == 5:
        break
    print(num)
    num += 1

# continue: Pula o 5
num2 = 1
while num2 <= 10:
    num2 += 1
    if num2 == 5:
        continue
    print(num2)

