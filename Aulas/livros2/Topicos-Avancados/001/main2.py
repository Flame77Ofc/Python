# ARGS E KWARGS
"""args
args: Usado quando não se sabe exatamante quantos argumentos uma função terá.
args te permitem colocar múltiplos valores na chamada da função
"""
def informacoes(*args):
    print(args)

# É retornado uma tupla
informacoes('João', 14, 'Maria', True) # Retorno: ('João', 14, 'Maria', True)



"""kwargs
semelhantes as args, porém agora você deve especificar o dado.
nos args, os dados ficavam soltos, porém agora você deve especificar
"""
def informacoes_pessoais(**kwargs):
    print(kwargs)

# É retornado um dicionário de chave-valor.
informacoes_pessoais(nome='João', idade=20) # Retorno: {'nome': 'João', 'idade': 20}

# também é possível fazer isso:
def infos(**dados):
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')

infos(nome='Matheus', idade=19)



# Praticando:
def animais(*args):
    print(*args)
animais('gato', 'cachorro', 'papagaio', 'baleia')

def vendas(*args):
    print(args)
vendas(12, 45, 98, 43, 6)


def pacientes(**kwargs):
    print(kwargs)
pacientes(ID458 = 'Fernando', ID476 = 'Lucas', ID465 = 'Maria')

def frutas(**kwargs):
    print(kwargs)
frutas(banana = 4.99, melancia = 6.99, laranja = 4.55)