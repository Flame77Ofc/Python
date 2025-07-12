# Faça uma função que dada uma lista de números, retorne a média entre eles.
def media(lista):
  soma = sum(lista)
  return soma / len(lista)
print(media([5, 5]))
print(media([10, 15, 20]))
print(media([60, 24, 525, 460, 56]))