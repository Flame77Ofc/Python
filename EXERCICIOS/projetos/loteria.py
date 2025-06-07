# Simulador de Loteria: Gere números aleatórios para simular jogos de loteria e compare com a entrada do usuário.
import random

numeros_usuario = []
numeros_computador = []
for i in range(6):
    computador = random.randint(1, 60)
    print(computador)
    numero = int(input(f'Digite o número {i+1}: '))

    while (numero < 1 or numero > 60) or (numero in numeros_usuario):
        numero = int(input(f'Por favor, digite corretamente\nDigite o número {i+1}: '))

        
    numeros_computador.append(computador)
    numeros_usuario.append(numero)

print(numeros_computador)
print(numeros_usuario)

total = 1

for i in numeros_usuario:
    for x in numeros_computador:
        if i == x:
            total += 3600

print(total)