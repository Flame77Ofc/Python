import random
machine = random.choice(["pedra", "papel", "tesoura"])
escolha = input("Pedra, papel ou tesoura? ").lower()
print("A máquina escolheu:", machine)

if machine == escolha:
    print("Empate!")
elif (machine == "pedra" and escolha == "papel") or \
     (machine == "papel" and escolha == "tesoura") or \
     (machine == "tesoura" and escolha == "pedra"):
    print("Você ganhou! A máquina perdeu.")
elif (machine == "pedra" and escolha == "tesoura") or \
     (machine == "papel" and escolha == "pedra") or \
     (machine == "tesoura" and escolha == "papel"):
    print("Você perdeu! A máquina ganhou.")
else:
    print("Escolha inválida! Digite pedra, papel ou tesoura.")