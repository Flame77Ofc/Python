# Tuplas são imutáveis, ou seja, não é possível alterar seus valores. Podem incluir diferentes tipos de dados
"tuplas podem ser criadas COM ou SEM PARÊNTESES. Porém, é mais recomendado utilizar PARÊNTESES"
tupla = 1, 2, 3
print(tupla)
print(type(tupla))

tupla = (1, 2, 3)
print(tupla)
print(type(tupla))


# Gera uma tupla onde filtra 100 valores e retorna apenas os pares
tupla = tuple(range(0, 101, 2))
print(tupla)



# Imprime os valores individuais(letras) da palavra 'Python', semelhante a um laço for.
a = tuple('Python')
print(a)



comidas = ('Arroz', 'Feijão', 'Macarrão', 'Churrasco')
print(len(comidas)) # Imprime a quantidade de itens que a tupla possui

print(comidas[1]) # Imprimindo o elemento do índice 1
print(comidas[0:3]) # Imprimindo com fatiamento
"comidas[2] = 'Salada' # Isso dá um erro (Não é possível alterar uma tupla!)"

# Tuplas são iteráveis
compras = ('Tapete', 'Mesa', 'Sofá', 'Televisão')
precos = (135.50, 390.99, 760.59, 3465.99)
for compra, preco in zip(compras, precos):
    print(compra, preco)

# in e not in: verifica se algum VALOR está na TUPLA
vogais = ('a', 'e', 'i', 'o', 'u')
'e' in vogais # 'e' está na tupla vogais? True
'd' in vogais # 'd' está na tupla vogais? False
'r' not in vogais # r não está na tupla vogais? True
'u' not in vogais # u não está na tupla vogais? False