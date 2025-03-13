# Pedir ao usuário inserir uma velocidade, e comparar com seus devidos valores de condição.
try:
    velocidade = int(input('Qual é a sua velocidade?\n'))
    if velocidade < 80:
        print('Parabéns por seguir as regras de trânsito.')
    elif velocidade >= 80 and velocidade <= 90:
        print('Multa leve')
    elif velocidade >= 91 and velocidade <= 110:
        print('Multa grave')
    elif velocidade >= 121 and velocidade <= 150:
        print('MULTA MUITO GRAVE')
    else:
        print('Acusação de usar um foguete numa estrada')
except:
    print('Ocorreu um erro, por favor, tente novamente.')

"""
CORRETO:
try:
    velocidade = int(input('Qual é a sua velocidade?\n'))
    velocidade_maxima = 80
    if velocidade <= velocidade_maxima:
        print('Parabéns por seguir as regras de trânsito.')
    elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
        print('Multa leve')
    elif velocidade > velocidade_maxima +11 and velocidade <= velocidade_maxima + 20:
        print('Multa grave')
    elif velocidade > velocidade_maxima+ 20:
        print('MULTA MUITO GRAVE')
    else:
        print('Acusação de usar um foguete numa estrada')
except:
    print('Ocorreu um erro, por favor, tente novamente.')
"""