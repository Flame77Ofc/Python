# Faça um programa que receba a idade e a altura de várias pessoas e que calcule e mostre a média das alturas das pessoas com mais de 50 anos. Para encerrar a entrada de dados digite idade menor ou igual a zero.

lista = []
while True:
  idade = int(input('Digite a idade da pessoa: '))
  if idade <= 0:
    break
  altura = float(input('Digite a altura da pessoa em metros: '))

  if idade > 50:
    lista.append(altura)

if len(lista) >= 1:
  media = sum(lista) / len(lista)
  print(f'A média das alturas de pessoas com mais de 50 anos é de {media} metros')
else:
  print(f'Não houve pessoas com mais de 50 anos')
  
