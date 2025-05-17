# FUNÇÕES
# Imagine que você tenha diversos blocos de códigos repetidos ao longo do programa. Isso é muito ruim pois utiliza diversas linhas de código atoa, mas por outro lado é uma bela oportunidade para as funções entrarem no caminho. Funções basicamente são blocos de códigos que são gerenciáveis e tem uma alta facilidade de reúso, evitando a repetição de códigos. Vamos ver como isso funciona:
# Sintaxe básica
# def nome_da_funcao(argumentos/parâmetros opcionais):
#     <bloco de codigos>
# nome_da_funcao(argumentos/parâmetros opcionais)
# Lembrete: Argumentos e parâmetros são usados para se referirem a mesma coisa.


# As funções possuem 3 partes principais:
# - Nome da função: É o que identificará a função
# - Argumentos: São as variáveis da função que serão retornadas e são opcionais.
# - Chamada da função: É a saída da função. Quando é chamada uma função, executará o que estiver dentro da função, ou seja, o bloco de código dentro dela.

# Vamos esclarecer melhor isso:
# Primeiro utilizamos a palavra-chave def, seguido do nome que você quiser atribuir a função e por fim utiliza-se parênteses e os dois pontos (:). Em seguida, dentro do bloco de código indentado que pertence a função, é colocado o que você quiser para quando executar a função, exibir o que está lá dentro. Por fim, fora do bloco de comando da função, é chamada a função, com o nome da função e os parênteses.
def prazer(): # Utiliza-se a palavra-chave def, seguido do nome da função e parênteses.
    print('Olá, Mundo!') # É imprimido 'Olá, Mundo' na tela, mas só será executado quando a função é chamada.
prazer() # Para chamar a função, basta escrever o nome da função seguida por parênteses.
# saída: Olá, Mundo!

# Podemos executar essa função quantas vezes quisermos, basta chamá-las quantas vezes precisar. Cada chamada de função executará o bloco de comando dentro da função.
prazer() # saída: Olá, Mundo!
prazer() # saída: Olá, Mundo!
prazer() # saída: Olá, Mundo!



# Existem dois tipos de funções: as funções sem argumentos/parâmetros (as que não possuem nada dentro dos parênteses) e as funções com argumentos/parâmetros (que possuem uma variável dentro dos seus parênteses)
# Vamos ver novamente uma função sem argumentos:
def oi():
    print("Oi! prazer em te conhecer!")
oi() # saída: Oi! prazer em te conhecer!

def clima():
    print("O clima está chuvoso")
clima() # saída: O clima está chuvoso


# As funções podem imprimir quantos blocos de código forem necessários, não tem limites. Apenas coloque o que deseja que seja impresso dentro do bloco de código da função.
def restaurante():
    print("O garçom está a caminho")
    print("O garçom chegou")
    print("Comemos a pizza")
restaurante() # saída:
"""
"O garçom está a caminho"
"O garçom chegou"
"Comemos a pizza"

"""

# Agora vamos ver uma função com argumentos/parâmetros. A única diferença é que ela possui algo dentro dos seus parênteses.
def prazer(nome): # O argumento da função é nome
    print(f'Oi, {nome}!') # Imprimindo 'Oi, {e o nome da pessoa}'
prazer('Gustavo') # Na chamada da função é especificado o nome da pessoa
prazer('Guilherme')
prazer('Nicolas')
# saída: Oi, Gustavo
# saída: Oi, Guilherme
# saída: Oi, Nicolas


# Mais um exemplo utilizando funções com argumentos:
def exibe_lugar(lugar):
    print(f'Você está em {lugar}')
exibe_lugar('Casa do Tio Bento')
# Primeiramente criamos o nome da função, seu nome é 'exibe_lugar' e tem como parâmetro a variável 'lugar'. Em seguida o bloco de código imprime 'Você está em {e o nome do lugar}'. Chamamos a função e colocamos o parâmetro para 'Casa do Tio Bento'. Então após executar o programa, retornará: 'Você está em Casa Do Tio Bento'


# Mais um exemplo:
def imprime_dobro(lista):
    for elemento in lista:
        print(elemento * 2)
lista = [6, 7, 12, 4, 8]
imprime_dobro(lista)

# Esse código já é um pouco mais complexo, mas vamos entender: Criamos uma função e seu nome é imprime_dobro, ela possui um argumento (lista) e dentro de seu bloco de código, é utilizado uma iteração para cada elemento da lista. Esses elementos individuais são multiplicados por 2, e logo após isso criamos uma lista e atribuímos alguns valores a ela. Logo, chamamos a função com o nome da lista e o programa automaticamente duplicará cada elemento. saída:
"""
12
14
24
8
16
"""


# Tópicos Avançados
# Valores padrão
# Imagine que você crie uma função que possui argumentos. Se você de alguma maneira esquecer de responder ao argumento na chamada de função, isso resultará em um erro. Veja um exemplo:
def informacoes(nome, idade):
    print(f"Seu nome é {nome} e você tem {idade} anos")
# informacoes() # Isso resultaria em um erro pois não foi preenchido aos argumentos da função.
informacoes('Lucas', 25) # Isso executaria o programa normalmente pois você preencheu o argumento que a função pedia.

# Sabendo disso, é possível criar argumentos pre-preenchidos para evitar erros. Vamos entender isso:
def informacoes(nome='usuario', idade=0):
    print(f"Seu nome é {nome} e você tem {idade} anos")
# Ok, vamos entender. Repare nos argumentos da função, dentro dos parênteses. Percebeu que já possui argumentos pre-definidos? nome está pre-definido como 'usuario' e idade está pre-definida como '0'. Então se você de repente esquecer de preencher aos argumentos na chamada da função, por padrão aqueles argumentos pre-definidos serão exibidos, veja só:
informacoes() # Seu nome é usuario e você tem 0 anos
# Mas também ainda é possível preencher seus próprios argumentos:
informacoes('Jorge', 19) # Seu nome é Jorge e você tem 19 anos

# vamos ver mais algum exemplo:
def info(continente='América do Norte', pais='Estados Unidos'):
    print(f'Você está na {continente} em {pais}')
info() # Você está na América do Norte em Estados Unidos^
info('América do Sul', 'Brasil')


# Tópicos avançados
# Return
# Como vimos, os blocos de código podem ter qualquer coisa dentro do seu bloco de código, porém utilizamos apenas os comandos print(). Mas existe um comando específico apenas para funções, o return. Pelo seu próprio nome, ele retorna algo. Quando usamos a função print, estamos apenas imprimindo na tela nossa mensagem. Porém a função return retorna um argumento ou qualquer outra coisa que desejar. Vamos ver com um exemplo simples:
def mensagem(nome):
    texto = f'Seu nome é {nome}'
    return texto
# Para chamar uma função com o return, devemos utilizar o print agora.
print(mensagem('João')) # Seu nome é João

# E é apenas isso. Apesar de ser simples, é recomendável que toda função retorne algo. Elas podem retornar textos também, não apenas argumentos. Veja o exemplo a seguir:
def retorna_texto():
    return 'Um exemplo de texto'
print(retorna_texto()) # Um exemplo de texto







# ARGS E KWARS [Já feito]