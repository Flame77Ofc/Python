# Formatação de Strings
string = 'Olá, Mundo!'

# len: retorna o tamanho, em letras, da string.
print(len(string)) # 11

# capitalize: retorna a primeira letra da string em maiúsculo.
print(string.capitalize())

# count: retorna quantas vezes uma letra ou sequência de palavras aparece na string.
print(string.count('u'))

# startswith: retorna um boolean dizendo se uma string inicia com determinada letra ou sequência
print(string.startswith('O'))

# endswith: retorna um boolean dizendo se uma string termina com determinada letra ou sequência
print(string.endswith('ndo!'))

# isalnum: retorna um boolean dizendo se a string possui conteúdo alfanúmerico (letra ou número)
print(string.isalnum())

# isalpha: Verifica se a string possui apenas conteúdo alfabético
print(string.isalpha())

# islower: Verifica se todas as letras de uma string são minúsculas.
print(string.islower())

# isupper: Verifica se todas as letras de uma string são maiúsculas.
print(string.isupper())

# upper: Retorna uma cópia da string trocando todas as letras para minúsculo.
print(string.upper())

# lower: Retorna uma cópia da string trocando todas as letras para minúsculo.
print(string.lower())

# swapcase: Inverte o conteúdo da string (Minúsculo / Maiúsculo).
print(string.swapcase())

# split: Transforma a string em uma lista, utilizando os espaços como referência.
print(string.split())

# replace(x, y): Substitui na string o trecho x pelo trecho y.
print(string.replace('Olá', 'Oi'))

# strip: Remove todos os espaços em branco da string.
print(string.strip())