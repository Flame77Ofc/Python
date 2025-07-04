# Crie uma função que retorna um número, baseado na string da chamada de função.
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
strings = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
def retorna_numero(string):
  posicao = strings.index(string)
  return numeros[posicao]
print(retorna_numero('seis'))
print(retorna_numero('nove'))
print(retorna_numero('zero'))
