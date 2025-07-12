import time
inicio = int(input("Digite o número para iniciar a contagem regressiva: "))

for i in range(inicio, -1, -1):
    print(i)
    time.sleep(1)

print("⏰ Tempo esgotado!")
