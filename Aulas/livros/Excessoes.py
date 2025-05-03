# Excessões prevem que o código seja interrompido se ele encontrar um erro.
"numero = int(input('Digite um número: '))" # O usuário pode digitar um texto ao invés de um número.

# Solução:
try:
    numero = int(input('Digite um número: '))
    print(f'Voce digitou o número {numero}.')
except:
    print('Isso não é um número.')