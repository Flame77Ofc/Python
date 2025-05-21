# faça uma tabuada, que leia o número que o usuário digitar
tabuada = int(input("Qual a tabuada que você deseja? "))

for i in range(0, 11):
    print(f'{tabuada} x {i} = {tabuada * i}')