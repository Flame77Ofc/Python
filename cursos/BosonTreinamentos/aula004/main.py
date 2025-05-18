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