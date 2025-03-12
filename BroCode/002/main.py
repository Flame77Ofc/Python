# Número aleatório
import random
low = 1
high = 100

number = random.randint(low, high)
print(number)


opcoes = ('pedra', 'papel', 'tesoura')
opcao = random.choice(opcoes)
print(opcao)