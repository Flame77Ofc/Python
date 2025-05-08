jogo_da_velha = """[1, 2, 3]
[4, 5, 6]
[7, 8, 9]"""

print(jogo_da_velha)



contador = 10
while contador > 1:
    if contador % 2 == 0:
        numero = int(input('Digite um número: '))
        if numero == 1:
            jogo_da_velha = jogo_da_velha.replace('1', 'x')
            print(jogo_da_velha)
            if jogo_da_velha == 'o':
                print('Erro')
        elif numero == 2:
            jogo_da_velha = jogo_da_velha.replace('2', 'x')
            print(jogo_da_velha)
        elif numero == 3:
            jogo_da_velha = jogo_da_velha.replace('3', 'x')
            print(jogo_da_velha)
        elif numero == 4:
            jogo_da_velha = jogo_da_velha.replace('4', 'x')
            print(jogo_da_velha)
        elif numero == 5:
            jogo_da_velha = jogo_da_velha.replace('5', 'x')
            print(jogo_da_velha)
        elif numero == 6:
            jogo_da_velha = jogo_da_velha.replace('6', 'x')
            print(jogo_da_velha)
        elif numero == 7:
            jogo_da_velha = jogo_da_velha.replace('7', 'x')
            print(jogo_da_velha)
        elif numero == 8:
            jogo_da_velha = jogo_da_velha.replace('8', 'x')
            print(jogo_da_velha)
        elif numero == 9:
            jogo_da_velha = jogo_da_velha.replace('9', 'x')
            print(jogo_da_velha)


    elif contador % 2 == 1:
        numero = int(input('Digite um número: '))
        if numero == 1:
            jogo_da_velha = jogo_da_velha.replace('1', 'o')
            print(jogo_da_velha)
        elif numero == 2:
            jogo_da_velha = jogo_da_velha.replace('2', 'o')
            print(jogo_da_velha)
        elif numero == 3:
            jogo_da_velha = jogo_da_velha.replace('3', 'o')
            print(jogo_da_velha)
        elif numero == 4:
            jogo_da_velha = jogo_da_velha.replace('4', 'o')
            print(jogo_da_velha)
        elif numero == 5:
            jogo_da_velha = jogo_da_velha.replace('5', 'o')
            print(jogo_da_velha)
        elif numero == 6:
            jogo_da_velha = jogo_da_velha.replace('6', 'o')
            print(jogo_da_velha)
        elif numero == 7:
            jogo_da_velha = jogo_da_velha.replace('7', 'o')
            print(jogo_da_velha)
        elif numero == 8:
            jogo_da_velha = jogo_da_velha.replace('8', 'o')
            print(jogo_da_velha)
        elif numero == 9:
            jogo_da_velha = jogo_da_velha.replace('9', 'o')
            print(jogo_da_velha)


    
    contador -= 1