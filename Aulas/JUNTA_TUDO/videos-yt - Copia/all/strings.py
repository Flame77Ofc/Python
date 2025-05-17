# Strings
def split_e_iteracao(): #split: cria uma lista de strings individuais onde cada palavra é separada.
    frase = 'Vamos aprender python'
    palavras = frase.split()
    print(palavras)

    for palavra in palavras: # Exibe cada PALAVRA da lista
        pass

    for letra in frase: # Exibe cada LETRA da lista
        pass

def fatiacao():
    frase = 'Vamos aprender python'
    print(frase[2:11])

def email():
    email = input('Digite o seu email ')
    print(email.find("@"))

def funcao_in():
    produtos = 'celular e notebook'
    print("celular" in produtos)

def upper_lower_capitalize_title():
    print('upper, lower, capitalize e title')
    objeto = 'Bola, BALÃO e chinelo'
    print('padrão:', objeto)
    print(objeto.upper()) # Maiúsculo
    print(objeto.lower()) # Minúsculo
    print(objeto.capitalize()) # Primeira letra maiúscula
    print(objeto.title()) # Todas as letras iniciais maiúsculas

def replace(): # replace: substitui tal palavra por outra.
    brinquedo = 'Carrinho'
    print(brinquedo.replace('Carrinho', 'Caminhão e Boneca'))

def strip(): # strip: elimina espaços antes e depois da string
    frase = '   Meu nome é   Flame'
    print(frase.strip())

def rjust_ljust_center():
    # print(variavel.center/ljust/rjust(num. espaços, preechimento-opcional))
    fruta = 'Abacaxi'
    print(fruta.ljust(15))
    print(fruta.center(25, "-"))
    print(fruta.ljust(23))

def doc_string():
    texto = """ Isso é uma doc string!
É tipo um mega comentário!
Porém... Não é recomendado utilizar docstrings como comentários. """
    print(texto)






message = 'Hello, World!'
print(message)  # Exibe a mensagem inicial

doc_string = """This is a
doc string
and allow you
to write in 
many lines"""
print(doc_string)  # Exibe uma string de múltiplas linhas

# Calcula e exibe o número de caracteres em uma string
name = 'Gabriel'
print(len(name))  # Mostra o comprimento da string 'name'

message = 'I love learn python!'
print(len(message))  # Mostra o comprimento da string 'message'

# Indexação: acessa caracteres ou trechos de uma string por seus índices
print(name[0])  # Exibe o primeiro caractere de 'name'
print(name[0:4])  # Exibe os caracteres do índice 0 ao 3
print(message[3:11])  # Exibe a substring do índice 3 ao 10
print(message[:6])  # Exibe os primeiros 6 caracteres
print(message[8:])  # Exibe a partir do índice 8 até o final

# Manipulação de letras maiúsculas e minúsculas
gift = 'toy car'
print(gift.upper())  # Converte toda a string para maiúsculas
print(gift.lower())  # Converte toda a string para minúsculas
print(gift.capitalize())  # Capitaliza apenas a primeira letra
print(gift.title())  # Capitaliza a primeira letra de cada palavra

# Conta ocorrências de um caractere ou substring
print(gift.count('y'))  # Conta quantas vezes 'y' aparece em 'gift'

# Localiza a posição (índice) de um caractere ou substring
print(gift.find('r'))  # Retorna o índice da primeira ocorrência de 'r'

# replace: substitui uma letra ou palavra por outra
gift = 'toy'
print(gift.replace('toy', 'bus'))

# concatenação de variáveis
greeting = 'Hello'
name = 'Flame'
message = greeting + ' ' + name
print(f"{greeting}, {name}! How are you?")



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