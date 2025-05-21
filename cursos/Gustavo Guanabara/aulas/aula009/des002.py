# Um programa que pede ao usuário acertar o número escolhido pelo computador
import random
computador = random.randint(0, 10)
escolha = int(input("Tente acertar o número: "))

palpites = 1
while escolha != computador:

    # Verifica se escolha é menor que 0 ou maior que 10 e repete até ser um número válido
    while escolha < 0 or escolha > 10:
        print('Por favor, escolha um número entre 0 a 10!')
        escolha = int(input("Tente acertar o número: "))

    if escolha > computador:
        print('Chute alto')
    elif escolha < computador:
        print('Chute baixo')

    escolha = int(input("Tente acertar o número: "))
    palpites += 1

else:
    print("Você acertou!")
print(f'Foram necessários {palpites}')