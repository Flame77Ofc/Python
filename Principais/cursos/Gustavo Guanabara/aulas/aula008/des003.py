# Um programa que calcula a soma entre todos os números ímpares entre 1 a 500
soma = 0
contador = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        contador += 1
        soma += i  
print(f'São {contador} números que se somam num intervalo de 1 a 500 que sejam ímpares e divisiveis por 3. Resultado: {soma}')