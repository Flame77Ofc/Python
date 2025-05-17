"# TERMOS INICIAIS"
# Comentários
# Os comentários em python são partes de códigos onde os comandos não são executados, ou seja, o programa simplesmente ignora os comentários.
# Para fazer um comentário, utiliza-se o hashtag (#), e logo após isso você pode escrever o que quiser que o programa não executará. Importante lembrar que os comentários só funcionam em uma linha. Ou seja, se você quiser colocar mais comentários, a cada linha terá que digitar o hashtag (#). Os comentários são muito úteis para você mesmo explicar o que tal comando faz. Vamos ver alguns exemplos de comentário

# Isso é um comentário
# Isso também é um comentário
# Mas, seu eu utilizar # o hashtag após o texto que que queria, dará um erro. Todos os caracteres devem estar APÓS a hashtag.

# Saída de informações
# Imagine um programa sem saídas, por exemplo, uma calculadora. Imagine que você digita a operação que você quer fazer, como 5 + 4 e a calculadora simplesmente não te responde, em outras palavras, não te dá uma saída. Isso não seria uma calculadora, certo? Não serveria pra nada, pois eu não consegui ver o resultado dessa operação. É exatamente essa a saída que vamos ver, que tal?
# Seu primeiro código: Digite print() e dentro dos parênteses, escreva um texto cercado por aspas (podem ser simples ou duplas), como esse:
print("Olá, Mundo!")
# Isso produzirá uma saída. O interpretador (executador) do python executará esse print e mostrará na tela Olá, Mundo! Legal, né?? No mundo da programação, quando utilizamos o comando print(), dizemos que estamos imprimindo algo. Vamos imprimir mais coisas!
print('Meu nome é Lucas')
print('Eu tenho 17 anos')
# Um lembrete: Sempre que você executar um comando, digite um abaixo do outro, pulando uma linha.
print('Gosto de gatos')

# podemos utilizar o comando print() e ainda pode haver comentários após ele. Vamos ver um exemplo:
print('Exemplo') # Esse comentário não será executado, mas o comando print sim.

# Podemos utilizar um comentário especial chamado 'docstring'. Ele não é bem um comentário, e não é recomendado utilizar ele, porém vamos ver como ele funciona:
"""Uma docstring que
se parece com um comentário
porém não é recomendado
mas pode ser útil"""

'''Outro exemplo
de docstrings com
3 aspas simples'''
# Utiliza-se 3 aspas (simples ou duplas) e coloca o que você quiser ali dentro. É possível imprimir as dosctrings também, veja um exemplo:
print("""Veja um exemplo
de uma docstring""") # saída: Veja um exemplo 
# de uma docstring

# Utiliza-se uma barra invertida (\) para múltiplas linhas, mas só será impresso apenas uma única linha. Veja um exemplo:
print("Utilizando uma \
barra invertida. Isso é \
impresso em apenas uma linha, por \
incrível que pareça") # saída: Utilizando uma barra invertida. Isso é impresso em apenas uma linha, por incrível que pareça

# Lembrete: Não esqueça que print() se escreve tudo em minúsculos. Não é possível digitar algo como Print(), PRINT() ou PrInt(), pois isso é um erro e o programa diferencia as letra minúsculas das maiúsculas.

# [EXERCÍCIOS]

# Agora vamos avançar um pouco e aprender sobre variáveis.
"# VARIÁVEIS"
# As variáveis são usadas para armazernar dados na memória do computador. São muito úteis para utilizar em um caso posterior. Vamos ver alguns exemplos:
nome = 'Maria' # Isso é uma string
idade = 17 # Isso é um número do tipo inteiro.


# Vamos avançar em direção aos TIPOS DE DADOS para entender como criar variáveis claramente
# TIPOS DE DADOS
# Os tipos de dados representam qual o tipo de valor de uma variável. A sintaxe básica de uma variável é a seguinte:
# nome_da_variavel = 'tipo de dado'
# Vamos conhecer os tipos de dados para compreender melhor.

# string ou caractere (str): A string é todo texto delimitado por aspas, sejam elas simples ('') ou duplas (""). Seja lá o que for, desde que esteja entre aspas então é uma string. Vamos ver alguns exemplos:
nome = 'Lucas'
estado = "São Paulo"
continente = 'América'

# int ou inteiros (int): O int é responsável por números inteiros e sem casa decimal (números após a vírgula), sejam eles positivos ou negativos. Exemplos:
idade = 14
pontos = 560
alunos = 35

# float ou flutuantes/decimais (float): Os decimais são todos os números positivos ou negativos que possuem casas decimais (números após a vírgula). Vamos ver:
nota = 8.90
altura = 1.75
peso = 90.65

# booleans ou booleanos (bool): Os booleanos representam o estado de verdadeira ou falso, ligado ou desligado, sim ou não. Existem apenas dois valores booleanos, eles são o True (Que representa o verdadeiro, o ligado, o sim) e o False (Que representa o falso, o desligado, o não) Vamos ver:
lampada = True # Lâmpada está ligada
disjuntor = False # Disjuntor está desligado
filhos = False # Não tem filhos

# "Mas e se eu esquecer?" Ainda é possível verificar o tipo de dado utilizando o comando type(). Vamos ver como isso funciona:
# Vamos supor que você tenha a variável altura e quer saber que tipo de dado ela é:
altura = 1.75
print(type(altura)) # saída: <class 'float'> Isso significa que a variável é do tipo float (flutuante)

copos = 7
print(type(copos)) # saída: <class 'int'>


# RESTRIÇÕES DE CRIAÇÃO DE VARIÁVEIS
# Os nomes das variáveis precisam seguir algumas regras:
# 1. Números, espaços e caracteres especiais
# O nome das variáveis não podem começar com um número, nem espaços e nem caracteres especiais, como (-, @, !, #). O traço (_) é o único caractere especial permitido. Vamos ver alguns exemplos incorretos e corretos
# Exemplos incorretos: 
# a. 2gatos # Inicia com número
# b. nome completo # Contém espaço
# c. numero-de-telefone # Contém o símbolo '-'
# d. @nomedeusuario # Contém @ e é difícil de ler
# Exemplos corretos:  
# a. nome_completo
# b. cidade
# c. nome_de_usuario
# d. numero_de_telefone

# 2. Não é permitido o uso de palavras reservadas
# As palavras reservadas, também conhecidas como keywords são palavras que o próprio python adotou em sua linguagem, então não é possível utiliza-lás como nome de variáveis. Por sorte elas são todas em inglês o que dificulta que você utilize sem querer e não saiba. Veja a seguinte tabela incluindo todas as palavras reservadas:
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield
# # Se assustou? Calma! Você aprenderá todas logo logo, assim evitando o uso delas em nomes de variáveis

# # Cuidado! O python é case sensitive. Isso significa que letras maiúsculas e minúsculas fazem diferença! Exemplos:
# a. a variável 'nome' é diferente da variável 'Nome'
# b. a variável 'Cidade' é diferente da variável 'CIDADE'


# # Dicas e boas práticas
# Uma boa prática na programação signfica que é recomendado fazer tal coisa (porém não é obrigatório). A seguir vou te apresentar algumas boas práticas que você pode seguir:
# 1. Nomes claros: Sempre utilize nomes claros para a criação de variáveis. Veja exemplos:
# a. Se você quer criar uma variável que quer guardar um nome, não use letras aleatórias (como x, y, a, r, t). Utilize simplesmente nome
# b. Não utilize abreviações nem acrônimos para variáveis. Exemplo: numero de telefone -> numdetel

# 2. Não utilize acentuações (~, ^, `): Mesmo que pareça estranho, não crie variáveis con acentuações! Exemplos:
# a. aniversário -> aniversario
# b. média -> media
# c. salário -> salario

# 3. Utilize snake_case: A comunidade python adotou uma forma de substituir os espaços pelo traço "_". O nome desse estilo é snake_case, onde as palavras que precisavam de espaços foram substituidas pelo traço.
# Exemplo de snake_case:
# a. nome completo -> nome_completo
# b. número de telefone -> num_telefone



# Agora que você já sabe os tipos de dados, podemos prosseguir para mais alguns exemplos de variáveis:
nome = 'Maria' # Esse é o tipo de dado string, pois há aspas, lembra?
idade = 14 # Isso é um int (inteiro)

# Ok, criamos variáveis, e aí? É possível imprimir o valor de uma variável pelo seu nome! Vamos ver uns exemplos:
nome = 'Felipe' # Declaramos a variável nome e atribuímos a ela o valor Felipe
print(nome) # Imprimimos o nome, que era Felipe. Então a saída será Felipe

# As strings não são apenas tipos de dedos. É possível fazer inúmeras coisas com as strings, ela possui diversas funções, o que deixa as strings mais poderosas e com mais funcionalidades. Vamos ver o que é possível fazer com elas?

# Indexação: Acessando caracteres ou sequências de strings
# O índice de strings é uma forma de acessar um caractere ou uma sequência de caracteres.
# Os índices podem ser positivos e negativos. Os índices positivos sempre começam do 0, e terminam até a quantidade da string -1. Então se uma string possui 23 caracteres, por exemplo, o seu último índice será 22, o último caractere da string será 22. Já os índices negativos, o primeiro índice é o total de caracteres, porém negativos, e o último caractere sempre será -1. Exemplo: se uma string possui 15 caracteres, é possível acessar o seu primeiro índice com o -15, que representa o primeiro caractere.
nome_do_estabelecimento = 'La Praire'
# ìndices positivos:     012345678
# índices negativos:    -987654321
# Acessando os caracteres: Para acessar os caracteres pelos seus índices, basta utilizar a seguinte sintaxe:
# nome_da_string[índice]
print(nome_do_estabelecimento[4]) # r
print(nome_do_estabelecimento[-8]) # a
# Fatiamento de Strings: Também é possível acessar sequências da string
# Os fatiamento de Strings sempre serão assim:
# string[inicio:fim +1] # fim+1 porque é a sintaxe do python, ou seja, foi definido assim;
# Se você quer ir do índice 1 até o 6, na verdade estaria indo do 1 até o 5. Então incremente mais um, ficando:
# string[1:6+1] Ou simplesmente string[1:7] (Mais recomendável)
nome_do_estabelecimento[1:6] # a Pra
nome_do_estabelecimento[-5:-1] # rair
# Nesse caso, estará acessando a partir do índice da string 4 até o final da string.
# string[indice:(acessará o final da string)]
# nome_do_estabelecimento[4:] # raire
# Nesse caso, estará acessando o começo da string até o 
# string[(começo atééé...):índice]
# print(nome_do_estabelecimento[:6]) # La Pra
# acessando a quantidade de caracteres de uma string com a função len()
string = 'Acessando a quantidade de caracteres dessa String'
print(len(string)) # saída: 49


# MÉTODOS DE STRING
# vamos supor que por algum motivo você tem um nome de uma empresa enorme, e queria alterar todas as suas letras em maiúsculas. É possível fazer isso utilizando a função .upper()
empresa = 'empresa ltca produtora de produtos tecnológicos e inovadores lctd importação da china e estados unidos'
print(empresa.upper()) # saída: EMPRESA LTCA PRODUTORA DE PRODUTOS TECNOLÓGICOS E INOVADORES LCTD IMPORTAÇÃO DA CHINA E ESTADOS UNIDOS


# Agora imagine que você tenha um texto e quer modificar todas as suas letras para minúsculas. Utilizando a função .lower() conseguimos fazer isso:
texto = 'O RATO ROEU A ROUPA DO REI DE ROMA'
print(texto.lower()) # saída: o rato roeu a roupa do rei de roma

# Você tem um estado e quer alterar o primeiro caractere da string para maiúscula. O capitalize() é responsável por isso.
estado = 'mato grosso do sul'
print(estado.capitalize()) # Mato grosso do sul

# Você pede ao usuário seu nome, mas ele pode fornecer esquecendo de colocar as primeiras letras da palavra como maiúsculas. É isso que a função title() faz:
nome = 'joão felipe dos santos'
print(nome.title()) # João Felipe Dos Santos


# Removendo espaços desnecessários de uma string: Utilizando .strip()
string = '  texto        ' # Veja que há diversos espaços desnecessários antes e depois do conteúdo principals
# É possivel remover utilizando a função .strip()
print(string.strip()) # texto


# Verificando se uma string começa ou termina com uma sequência especifica de caracteres: utlizando o startswith e o endswith
# As funções startswith e endswith avalia se alguma parte está presente numa string, retornando um valor booleano (True ou False). Vamos ver alguns exemplos:
comida = 'pizza'
print(comida.endswith('zza')) # Verifica se pizza termina com 'zza'. saída: True

animal = 'leão'
print(animal.startswith('le')) # Verifica se leão começa com 'le'. saída: True

# Encontrar um caractere em uma string: utilizando o .find()
# O find retorna o índice em que o caractere se encontra. Vamos ver um exemplo:
frase = 'Estou aprendendo Python'
print(frase.find('aprendendo')) # saída: 6

# Substituir um caractere ou uma sequência de caracteres antigas por outra nova com a função .replace()
# .replace('caracteres antigos', 'novos caracteres')
string = 'Olá, Mundo'
string = string.replace('Mundo', 'Marte')
print(string) # Olá, Marte

"# Operadores Aritméticos: São os operadores matemáticos básicos que permitem efetuar expressões matemáticas. A partir deles são formadas as expressões. Vamos ver quais são!"
# (+) Adição: Soma dois valores
5 + 6 # 11
3 + 9 # 12

# (-) Subtração: Subtrai o segundo valor do primeiro
4 - 2 # 2
6 - 10 # -4

# (*) Multiplicação: Multiplica dois valores 
6 * 6 # 36
3 * 8 # 24

# (/) Divisão: Divide o primeiro valor pelo segundo, retornando um resultado em ponto flutuante (float)
12 / 3 # 4.0
15 / 2 #  7.5

# (//) Divisão de inteiros: Divide dois números e retorna um valor inteiro
15 // 7 # 2
120 // 10 # 12

# (%) Resto da divisão: Retorna o resto da divisão do primeiro valor pelo segundo
17 % 5 # 2
10 % 3 # 1

# (**) Exponenciação: Eleva o primeiro valor à potência do segundo
2**3 # 8 (2*2 = 4, 4*2 = 8)
5**3 # 125 (5*5 = 25, 25*5 = 125)

# Ordem de precedência
# As expressões possuem uma ordem específica de execução. Por exemplo, multiplicação é mais importante que adição, então multiplicação será sempre executado primeiro do que adição. Porém com a ordem de precedência é possível modificar a ordem de execução de expressões utilizando os parênteses, pois é prioridade. Vamos ver como funciona!
# Imagine que você queira calcular a seguinte expressão:
5 + 6 * 2 # Executa primeira a multiplicação, resultando em 17
(5 + 6) * 2 # Executa o que está dentro dos parênteses, resultando em 22
12 + 3 * 5 # 27
(12 + 3) * 5 # 75



# Operadores de Atribuição
# São usados para atribuir novos valores nas variáveis. Existe uma diferença entre essas duas declarações:
x = 10
x + 5 # Isso é um comando solto que não altera o valor da variável
print(x) # O valor de x ainda será 10, pois 5 não foi incrementado no x.

# Para alterar o valor de x, usamos os operadores de atribuição. Agora vamos ver um exemplo de atribuição de x:
x = 10
x = x + 5 # Isso incrementa ao valor antigo da variável x, alterado seu valor
print(x) # Agora sim o valor de x é 15, pois atribuímos a ela o seu valor antigo + 5
# Veja quais são os operadores de atribuição
# Atribuição Simples (=): Atribui o valor à direita a uma variável à esquerda.

y = 6
x = 12
# Atribuição com adição(+=): Soma o valor à direita ao valor atual da variável e atribui o resultado à variável. 

x = 6
x += 2 # x agora é 8
y = 7
y += 5 # y agora é 12
# Atribuição com subtração(-=):

x = 4
x -= 4 # x agora é 0
y = 5
y -= 1 # y agora é 3
# Atribuição com multiplicação: Multiplica o valor atual da variável pelo valor à direita e atribui o resultado

x = 6
x *= 5 # x agora é 30
y = 9
y *= 5 # y agora é 45
# Atribuição com divisão:  Divide o valor atual da variável pelo valor à direita e atribui o resultado (retorna float)

x = 6
x /= 3 # x agora é 2
y = 20
y /= 5 # y agora é 4
# Atribuição com divisão inteira: Divide o valor atual da variável pelo valor à direita e atribui a parte inteira do resultado. 

x = 10
x //= 2 # x agora é 5
y = 7
y //= 3 # y agora é 2
# Atribuição com módulo: Calcula o resto da divisão do valor atual da variável pelo valor à direita e atribui o resultado.  

x = 15
x %= 5 # x agora é 0
y = 8
y %= 3 # x agora é 2
# Atribuição com exponenciação: Eleva o valor atual da variável à potência do valor à direita e atribui o resultado.  


"# Entrada de dados"
# Entrada de dados é responsável por pedir para o usuário qualquer coisa que se possa imaginar. Desde nome, idade, cidade, cpf, número de telefone entre outros. Vamos ver como perguntar ao usuário o seu nome:
# Utilizando a função input()
# Para pedir algo ao usuário, basta escrever o comando input() e pedir o que quiser dentro dos parênteses. Vamos pedir o nome do usuário:
input('Qual o seu nome? ')
# Ao executar esse programa, é exibido a mensagem que está dentro do input (Qual o seu nome?). O programa espera você digitar algo e quando teclar enter, nada acontecerá. O nome que você digitou é perdido e não poderá ser acessado, pois não guardamos essa informação na memória RAM do computador... É aí que entram as variáveis! Você pode criar uma variável e atribuir o seu valor como um input! Vamos ver um exemplo:
nome = input("Digite o seu nome: ")
# Ao executar o programa, pede para o usuário digitar o seu nome, então você digita, e... ainda não aparece nada, que estranho! Isso acontece pois esquecemos de utilizar o print()! Sempre que você quer mostrar algo, lembre-se do print()! Então o código ficaria assim:
nome = input('Digite o seu nome: ')
print(nome) # saída: o nome que o usuário digitar

# Vamos pedir ao usuário sua idade
idade = input('Digite a sua idade: ')
print(idade)

# Ok, conseguimos imprimir agora a idade do usuário. Mas tem uma pequena coisa errada na variável idade. Como você sabe, o input() pergunta algo ao usuário. Porém essa pergunta é feita e retornada um tipo de dado string, e nós estamos perguntando a idade, ou seja, é do tipo int (inteiro). Quando você responde a variável idade, sempre retornará uma string. Vamos supor que o usuário digitou a idade como 25. Retorna na verdade uma string '25' e não um número inteiro 25. Isso é muito ruim pois não permite realizar cálculos matemáticos. Vamos ver um exemplo
# Pede ao usuário a sua idade e subtrai o ano atual - idade, para descobrir em que ano o usuário nasceu:
"""idade = input('Digite a sua idade: ')
ano = 2025
print(ano - idade) # Subtrai o ano atual - a idade do usuário
"""
# Se o usuário digitasse que sua idade é 10, então ele nasceu em 2015 pelo cálculo. Mas há um grande problema, pois isso resultará em um erro, porque esquecemos de um pequeno detalhe. Como eu disse, o comando input() SEMPRE RETORNARÁ uma string. É aí que está o problema. Quando o programa executa aquele código, o programa se pergunta: "Mas como eu vou subtrair 2025 de um texto?". Não é possível fazer cálculos utilizando um inteiro e uma string. Mas é possível resolver isso utilizando o int() antes do input para indicar que isso precisa retornar um inteiro. Vamos ver como fica:
idade = int(input('Digite a sua idade: '))
ano = 2025
print(ano - idade)
# Agora sim, o programa efetuará o cálculo e retornará o ano em que o usuário nasceu. Então lembre-se de utilizar o int() quando for fazer cálculos envolvendo entradas do usuário com input(). Vamos ver mais um exemplo:
# Pede ao usuário o seu saldo e efetua a adição entre o saldo e a aposentadoria
"""saldo = input('Digite o seu saldo: ')
aposentadoria = 2400
print(saldo + aposentadoria)
"""
# Consegue perceber se tem algum erro neste código? Analise bem!
# Se você consegui que falta o int, parabéns! Vamos ajustar o código novamente:
saldo = int(input('Digite o seu saldo: '))
aposentadoria = 2400
print(saldo + aposentadoria)

# Também é possível utilizar o float, aquele tipo de dado que possui casas decimais, se lembra? Um exemplo que pede ao usuário seu peso:
peso = float(input("Olá, você pesa quantos quilos? "))
print(peso)

# Fazendo uma cálculadora de soma
# Agora vamos fazer um pequeno projetinho de uma calculadora que apenas soma. Será assim:
# pede para o usuário digitar dois números, e o programa retorna a soma entre eles. Vamos ver:
num1 = int(input('Digite o primeiro número: ')) # Pede ao usuário o primeiro número
num2 = int(input('Digite o segundo número: ')) # Pede ao usuário o segundo número
soma = num1 + num2 # Criamos uma variável a atribuímos o seu valor como soma dos dois números, é totalmente possível fazer isso!
print(soma) # Imprime a soma dos dois números

# Imprimindo de um jeito diferente
# Você percebeu que imprimimos as coisas, mas não especificamos o que é aquela mensagem? Exemplo: Você pede ao usuário seu nome, e você só imprime na tela o nome do usuário. Parece um pouco sem graça, então que tal criar mensagens personalizadas para as mensagens que são impressas? Vamos ver como funciona:
# Concatenação
# A concatenação mescla dois valores utilizando o operador de adição (+). Vamos supor que você tenha que pedir o nome do usuário e o seu sobrenome, e no final, você junta tudo e mostra seu nome completo:
nome = input("Digite o seu primeiro nome: ")
sobrenome = input("Digite o seu sobrenome: ")
nome_completo = nome + sobrenome
print(nome_completo)
# Ainda há um pequeno probleminha neste código, pois não há espaço. Vamos apenas adicionar um espaço:
nome = input("Digite o seu primeiro nome: ")
sobrenome = input("Digite o seu sobrenome: ")
nome_completo = nome + ' ' + sobrenome
print(nome_completo)
# Não vou detalhar muito sobre esse código, apenas siga em frente e você entenderá.
# Ok, isso só imprime o nome completo. Mas vamos supor que queremos enviar uma mensagem do tipo "Seu nome completo é: {e nesse espaço aqui mostre o nome que o usuário digitou}". Isso é totalmente possível e muito fácil. Vamos ver como funciona:
nome = input("Digite o seu primeiro nome: ")
sobrenome = input("Digite o seu sobrenome: ")
nome_completo = nome + ' ' + sobrenome
print('Seu nome completo é ' + nome_completo)
# Perfeito! Se o usuário digitar Lucas dos Santos, então a saída será: Seu nome completo é Lucas dos Santos

# Que legal, não é? Mas ainda há um jeito que facilita a concatenção! Essa forma se chama f-string, que consiste em utilizar um f antes das aspas. Vamos ver como é:
# Vamos supor que queremos pedir a cidade do usuário:
cidade = input('Qual a sua cidade? ')
print(f'Você mora em {cidade}')

# Uau, fácil, não acha? Apenas utilizamos um f antes das aspas, seguido pela mensagem que queremos e em seguida utilizamos chaves e a variável dentro das chaves. Mais simples que a concatenação! Vamos ver outro exemplo
# Vamos pedir ao usuário quantos amigos ele tem:
amigos = int(input('Quantos amigos você tem? ')) # Não esqueça do int!!
print(f'Uau! Você tem {amigos} amigos')

# Se o usuário digitar 16, então a imprimirá na tela: 'Uau! Você tem 16 amigos'


# Operadores de comparação
# Os operadores de comparação utilizam símbolos para comparar expressões. Ao fazer a comparação, o programa retorna um valor booleano (True ou False). Vamos supor que você faça a seguinte comparação entre dois valores: Você se pergunta: "3 é maior que 1?" Então você analisa, e dirá verdadeiro ou falso. É isso que um programa faz, avalia a expressão e retorna verdadeiro (True) ou falso (False). Vamos ver melhor como esses operadores funcionam.
# Operador Maior Que(>):
# Compara se o valor da esquerda é MAIOR que o valor da direita. Vamos ver alguns exemplos:
5 > 9 # Pergunte-se a si mesmo: 5 é maior que 9? Não, certo? Então o programa retornará False
4 > 1 # 4 é maior que 1? verdadeiro, então o programa retornará o booleano True
10 > 0 # 10 é maior que 0? True

# Operador Menor Que(<):
# Compara se o valor da esquerda é MENOR que o valor da direita. Veja os exemplos:
3 < 10 # 3 é menor que 10? True
5 < 2 # 5 é menor que 2? False, 5 é MAIOR que 2
8 < 15 # 8 é menor que 15? True

# Operador Maior ou Igual Que (>=):
# Compara se o valor da esquerda é MAIOR OU IGUAL que o valor da direita. Exemplos:
5 >= 10 # 5 é maior ou igual a 10? False
10 >= 10 # 10 é maior ou igual a 10? True, 10 não é maior, mas sim igual
15 >= 5 # 15 é maior ou igual a 5? True, 15 é maior

# Operador Menor ou Igual Que (<=):
# Compara se o valor da esquerda é MENOR OU IGUAL que o valor da direita. Vamos ver!:
8 <= 10 # 8 é menor ou igual a 10? True, 8 é menor
10 <= 5 # 10 é menor ou igual a 5? False
4 <= 1 # 4 é menor ou igual a 1? False

# Operador Diferente de (!=):
# Compara se o valor da esquerda é DIFERENTE do valor da direita. Em outras palavras, comparam se ambos são diferentes:
10 != 5 # 10 é diferente de 5? True
5 != 5 # 5 é diferente de 5? False, ambos são iguais
3 != 7 # 7 é diferente de 7? True

# Operador Igual a (==):
# Compara se o valor da esquerda é IGUAL ao valor da direita. Em outras palavras, comparam se ambos são iguais:
6 == 7 # 6 é igual a 7? False, são diferentes
5 == 5 # 5 é igual a 5? True
10 == 5 # 10 é igual a 5? False, são diferentes

# Operadores lógicos: Unem as expressões condicionais. Por exemplo, você pode unir operadores de comparação. Vamos ver como isso funciona:
# and: Compara se a expressão da esquerda e da direita são verdadeiras. Se ambas as expressões forem verdadeiras, então retornará True. Mas, se ao meno uma expressão for falsa, então o programa retornará False. Vamos ver com alguns exemplos:
5 == 5 and 12 > 8
# 5 é igual a 5? True! 
# 12 é maior que 8? Sim, então retornará True

12 < 8 and 5 != 3
# 12 é menor que 8? False
# 5 é diferente de 3? True, porém como a expressão anterior é False, retornará False

6 > 3 and 8 > 10 
# 6 é maior que 3? True
# 8 é maior que 10? False, então o resultado será False
# Resumo: As duas expressões precisam ser True para retornar True, caso contrário retornará False

# or: Compara se o valor da esquerda e o valor da direita são verdadeiras. Se ambas forem falsas, então retornará False. Mas para retornar True, ao menos uma expressão deve ser True. Vamos ver como funciona:
7 < 10 or 6 == 6
# 7 é menor que 10? True
# 6 é igual a 6? True, então retornará True

4 == 5 or 9 > 5
# 4 é igual a 5? False
# 9 é maior que 5? True, então retornará True, pois uma expressão é True

9 != 9 or 4 < 4
# 9 é diferente de 9? False
# 4 é menor que 4? False, são iguais, então retornará False
# Resumo: Ao menos uma expressão deverá ser True para retornar True. retornará False quando ambas as expressões forem falsas.

# not: O not é o operador que nega um booleano, ou seja, você utilizar uma negação num True, ele será alterado para False e vice-versa. Vamos ver como funciona:
not True # False
not False # True

not 12 > 5 # Era True, mas foi invertido, resultando em False
not 5 < 1 # A expressão era False, mas o operador not interteu o valor, resultando em True
# Resumo: Inverte um booleano


"# Estruturas de Condição Simples (Condicionais Simples) If"
# Você já deve saber que o computador executa suas instruções (códigos) de cima para baixo e da esquerda para a direita (O modo como lemos). Porém as estruturas condicionais servem justamente para alterar o fluxo de execução, avaliando condições para determinar se algum bloco de código será executado ou não. As condições são as verificações, ou seja, o programa verifica se a expressão é verdadeira (True) ou falsa (False). Você se lembra dos booleanos? Imagine se eu te perguntar: 5 é maior que 10? Não, né? Então, isso é uma condição. Condições basicamente são expressões que o computador precisa verificar se está certa ou errada, e sempre executará aquela condição que for verdadeira.
# Sintaxe básica do if:
# if condição:
    # <bloco de códigos>
# Vamos ver alguns exemplos:
if 5 > 10:
    print('5 é maior que 10') 
print('Fim')
# Antes de mais nada, uma coisa muitíssima importante é observar os espaços antes da instrução print(), detro do bloco de códigos do if. Consegue observar que há alguns espaços? O nome disso é indentação, e isso é obrigatório para que o código funcione. Sempre que houver 2 pontos(:) então isso significa que a próxima linha deverá estar indentada (com 4 espaços). Isso sinaliza que aquele bloco de código está dentro da estrutura do if. Não esqueça desses 4 espaços! Quando não existe mais esses 4 espaços, então quer dizer que a instrução não está dentro do bloco de código.
# Vamos entender: O programa está comparando se 5 é maior que 10. Essa condição é falsa, pois 5 é menor, e não maior que 10, então o programa simplesmente ignora este bloco de código e não executa o que está dentro dele, aquela parte indentada, e logo após imprime 'Fim'. Vamos ver outro exemplo:

if 10 > 1:
    print('10 é maior que 1')
print('Fim')
# Agora vamos nos perguntar: "10 é maior que 1?" sim, então a condição é True, ou seja, será executado o bloco de código dentro do if, e imprimirá '10 é maior que 1') e por último Fim


# Vamos ver um exemplo utilizando uma variável
chovendo = True
if chovendo == True:
    print('Está chovendo!')
print('Fim')

# Declaramos a variável chovendo, atribuímos o valor dela para True e logo em seguida o programa verificou se a variável chovendo era verdadeira, e executou o bloco de código do if. Logo após isso imprimiu 'Fim'

# Mais um exemplo:
pets = False # Declarando a variável pets e atribuindo seu valor para False
if pets == True: # O programa verifica ses pets é True, ou seja, se tem pets
    print("Você tem pets!") # Se a condição pets for verdadeira (True) então será executado esse bloco de código

# Declaramos a variável pets como False e o programa verificou se a variável é True. Como a variável é False, o programa simplesmente ignorou o bloco de código.

# Bem fácil de entender as condicionais, não é? Resumo: O programa verifica se a condição é verdadeira, se for executa a parte indentada (o bloco de código), mas se não for apenas ignora e continua a executar o programa normalmente.



# Estruturas de condição compostas (Condicionais compostas) If, else:
# Como você já viu anteriormente, as condicionais compostas são muito limitadas e serão poucas vezes executadas, pois testam apenas uma condição. Pensando nisso, existem as condicionais compostas, que permite que o programa escolha entre um bloco de código ou outro. Na estrutura composta, funciona da seguinte forma: 
# O programa primeiramente verifica se a condição do If é verdadeira, e se for, executará o bloco de código que pertence a ele (o bloco de código indentado). Porém, se a condição do if for falsa, o programa automaticamente executará o bloco de código do else, pois é sua única opção.
# Vamos ver um exemplo:

luz = True # Declarando a variável luz para True, que significa que a lâmpada está acessa
if luz == True: # O programa verifica se luz é True. Nesse caso é.
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

# Veja um exemplo em que a codição do if é falsa:
altura = 1.59 # Declaramos a variável altura e seu valor é 1.59
if altura > 1.65: # O programa verifica se altura é maior que 1.65, nesse caso não é
    print('Pode entrar na montanha russa') # Esse bloco de código não será executado pois a condição do if é False
else: # Então só resta o programa executar o código do else
    print('Altura insuficiente') # Imprime 'Altura insuficiente', pois altura é menor que 1.65

# Novamente mais um
nome = 'Henrique'
if nome == 'Admin':
    print('Bem vindo, Admin!')
else:
    print('Bem vindo, usuário')
# Declaramos uma variável nome e seu valor é Henrique, logo em seguida, o programa verifica se o nome é 'Admin', nesse caso, não é, então será executado o bloco de código do else, e imprimirá 'Bem vindo, usuário'



# Estruturas de condicão encadeada (Condicional Encadeada) If, elif, else: Essa é uma etapa muito importante, então se entender isso, entenderá facilmente qualquer outra estrutura condicional. A única grande diferença entre a condição encadeada e a condição composta é que a condição encadeada utiliza o elif, permitindo que o programa verifique quantas condições forem necessárias. As estruturas compostas como vimos acima, são também um pouco limitadas, pois permite que o programa verifique apenas duas condições. Mas também existe outra forma de verificar mais condições, na verdade, quantas você quiser! Dê uma olhada rápida neste código:
idade = 23
if idade <= 18:
    print('Você é um Jovem')
elif idade <= 60:
    print('Você é um adulto')
else:
    print('Você é um idoso')
# Vamos lá, declaramos a variável idade que recebe um inteiro 23 e logo em seguida verificamos se a idade é menor ou igual a 18. Vamos pensar: 23 é menor ou igual a 18? Não, certo? Então essa condicional já não será executada, vamos para a próxima. Verificamos: A idade (23) é menor ou igual a 60? Opa! A idade é menor que 60, por que 23 não é maior que 60, e sim menor, então esse bloco de código será executado, e imprimirá na tela: Você é um adulto
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
# É recomendado utilizar o else em todas as condições, porque pode ser útil para evitar erros, imagine fosse uma entrada de usuário, e o usuário digitasse 'azul'?

# Tópicos Avançados
# Quando você tem uma condição verdadeira, você pode simplesmente omite a parte que compara. Veja um exemplo para esclarecer:
if True == True:
    print('Isso é verdadeiro')
# Você pode simplesmente fazer isso, e será a mesma coisa:
if True: # Omitindo a comparação 'True == True'
    print('Isso é verdadeiro')


# Listas são um tipo de dado (como os inteiros, booleanos, strings), mais especificamente, são sequências ordenadas e mutáveis (É possível alterar seus elementos) e possuem índices. Seus elementos são cercados por colchetes [] e cada elemento é separado por vírgulas. O índice é o identificador de um elemento, e começa do 0 até a quantidade de elementos - 1. Por exemplo, se uma lista tem 50 elementos, o primeiro índice será 0 e o último será a quantidade -1, que é 49.
# sintaxe básica
# lista = ['e1', 'e2', 'e3']

# Enquanto valores ficam espalhados por aí, listas 'juntam' tudo ->
# Exemplo muito ruim de usuários espalhados pelo programa
usuario1 = 'João Ferreira'
usuario2 = 'Felipe Almeida'
usuario3 = 'Julio Alberto'
usuario4 = 'Lucas Golmes'
# Exemplo muito bom e recomendável de uma lista de usuários que junta todos os usuários
usuarios = ['João Ferreira', 'Felipe Almeida', 'Julio Alberto', 'Lucas Golmes']


# Começando a entender as listas
# Vamos começar a declarar uma lista com 3 elementos:
lista = ['elemento1', 'elemento2', 'elemento3']
# índices:    0            1            2
# Repare que o índice começa sempre no primeiro elemento, e começa do índice 0. Como já disse anteriormente, os índices são como IDs para os elementos, você pode acessar um elemento pelo seu índice.
# Acessando os elementos pelo índice
# Para acessar um elemento pelo seu índice, basta seguir a seguinte sintaxe:
# nome_da_lista[índice]
# Sabendo que os índices iniciam em 0, vamos tentar acessar o elemento1 utilizando o seu índice:
print(lista[0]) # a saída desse comando será 'elemento1', pois ela está no índice 0.
# Acessando o elemento 2, que está no índice 1
print(lista[1])
# Acessando o elemento 3, que está no índice 2
print(lista[2])

# Um pouco chato acessar cada elemento pelo seu índice individualmente, que tal acessar todos os elementos de uma vez? Basta imprimir o nome da lista:
print(lista)

# Listas também aceitam diferentes tipos de dados: Sejam strings, booleans, inteiros e floats, listas armazenam todos esses valores:
lista = ['Pedro', 15, True, 'Maria', False]
# índices   0     1     2      3       4
# Acessando novamente um elemento pelo seu índice:
print(lista[3]) # Maria

# Algumas funções de listas
# Listas possuem funções, e isso é muito bom, pois com funções as listas ganham muitas funcionalidades. Vamos ver algumas delas:
# Imagine que você tem uma lista enorme de vendas, e por algum motivo quer saber qual é o MAIOR número da lista, o número mais grande do que todos os outros. Você pode fazer isso utilizando a função max():
vendas = [120, 456, 123, 986, 965, 329, 943, 542, 239, 236, 823, 967, 327, 432, 534, 976, 321, 743, 658, 735, 885, 364, 785, 984, 651, 798]
# Essa lista é relativamente grande, e ée difícil achar o maior númro logo de cara, então vamos utilizar a função max:
# sintaxe:
# max(nome-da-lista)
print(max(vendas))
# Bem fácil, não é? Agora como achar o menor número da lista? Podemos achar facilmente utilizando a função min():
# sintaxe: min(nome-da-lista)
print(min(vendas))
# Bem fácil também! que tal ver mais um exemplo?

# Queremos achar a maior idade e a menor idade nesta lista:
idades = [34, 12, 43, 65, 86, 87, 21, 33, 43, 90, 32, 43, 45, 15, 56, 23, 54, 43, 7, 8]
print(max(idades)) # Imprimindo o maior valor
print(min(idades)) # Imprimindo o menor valor


# Também é possível somar os elementos de uma lista, sim!!! Vamos ver como funciona:
# Vamos supor que você tem a tarefa de somar todas as notas de 15 alunos de uma escola, uma tarefa bem fácil! Vamos ver:
notas = [8, 9, 1, 4, 5, 6, 7, 4, 4, 5, 7, 10, 2, 4, 8]
# para somar todos os valores, utiliza-se a função sum(nome-da-lista):
print(sum(notas))
# Muito fácil também, concorda??



# Agora pense que você está fazendo uma festa de aniversário. Você anotou o nome de todos os seus amigos que vão à festa, porém a lista é gigantesca! Será uma super festa! Sua tarefa é saber a quantidade de pessoas que vão à festa, você já tem o nome das pessoas, e quer saber quantas pessoas são. Então para essa tarefa utilizaremos a função len(nome-da-lista):
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana", "Karine", "Lucas", "Maria" "Nicolas", "Olivia", "Patrick", "Heliezer", "Rafael", "Sofia", "Tiago", "Jorge", "Vitória", "William", "Maria", "Roberto", "Julia", "Amanda", "Bruna", "Caio", "Matheus"]
# Muitos itens, não é mesmo? Vamos descobrir quantos amigos terá na festa utilizando a função len(nome-da-lista):
print(len(nomes))




# Vamos supor que você quer acessar o último elemento de uma lista, mas a lista é gigante. É aí que entram os índices negativos.
# índices negativos são iguais aos índices positivos normais mas agora ocorre uma inversão. O último índice é o -1 e o primeiro depende de quantos elementos uma lista tem. Vamos criar a seguite lista:
cores = ['vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'violeta', 'roxo', 'marrom', 'preto', 'branco', 'cinza', 'rosa', 'bege']
# negativos  -13       -12         -11      -10       -9        -8       -7       -6        -5       -4       -3       -2      -1
# a lista é enorme, e você quer acessar o último elemento, o bege.
# para isso, basta colocar o índice -1, pois -1 sempre será o último elemento de toda e qualquer lista, não importa o seu tamanho.
cores[-1] # bege



# Você já sabe acessar elementos pelos seus índices, mas e se você quisesse acessar múltiplos elementos de uma lista? É até possível acessar elemento por elemento, mas esse jeito é um pouco demorado e utiliza muitas linhas de código. Mas é por isso que surgiu a fatiação de listas.
# FATIAÇÃO DE LISTAS: Permite acessar múltiplos elementos de uma só vez!
# sintaxe básica:
# nome_da_lista[índice_de_inicio:índice_de_fim]
# Veja a seguinte lista:
materiais = ['Ferro', 'Madeira', 'Metal', 'Concreto', 'Pedra']
# índices:      0         1         2         3          4
# Vamos supor que eu quero acessar a Madeira, o Metal e o Concreto.
# Sem a fatiação de listas:
materiais[1]
materiais[2]
materiais[3]

# Com a fatiação de listas:
materiais[1:4]
# Repare que sem a fatiação acessamos individualmente os elementos de índice 1, 2 e 3. Mas já na fatiação acessamos do índice 1 até o índice 4. É aqui que surgem muitas dúvidas. Ao fatiar uma lista, você deve especificar o ínicio e o fim, ou seja, aonde que começa a acessar a lista até aonde para de acessar a lista, porém no índice de fim, sempre é escrito o índice final somando + 1.
# Vamos ver mais exemplos

minerios = ['Diamante', 'Ferro', 'Ouro', 'Cobre']
# índices:      0          1       2        3
# Vamos supor que queremos acessar o Diamante, o Ferro e o ouro
# Sem a fatiação:
minerios[0]
minerios[1]
minerios[2]

# Com a Fatiação:
minerios[0:3]
# Ou você pode fazer isso (não é recomendável, mas pode ser útil para aprendizado)
minerios[0:2+1]
# O resultado é o mesmo

# Também existe a fatiação de listas com o índice inverso
animais = ['Gato', 'Coruja', 'Aranha', 'Escorpião']
# índices:   -4       -3        -2         -1
# vamos supor que queremos acessar a coruja e a aranha
# segue a mesma regra do que a fatiação com índices positivos
animais[-3:-1] # Começa a fatiar do índice -3, e para até o -2.
# A mesma fatiação pode ser feita assim:
animais[-3:-2+1] # Vamos pensar: Começa do índice -3, acessa a coruja. Depois vai para o índice -2 e acessa a Aranha, e para por aí.
# Fatiação com índices negativos é mais complexo do que fatiação a fatiação tradicional com índices positivos. Então sempre que puder utilize fatiação com índices positivos, é menos confuso e é mais fácil de compreender.



# Alterando os elementos da lista
# Você pode alterar os elementos de uma lista tanto explicitamente (alterar direto a lista) quanto alterar implicitamente (utilizar funções do python que modifiquem os elementos de uma lista). Vamos apresentar como alterar listas implicitamente, ou seja, utilizando funções.
# Visualize a lista a seguir:
automoveis = ['Carro', 'Caminhão', 'Moto', 'Bicicleta']
# Analisando, há um item errado na lista. Bicicleta não é um automóvel, então podemos utilizar as funções de lista. Você deve estar se perguntando: Mas por que não apago o elemento simplesmente apagando pela lista?
# Ao usar as funções de lista, você evita confusões. É muito usado em loops e em condições (Assuntos mais avançados), quando você executar um programa, você não consegue simplesmente apagar ou adicionar manualmente elementos. O programa pode fazer essa tarefa para você, permitindo que você alcance a sua tarefa.
# Voltando a explicação... Vamos supor que queremos remover o elemento 'Bicicleta' da lista, pois ele não é um automóvel.
# utilizamos a função .remove('elemento')
# vamos ver como funciona:
automoveis.remove('Bicicleta')

# É só isso! Já podemos remover elementos de uma lista!
# Vejamos outros exemplos:
materias = ['Geografia', 'Tijolo', 'Artes', 'Matemática', 'Parede']
# Que estranho, concorda? Tijolo e Parede são matérias escolares? Então vamos remové-los!
materias.remove('Tijolo')
materias.remove('Parede')

# Simples, né?
# Podemos remover qualquer elemento de uma lista utilizando o índice!
frutas = ['Maçã', 'Banana', 'Laranja', 'Kiwi', 'Massinha', 'Abacaxi', 'Slime']
# índices:  0        1          2        3         4           5         6
# nome_da_lista.pop(índice)
frutas.pop(4)
# Removemos o elemento do índice 4, que era Massinha
# podemos remover também o último elemento, sem colocar o índice entre os parênteses:
frutas.pop() # Remove o último elemento
frutas.pop(-1) # Também é possível fazer isso, resultando na mesma coisa


# ADICIONANDO ELEMENTOS
# Vamos supor que você queria adicionar algum elemento em uma lista. Veja por exemplo, a seguinte lista:
estados_sul = ['Paraná', 'Rio Grande do Sul']
# Está faltando Santa Catarina, e para isso podemos utilizar a função append, vamos ver:
# sintaxe:
# lista.append('elemento')
estados_sul.append('Santa Catarina')
# Siples demais! Mas uma coisa importante a lembrar é que a função append sempre adiciona os elementos no último índice ou seja, após adicionar um elemento, esse elemento passa a ser o último elemento
# Vamos ver outros exemplos
IAs = ['ChatGPT', 'DeepSeek', 'Grok']
# Queremos adicionar Sider, já sabe como?
IAs.append('Sider')
print(IAs)
# Moleza!

# E também podemos adicionar elementos no índice que quisermos!
# A função insert te permite adicionar um elemento no índice que desejar, mas sem substituir o elemento que estava naquele índice.
# Veja alguns exemplos:
mamiferos = ['Baleia', 'Morcego']
# índices       0          1
# queremos adicionar 'Humano' no índice 1, logo após o índice 0 que está sendo ocupado pelo elemento 'Baleia'. Se adicionarmos o elemento 'Humano' no índice 1, o Morcego não será substituído, mas sim ocupará o próximo índice, que é o índice 2. Vamos ver na prática:
# sintaxe básica:
# lista.insert(indice, elemento)
mamiferos.insert(1, 'Humano') # Estamos inserindo 'Humano' no índice 1.
# A lista agora está assim:
mamiferos = ['Baleia', 'Humano', 'Morcego']
# Bem fácil, não acha? Mas não esqueça que insert NÃO subtitui um elemento, mas sim 'joga' os elementos para frente, É como se o insert fosse uma pessoa e estivesse pulando a fila do supermercado, mas sem empurrar a pessoa que estava atrás dele.

# Vamos ver mais um último exemplo para fixar!
fila = ['Pessoa1', 'Pessoa2', 'Pessoa3', 'Pessoa4', 'Pessoa5']
fila.insert(1, 'Furão de Fila') # O Furão de Fila furou e entrou no lugar 2!
print(fila)

# Também existe outra forma de alterar um elemento pelo seu índice
# Esta forma agora sim SUBSTITUI um novo elemento pelo antigo elemento. Vamos ver como funciona
compras = ['Tomate', 'Sabonete', 'Detergente', 'Abacaxi', 'Laranja']
# índices     0          1            2            3           4
compras[3] = 'Abacate'
# Estamos alterando o elemento do índice 3, que era 'Abacaxi', e que agora passa a ser 'Abacate'
# Então quando você quer SUBSTITUIR um elemento que já existia na lista por outro novo elemento, utilize esse método.

# Vamos fazer o exemplo da fila denovo!
fila = ['Pessoa1', 'Pessoa2', 'Pessoa3', 'Pessoa4', 'Pessoa5']
# índices   0          1           2         3           4
fila[1] = 'Intrusor' # Agora sim, o Intrusor empurra a pessoa2 e ela sai da fila


# Juntando listas
# Já pensou juntar listas para criar uma nova lista? Com o python isso é possível, utilizando a função extend! Vamos ver como funciona!
# Vamos supor que temos duas listas, e queremos unir todas em apenas uma, veja o exemplo:
# sintaxe básica:
# lista1.extend(lista2)
planetas = ['Terra', 'Marte', 'Vênus']
estrelas = ['Sol', 'Sagittarius A']
planetas.extend(estrelas) # planetas agora possui os elementos: ['Terra', 'Marte', 'Vênus', 'Sol', 'Sagittarius A']

# Também é possível juntar listas utilizando o operador de adição +
sucos = ['Laranja', 'Limão', 'Abacaxi']
refrigerantes = ['Coca-Cola', 'Pepsi']
print(sucos + refrigerantes)
# Escolher entre a função extend e juntar utilizando o operador de adição é que o extend já é próprio para fazer isso, então é mais recomendado.


# Organizando listas
# Imagine que você tenha uma lista toda embaralhada, e precisava colocar em ordem alfabética ou númerica essa lista? Seria trabalhoso, não é? Mas graças a função sort, você consegue organizar sua lista em ordem crescente! Vamos ver isso na prática:
# sintaxe: lista.sort()
letras = ['c', 'd', 'y', 'w', 'b', 'a', 'z', 'j', 'o', 'r', 'f', 't']
letras.sort() # Prontinho, a sua lista já está toda organizada em ordem alfabética!
print(letras)

# Um exemplo em ordem númerica crescente
numeros = [4, 8, 12, 5, 9, -4, 0, 5, 6, -6, 120, 450, 32, 21, 7]
numeros.sort() # Lista organizada
print(numeros) 

# OK, mas e se precisar ordenar em ordem decrescente?
# Simples, apenas utilize a função reverse! Veja como fica:
nomes = ['Pedro', 'João', 'Maria', 'Zazu', 'Antônio']
nomes.sort() # Primeiro ordenamos a lista normalmente
nomes.reverse() # Depois invertemos a ordem, ficando em ordem decrescente!
print(nomes)



# Operadores de pertencimento
# Os operadore de pertencimento verificam se um valor está contido ou não está contido em uma sequência ou coleção (como listas, strings, dicionários, etc). Vamos ver um exemplo:
# Verificamos se um elemento ou valor está presente na lista utilizando as palavras-chave in e not in. Vamos ver como funciona:
# Primeiro criamos uma lista
passaros = ['Tucano', 'Bem-te-vi', 'Quero-Quero']
# Logo em seguida vamos verificar se algum valor está presente na lista utilizando a palavra-chave 'in':
'Tucano' in lista # Tucano está na lista? O programa verifica e retorna o booleano True
# Agora vamos verificar se algum valor NÃO está na lista:
'Pombo' not in lista # Pombo não está na lista? O programa analisa e retorna um booleano, nesse caso, True.



# Desempacotamento de listas
# O desempacotamento de listas é utilizado quando você quer atribuir diversas variáveis para cada elemento da lista. Vamos supor que eu tenho uma lista chamada nomes e apresenta os seguintes nomes: 'João', 'Felipe', 'Fábio'; E eu quero atribuir uma variável para cada um desses nomes. Vamos ver como isso é feito:
lista = ['João', 'Felipe', 'Fábio']
user001, user002, user003 = lista # Agora cada variável dessa possui o seu respectivo elemento da lista, ou seja, user001 armazena o valor 'João', user002 armazena 'Felipe' e user003 armazena 'Fábio'
print(user001) # user001 = 'João'
print(user002) # user002 = 'Felipe'
print(user003) # user003 = 'Fábio'

# Mas esse tipo de desempacotamento pode gerar erros, um dos motivos é que há chances de ter 5 elementos na lista e você ter declarado apenas 4 variáveis e na hora de desempacotar os elementos isso retornará um erro, pois o número de elementos é diferente do número de desampacotamento de variáveis. Mas podemos corrigir isso utilizando o asterisco. Vamos ver:
# Uma lista com 5 elementos, mas possui apenas duas variáveis:
lista = ['Pedro', 'Maria', 'João', 'Felipe', 'Jorge']
user1, *users = lista
print(user1) # Pedro
print(users) # ['Maria', 'João', 'Felipe', 'Jorge']
# vamos enteder, declaramos uma lista onde ela possui 5 elementos, e em seguida, criamos a variável user1, que se refere ao elemento 'Pedro' da lista, e a variável users com um asterisco. Por incrível que pareça, isso não resulta em um erro, mas todo o segredoe está no asterisco. Quando você desempacota utilizando uma variável com um asterisco, isso significa que agora a variável com asterisco está armazenando todos os elementos após o 'Pedro', pois já está sendo ocupado pelo user1. Ou seja, users está armazenando 'Maria', 'João', 'Felipe' e 'Jorge'! Vamos ver mais um exemplo:

frutas = ['Melancia', 'Abacaxi', 'Maçã', 'Laranja']
fruta1, *frutas_restantes = frutas
print(fruta1) # Melancia
print(frutas_restantes) # ['Abacaxi', 'Maçã', 'Laranja']
# Agora fruta1 está armazenando Melancia e frutas_restantes está armazenando os elementos restantes da lista, que são: ['Abacaxi', 'Maçã', 'Laranja']

# Também é possível utilizar o asterisco como a primeira variável, então ela armazenará os primeiros elementos da lista:
animais = ['Tubarão', 'Crocodilo', 'Gato', 'Morcego']
*inicio, fim = animais
print(inicio) # ['Tubarão', 'Crocodilo', 'Gato']
print(fim) # Morcego
# Agora como a ordem foi alterada, a variável inicio possui os primeiros elementos da lista, e o fim possui o último elemento da lista, que é o Morcego.


# Os dicionários apresentam pares de chave-valor, isso é muito útil quando você precisa de uma forma mais organizada de criar dados mais significativos pelo seu programa. Dicionários também são mutáveis, o que significa que podem ser usados funções implicitamente para alterar os pares chave-valor do dicionário. Chaves serão os identificadores dos valores (como um índice que identifica os elementos em uma lista)
# Vamos ver alguns exemplos:

compras = {
    'Arroz': 3.45,
    'Feijão': 2.90,
    'Macarrão': 4.50
#   chave: valor
}
# Criamos um dicionário e seu nome é compras. Repare que todos os 3 pares de chave-valor tem a mesma estrutura, primeiro a chave, seguido dos dois pontos e por fim o seu valor. As chaves são únicas, isso quer dizer que um único dicionário não pode contér duas chaves iguais. Exemplo: duas chaves do dicionário possuem o nome 'Abacaxi'. Isso pode causar confusões no seu dicionário.
# Imprimindo os dicionários
# É possível imprimir o dicionários apenas digitando print() e dentro dos parênteses o nome do dicionário:
print(compras)
# Também é possível acessar o valor de um dicionário pela sua chave, quase igual uma lista com índices:
print(compras['Arroz']) # saída: 3.45 (imprime o valor)


# Modificando e alterando os pares-chave
# Neste tipo de modificação ou acrescentação, o programa verifica no dicionário se a chave já existe no dicionário, veja:
compras['Sushi'] = 1.35 # O programa verifica se já existe 'Sushi' no dicionário. Como não existe, então apenas adicinará um novo elemento, juntamente com o seu valor. Porém se já existisse, apenas alteraria o seu valor. Veja um exemplo em que a chave já existe:
compras['Macarrão'] = 0.35 # Como a chave já existe no dicionário, apenas substituirá o seu valor, que antes era 4.50 e agora passa a ser 0.35.



frutas = {
    'Maçã': 3.99,
    'Laranja': 4.99,
    'Limão': 2.99,
    'Abacaxi': 1.99,
    'Manga': 1.59,
}
# Funções e métodos de dicionários
# As funções e métodos permitem deixar os dicionários com mais funcionalidades e com mais poder. Vamos quais são:
# del: A função del serve para deletar o par de chave-valor do dicionário
del frutas['Abacaxi']
print(frutas) # {'Maçã': 3.99, 'Laranja': 4.99, 'Limão': 2.99, 'Manga': 1.59}

# popitem: A função popitem é responsável por remover o último par de chave-valor do dicionário
frutas.popitem()
print(frutas) # {'Maçã': 3.99, 'Laranja': 4.99, 'Limão': 2.99}

# pop: O pop remove um par de chave-valor pela sua chave
frutas.pop('Maçã')
print(frutas) # {'Laranja': 4.99, 'Limão': 2.99}

# get('valor', 'mensagem se não encontrar'): Retorna o valor da chave. Muito útil para evitar erros
print(frutas.get('Limão', 'Fruta não foi encontrada')) # 2.99
print(frutas.get('Pêra', 'Fruta não foi encontrada')) # Fruta não foi encontrada


# operadores de pertencimento (in e not in): Retornam um boolean dizendo se tal item está presente no dicionário
print('Laranja' in frutas) # True
print('Tomate' not in frutas) # True

# clear: Limpa todos os pares chave-valor da lista
frutas.clear()
print(frutas)

# Acessando a chave, o valor e item
compras = {
    'Arroz': 3.45,
    'Feijão': 2.90,
    'Macarrão': 4.50
#   chave: valor
}

# chave, valor, item
# keys: Chaves do dicionário (Identificadores)
print(compras.keys()) # dict_keys(['Arroz', 'Feijão', 'Macarrão', 'Sushi'])

# values: Valores das chaves
print(compras.values()) # dict_values([3.45, 2.9, 0.35, 1.35])

# items: São tuplas individuais que contém os pares de chave-valor
print(compras.items()) # dict_items([('Arroz', 3.45), ('Feijão', 2.9), ('Macarrão', 0.35), ('Sushi', 1.35)])

# Vamos supor que eu tenho um dicionário de alunos e quero ter uma visão geral desse dicionário, como o total de notas, a média de notas e quantos alunos há no dicionário. Vamos ver:
alunos = {
    'João': 7.90,
    'Mariane': 5.60,
    'Cristopher': 8.55,
    'Lucas': 4.50
#   nome: nota
}
# Queremos o total de notas, a média e quantos alunos há, vamos fazer isso.
# Primeiramente, para descobrir o total de notas, deveremos utilizar as values e a função sum. Vamos ver como isso ficaria:
total = sum(alunos.values())
print(total)
# A variável total está armazenando a soma dos valores do dicionários alunos, e os valores são as notas.
# Agora para saber a quantidade de alunos, utilizamos a função len() e dentro dos parênteses as chaves do dicionário. Ficará assim:
quantidade = len(alunos.keys())
print(quantidade)
# A variável quantidade está armazenando a quantidade de alunos baseado na quantidade de chaves
# Por fim, para saber a média, apenas dividimos o total das notas pela quantidade de alunos
media = total / quantidade
print(media)
# A média está armazenando a divisão do total das notas pela quantidade de alunos


# Tópicos avançados
# Iteração com dicionários
# É possível iterar sobre cada par de chave-valor de um dicionário. Isso é um assunto mais avançado, porém muito útil. Não vou explicar detalhadamente o que são iterações nesta aula, mas sim na própria aula de iterações com o loop for. Enfim, não se preocupe se não entender o código a seguir. Darei uma breve explicada:
# Loops for são laços de repetição que podem iterar sobre elementos ou sequências, como listas, strings e dicionários também. Ou seja, eles podem acessar cada elemento individualmente. Tudo que quero te mostrar a seguir é apenas um jeito elegante de imprimir as chaves e os valores de um dicionário. Veja o seguinte código:
# Considere o seguinte dicionário:
produtos = {
    'smartphone': 3500,
    'tablet': 2675,
    'smartwatch': 375
}
items = produtos.items()

for chave, valor in items:
    print(chave, valor)

# A saída deste código será:
"""
smartphone 3500
tablet 2675
smartwatch 375
"""
# Isso imprime os itens de maneira mais organizadas.




# ESTRUTURAS DE REPETIÇÃO: # while
# As vezes você quer executar repetidas vezes um bloco de código, e geralmente faz algo como isso:
print('Hello, World!')
print('Hello, World!')
print('Hello, World!')
print('Hello, World!')
print('Hello, World!')
# Mas o while simplifica tudo isso. O que ele faz é repetir algum bloco de código ENQUANTO (while) sua condição for verdadeira. Lembram muito as estruturas condicionais, não é? Mas a grande diferença é que as estrututas condicionais executam apenas uma vez o bloco de código se sua condição for verdadeira, e as estruturas de repetição executam repetidas vezes um bloco de códigos. Vamos ver o exemplo mais simples possível:
# Queremos imprimir na tela 5 vezes 'Hello, World!'
# O primeiro passo para a criação de um loop while é seu contador. Pode ser de qualquer nome (defina nomes claros), então vamos utilizar neste exemplo uma variável contador, e atribuir o seu valor para 1, apenas isso:
contador = 1
# Em seguida, adicionamos a palavra-chave while, seguida de sua condição. Como queremos executar 5 vezes, colocamos essa condição:
while contador <= 5: # Enquanto a variável contador for menor ou igual a 5, então vamos executar repetidas vezes o bloco de código:
    print('Hello, World!') # Vamos imprimir o bloco de código 'Hello, World'
    contador = contador + 1 # E por fim, vamos incremetar +1 a variavel contador, pra ela não entrar em um loop infinito (jajá falamos disso)
# Perceba mais uma vez que o código está indentado com 4 espaços, sinalizando que aquele bloco de código faz parte da estrutura while.
# Recapitulando: O código acima executa 5 vezes o bloco de código 'Helllo, World!'. Lembrando que a cada repetição, a variável contador aumenta em 1.


# Vamos criar um programa que repete 5 vezes o código 'Contagem: 1, 2, 3, 4, 5...'
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


# Agora um programa que pergunta ao usuário seu nome. O loop quebrará apenas quando o usuário digitar 'exit':
while True:
    nome = input("Digite o seu nome: ")
    if nome == 'quit':
        break


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

# Loops infinitos: Executam o programa até o infinito.. e além
# Loops infinitos são loops que nunca param de executar, executam o bloco de código que está dentro deles para sempre. Issso acontece quando você acidentalmente esquece de incrementar ou decrementar a variável contadora responsável pela quantidade de execuções de um bloco. Exemplo:
# contador = 1
# while contador < 10:
#     print('Contando!')
# O código a seguir é um exemplo de loop infinito. Vamos descobrir o porque. Primeiramente declaramos a variável contador e atribuí-mos a ela o valor 1 normalmente, tudo certo. Criamos um loop while que verifica se o contador é menor que 10, se for menor que 10, continua executando, até chegar a um momento em que a condição se torna falsa (até o contador ser 10). Nós imprimos 'Contando!', mas o único detalhe é que esquecemos de incrementar + 1 dentro de seu bloco de código, por isso o loop ficará executando eternamente. Isso consome muita memória RAM e Bateria, então quando acidentalmente entrar em um loop infinito, feche o programa o mais rápido possível. Então a correção deste loop infinito seria esse:
contador = 1
while contador < 10:
    print('Contando!')
    contador = contador + 1 # Evitando que o loop seja infinito
# Agora sim, adicionamos o incrementador! Não se esqueça disso!


# While...else:
# Semelhante as condições, os laços de repetição while também aceitam else. O else só é executado quando a condição do while for falsa, como as estruturas de condição. Vamos ver na pratica:
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('As repetições acabaram')

# Isso imprime os números de 1 a 10, e quando a condição do while for falsa, isso é, quando a variável i atingir o valor 11, o programa verifica se 11 é menor que 10, e como isso retorna um booleano False, então o else será executado seguido de seu bloco de código, imprimindo 'As repetições acabaram'


# ESTRUTURA DE REPETIÇÃO: for
# Além do loop while, também existe um outra alternativa para repetições no python, o for. O for possui uma sintaxe bem menos verbosa (isso significa que o for pode fazer a mesma coisa que o loop while, porém com menos linhas de código) e ainda te permite iterar sobre listas ou coleções (Assunto mais adiante). 


# Exemplo ruim de uma contagem até 5:
print('Contagem: 1')
print('Contagem: 2')
print('Contagem: 3')
print('Contagem: 4')
print('Contagem: 5')
# Exemplo recomendável e certo de contar até 5:
for contagem in range(1, 6):
    print(f'Contagem: {contagem}')


# Entendendo o loop for range
# for range: Conta do início até o fim, como uma contagem regressiva (ou progressiva).
# Sintaxe:
# for contador in range(inicio, fim, passos):
    # bloco de códigos
# primeiramente utiliza-se a palavra-chave for, em seguida uma variável desejada, como contador, e por fim utiliza-se 'in' e o range(), contendo dentro dos seus parênteses os números especificados. Vamos ver um exemplo
for contador in range(0, 5, 1):
    print(contador)
# Utilizamos o for, a variável contador, logo em seguida o in range(0, 5, 1). Vamos explicar o range. O primeiro número do range significa em qual número ele deve começar, nesse caso, 0. O segundo número diz até quando o contador deve parar, nesse caso 4, pois o fim sempre é subtraído em -1, ou seja, se o número final é 10, então na verdade seu fim é 9. E o último número diz quantos em quantos passos o contador irá pular, nesse caso é 1, então contará normalmente de 0 a 4. Por fim é colocado dentro da estrutura do for o comando de blocos, nesse caso, imprimirá o contador, ou seja, imprimirá: 0, 1, 2, 3, 4.
# Vamos ver mais um exemplo:

for i in range(1, 6, 1):
    print(i)
# Declaramos a variável i, e o range começa do 1, termina até o 6, e pula de 1 em 1 número (isso é, normalmente). A saída será: 1, 2, 3, 4, 5
# Lembre-se que o for é uma estrutura de repetição, então sempre que executar uma vez o bloco de código dentro dele, a variável contador será subtraída ou adicionada em 1, como um loop while. Veremos mais a frente a diferença entre loop while e loop for.

# Mas não é necessário colocar em quantos em quantos passos a variável vai pular. podemos utilizar essa sintaxe:
# for i in range(inicio, fim):
    # <bloco de comandos>

# Vamos ver um exemplo:

for i in range(1, 4):
    print(i)
# Declaramos a variável contadora 'i', e o seu range de início é de 1, ou seja, comecará em 1, e seu range de fim é 4, ou seja, terminará em 3, pois o fim é sempre subtraído. A saída desse for é: 1, 2, 3


# Porém ainda é possível omitir o range de início, restando apenas o range de fim! Vamos ver como isso ficaria:
# for i in range(fim):
    # <bloco de comandos>

for i in range(5):
    print(i)
# Aqui omitimos o range de início, então ele começará em 0, e terminará em 4, bela reduzida, não é mesmo?

# Vamos ver um exemplo mais avançado:
for foguete in range(4):
    print(f'Lançando em {foguete}')
# Vamos entender o código. Declaramos a variável foguete, que conta de 0 até 3. O seu bloco de código imprimirá 'Lançando em {e o número do contador}'. Cada execução que o loop realizar, será incrementado em +1 a variável foguete. Vamos entender melhor isso:

for i in range(1, 4):
    print(i)
# Esse bloco de código começa em 1, e termina em 3. A cada execução, é incrementada +1 a variável i, e o programa verifica se i é maior que 3. Se a variável i for maior que 3, então o loop para de executar, pois sua condição já esteve satisfeita. Não parece, mas o loop for também há uma condição, conseguiu perceber?
# for i in condição:
    # <bloco de código>
# Mas nesse caso a condição é o range, e não uma comparação tradicional com operadores de comparação como num loop while. É claro que o programa faz comparação no loop for, mas isso não é visível. Vamos ver apenas um último exemplo:
for repeticao in range(1, 6):
    print('Estou repetindo!')
# Ok, declaramos uma variável repeticao e agora ela repete de 1 até 5, e a cada repetição, será incrementada +1 na variável, executando o bloco de código 'Estou repetindo!'. Acompanhe comigo: A variável repeticao tem o valor de 1, então o programa verifica se a repeticao é menor que 5, e como 1 é menor que 5, então executa o bloco de código, imprimindo o que estiver lá dentro. Na segunda, terceira, quarta, quinta repetição, o programa verifica se ainda a variável não é 5, então executa novamente. Mas quando a variável repeticao é 6, o programa compara, e vê que a variável já chegou ao fim, já terminou. Então simplesmente para de executar o loop e executa o resto do programa.

# Então, que tal ver um loop for com um else, lembrando muito as condições?
for foguete in range(4):    
    print(f'Lançando em {foguete}')
else:
    print('Lançar!')
# Vamos lá, foi declarada a variável foguete, que começa em 0 e termina em 3. Na primeira repetição é executado o loop, executando o seu bloco de código, e imprime 'lançando em {e a variável}'. Como nesse caso não especificamos o início e apenas o fim, então a repetição começará do 0. Ou seja, na primeira repetição imprimirá 'Lançando em 0', pois a variável foguete tem o valor 0. Então é feita mais uma repetição, e desta vez o valor da variável é 1, pois a cada execução a variável é incrementada em 1, e então, imprime 'Lançando em 1'. E repete isso até chegar na repetição 4. O programa veifica se a variável é 4, e então, ignora o bloco de código do loop for e executa o else. Lembra do else, aquele utilizado em condições, que quando uma condição é falsa, ele é executado? Então, o programa viu que a condição do loop for é falsa e executou o else, imprimindo na tela 'Lançar!'.


# Vamos lá, hora de responder algumas perguntas

# Qual a diferença entre loop while e loop for?
# Um loop while pode ser usado quando não se sabe ao certo quantas repetições você quer que algo repita. o while True é um exemplo muito bom disso, pois executa a repetição infinitamente, e só para quando é feito o uso de um break. Vamos ver um loop while True:
while True:
    nome = input("Digite o seu nome ou 'exit' para sair: ")
    if nome == 'exit':
        break
# Vamos explicar: Criamos um loop while True, isso significa que o loop executará infinitamente. Pedimos ao usuário o seu nome, e isso ficará executando. O loop while só terminará de executar quando o usuário digitar 'exit', pois foi feito o uso do break, quebrando o laço while. Então enquanto o usuário digitar qualquer outra coisa que não seja 'exit', o loop ficará executado seu bloco de código para sempre, perguntado ao usuário seu nome infinitamente. A única forma de parar essa repetição é utilizando um break.
# Já um loop for pode ser usado quando já se sabe o número de repetições que você quer. Um exemplo:
for i in range(6):
    print('Já sei quantas vezes serei executado! 5 vezes!')



# Agora vamos ver alguns exemplos de iteração em listas
# A iteração em listas segue o mesmo conceito da iteração com strings, mas a grande diferença é que a iteração em listas imprime cada elemento da lista, e não cada letra. Vamos ver alguns exemplos
# Iterando com o loop for
# Uma iteração significa acessar cada elemento ou caractere de uma sequência, como uma lista ou uma string. Vamos ver alguns exemplos:
# Vamos supor que temos uma string, e queremos imprimir cada letra da string individualmente. É possível fazer isso com uma iteração:
string = 'texto'
for letra in string:
    print(letra)
# Aqui já é notável que as coisas mudaram, vamos entender. Declaramos a variável string e atribuímos seu valor a 'texto'. Em seguida, criamos um loop for e uma variável letra, ela será responsável por iterar sobre cada caractere da string, ou seja, imprimir cada letrinha. Lembrando que o nome da variável após o loop for pode ser qualquer um que você desejar. O código acima se lê assim:
# para cada letra na string, então imprima a letra.
# Vamos ver mais exemplos:

pais = 'Brasil' # Lembrando que variáveis não devem ter acentuações!
for letra in pais:
    print(letra)
# Vamos entender: Declaramos a variável pais, e em seguida o loop for, seguido da variável letra, que itera sobre cada letra da variável pais (Brasil). Então isso imprimirá cada letra do Brasil em uma linha diferente, ou seja:
"""
B
r
a
s
i
l
"""

# Hora de iterar sobre listas
# Agora vamos falar de iterações com listas. As iterações com listas diferentemente das iterações com strings, imprimem cada elemento da lista, e não cada letra da lista. É feito quase a mesma coisa com a iteração de strings, vamos ver um exemplo:
# Vamos supor que queremos imprimir individualmente cada elemento de uma lista de frutas:
frutas = ['Maçã', 'Banana', 'Laranja']
# então utilizamos o for, seguido da variável que desejamos e em seguida a palavra-chave in, e por fim, o nome da lista, com o seu bloco de código. Vamos ver:
for fruta in frutas:
    print(fruta)
# Vamos entender: Declaramos a lista frutas, declaramos o laço for seguido pelo nome da variável e a palavra-chave in com a lista frutas, e no seu bloco de código imprime cada fruta, resultado em:

"""
Maçã
Banana
Laranja
"""
# Uma coisa muito importante a dizer é que, ao executar o bloco de códigos dentro do loop for, a repetição é feita novamente até não possuir mais elementos dentro da lista.
# Repare que o nome da lista está escrito no plural ('frutas') e o nome da variável após o for está escrito em singular ('fruta') indicando que isso acessará cada elemento da lista individualmente.

# Vamos ver mais um exemplo:
animais = ['Coruja', 'Lobo', 'Cachorro', 'Cavalo']
for animal in animais:
    print(animal)
# O loop for acima se lê assim: Para cada animal na lista de animais, então: imprima animal. Vamos entender melhor, declaramos a lista animais seguido pelo loop for, que itera a cada elemento, e imprime cada elemento individualmente, conseguiu compreender?

# Vamos a alguns exemplos mais avançados:
# Vamos supor que estavamos minerando numa caverna, mas não queremos que tenha Ferros, apenas queremos outros minérios, e ignorar o minério Ferro. Podemos utilizar um loop for e dentro desse loop utilizar uma estrutura de condição verificando se Ferro está na lista. Se estiver, então queremos que o programa ignore esse minério. Vamos como isso funciona:
minerios = ['Diamante', 'Ouro', 'Ferro', 'Cobre']
for minerio in minerios:
    if minerio == 'Ferro':
        continue
    print(minerio)
# Vamos entender esse código. Criamos uma lista e dentro dela possui minérios. Em seguida utilizamos o loop for, para iterar sobre cada elemento. Dentro deste loop for, utilizamos uma estrutura de condição para verificar se o elemento que estamos iterando é Ferro. Se o elemento for ferro, então simplesmente ignoramos esse elemento e a repetição retorna ao início, verificando se o elemento é ferro novamente, se não for, apenas imprime o minério. A saída desse código é a seguinte:
"""
Diamante
Ouro
Cobre
"""

# Tópicos avançados
# Vamos supor que você está iterando uma lista, e quer verificar se algum elemento está na lista. Você utiliza uma condição para verificar e quando verifica, o elemento dentro da lista era maiúsculo, e você utilizou letras minúsculas. Veja o exemplo a seguir:
produtos = ['Fone', 'Celular', 'Tablet', 'Computador']
for produto in produtos:
    if produto == 'celular':
        print('Achei um celular!')
# Aqui há um grande problema. Repare que na lista, celular está com sua primeira letra em maiúsculas ('Celular') e você está verificando se 'celular' (em minúsculas) está na lista produtos. Não vai ter nenhuma saída, pois 'Celular' é diferente de 'celular'. Por sorte podemos utilizar uma função de strings para converter todos os produtos em minúsculas, o lower(). O código ficaria assim:
produtos = ['Fone', 'Celular', 'Tablet', 'Computador']
for produto in produtos:
    produto = produto.lower()
    if produto == 'celular':
        print('Achei um celular!')
# Agora sim. O que foi alterado nesse código é que antes de tudo, convertemos todos os produtos da lista para minúsculas, e em seguida, verificamos se celular está na lista. Veja como a função lower() é muito importante.


# Operador ternário
# Se você analisar uma estrutura condicional com o if, elif e o else, notará que eles utilizam muitas linhas de código. Foi pensando nisso que foi criado o operador ternário, prometendo diminuir mais linhas, e fazer a mesma coisa mas em apenas UMA LINHA! Sua sintaxe é um pouco diferente de uma estrutura condicional utilizando o if. Vamos ver como funciona:
# Sintaxe:
# 'valor verdadeiro' if True else 'valor falso'
print('Verdadeiro' if True else 'Falso')
# Ok, vamos entender esse código. Primeiro dizemos o que é para imprimir se a condição for True, nesse caso, utilizamos 'Verdadeiro' Ou seja, será imprimido 'Verdadeiro' se True == True. Mas se for falso, então executará o que vem logo após o else, ou seja, imprimirá 'Falso'. Vamos ver mais um exemplo e comparar com uma condição if:
pet = True
# Estrutura condicional
if pet:
    print('Possui um pet')
else:
    print('Não possui um pet')

# Operador ternário
print('Possui um pet' if pet else 'Não possui um pet')
# O código se lê assim:
# Imprima 'possui um pet' se pet for True, se não, imprima 'Não possui um pet'. Neste caso, pet é True, então executará 'Possui um pet'. Vamos ver mais um exemplo


idade = 151
if idade < 18:
    print('Jovem')
else:
    print('Adulto')

print('Jovem' if idade < 18 else 'Adulto')
# Vamos entender: O programa imprimirá 'Jovem' se idade for menor que 18, mas se idade não for menor que 18, isso é, se idade for maior que 18, então imprimirá 'Adulto'. Os operadores ternário possuem uma sintaxe bem menor se comparado a uma estrutura condicial tradicional, não é mesmo? Vamos a mais alguns exemplos
luz = True
ternario = 'luz acessa' if luz else 'luz apagada'
print(ternario) # 'luz acessa'