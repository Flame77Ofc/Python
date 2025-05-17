def func(*agrs, **kargs):
    print(agrs)
    print(kargs)
func('João', idade=13)

# agrs: Permite que uma função receba valores indefinidos, útil quando não se sabe a quantidade de valores que é preciso.
def mult(*num):
    for i in num:
        print(i * 2)
mult(5, 6, 7, 8, 9)

# wkargs: Semelhante aos args, mas agora é necessário especificar chave=valor, semelhante a um dicionário
def nome_idade(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
nome_idade(nome='João', idade=27)


def cubo(*num):
    for i in num:
        print(i**3)
cubo(2, 3)