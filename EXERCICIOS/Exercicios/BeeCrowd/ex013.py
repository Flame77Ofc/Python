"""Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.
[DIAGRAMA IMCOMPATÍVEL]
"""

vertebrado = input('Seu animal é vertebrado ou invertebrado?: ')
if vertebrado == 'vertebrado':
    ave_mamif = input('Seu animal é uma ave ou um mamífero?: ')
    if ave_mamif == 'ave':
        carn_oniv = input('Seu animal é carnívoro ou onívoro?: ')
        if carn_oniv == 'carnivoro' or carn_oniv == 'carnívoro':
            print('Seu animal é a águia')
        else:
            print('Seu animal é a pomba')
    else:
        oniv_herb = input('Seu animal é onívoro ou herbívoro?: ')
        if oniv_herb == 'onivoro':
            print('Seu animal é o homem')
        else:
            print('Seu animal é a vaca')

elif vertebrado == 'invertebrado':
    inseto_anelideo = input('Seu animal é um inseto ou um anelideo?: ')
    if inseto_anelideo == 'inseto':
        hema_herb = input('Seu animal é hematofago ou herbivoro?: ')
        if hema_herb == 'hematofago' or hema_herb == 'herbivoro':
            print('Seu animal é a pulga')
        else:
            print('Seu animal é a lagarta')
    else:
        oniv_herb = input('Seu animal é hematofago ou onivoro?: ')
        if oniv_herb == 'hematofago':
            print('Seu animal é a saguessuga')
        else:
            print('Seu animal é a minhoca')