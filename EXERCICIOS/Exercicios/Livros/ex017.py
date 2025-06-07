# Elabore um algoritmo que solicite que o usuário entre com dois números (inicial e final). Ao final o algoritmo deverá apresentar o valor total da soma de todos os números do intervalo digitado pelo usuário.
inicio = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))

if inicio >= fim:
  print(f'O valor inicial deve ser MENOR que o valor final')
else:
  total = 0
  for i in range(inicio, fim+1):
    total += i
  print(f'A soma de todos os números desde o inicio até o fim é {total}')
