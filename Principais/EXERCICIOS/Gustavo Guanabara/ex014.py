# Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.

dias = int(input('Quantos dias em um mês você trabalha? '))
horas = 8
ganha = 25

salario = (ganha * horas) * dias

print(f'O salário do funcionário é de {salario}')