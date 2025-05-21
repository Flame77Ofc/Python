# Escreva um programa que pergunte ao usuário o seu salário e calcule o aumento
salario = int(input("Digite o seu salário: "))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print(f'O seu salário ajustado é {salario + aumento}')