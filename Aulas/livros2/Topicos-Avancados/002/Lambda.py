# lambdas: Funções anônimas que não possuem nome
""" Uma Função normal
def nome_da_funcao(argumentos):
    bloco de codigo
"""

# um exemplo
soma = lambda x, y: print(x + y)
soma(15, 4)

# soma vs lambda
def cubo(y):
    print(y**3)
cubo(4)

cubo = lambda y: print(y**3)
cubo(6)