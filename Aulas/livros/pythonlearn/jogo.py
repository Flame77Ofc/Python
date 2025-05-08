jogo_da_velha = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
for visualizacao in jogo_da_velha:
    print(visualizacao)

def visu(indice1, indice2, letra):
    jogo_da_velha[indice1][indice2] = letra
    for visualizacao in jogo_da_velha:
        print(visualizacao)

contador = 10
while contador > 1:
    if (jogo_da_velha[0][0] == 'x' and jogo_da_velha[0][1] == 'x' and jogo_da_velha[0][2] == 'x') or (jogo_da_velha[1][0] == 'x' and jogo_da_velha[1][1] == 'x' and jogo_da_velha[1][2] == 'x') or (jogo_da_velha[2][0] == 'x' and jogo_da_velha[2][1] == 'x' and jogo_da_velha[2][2] == 'x') or (jogo_da_velha[0][0] == 'x' and jogo_da_velha[1][0] == 'x' and jogo_da_velha[2][0] == 'x') or (jogo_da_velha[0][1] == 'x' and jogo_da_velha[1][1] == 'x' and jogo_da_velha[2][1] == 'x') or (jogo_da_velha[0][2] == 'x' and jogo_da_velha[1][2] == 'x' and jogo_da_velha[2][2] == 'x') or (jogo_da_velha[0][0] == 'x' and jogo_da_velha[1][1] == 'x' and jogo_da_velha[2][2] == 'x') or (jogo_da_velha[2][0] == 'x' and jogo_da_velha[1][1] == 'x' and jogo_da_velha[0][2] == 'x'):
        print('Ganhou')
        break

    if contador % 2 == 0:
        numero = int(input('Digite um número: '))
        if numero == 1:
            visu(0, 0, 'x')
        elif numero == 2:
            visu(0, 1, 'x')
        elif numero == 3:
            visu(0, 2, 'x')
        elif numero == 4:
            visu(1, 0, 'x')
        elif numero == 5:
            visu(1, 1, 'x')
        elif numero == 6:
            visu(1, 2, 'x')
        elif numero == 7:
            visu(2, 0, 'x')
        elif numero == 8:
            visu(2, 1, 'x')
        elif numero == 9:
            visu(2, 2, 'x')

    elif contador % 2 == 1:
        numero = int(input('Digite um número: '))
        if numero == 1:
            visu(0, 0, 'o')
        elif numero == 2:
            visu(0, 1, 'o')
        elif numero == 3:
            visu(0, 2, 'o')
        elif numero == 4:
            visu(1, 0, 'o')
        elif numero == 5:
            visu(1, 1, 'o')
        elif numero == 6:
            visu(1, 2, 'o')
        elif numero == 7:
            visu(2, 0, 'o')
        elif numero == 8:
            visu(2, 1, 'o')
        elif numero == 9:
            visu(2, 2, 'o')

    else:
        numero = int(input('Digite um número: '))
    
    contador -= 1