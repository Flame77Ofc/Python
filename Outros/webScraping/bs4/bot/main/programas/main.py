print('Deseja ver a programação de qual programa?')
print('1 - GLOBO')
print('2 - SBT')

menu = int(input('Digite:\n>>>'))
while menu not in range(1, 3):
    menu = int(input('Digite corretamente:\n>>>'))

if menu == 1:
    from . import globo
elif menu == 2:
    from . import sbt