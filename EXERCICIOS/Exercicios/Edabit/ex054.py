# Crie uma função que pega um número como argumento e retorna "Fizz", "Buzz" ou "FizzBuzz".

# Se o número for um múltiplo de 3, a saída deve ser "Fizz".
# Se o número dado for um múltiplo de 5, a saída deve ser "Buzz".
# Se o número dado for um múltiplo de 3 e 5, a saída deve ser "FizzBuzz".
# Se o número não é um múltiplo de 3 ou 5, o número deve ser emitido por conta própria, como mostrado nos exemplos abaixo.
# A saída deve ser sempre uma string, mesmo que não seja um múltiplo de 3 ou 5.
def fizz_buzz(numero):
  if numero % 3 == 0 and numero % 5 == 0:
    return 'FizzBuzz'
  elif numero % 3 == 0:
    return 'Fizz'
  elif numero % 5 == 0:
    return 'Buzz'
  else:
    return numero
print(fizz_buzz(15))
print(fizz_buzz(5))
print(fizz_buzz(3))
print(fizz_buzz(4))
