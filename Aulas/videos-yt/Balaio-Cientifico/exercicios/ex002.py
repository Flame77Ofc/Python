# Problema: Você precisa criar um robô que é capaz de responder ao usuário se determinado número é par ou impar. Você deve pedir a pessoa para digitar um número aleatório e responder com uma mensagem dizendo: "O número inserido é par" ou "O número inserido é impar

numero = int(input("Digite um número: "))

def robo(numero):
    if numero % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
        
robo(numero)