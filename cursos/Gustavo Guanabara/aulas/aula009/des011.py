print(f'================================\n{'BANCO'.center(31, ' ')}\n================================')
cinquenta = 0
vinte = 0
dez = 0
real = 0

while True:
    valor = int(input(("Digite o valor a ser sacado: ")))
    while valor - 50 >= 0:
        valor -= 50
        cinquenta += 1
    while valor - 20 >= 0:
        valor -= 20
        vinte += 1
    while valor - 10 >= 0:
        valor -= 10
        dez += 1
    while valor - 1 >= 0:
        valor -= 1
        real += 1
    else:
        break
print(f'Total de {cinquenta} {'cédula' if cinquenta == 1 else 'cédulas'} de R$50')
print(f'Total de {vinte} {'cédula' if vinte == 1 else 'cédulas'} de R$20')
print(f'Total de {dez} {'cédula' if dez == 1 else 'cédulas'} de R$10')
print(f'Total de {real} {'cédula' if real == 1 else 'cédulas'} de R$1')
print('================================')
