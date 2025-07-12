def aumentar(preco, quantidade):
    aumento = (preco * quantidade) / 100
    return preco + aumento


def diminuir(preco, quantidade):
    reducao = (preco * quantidade) / 100
    return preco - reducao


def dobro(preco):
    return preco * 2


def metade(preco):
    return preco / 2
