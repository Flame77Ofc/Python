# Criar uma função que recebe um número e faz uma contagem regressiva desse número
def contador(numero):
    contagem = [i for i in range(numero, 0, -1)]
    return contagem
print(contador(15))
print(contador(5))
