def soma(*numeros):

    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma(10, 20, 30, 40))
