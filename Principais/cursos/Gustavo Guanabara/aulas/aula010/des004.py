tupla = []
pares = 0
for i in range(4):
    numero = int(input("Digite um número\n>>>"))
    tupla.append(numero)
    if numero % 2 == 0:
        pares += 1
tupla = tuple(tupla)
print(tupla)

print(f'O valor 9 aparece {tupla.count(9)} vezes')
if 3 not in tupla:
    print('3 Não aparece na tupla.')
else:
    print(f'A primeira posição do número 3 está no índice {tupla.index(3)}')
print(f'Foram ao total {pares} pares')