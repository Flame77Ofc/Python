# Crie uma função que tem um número como parâmetro e retorna os 10 primeiros múltiplos do número incrementado a +1
def multiplo(numero):
  lista = []
  repeticao = numero * 10

  for i in range(1, repeticao+1, numero):
    lista.append(numero + i)
  lista = str(lista)

  return lista
print(multiplo(3))
print(multiplo(9))
print(multiplo(12))
print(multiplo(1))
