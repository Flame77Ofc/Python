# Crie uma função que simule uma operação booleana.
def boolean(operador, bool1, bool2):
    operador = operador.lower()
    if operador == 'e' or operador == 'and':
        return True if bool1 and bool2 else False
    elif operador == 'ou' or operador == 'or':
        return True if bool1 or bool2 else False
    else:
        return 'ERRO! Não foi possível realizar a comparação'
print(boolean('e', True, True))
print(boolean('and', True, False))
print(boolean('or', False, True))
print(boolean('ou', False, False))