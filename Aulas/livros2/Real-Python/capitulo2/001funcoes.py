# Funções: São blocos de códigos que são gerenciáveis e tem uma alta facilidade de reúso
# def nome_da_funcao(argumentos(opcional)):
#     <bloco de codigo>
#     <bloco de codigo>
#     <bloco de codigo>



# Funções: São blocos de códigos que permite a reutilização de bloco de códigos. São extremamente importantes para evitar a repetição de códigos que já foram utilizados anteriormente
# Sintaxe básica
# def nome_da_funcao(argumentos opcionais): # 
#     <bloco de codigos>
# nome_da_funcao(argumentos opcionais)

# As funções possuem 3 partes principais:
# - Nome da função: É o que identificará a função
# - Argumentos: São as variáveis da função que serão retornadas e são opcionais.
# - Chamda da função: É a saída da função. Quando é chamada uma função, executará o que estiver dentro da função

# Vamos esclarecer melhor isso:
def prazer(): # Utiliza-se a palavra-chave def, seguido do nome da função e parênteses.
    print('Olá, Mundo!') # É imprimido 'Olá, Mundo' na tela, mas só será executado quando a função é chamada.
prazer() # Para chamar a função, basta escrever o nome da função seguida por parênteses

# Funções que não possuem argumentos são chamadas de funções sem argumentos
def oi():
    print("Oi! prazer em te conhecer!")
oi()

def clima():
    print("O clima está chuvoso")
# Podemos executar essa função quantas vezes quisermos, basta chamá-las quantas vezes precisar
clima()
clima()
clima()


def restaurante():
    print("O garçom está a caminho")
    print("O garçom chegou")
    print("Comemos a pizza")
restaurante()


# Já funções que possuem argumentos são chamadas de funções com argumentos
def prazer(nome): # O argumento da função é nome
    print(f'Oi, {nome}!') # Imprimindo 'Oi, [e o nome da pessoa]'
prazer('Gustavo') # Na chamada da função é colocado o nome da pessoa
# saída: Oi, Gustavo