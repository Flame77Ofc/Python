# Verifica se o usuário digitou um número entre 1 a 10:
numero = int(input("Digite um número inteiro entre 1 a 10: "))

if numero > 0 and numero < 11:
  print("Número está entre 1 e 10!")
else:
  print("Era um número entre 1 e 10...")