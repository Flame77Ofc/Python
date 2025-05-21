# Escreva um programa que permite que o programa escolha um número entre 0 a 5 e peça ao usuário descobrir qual o número que o computador escolheu
import random
import time

computador = random.randint(0, 5)
escolha = int(input("Escolha um número entre 0 a 5: "))
print('PROCESSANDO AS INFORMAÇÕES...')
time.sleep(2)

if escolha == computador:
    print("Você acertou!")
else:
    print("Você errou!")
print(f"O número era {computador}")
