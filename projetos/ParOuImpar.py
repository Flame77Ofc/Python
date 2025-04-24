import random
print("""----------------------------------------------------------------------------------
Bem vindo ao par ou impar! (Você estará jogando contra uma máquina). As regras são:
1- escolha entre par ou impar
2- escolha um número entre 1 a 100
Se você escolher par, e o resultado da soma do seu número com a da máquina der
par, então você ganha, vice-versa.
⚠ Aviso: O programa está se repetindo. Portanto, se você quer sair do programa, digite 777
Boa sorte!
----------------------------------------------------------------------------------""")
rodada = 1
try:
    while rodada < 1000:
        print(f'----------\nrodada {rodada}\n----------')
        rodada += 1
        machineChoice = random.randint(1, 100)
        pergunta = input('par ou impar: '); pergunta = pergunta.lower()
        userChoice = int(input('Escolha um número: '))
        soma = userChoice + machineChoice

        if userChoice == 777 or pergunta == 777:
            break

        elif pergunta != 'par' and pergunta != 'impar':
            print('POR FAVOR, DIGITE PAR OU IMPAR.')
            continue

        if userChoice >= 100 or userChoice <= 0:
            print('POR FAVOR, ESCOLHA UM NÚMERO ENTRE 1 A 100!\n')
            continue

        if (pergunta == 'par' and soma % 2 == 0) or (pergunta == 'impar' and soma % 2 != 0):
            print(f'VOCÊ GANHOU! A máquina escolheu {machineChoice} e você escolheu {userChoice} ({machineChoice + userChoice})')
        else:
            pontoMachine =+ 1
            print(f'A MÁQUINA GANHOU! A máquina escolheu {machineChoice} e você escolheu {userChoice} ({machineChoice + userChoice})')
except:
    print('ERRO!')