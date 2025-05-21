# Escreva um programa que leia a velocidade de um carro
# se ele ultrapassar 80 km, mostre uma mensagem dizendo que ele foi multado. A multa deve custar 7 reais para cada km acima do limite
velocidade = float(input("Qual a velocidade do carro? "))

if velocidade > 80:
    print("Você foi multado!")
    multa = (velocidade - 80) * 7
    print(f"A multa custou {multa} reais")
else:
    print("Tudo certo!")