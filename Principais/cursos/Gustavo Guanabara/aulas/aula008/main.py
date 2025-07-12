# # Laços de repetição
# # Executam um determinado bloco de código até a sua condição sere satisfeita, ou seja, False.
# for contador in range(1, 11):
#     print(contador)

# for c in range(1, 10, 3):
#     print("Olá, Mundo!")
# print('Fim')


# numero = int(input("Até que número o contador deve ir? "))

# for contador in range(1, numero+1):
#     print(contador)


# inicio = int(input("Deseja começar de qual número? "))
# fim = int(input("Deseja terminar em qual número? "))
# passos = int(input("Deseja dar quantos em quantos passos? "))
# fim = fim + 1

# for i in range(inicio, fim, passos):
#     print(i)




# Somando todos os valores
soma = 0

for i in range(1, 11):
    numero = int(input("Digite o número: "))
    soma += numero
print(soma)
