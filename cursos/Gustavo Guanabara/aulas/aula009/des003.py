# Crie um programa que mostre um menu na tela:
"""
1: somar
2: multiplicar
3: qual o maior valor
4: novos números
5: sair do programa
"""

n1 = int(input(">>> Digite o número: "))
n2 = int(input(">>> Digite o número: "))

while True:
    opcoes = """\nDigite:\n1: Somar os dois números\n2: Multiplicar os dois números\n3: Ver qual o maior valor\n4: Digitar novos números\n5: Sair do programa"""
    print(opcoes)
    menu = int(input(">>> O que deseja? "))

    while menu not in [1, 2, 3, 4, 5]:
        print(f'{opcoes}')
        menu = int(input(">>> Por favor, digite a operação certa: "))

    if menu == 1:
        print(f'A soma dos dois números é {n1 + n2}')
    elif menu == 2:
        print(f'A multiplicação entre os dois números é {n1 * n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n1} é menor que {n2}')
    elif menu == 4:
        n1 = int(input(">>> Digite o número: "))
        n2 = int(input(">>> Digite o número: "))
    elif menu == 5:
        print("Foi ótimo te ver!")
        break