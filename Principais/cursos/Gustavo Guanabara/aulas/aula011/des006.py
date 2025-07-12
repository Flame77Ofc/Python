numeros = []
maior = menor = 0

for repeticao in range(5):
    numero = int(input("Digite um número:\n>>>"))

    if repeticao == 0 or numero > numeros[-1]:
        numeros.append(numero)
    else:
        pos = 0
        while pos < len(numeros):
            if numero <= numeros[pos]:
                numeros.insert(pos, numero)
                break
            pos += 1
print(numeros)