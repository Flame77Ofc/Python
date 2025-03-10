# Exceções: Tratamento de Erros ⇒
n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))
try:
    r = round(n1/n2, 2) # 2 ⇒ Casas decimais
except ZeroDivisionError:
    print('Não é possível dividir por 0')
else:
    print(f'Resultado: {r}')