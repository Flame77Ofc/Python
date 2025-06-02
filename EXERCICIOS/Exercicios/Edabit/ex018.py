"""Crie uma função que retorne True se a mensagem for vazia"""
def vazio(mensagem = ''):
    return mensagem == ''
print(vazio(''))
print(vazio(""))
print(vazio())
print(vazio('abcdef'))