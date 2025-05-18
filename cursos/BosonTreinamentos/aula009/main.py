# Exceções: Um erro que ocorre no código e que pode ser corrigido

"""n1 = int(input('Digite um número '))
n2 = int(input('Digite um número '))

print(n1 + n2)"""

try:
    n1 = int(input('Digite um número '))
    n2 = int(input('Digite um número '))

    print(n1 + n2)
except:
    print("Erro!")