# [A função print()]

# Controles de fluxo: Permite que o programa tome decisões e execute diferentes instruções dependendo da sua condição. Normalmente, a execução de um programa é feita de cima para baixo, da esquerda para a direita. Porém as estruturas condicionais permitem que o cumputador possa decidir qual bloco de código executar. Sua condição deve ser verdadeira (True) para poder executar determinado bloco de código. 
# Condicionais simples: possuem apenas uma estrutura condicional e verificam se a condição é verdadeira. Caso a condição seja verdadeira, então será executado o bloco de código daquela condicional. Se a condição for falsa (False), então, nada acontece e o programa segue executando o resto do programa normalmente.

# Estruturas de Condição Simples (Condicionais Simples) If:
# Sintaxe:
# if condição:
    # <bloco de codigo>

# Vamos ver alguns exemplos:
chovendo = True
if chovendo == True:
    print('Está chovendo!')

print('Acabou o programa!')
# Declaramos uma variável, atribuímos o valor dela para verdadeiro (True) e logo em seguida o programa verificou se a variável chovendo era verdadeira, e nesse caso é, então executou o bloco de código "Está chovendo!". Logo após isso imprimiu 'Acabou o programa' para sinalizar.

pets = False # Declarando a variável pets e atribuindo seu valor para False
if pets == True: # O programa verifica ses pets é True, ou seja, se tem pets
    print("Você tem pets!") # Se a condição pets for verdadeira (True) então será executado esse bloco de código

print('Fim do programa') # Uma mensagem de fim do programa para sinalizar o fim
# Nesse caso, o bloco de código nem será executado, pois a condição é falsa (False). Então o programa simplesmente irá ignorar o bloco de código dentro da estrutura condicional e executará apenas o 'Fim do programa'


# Estruturas de condição compostas (Condicionais compostas) If, else:
# Como você já viu anteriormente, as condicionais compostas são muito limitadas e serão poucas vezes executadas, pois testam apenas uma condição. Pensando nisso, existem as condicionais compostas, que permite que o programa escolha entre um bloco de código ou outro. Na estrutura composta, funciona da seguinte forma: 
# O programa primeiramente verifica se a condição do If é verdadeira, e se for, executará o bloco de código que pertence a ele (o bloco de código indentado). Porém, se a condição do if for falsa, o programa automaticamente executará o bloco de código do else, pois é sua única opção.
# Vamos dar um exemplo:

luz = True # Declarando a variável luz para True, que significa que a lampada está acessa
if luz == True: # O programa verificar se luz é True. Nesse caso é.
    print('A luz está acessa') # Então executará este bloco de código
else: # E ignora este bloco de código, porque a condição já foi satisfeita.
    print('A luz está apagada')

# Simplificando: Verifica se a condição do if é verdadeira
# Se for, executará o bloco de código dentro dele (a parte indentada)
# Mas se a condição do if for falsa, automaticamente executará a condição do else. O else é sempre o "Se a condição if for falsa, serei executado".

# Vamos ver mais exemplos, dessa vez usando operadores de comparação:
animais = 5 # Declaramos a variável animais atribuindo seu valor a 5
if animais > 3: # O programa verifica se animais é maior que 5. Nesse caso é, então será executado o bloco de código indentado:
    print('Você não pode entrar com mais de 5 animais aqui!')
else: # O else não será executado pois a condição já foi satisfeita
    print('Pode entrar!')

# Mais um exemplo
altura = 1.59 # Declaramos a variável altura e seu valor é 1.59
if altura > 1.65: # O programa verifica se altura é maior que 1.65, nesse caso não é
    print('Pode entrar na montanha russa') # Esse bloco de código não será executado pois a condição do if é False
else: # Então só resta o programa executar o código do else
    print('Altura insuficiente') # Imprime 'Altura insuficiente', pois altura é menor que 1.65

# Mais um último:
nome = 'Henrique'
if nome == 'Admin':
    print('Bem vindo, Admin!')
else:
    print('Bem vindo, usuário')
# Declaramos uma variável nome e seu valor é Henrique, logo em seguida, o programa verifica se o nome é 'Admin', nesse caso, não é, então será executado o bloco de código do else, e imprimirá 'Bem vindo, usuário'


# Estruturas de condicão encadeada (Condicional Encadeada) If, elif, else: Esse é o estágio fundamental, então se entender isso, entenderá facilmente qualquer outra estrutura condicional. As estruturas compostas como vimos acima, são também um pouco limitadas, pois permite que o programa verifique apenas duas condições (Na verdade apenas uma, pois se a condição if for falsa, automaticamente será executado o else). Mas também existe outra forma de verificar mais condições, na verdade, quantas você quiser! Dê uma olhada rápida neste código e tente entender:
idade = 23
if idade <= 18:
    print('Você é um Jovem')
elif idade <= 60:
    print('Você é um adulto')
else:
    print('Você é um idoso')
# Vamos lá, declaramos a variável idade que recebe um int 23 (23 anos) e logo em seguida verificamos se a idade é menor ou igual a 18. Vamos pensar: 23 é menor ou igual a 18? Não, certo? Então essa condicional já não será executada, vamos para a próxima. Verificamos: A idade (23) é menor ou igual a 60? Opa! A idade é menor que 60, por que 23 não é maior que 60, e sim menor, então esse bloco de código será executado, e imprimirá na tela: Você é um adulto
# O que achou? Fácil? Que tal mais um exemplo um pouco mais difícil?
semaforo = 'vermelho'
if semaforo == 'verde':
    print('Acelerar!')
elif semaforo == 'amarelo':
    print('Esperar!')
elif semaforo == 'vermelho':
    print('Parar!')

# Vamos analisar: Criamos uma variável semaforo e atribuímos o valor dela para 'vermelho'. Logo em seguida, verificamos se o semaforo está verde. O semaforo está verde? Não, né? Então simplesmente pulamos para a próxima condição. No elif, a condição está comparando se o semaforo é 'amarelo'. o semaforo não é amarelo, então pulamos essa condição e não executamos o bloco de código. Na última condição está comparando se o semaforo é 'vermelho', então basta olhar para a variável e... o semaforo é vermelho! Então este bloco de códigos será executado! Uma boa recomendação é sempre utilizar um else, ficando assim:

semaforo = 'vermelho'
if semaforo == 'verde':
    print('Acelerar!')
elif semaforo == 'amarelo':
    print('Esperar!')
elif semaforo == 'vermelho':
    print('Parar!')
else:
    print('Cor desconhecida!')
# O programa verifica as cores do semaforo, e como só existem 3 cores de semáforo, se nenhuma das condições acima forem verdadeiras, só resta executar o else, que é um bloco de código atendendo os erros

















# ESTRUTURAS DE REPETIÇÃO: Os loops
# while: Repetindo códigos
# As vezes você quer executar repetidas vezes um bloco de código, e geralmente faz algo como isso:
print('Hello, World!')
print('Hello, World!')
print('Hello, World!')
print('Hello, World!')
print('Hello, World!')
# Mas o while simplifica tudo isso. O que ele faz é repetir algum bloco de código ENQUANTO (while) sua condição for verdadeira. Lembram muito as estruturas condicionais, não é? Mas a grande diferença é que as estrututas condicionais executam apenas uma vez o bloco de código (a não ser que você coloque um loop dentro dele) se sua condição for verdadeira, e as estruturas de repetição executam repetidas vezes um bloco de códigos. Vamos ver o exemplo mais simples possível:
# Queremos imprimir na tela 5 vezes 'Hello, World!'
# O primeiro passo para a criação de um loop while é seu contador. Pode ser de qualquer nome (defina nomes claros), então vamos utilizar neste exemplo uma variável contador, e atribuir o seu valor para 1, apenas isso:
contador = 1
# Em seguida, adicionamos a palavra-chave while, seguida de sua condição. Como queremos executar 5 vezes, colocamos essa condição:
while contador <= 5: # Enquanto a variável contador for menor ou igual a 5, então vamos executar repetidas vezes o bloco de código:
    print('Hello, World!') # Vamos imprimir o bloco de código 'Hello, World'
    contador = contador + 1 # E por fim, vamos incremetar +1 a variavel contador, pra ela não entrar em um loop infinito (jajá falamos disso)
# Recapitulando: O código acima executa 5 vezes o bloco de código 'Helllo, World!'. Lembrando que a cada repetição, a variável contador aumenta em 1.

# O que são loops infinitos?
# É quando você acidentalmente esquece de incrementar ou decrementar a variável contadora responsável pela quantidade de execuções de um bloco. Exemplo:
# contador = 1
# while contador < 10:
#     print('Contando!')
# O código a seguir é um exemplo de loop infinito. Vamos descobrir o porque. Primeiramente declaramos a variável contador e atribuí-mos a ela o valor 1 normalmente, tudo certo. Criamos um loop while que verifica se o contador é menor que 10, se for menor que 10, continua executando, até chegar a um momento em que a condição se torna falsa. Nós imprimos 'Contando!', mas o único detalhe é que esquecemos de incrementar + 1 dentro de seu bloco de código, por isso o loop ficará executando eternamente. Isso consome muita memória RAM e Bateria, então quando acidentalmente entrar em um loop infinito, feche o programa o mais rápido possível. Então a correção deste loop infinito seria esse:
contador = 1
while contador < 10:
    print('Contando!')
    contador = contador + 1 # Evitando que o loop seja infinito
# Agora sim, adicionamos o incrementador! Não se esqueça disso!

# Voltando ao loop while, vamos falar mais sobre ele. Vamos criar um programa que repete 5 vezes o código 'Contagem: 1, 2, 3, 4, 5...'
# Primeiramente, criamos a variavel contadora
contador = 1
# Colocamos a condição e verificamos se contador é menor ou igual a 5. Enquanto isso for True, executamos o bloco de código
while contador <= 5: # Lembrete: Se você tem uma variável 1 que vá até 5 ou 10/15/20, utilizw o operador "<="
    print(f'Contagem: {contador}') # Irá exibir sempre a contagem e o número que o contador está, já que a cada repetição o contador muda de valor
    contador = contador + 1 # Incrementando +1 para evitar o loop inifinito
# E prontinho, o código executará direitinho!

# Vamos ver mais exemplos
# Agora um exemplo de programa que começa o contador em 5 e o contador termina em 1:
# Declaramos a variável contadora
contador = 5 # Agora começa em 5
while contador >= 1: # Enquanto contador for maior que 1:
    print(f'Contagem: {contador}') # Imprime na tela o atual valor da contagem
    contador = contador - 1 # Agora estamos decrementando, subtraindo -1, por que a variável deve ser em algum momento menor que 1.


# Quebrando e continuando com o break e o continue
# Há algumas situações que você precisará parar de executar um bloco de repetiçaõ while mesmo que  condição ainda não seja satisfeita. É possível fazer isso utilizando a palavra-chave break. Vamos supor que quer repetir os números de 1 a 10, mas quando o número ser 7, o loop while simplesmente parasse? É totalmente possível fazer isso utilizando o break! Vamos ver como isso funciona
# Exemplo de programa que executa os números de 1 a 10, mas quando chega no 7, para a execução do loop
contador = 1
while contador <= 10:
    print(contador)
    if contador == 7:
        break
    contador = contador + 1
# Vamos entender este código. Criamos a variável contadora como sempre, declaramos o loop while e sua condição, logo em seguida, imprimimos o valor da variável contador e surge uma estrutura condicional: avalia se a variável contadora é igual a 7. Se for, a função break quebrará o loop e não será mais executado. E por último incrementa +1 para evitar o loop infinito.

# Quando o programa executar o comando continue, a execução do programa retornará novamente ao início do loop e a condição e será verificada novamente. Vamos supor que você queira imprimir os números de 1 a 5, porém deseja pular o número 4. Vamos ao exemplo: 
contador = 1
while contador <= 5:
    if contador == 4:
        contador = contador + 1
        continue
    print(contador)
    contador = contador + 1
# Vamos entender o código: Declaramos a variável contador, e enquanto o contador for menor ou igual a 5, verifica se contador é igual a 4, se for, adiciona +1 no contador e ignora o resto do código abaixo do continue. Se a condição for falsa, imprimimos o conntador e adicionamos +1 na variável.


# Tópicos Avançados
# Substiuição de 'contador' por 'i'
# Os desenvolvedores utilizam a variável i em vez de contador. Parece um pouco contraintuitivo, pois as variáveis devem ser claras e significativas. Porém a comunidade adotou a forma de substituir contador por i. Vamos ver como ficaria num exemplo:
i = 5
while i >= 1:
    print(i)
    i = i - 1

# Utilizando operadores de atribuição
# O while possui bastante código, ou seja, é relativamente grande o espaço de linhas necessário para fazer repetições. Há uma forma de diminuir essa 'verbosidade' toda. Vamos utilizar o operador de atribuição para diminuir um pouco isso:
i = 1
while i < 5:
    print(i)
    i += 1 # Operador de atribuição
# A diferença aqui é que utilizamos o sinal 'i += 1'. Isso é a mesma coisa do que dizer 'i = i + 1'. Veja mais um exemplo:
i = 1
while i < 5:
    print(i)
    i += 1 # é a mesma coisa do que 'i = i + 1'