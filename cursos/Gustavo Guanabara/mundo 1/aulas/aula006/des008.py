# Desenvolva um programa que leia o comprimento de três retas e diga se podem formar um triângulo
r1 = int(input("Digite a reta 1: "))
r2 = int(input("Digite a reta 2: "))
r3 = int(input("Digite a reta 3: "))
# "se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo"

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")