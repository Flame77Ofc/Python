# Escopo
variavel = 'valor'

# def function():
#     variavel = 'VALOR'
#     print(variavel)
# function()

# Resolvendo o problema de escopo: keyword global
def function():
    global variavel
    variavel = 'VALOR'
    print(variavel)
function()

print(variavel)