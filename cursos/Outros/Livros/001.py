# Comentários
# Comentários são partes onde o código que você inserir não será executado.

""" Os comentários
também podem ser
de múltiplas linhas
utilizando 3 aspas 
sendo elas aspas
simples ou duplas

"""


# Variáveis
# Variáveis são conteiners que armazenam um valor
nome = 'Pedro'

x = 5
y = 12

print(x + y)

# É possível atribuir variáveis com diversos valores em apenas uma linha de código.
# atribuição normal
animal = 'Gato'
cor = 'Azul'
professor = 'Guanabara'

# atriibuição múltipla de valores (em apenas uma linha)
animal, cor, professor = 'Gato', 'Azul', 'Guanabara'
print(animal, cor, professor) # Gato Azul Guanabara


# É possível também criar múltiplas variáveis para apenas um valor.
# Criação comum de variáveis
cor = 'Laranja'
fruta = 'Laranja'
print(cor, fruta) # Laranja Laranja
# Criamos a variável cor com o valor de 'Laranja' e  Criamos a variável fruta com o valor de 'Laranja'.

# Criação de múltiplas variáveis com apenas um valor
cor = fruta = 'Laranja'
print(cor, fruta) # Laranja Laranja
# Criamos a variável cor atribuímos seu valor para a variável fruta e a variável fruta recebe o valor de 'Laranja'. Ou seja, ambas as variáveis cor e fruta possuem o mesmo valor 'Laranja'.





# ------------Livro 2---------------
# Variáveis, expressões e instruções
# Uma variável armazena um valor e esse conjunto é guardado na memória do computador
mensagem = 'Curso de Python'
x = 12
nome = 'Flame'

# Expressões e instruções
# Uma expressão é uma combinação de valores, variáveis e operadores. Um valor por si mesmo é considerado uma expressão, assim como uma variável, portanto as expressões seguintes são todas legais:
42
n = 17
n
n + 34


# Ordem das operações
# O parênteses pode alterar a ordem com que o programa executa uma expressão. Vamos ver o exemplo:
2 + 8 * 2 # 18
(2 + 8) * 2 # 20

# Isso porque na primeira linha, foi executado primeiro a multiplicação, e logo em seguida a soma.
# Na segunda linha, como os parênteses são mais importantes, então foi executado primeiro a soma e depois a multiplicação

# Concatenação
str1 = 'Programando'
str2 = 'Python'
print(str1 + ' em ' + str2)





# W3Schools
# Tuplas
# Tuplas são ordenadas, aceitam valores duplicados e imutáveis, ou seja, não é possível alterar seus valores com funções ou métodos
tupla = ('Banana', 'Laranja', 'Abacaxi', 'Melão')
print(tupla)

animais = 'Gato', 'Cachorro', 'Urso', 'Panda' # Tuplas podem ser escritas sem parênteses
quantidade = len(animais)
print(quantidade)


# Sets
# Sets são desordenados, não aceitam valores duplicados e são imutáveis.
IDS = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(5 in IDS)

IDS.add(11)
print(IDS)

IDS.remove(5)
print(IDS)

IDS.clear()
print(IDS)

del IDS


cores = {'Azul', 'Amarelo', 'Vermelho', 'Roxo'}
cores.pop()
print(cores)