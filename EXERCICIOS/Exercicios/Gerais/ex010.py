#  Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.
def tabuada(numero):
  lista = [numero * i for i in range(1,11)]
  return lista
print(tabuada(4))
print(tabuada(24))
print(tabuada(89))
