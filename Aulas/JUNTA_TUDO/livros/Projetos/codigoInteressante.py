# Se lembra, Flame?... Esse código retorna os diamantes e guarda num arquivo.
dima = int(input('Quantos diamantes você tem? '))

if dima > 0:
    dima = str(dima)
    a = len(dima)
    print('len:', a)

    with open('arquivo.txt', 'w') as arquivo:
        arquivo.write(str(dima))
        arquivo.seek(0)
        arquivo.close()
else:
    dima = str(dima)
    a = len(dima)
    dima = int(input('Quantos diamantes você tem? '))
    dima = str(dima)
    a = len(dima)
    with open('arquivo.txt', 'w') as arquivo:
        arquivo.write(str(dima))
        arquivo.seek(0)
        arquivo.close()

a = dima
print(a)