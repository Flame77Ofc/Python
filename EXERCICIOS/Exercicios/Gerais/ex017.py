# Crie uma função que receba um número e retorne a lista de divisores desse número de 1 até esse mesmo número. Também diga se este número é primo
def divisores(numero):
    lista = [item for item in range(1, numero + 1) if numero % item == 0]
    if len(lista) == 2:
        return f'O número {numero} é primo. Divisores: {lista}'
    else:
        return f'O número {numero} é composto. Divisores: {lista}'
print(divisores(16))
print(divisores(32))
print(divisores(160))
print(divisores(17))
