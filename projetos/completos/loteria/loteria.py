# Simulador de Loteria: Gere números aleatórios para simular jogos de loteria e compare com a entrada do usuário.
import random

nums_usuario = []
nums_computador = []
for i in range(6):
    computador = random.randint(1, 60)
    nums_computador.append(computador)

    while nums_computador.count(computador) > 1:
        nums_computador.pop()
        computador = random.randint(1, 60)
        nums_computador.append(computador)

    numero = int(input(f'Digite o número {i+1}: '))

    while (numero < 1 or numero > 60) or (numero in nums_usuario):
        numero = int(input(f'Deve estar entre 1 a 60 e não deve ser repetido!\nDigite o número {i+1}: '))

    nums_usuario.append(numero)

dinheiro = 0
acertos = 0

for i in nums_usuario:
    for x in nums_computador:
        if i == x:
            dinheiro += 250000
            acertos += 1

if acertos == 0:
    print('Você não acertou nenhum número!')
else:
    print(f'Parabéns!! Você acertou {acertos} numero(s)!')
    print(f'Dinheiro: {dinheiro}')

print(f'Seus números foram: {nums_usuario}')
print(f'Os números do computador foram: {nums_computador}')
