bebidas = []

for i in range(5):
    bebida = input('Digite sua bebida favorita: ')
    bebidas.append(bebida)

bebidas.sort()

for bebida in bebidas:
    print(bebida)