import random, time
computador = random.randint(1, 3)
escolha = input("Escolha entre PEDRA, PAPEL, TESOURA: ").lower()
if escolha not in ['pedra', 'papel', 'tesoura']:
    print("Por favor, escolha entre pedra, papel e tesoura!")
else:
    print("PREPARAR...")
    time.sleep(1)
    print('PEDRA')
    time.sleep(1)
    print('PAPEL')
    time.sleep(1)
    print('TESOURA')
    time.sleep(0.5)
    print('Já')

    if computador == 1:
        computador = 'pedra'
    elif computador == 2:
        computador = 'papel'
    elif computador == 3:
        computador = 'tesoura'

    empate = escolha == computador
    derrota = (escolha == 'pedra' and computador == 'papel') or \
              (escolha == 'papel' and computador == 'tesoura') or \
              (escolha == 'tesoura' and computador == 'pedra')

    if empate:
        print(f"Empate! Ambos escolheram {escolha}.")
    elif derrota:
        print(f"Você perdeu! Você escolheu {escolha} e o computador escolheu {computador}.")
    else:
        print(f"Você ganhou! Você escolheu {escolha} e o computador escolheu {computador}.")
