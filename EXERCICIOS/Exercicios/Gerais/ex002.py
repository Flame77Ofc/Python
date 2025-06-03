# Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório desses números na tela. Após exibir a soma, o programa deve mostrar também os números que o usuário digitou, um por linha.  
lista = []
total = 0

for i in range(5):
    numero = int(input(f'Digite o número {i+1}: '))
    lista.append(numero)
    total += numero

print(f'A soma dos números digitados é {total}')
print(f'Os números digitados foram: ')
for num in lista:
    print(num)
