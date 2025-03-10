# Escopo Global e Local
varGlobal = 'Curso completo de python'
def escreveTexto():
    varLocal = 'Nome'
    print(varGlobal)
    print(varLocal)

if __name__ == '__main__':
    print('escreve texto')
    escreveTexto()

    print(varGlobal)
    print(varLocal)