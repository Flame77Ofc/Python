# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
ano = int(input("Digite um ano qualquer: "))

if ano % 4 == 0:
    print("Ano bissexto")
else:
    print("Não é um ano bissexto")