def nome_da_funcao ():
    print('Hello, World!')
nome_da_funcao()


def prazer(nome):
    mensagem = print(f'Olá, {nome}')
    return mensagem
prazer('Gabriel')


def informacoes(**info):
    print(info)
informacoes(name='Flame', age=34)

def frutas(**fruta):
    print(fruta)
frutas(maçã = 3.90, laranja = 1.55, tomate = 0.50)