total = 0
numeros = 0

while True:
    numero = int(input("Digite um número[999 para parar]: "))
    if numero == 999:
        break
    
    numeros += 1
    total += numero

print(f'O total é {total}')
print(f'Foram {numeros} números digitados')