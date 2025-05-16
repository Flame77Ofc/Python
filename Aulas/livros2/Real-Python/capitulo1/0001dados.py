# Variáveis: As variáveis são indispensáveis num programa. Em todo e qualquer programa o programador deve utilizar as variáveis.
# Sintaxe de uma variável



# Tipos de dados: Existem 4 tipos de dados essenciais na programação:
# 1. str - string ou caractere: São textos delimitados por aspas simples ou duplas. Qualquer coisa delimitada por aspas são strings.
string = 'Olá, Mundo!'
nome = 'João'
texto = 'meu texto'

# 2. int - integer ou inteiros: São números que não apresentam casas decimais, ou seja, números após a vírgula
numero = 1
ursos = 7
pontos = 560

# 3. float - float ou decimais: São números que possuem casas decimais, números após a vírgula
quilometros = 12500.450
area = 325.12
pi = 3.14

# 4. bool - boolean ou booleanos: Representam o verdadeiro(True) e o falso(False), existindo apenas dois valores: True e False
pet = True # A pessoa tem um pet
lampada = False # A lâmpada está desligada


# Eu não sei qual o tipo, como verificar? Utilizando o type()
variavel = True
print(type(variavel)) # <class 'bool'> --> significa que é um tipo booleano, que é True

numero = 34
print(type(numero))