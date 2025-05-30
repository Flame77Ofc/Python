temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input('Nome:\n>>>')))
    temp.append(float(input('Peso:\n>>>')))

    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()

    resp = input("Deseja continuar? [S/N]\n>>>")
    if resp in 'Nn':
        break

print(f'Os dados foram {princ}')
print(f'O maior peso foi de {maior}kg')
print(f'O menor peso foi de {menor}kg')
