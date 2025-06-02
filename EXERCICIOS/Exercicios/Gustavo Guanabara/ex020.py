# Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO.
ano = int(input('Digite um ano qualquer: '))

# print('Ano é Bissexto' if ano % 4 == 0 else 'Ano não é Bissexto')

if ano % 4 == 0 and ano % 100 != 0:
    print('Ano é Bissexto')
else:
    print('Ano não é Bissexto')