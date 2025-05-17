# Tuplas: São mutáveis, ou seja, não podem ser modificadas. Não precisa necessariamente possuir parênteses
tupla = (1, 2, 3, 4, 5)
print(tupla)

"tupla[3] = 8" # erro

# Tuplas: Seus elementos não podem ser trocados nem modificados.
x = 120
y = -98
coordenadas = (x, y)
print(coordenadas)
"coordenadas[1] = 15 # erro: tentativa de modificação"

# Unindo/Juntando tuplas
tupla1 = (250, 120)
tupla2 = (-35, 90)
tupla = tupla1 + tupla2 # 250, 120, -35, 90
print(tupla) 


teste = (1,2,3)
print(teste[1] + teste[2]) # 5

# Unpacking: Cada variável tem um valor da tupla
Tupla = (1234, 5678, 'Oi!')
x,y,z = Tupla
print(x)
print(y)
print(z)


# Tuplas são imutáveis: Não é possível alterar seus elementos
cores = ('Azul', 'Branco', 'Verde', 'Preto', 'Laranja')
# Acessando o seu índice
print(cores[1])
print(cores[-2])
print(cores[1:4])
# cores[2] = 'Amarelo' ERRO, NÃO É POSSÍVEL MODIFICAR ELEMENTOS!

# Juntando tuplas com o operador +
tupla1 = 'elemento1', 'elemento2' # tuplas podem ser escritas sem aspas!
tupla2 = 'elemento3', 'elemento4'
juntando_tupla = tupla1 + tupla2
print(juntando_tupla)

# Multiplicando tuplas com o operador * (Não é feita a multiplicação, mas sim uma repetição)
coral = 'hello', 'world'
mult = coral * 2
print(mult) # ('hello', 'world', 'hello', 'world')


# Funções com tuplas
tupla = 'Olá,', 'Mundo!'
len(tupla)

tupla = 1, 2, 3
max(tupla)
min(tupla)