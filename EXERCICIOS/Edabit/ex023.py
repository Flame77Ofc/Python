"""Crie uma função que verifica se todos os elementos de uma lista são True"""
def todos_True(*args):
    return all(args)
print(todos_True(True, True, True))
print(todos_True(True, False, True))
print(todos_True(0))
print(todos_True(1))
