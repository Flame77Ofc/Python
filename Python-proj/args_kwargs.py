# Args e Kwargs
# Bom, evoluindo mais em questões sobre as funções, vamos ver sobre args e kwargs. Isso é mais fácil do que muitos pensam, vamos ver como isso funciona
# *args
# Permite que uma função receba múltiplos argumentos, muito útil quando não se sabe a quantidade de argumentos que será necessário. Vamos voltar um pouco nas funções normais que recebem um argumento:
def imprime_nome(nome):
    print(f'Seu nome é {nome}')
imprime_nome('Lucas') # saída: Seu nome é Lucas
# Como vimos acima, a função recebeu um argumento, e quando chamamos a função, especificamos o valor do argumento, que era Lucas. Mas imagine só se houvesse uma função que recebe uma fila. Como você sabe, uma fila não tem um número exato de pessoas, pode ser uma fila de 3 pessoas até uma fila de 50 mil, quem saiba mais! É nesse momento em que entram as args, quando você não sabe quantos argumentos será necessário. Vamos ver um exemplo:
def fila(*nomes):
    print(f'Está agora na fila: {nomes}')
fila('Maria', 'Pedro', 'Lucas', 'Ricardo', 'João', 'Paulo', 'Emanuel') # Está agora na fila: ('Maria', 'Pedro', 'Lucas', 'Ricardo', 'João', 'Paulo', 'Emanuel')
# !Lembre-se de que os args sempre retornam uma tupla
# Vamos entender o código. Criamos uma função nomeada de fila. Essa função tem o argumento de nomes, e note que há um asterisco neste argumento, indicando que é uma arg. No bloco de código da função é exibida a mensagem 'Está agora na fila {nome da pessoa}' e note que dentro das chaves não é colocado '*nomes' com asterisco, apenas nomes. Na chamada da função, usamos o nome da função e dentro dos parênteses declaramos 7 nomes de pessoas que estão na fila, ou seja, os agrs permitem que você especifique quantos argumentos desejar, diferentemente da função normal que segue um limite de argumentos, nada mais e nada menos que aqueles argumentos que precisam ser especificados.
# Vamos ver mais um exemplo:

def linguas(*idiomas):
    print(f'Você sabe falar {idiomas}')
linguas('Inglês', 'Espanhol', 'Coreano')
# A regra segue a mesma aqui, declaramos a função linguas que recebe como argumento args de idiomas, imprimindo 'Você sabe falar {e as linguas}', seguida da chamada da função, que declaramos 3 argumentos: Inglês, Espanhol e Coreano. Então a saída desta função será:
# Você sabe falar ('Inglês', 'Espanhol', 'Coreano')
# Entendeu bem as *args? Então vamos para as **kwargs!



# As kwargs são muito parecidas com as *args, porém a única diferença é que as kwargs possuem dois asteriscos e seus argumentos na chamada de função são diferentes. Vamos ver a um exemplo:
def loja(**produtos):
    print(f'A loja possui {produtos}')
loja(iphone = 3400, tablet = 2100, tv = 4500)
# Você conseguiu notar alguma coisa diferente, comparando com as args? Vamos lá, a primeira coisa foram os dois asteriscos no argumento produtos, indicando que isso é uma kwarg. Na chamada de função, as coisas são um pouco diferentes. Você deve especificar a chave e o valor daquele argumento que está criando. Nesse caso, a nossa chave é o nome do produto, e o valor dessa chave é o valor do produto. iphone = 3400 indica que a chave é 'iphone' e '3400' é o valor. Isso te lembra algo?... Chave... Valor...? As args retornam uma tupla, e as kwargs retornam um dicionário!
# Vamos ver mais um exemplo:


def informacoes(**dados):
    print(dados)
informacoes(Lucas = 12, Pedro = 56,  Maria = 35,  João = 16)
# Agora criamos um dicionário, onde o primeiro argumento é o nome da pessoa seguido da idade dela.