# Crie um programa que realiza a contagem regressiva de 20 segundos
from time import sleep

for i in range(20, 0, -1):
    print(i)
    sleep(1)
print('FIM!')
