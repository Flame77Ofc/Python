# Tópicos avançados

# Debugação de código
# Para debugar um código, digitamos Alt + Fn + F5
# Em seguida, no prorama, colocamos os breakpoints. Os breakpoints são os locais aonde você quer debugar
# Em seguida, clicamos em Executar e Depurar, e é executado o código.

for i in range(10):
    print(i)


# Operador Ternário
# O operador ternário em python é semelhante as condições if e else
# A grande diferença é sua sintaxe simples e de baixa 
# Sintaxe básica:
# 'condição verdadeira' if condicao == True else 'condição falsa'
porta = True # por aberta
print('porta aberta' if porta else 'porta fechada')



# Enumerate
# Enumerate serve para enumerar uma lista com seus elementos e índices.
# É um contador automático, que pode ser visto como os índices de uma lista ou string.
string = 'Python'
for indice, letra in enumerate(string):
    print(indice, letra)
"""
0 P
1 y
2 t
3 h
4 o
5 n
"""

lista = ['Cachorro', 'Gato', 'Galinha', 'Rinoceronte', 'Macaco', 'Girafa', 'Abelha', 'Crocodilo']
for indice, elemento in enumerate(lista):
    print(indice, elemento)

"""
0 Cachorro
1 Gato
2 Galinha
3 Rinoceronte
4 Macaco
5 Girafa
6 Abelha
7 Crocodilo
"""



# List comprehensions
# Compreensões de lista oferecem uma maneira curta e simples de criar listas. Consiste de colchetes contendo uma expressão seguida por uma cláusula for. Pode ser muito útil para criar listas rapidamente.
# A seguir veremos uma list comprehension e uma lista com um for normalmente.
pares = [x for x in range(0, 51) if x % 2 == 0]
print(pares)

lista = list(range(0, 51))
pares = []
for x in lista:
    if x % 2 == 0:
        pares.append(x)
print(pares)




# Lambdas
# Lambdas, também conhecidas como funções anônimas, são funções comuns, mas simplificam tudo o que uma função normal faz em uma linha de código.
def add(x, y):
    return x + y
print(add(5, 12)) # 17

add = lambda x, y: x + y
print(add(6, 8)) # 14





