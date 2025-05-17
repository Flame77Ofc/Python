# Tuplas: As tuplas são imutáveis, ou seja, seus elementos não podem ser alterados nem modificados implicitamente (utilizando funções ou métodos para alterar os seus elementos). Um dos motivos para se usar as tuplas é que elas são muito boas quando você não quer alterar os seus elementos. As tuplas, diferentemente das listas, possuem parênteses, e é apenas isso que diferencia uma tupla de uma lista. Mas as tuplas também podem ser escritas sem os parênteses! O python reconhece que quando uma variável possui diversos valores separados por vírgulas, sabe que é uma tupla. Vamos ver um exemplo:
# Uma tupla com os parênteses
tupla = ('elemento1', 'elemento2', 'elemento3')
print(tupla)

# Uma tupla sem os parênteses
tupla = 'elemento1', 'elemento2', 'elemento3'
print(tupla)
# Vamos nos aprofundar mais nas tuplas e ver mais exemplos:
# Criando uma tupla
tupla = (1, 2, 3, 4, 5)
print(tupla) # Imprimindo a tupla

# tentando alterar o seu valor
# tupla[2] = 6 # Erro

# Vamos acessar os valores de uma tupla pelo seu índice, funcionam como listas
cores = ('Azul', 'Branco', 'Verde', 'Preto', 'Laranja')
print(cores[1])
print(cores[-2])
print(cores[1:4])

# Unindo tuplas: Agora vamos supor que você tenha duas tuplas e quer junta-lás, mas não sabe como. É possível fazer isso simplesmente utilizando o sinal de adição (+), como se fosse uma expressão matemática. Isso não fará a soma dos elementos da tupla:
tupla1 = (250, 120)
tupla2 = (-35, 90)
tupla = tupla1 + tupla2 # 250, 120, -35, 90
print(tupla) 

# Sobre as tuplas há bem pouco do que falar, elas são quase iguais as listas, mas seus elementos não podem ser alterados implicitamente, isto é, com funções e métodos.