"""A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	  Percentual de Reajuste
0.00 - 400.00      15%
400.01 - 800.00    12%
800.01 - 1200.00   10%
1200.01 - 2000.00  7%
Acima de 2000.00   2%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual."""

salario = float(input('Digite o salário do funcionário: '))

if salario > 2000:
    aumento = salario * 0.02
elif salario > 1200.00:
    aumento = salario * 0.07
elif salario > 800:
    aumento = salario * 0.1
elif salario > 400:
    aumento = salario * 0.12
elif salario > 0:
    aumento = salario * 0.15

print(aumento + salario)