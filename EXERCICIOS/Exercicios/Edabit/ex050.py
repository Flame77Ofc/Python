# Crie uma função que tem um número como argumento. Adicione todos os número de 1 até o número que foi passado como argumento. Se o número for 4, então deverá retornar 10 porque 1 + 2 + 3 + 4 = 10
def contagem(numero):
  if numero < 1 or numero > 1000:
    return 'Limite atingido [1000]'
  else:
    for i in range(numero):
      numero += i
    return numero
print(contagem(4))
print(contagem(13))
print(contagem(600))
print(contagem(1570))