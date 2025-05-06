# O operador Ternário: É uma simplificação do If...else.
"sintaxe: TrueValue if Expression else FalseValue"
# Se a expressão for verdadeira, retornará TrueValue, caso contrário, retornará FalseValue.
x = "Olá" if True else 'Mundo'
print(x) # Olá

x = "Olá" if False else 'Mundo'
print(x) # Mundo

# Operadores Aritméticos: São os operadores básicos da matemática
x = y = 10
adicao = x + y # 20
subtracao = x - y # 0
multiplicacao = x * y # 100
divisao = x / y # float(1.0)
divisao = x // y # int(1)
exponenciacao = x**y # 10000000000
modulo = x % y # retorna o resto da divisão(0)

# Operadores de comparação: Comparam valores e retornam um valor Booleano(True ou False)
a, b = 12, 5
a > b # A é maior que B: True
a < b # A é menor que B: False
a >= b # A é maior ou igual a B: True
a <= b # A é menor ou igual a B: False
a == b # A é igual a B: False
a != b # A é diferente de B: True

# Operadores lógicos: Comparam conjuntos de valores e retornam um valor Booleano(True ou False)
# and: Retorna True se os dois valores forem True, se ao menos um for False, retornará False.
10 > 5 and 8 >= 9 # False
8 == 8 and 100 != 15 # True

# or: Retorna True se ao menos um valor for True, retorna False se ambos os valores forem False.
5 > 12 or 10 != 5 # True
5 == 2 or 9 > 10 # False

# not: Inverte um valor True para False e vice-versa.
not True # False
not False # True



# Operadores de Atribuição: Alteram o valor original de uma variável, diferentemente de apenas realizar uma operação.
a = 5
a += 1 # a = 5 + 1(6)
a -= 3 # a = 5 - 3(2)
a *= 2 # a = 5 * 2(10)
a /= 1 # a = 5 / 1(5.0)


# Operadores de Associação: Analisam se determinado valor está em outro valor e retornam um valor Booleano(True ou False)
string = "Olá, Mundo"
"Olá" in string # "Olá" está na variável string: True
"World" not in string # "World" não está na variável string: True



# Ordem de precedência: Altera a ordem que é realizado uma operação.
10 + 6 / 2 # 13, pois realiza primeiro a divisão e depois a soma.
(10 + 6) / 2 # 8, pois realiza primeiro o que está dentro dos parênteses e em seguida a divisão.

