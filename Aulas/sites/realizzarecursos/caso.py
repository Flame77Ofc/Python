numero = 2
match numero:
    case 1:
        print('O número é 1')
    case 2 | 3 | 4:
        print('O número é 2 ou 3 ou 4')
    case _:
        print('Que número é?')