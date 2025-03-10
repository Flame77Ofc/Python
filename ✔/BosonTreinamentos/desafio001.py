print('Por favor, diga suas 5 bebidas favoritas')
listaBebidas = []
for i in range(5):
    bebida = input(f'Digite a {i+1}ª bebida: ')
    listaBebidas.append(bebida)
    
listaBebidas.sort()

print("\nSuas bebidas favoritas:")
for bebida in listaBebidas:
    print(bebida)