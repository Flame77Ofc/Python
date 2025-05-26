# # Variáveis
# # Armazenam valores na memória do computador. São essenciais em todo programa
# nome = 'John'
# idade = 35

# print(f"Um homem chamado {nome} com {idade} anos")

# # Trabalhando com números
# numero = 6
# print(numero + 9)
# print(numero * 5)

# from math import *
# print(sqrt(81))
# print(ceil(65.212984))



# # Interação com o usuário
# nome = input("Digite o seu nome: ")
# print(f'O nome do usuário é {nome}')



# # Tuplas
# # Tupla é um tipo de dado que pode armazenar diversos valores
# # Tuplas são úteis para armazenar valores que não serão modificados
# animais = ('Gato', 'Jacaré', 'Macaco')

# # Não é possível alterar o valor de uma tupla
# # animais[1] = 'Urso'


# # Funções
# # Funções são blocos de código reutilizáveis e gerenciáveis que evita a repetição de código
# def mensagem():
#     print('Olá!')
# mensagem()

# Para executar o que estiver dentro da função é preciso chamar a função
# Chamar a função significa colocar o nome da função seguido pelos seus parênteses.


# def pizza():
#     print('Bem vindo à pizzaria!')
# pizza()

# Parâmetros e argumentos
# São as variáveis exclusivas que a função terá.
# def prazer(nome):
#     print(f'Olá, {nome}!')
# prazer('Flame')


# def informacoes(nome, idade):
#     print(f'Seu nome é {nome} e você tem {idade} anos.')
# informacoes('Flame', 14)




# Dicionários
# Dicionários são usados para armazenar pares de chave-valor.
# Os dicionários são odernados, mutáveis e não permitem itens duplicados
carros = {
    'VANS Mustang ESPT': 150000,
    'Civic HONDA GTR6': 54980,
    'SHELL Mac 54': 34560
}

print(len(carros)) # 3


# Alterar seus valores
frutas = {
    'Banana': 5.65,
    'Maçã': 2.56,
    'Manga': 2.99,
    'Uva': 0.99
}

frutas['Banana'] = 5.99 
print(frutas)

# Atualizar um item
frutas.update({'Uva': 0.59})
print(frutas)

# Remover um item
frutas.pop('Manga')
print(frutas)

# Remover o último item
frutas.popitem()
print(frutas)

# Deletando um item
del frutas['Banana']
print(frutas)


# chaves, valores e itens
frutas = {
    'Banana': 5.65,
    'Maçã': 2.56,
    'Manga': 2.99,
    'Laranja': 1.59,
    'Limão': 0.99
}

chaves = frutas.keys()
valores = frutas.values()
itens = frutas.items()
print(chaves)
print(valores)
print(itens)



# Match
# O Match pode ser usado quando há muitos valores a serem testados
luz = 'vermelho'

match luz:
    case 'vermelho':
        print('O sinal está vermelho')
    case 'verde':
        print('O sinal está verde')
    case 'amarelo':
        print('O sinal está amarelo')
    case _:
        print('Não foi possível verificar')

# Também é possível usar a barra vertical para verificar múltiplos valores
y = 7
match y:
    case 1 | 2 | 3 | 4:
        print('O valor está entre 1 a 4')
    case 5 | 6 | 7 | 8 | 9 | 10:
        print('O valor está entre 5 a 10')
    case _:
        print('Não foi possível encontrar! Erro :(')

    







# while
# Os loops while repetem um bloco de código enquanto uma determinada condição for verdadeira.
i = 1
while i < 10:
    print(i)
    i += 1

# continue: continuam executando o bloco de código, ignorando o loop atual
i = 1
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1

# break: quebra o loop, parando de executar o loop while
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1


# else: executa quando a condição do loop se torna falsa.
gatos = 3
while gatos >= 0:
    print(gatos)
    gatos -= 1
else:
    print('Acabou!')

