string = 'Olá, Mundo!'

# Concatenação de Strings
print("o conteudo da minha string é", string)
print(f"Uma pessoa disse {string}")
print('concatenando minha string cujo seu conteudo é ' + string)

# Funções com strings
string = 'Olá, Mundo!'
print(string.upper()) # O texto fica todo em maiúsculo
print(string.lower()) # O texto fica todo em minúsculo
print(string.capitalize()) # A primeira letra se transforma em maúsculo
print(string.isupper()) # Retorna um valor booleano
string = '  Olá, Mundo!'
print(string.strip()) # Remove os espaços antes e depois da string.
string = 'Olá, Mundo!'
print(string.replace(', ', '-')) # Substitui detereminada parte da string por outra.
print(len(string)) # Diz quantos caracteres tem a string.
# Fatiação de String
print(string[2]) # Retorna a 3a letra da string.
print(string[0: 7]) # Retorna um pedaço da string
# Índice
print(string.index('M')) # Retorna o indíce da letra especificada
print('Olá' in string) # Retorna um booleano dizendo se a palavra "Olá" existe na variável string


print("""Linha 1,
Linha 2,
Linha 3.""")

print('linha 1,\nlinha 2,\nlinha 3.')

# Imprimindo aspas
print('Olha as minhas \"aspas!\" ')
print('"Hello, World!"')