# Faça um Programa que leia um número e exiba o dia correspondente da semana

dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
for i, dia in enumerate(dias):
    print(i+1, dia)

numero = int(input('Digite um número do dia da semana: '))
if numero not in [i+1 for i in range(7)]:
    print('Não foi possível acessar')
else:
    print(dias[numero-1])