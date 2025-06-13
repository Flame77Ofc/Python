# Chutar um número
print("\n-------------------------------------------------------------------\n✨ Bem vindo ao jogo da adivinhação \nChute um número de 1 a 10 até acertar ✨ \n-------------------------------------------------------------------\n")
import random
numero = random.randint(1, 10)

try:
    while True:
        chute = int(input('Digite o número de 1 a 10: '))

        if chute == numero:
            print('Você acertou o número!')
            break
        elif chute <= 0 or chute > 10:
            print('Por favor, escreva um número entre 1 a 10.')
        elif chute > numero:
            print('Chute alto! O número é MENOR')
        else:
            print('Chute baixo! O número é MAIOR')   
except:
    print('Deve ser um número.')