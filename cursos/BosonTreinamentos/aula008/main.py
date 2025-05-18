# Escopos globais e locais
var_global = "global"

def escreve():
    var_local = "local"
    print(f'Variável local: {var_local}')
    print(f'Variável global: {var_global}')
escreve()

def div():
    print(var_global)
    print(var_local)
div()