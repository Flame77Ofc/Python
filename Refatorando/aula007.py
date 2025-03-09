# Exeções
try:
    numero = int(input('Digite um número: '))
    print(numero)
except ValueError:
    print('Será executado se o valor estiver errado')
except:
    print('Será executado se der outro erro')
finally:
    print('Isso sempre será executado')