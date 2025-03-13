# Chutar um número
print("\n-------------------------------------------------------------------\n✨ Bem vindo ao jogo da adivinhação \nChute um número de 1 a 10 até acertar ✨ \n-------------------------------------------------------------------\n")
import random
numero = random.randint(1, 10)

erro = 'Erro. por favor, tente novamente'
erro_num = 'Por favor, escreva um número entre 1 a 10.'

try:
    while True:
        chute = int(input('Digite o número de 1 a 10: '))
        if chute == 77:
            print('Shhhh, o número é', numero, end='!\n')
            continue
        elif chute == numero:
            print('Você acertou o número!')
            break
        elif chute <= 0 or chute > 10:
            print(erro_num)
            break
        elif chute > numero:
            print('O número é menor')
        else:
            print('O número é maior')
except ValueError:
    print(erro)