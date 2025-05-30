# Funções
def linha():
    print('-------------------------------')

linha()
print('Aprenda Python')
linha()
linha()
print('Gustavo Guanabara')
linha()


def contador(*num):
    print(len(num))
contador(4, 6, 2, 8, 3, 1, 2, 9, 10)