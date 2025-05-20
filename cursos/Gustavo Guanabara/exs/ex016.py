# Um programa que pergunte 4 usuários e imprima os 4 usuários em uma ordem embaralhada
import random
p1 = input("Digite o nome da primeira pessoa: ")
p2 = input("Digite o nome da segunda pessoa: ")
p3 = input("Digite o nome da terceira pessoa: ")
p4 = input("Digite o nome da quarta pessoa: ")

lista = [p1, p2, p3, p4]
random.shuffle(lista)

print(lista)