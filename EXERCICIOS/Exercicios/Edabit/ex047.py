# Crie uma função que receba dois parâmetros, o primeiro indica uma string, e o segundo verifica se aquela string termina com as letras da primeira
def termina(str1, str2):
  return str1.endswith(str2)
print(termina('Homem', 'mem'))
print(termina('Aranha', 'a'))
print(termina('Prédio', 'to'))
