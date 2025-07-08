from . import astronomia
from . import historia
from . import tecnologia

print('Quer ver qual assunto?')
print('1: Astronomia')
print('2: História')
print('3: Tecnologia')

assunto = int(input('Digite:\n>>>'))
while assunto not in range(1, 4):
    assunto = int(input('Digite corretamente.\n>>>'))

if assunto == 1:
    print('Deseja ver qual site? ')
    print('1: inovacaotecnologica')
    print('2: revistagalileu')
    print('3: canaltech')
    print('4: bbc')
    print('5: cnnbrasil')
    print('6: Todas')

    menu = int(input('Digite:\n>>>'))
    while menu not in range(1, 7):
        menu = int(input('Digite corretamente.\n>>>'))
    if menu == 1:
        astronomia.site1()
    elif menu == 2:
        astronomia.site2()
    elif menu == 3:
        astronomia.site3()
    elif menu == 4:
        astronomia.site4()
    elif menu == 5:
        astronomia.site5()
    elif menu == 6:
        astronomia.site1()
        astronomia.site2()
        astronomia.site3()
        astronomia.site4()
        astronomia.site5()

elif assunto == 2:
    print('Deseja ver qual site? ')
    print('1: veja abril')
    print('2: folha uol')
    print('3: super abril')
    print('4: Todas')

    menu = int(input('Digite:\n>>>'))
    while menu not in range(1, 5):
        menu = int(input('Digite corretamente.\n>>>'))
    if menu == 1:
        historia.site1()
    elif menu == 2:
        historia.site2()
    elif menu == 3:
        historia.site3()
    elif menu == 4:
        historia.site1()
        historia.site2()
        historia.site3()


elif assunto == 3:
    print('Deseja ver qual site? ')
    print('1: inovacaotecnologica (informática)')
    print('2: inovacaotecnologica (robótica)')
    print('3: oglobo')
    print('4: Todas')

    menu = int(input('Digite:\n>>>'))
    while menu not in range(1, 5):
        menu = int(input('Digite corretamente.\n>>>'))
    if menu == 1:
        tecnologia.site1()
    elif menu == 2:
        tecnologia.site2()
    elif menu == 3:
        tecnologia.site3()
    elif menu == 4:
            tecnologia.site1()
            tecnologia.site2()
            tecnologia.site3()