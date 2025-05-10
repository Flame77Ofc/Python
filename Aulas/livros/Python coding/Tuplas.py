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