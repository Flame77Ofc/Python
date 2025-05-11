def nome_da_funcao ():
    print('Hello, World!')
nome_da_funcao()


def prazer(nome):
    mensagem = print(f'Olá, {nome}')
    return mensagem
prazer('Gabriel')


def informacoes(**info):
    print(info)
informacoes(name='Flame', age=34)

def frutas(**fruta):
    print(fruta)
frutas(maçã = 3.90, laranja = 1.55, tomate = 0.50)




# Exercicio 1: Criar uma função que recebe um número e faz uma contagem regressiva desse número:
def contador(numero):
    for i in range(numero, 0, -1):
        print(i)
contador(15)
contador(5)


# Exercício 2: Criar uma função que recebe uma lista e retorna o maior número dessa lista:
def maior_numero(lista):
    maior = -1
    for i in lista:
        if i > maior:
            maior = i
    print(maior)
maior_numero([17, -5, 45, 9, 92, 64, 56])