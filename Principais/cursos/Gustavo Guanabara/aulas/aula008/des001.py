# Faça um programa que mostre na tela uma contagem regressiva para fogos de artificio, indo de 10 até 0, com pausa de um segundo entre eles
import time

for i in range(10, -1, -1):
    time.sleep(1)
    print(i)
print("fogos!!! 🎇🎆🎇🎆🎇🎇🎆")