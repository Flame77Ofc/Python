# Revisão python
def inicio():
    # f-strings
    # f-strings é uma nova maneira "recente" do python de escrever strings com variáveis
    # jeito antigo: concatenação
    frutas = 15
    print("Tenho " + str(frutas) + " frutas")  # Tenho 15 frutas

    # f-strings: É adicionado um f após o parênteses de abertura e escrito a variável entre chaves.
    print(f"Tenho {frutas} frutas")  # Tenho 15 frutas

    # Comentários
    """
    Comentários em python são trechos do código onde o programa não executará um código.
    São usados os hashtags antes do texto que deseja comentar
    Principais beneficíos e pra que servem:
    - Explicar uma parte do código
    - "Desativar" um código
    - Serve como lembrança para mais tarde, alguma tarefa pendente ou todo (que será apagado mais tarde)
    """

    # Exemplos
    # Explicação de um código
    print("Olá, Mundo!")  # Imprime "Olá, Mundo!" na tela

    # Desativar um código
    # if True:
    #     print("Bloco de código verdadeiro")
    # else:
    #     print("Bloco de código Falso")

    # Lembrete como um todo
    # Lembrar de finalizar essa parte do código depois do almoço
    horario = 15
    if horario >= 12 and horario <= 13:
        print("De Tarde")

    # Existe também comentários para múltiplas linhas, também chamados de docstrings.
    # Uma docstring funciona assim: Linhas e linhas são preenchidas por 3 aspas simples/duplas no começo e 3 aspas simples/duplas são preenchinas no final da linha desejada. As aspas devem ser coincidir.
    # Exemplos

    """
    Aqui está um exemplo de uma docstring
    com aspas duplas
    e 6 linhas de código
    sem a necessidade de usar inúmeros hashtags
    """

    '''
    E aqui, está outro exemplo de uma docstring
    porém, desta vez, utilizando aspas simples
    e com 6 linhas, criamos uma docstrings
    e evitamos a poluição de hashtags
    '''

    # Ajuda!
    # O python possui uma palavrinha especial quando o usuário tiver alguma dúvida a respeito sobre algo dentro do python.
    # A palavra mágica utilizada é o help(). Dentro dos parênteses é inserido algo como: print, int, any, all, True, etc...
    help(print)
    help(classmethod)
    help(help)



def tipos_de_dados():
    """
    Em python, existem 4 tipos de dados principais.

    São eles:
    - str (String): Caractere, é um tipo de dado para textos, delimitados por aspas simples ('string') ou aspas duplas ("string")

    - int (Inteiro): Inteiro, é um tipo de dado especialmente para números inteiros sem casas decimais, sem números após a vírgula

    - float (Flutuante): Flutuante ou Decimal, é um tipo de dado para números de ponto flutuante com casas decimais, possuindo números após a vírgula.

    - bool (Booleano): Booleanos, é um tipo de dado que existem apenas dois valores a serem preenchidos: True (verdadeiro) e False (falso)
    """

    # Exemplo (Sem estarem dentro de variáveis - próximo assunto)
    "Rafael"  # Tipo de dado string (str)
    'Revisão Python'  # Tipo de dado string (str)

    45  # Tipo de dado inteiro (int)
    945985498320459032  # Tipo de dao inteiro (int)

    12.5  # Tipo de dado flutuante/decimal (float)
    3.141592653589793  # Tipo de dado flutuante/decimal (float)

    True  # Tipo de dado booleano (bool)
    False  # Tipo de dado booleano (bool)

    # Que tipo é esse?
    # As vezes, podemos esquecer o TIPO de um dado. É justamente por isso que existe a função type("dado").
    # A função type() nos retorna o tipo de um dado, que pode ser passado como argumento uma variável.
    # O texto nos retornará algo como: <class 'tipo_de_dado'>. O que nos importa é apenas o tipo de dado, sem ser a class.
    tipo_desconhecido = "Opps! Esqueci o que isso é!"
    print(type(tipo_desconhecido))  # <class 'str'>

    tipo_desconhecido = classmethod
    print(type(tipo_desconhecido))  # <class 'type'>
    
    tipo_desconhecido = abs
    print(type(tipo_desconhecido)) # <class 'builtin_function_or_method'>

tipos_de_dados()


def variaveis():
    """
    Variáveis são minúsculos espaços localizados na memória do computador, e sua finalidade é guardar dados.
    """

    # Com anotação de tipo
    string: str = "String"
    inteiro: int = 15
    flutuante: float = 10.5
    booleano: bool = True
    booleano: bool = False

    # Sem anotação de tipo
    string = "String"
    inteiro = 15
    flutuante = 10.5
    booleano = True
    booleano = False

    # Exemplo
    nome: str = "João"
    idade: int = 21
    saldo: float = 13450.99
    tem_pet = True

    print(f"Meu nome é {nome}, tenho {idade} anos, e tenho mais de R${saldo} no meu banco! {"Também tenho um pet!" if tem_pet else "E infelizmente não tenho nenhum pet."}")


def constantes():
    """
    Constantes são semelhantes às variáveis, porém servempara armazenar dados que não se modifiquem ao longo do programa.
    A diferença visual em uma constante em relação a uma variável é que são escritas em upper_case. upper_case é um modo de escrita, que indica que devem seguir o padrão de serem escritas todas em maiúsculas.
    """

    PI = 3.1415  # O PI é uma constante na matemática, por isso podemos definir com uma constante em python também.
    VELOCIDADE_DA_LUZ = 299792458  # A velocidade da luz não muda, então é uma constante.
    GRAVIDADE = 9.81  # A gravidade (da terra) também não muda.
    DIAS_DA_SEMANA = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"]  # Os dias da semana não mudam, não existe Sétima-Feira para algum dia do mês.
    LIMITE_DE_TENTATIVAS = 5  # O número de tentativas de um jogo, por exemplo, não muda.
    FILE = "main.py"  # O nome de um arquivo também não muda (desde que você não altere)


def operadores():
    """
    Existem uma grande quantidade de operadores, e são divididos em pequenos tópicos.

    - Operadores Aritméticos
        Operadores aritméticos são responsáveis por fazer cálculos com números.
        É a matemática pura aplicada em python.
        - + Adição (Retorna a soma entre dois números)
        - - Subtração (Retorna a subtração entre dois números)
        - * Multiplicação (Retorna a multiplicação entre dois números)
        - / Divisão (Retorna a divisão entre dois números e retorna um float)
        - // Divisão inteira (Retorna a divisão entre dois números e retorna um inteiro)
        - % Módulo (Retorna o resto da divisão entre dois números. Por exemplo: 2/5, o módulo seria 1 (resto, o que sobrou da divisão))
        - ** Exponenciação ou Potenciação (Retorna a potenciação de um número elevado a ele mesmo tal quantidade de vezes)

    - Operadores de Atribuição
        Operadores de atribuição são responsáveis por atribuir um novo valor a uma nova variável.
        Importante dizer: A atribuição serve para atribuir a uma variável um novo valor, então é necessário:
        1. Já existir uma variável declarada anteriormente (so não é exigido isso para a atribuição simples)
        2. Entender que por exemplo, uma variável pets = 15. Se eu declaro pets + 5 e imprimo na tela, irá mostrar ainda 15, pois
        não atribuímos a essa variável um novo valor, apenas declaramos uma expressão que não faz diferença. Declarar print(pets + 5) resultará
        em 20, porém a variável pets ainda terá o valor de 15. Para incrementar o valor de pets, precisamos declarar pets += 5, por exemplo.
        Agora, pets passa a ser 20, e se imprimimos print(pets), resultará em 20.
        - = Atribuição Simples (Atribui um valor a uma variável)
        - += Atribuição com adição (Soma o valor da direita com o valor da variável)
        - -= Atribuição com subtração (Subtrai o valor da direita com o valor da variável)
        - *= Atribuição com multiplicação (Multiplica o valor da direita com o valor da variável)
        - /= Atribuição com divisão (Divide o valor da direita com o valor da variável)
        - //= Atribuição com divisão inteira (Divide como inteiro o valor da direita com o valor da variável)
        - %= Atribuição com resto (Atribui o resto do valor da direita com o valor da variável)
        - **= Atribuição com potenciação (Eleva o valor atual da variável à potência do valor à direita e atribui o resultado)

    - Operadores de Comparação
        Operadores de comparação são justamente para comparar um par de dois valores, um na direita e outro na esquerda.
        Estes operadores sempre retornarão um valor booleano.
        - == Igual a (Compara se o valor da esquerda é igual ao valor da direita)
        - != Diferente de (Compara se o valor da esquerda é diferente do valor da direita)
        - > Maior que (Compara se o valor da esquerda é maior que o valor da direita)
        - < Menor que (Compara se o valor da esquerda é menor que o valor da direita)
        - >= Maior ou igual que (Compara se o valor da esquerda é maior ou igual que o valor da direita)
        - <= Menor ou maior que (Compara se o valor da esquerda é menor ou igual que o valor da direita)

    - Operadores lógicos
        Operadores lógicos comparam duas expressões. Operadores lógicos também, assim como os de comparação, retornam
        um valor booleano, dizendo se as duas expressões são verdadeiras ou falsas.
        - and (Compara se a 1a expressão E a 2a expressão são verdadeiras ou falsas)
        - or (Compara se a 1a expressão OU a 2a expressão são verdadeiras ou falsas)
        - ! (not) (Nega uma expressão. Se a expressão era verdadeira, passa a ser falsa, e vice-versa)
    """

    # Aritméticos
    # Adição
    12.3 + 5  # 17
    45.0 + 4362.322  # 4407.322
    34.312 + 1  # 35.312

    # Subtração
    34 - 5.8  # 28.2
    12 - 45  # -33
    456.34 - 123.34  # 333.0

    # Multiplicação
    3 * 15  # 45
    7 * 35  # 245
    1245.4 * 500  # 622700.0

    # Divisão
    15 / 3  # 5.0
    45 / 5  # 9.0
    714 / 654  # 1.091743119266055

    # Divisão inteira
    2 // 7  # 0
    10 // 3  # 3
    510 // 90  # 5

    # Módulo/Resto
    12 % 5  # 2
    27 % 4  # 3
    54 % 2  # 0

    # Exponenciação/Potenciação
    16 ** 4  # 65536
    2 ** 3  # 8
    750 ** 5  # 237304687500000


    # Atribuição
    # Atribuição simples
    carros = 3
    casas = 9
    pessoas = 54100000

    # Atribuição com adição
    tijolos = 5
    tijolos += 15
    # tijolos agora são 20, pois 15 + 5 = 20

    # Atribuição com subtração
    frutas = 25
    frutas -= 20
    # frutas agora são 5, pois 25 - 20 = 5

    # Atribuição com multiplicação
    alunos = 30
    alunos *= 2
    # alunos agora são 60, pois 30x2 = 60

    # Atribuição com divisão
    bonecas = 50
    bonecas /= 5
    # bonecas agora são 10.0, pois 50 / 5 = 10

    # Atribuição com divisão inteira
    cores = 153
    cores //= 5
    # cores agora são 30, pois 153 / 5 = 30..., porém aceita apenas inteiros

    # Atribuição com exponenciação
    saldo = 50
    saldo **= 3
    # saldo agora é 125000, pois 50³ = 50x50x50 = 125000


    # Comparação
    # Igual a
    15 == 3  # False, 15 não é igual a 3
    26 == 45  # False, 26 não é igual a 45
    32 == 32  # True, 32 é igual a 32

    # Diferente de
    341 != 340.999  # True, 341 é diferente de 340.999
    6500 != 6500  # False, 6500 não é diferente de 6500
    451 != 450.99999999999999  # False, floats com GRANDIOSOS números após a vírgula são convertidos para um valor a cima

    # Maior que
    12 > 5  # True, 12 é maior que 5
    65 > 3  # True, 65 é maior que 3
    45 > 450  # False, 45 não é maior que 450

    # Menor que
    45 < 10  # False, 45 não é menor que 10
    12 < 8  # False, 12 não é menor que 8
    28 < 45  # True, 28 é menor que 45

    # Maior ou igual que
    35 >= 45  # True, 35 é maior (mas não igual) que 45
    12 >= 12  # True, 12 é igual (mas não maior) a 12
    45 >= 46  # False, 45 não é maior nem igual a 46

    # Menor ou igual que
    12 <= 5  # False, 12 não é maior nem igual a 5
    56 <= 56  # True, 56 é igual (mas não menor) a 56
    128 <= 54  # False, 128 não é maior nem igual a 54


    # Lógicos
    # A seguir, teremos algumas expressões, e verificaremos usando os operadores lógicos: and, or e not
    # and: Verifica se ambos as expressões são verdadeiras, e retorna um valor booleano - True (verdadeiro) ou False (falso)
    expressao1 = 12 > 5
    expressao2 = 5 < 6
    expressao1 and expressao2  # True, ambas expressões são verdadeiras

    expressao1 = 1 > 2
    expressao2 = 5 == 5
    expressao1 and expressao2  # False, apenas a segunda expressão é verdadeira

    expressao1 = "joao" == "joao"  # É possível comparar strings!
    expressao2 = 45 > 3
    expressao1 and expressao2  # True, ambas expressões são verdadeiras

    expressao1 = 5 > 2 if True else 3 > 6  # True, compara se 5 > 2
    expressao2 = 40 > 5 if False else 8 > 40  # False, compara se 8 > 40
    expressao1 and expressao2  # False, apenas uma expressão é True

    # or: Verifica se apenas uma expressão for verdadeira, e retorna um valor booleano - True (verdadeiro) ou False (falso)
    expressao1 = 5 > 6
    expressao2 = 12 == 12
    expressao1 or expressao2  # True, expressao1 é False, expressao2 é True

    expressao1 = 5 > 7
    expressao2 = 6 > 9
    expressao1 or expressao2  # False, ambas expressões são falsas

    expressao1 = "admin" != "owner"
    expressao2 = 76 + 5 > 80
    expressao1 or expressao2  # True, ambas expressões são verdadeiras

    expressao1 = 15 > 6 if True else 12 < 5
    expressao2 = 6 < 2 if False else 4 < 5
    expressao1 or expressao2  # True, ambas expressões são verdadeiras

    # not: Nega um expressão. Caso uma condição que antes, era verdadeira, agora passa a ser falsa e vice-versa
    expressao = not (5 > 6)  # Antes era False, agora é True
    expressao = not(4500 != 4510)  # Antes era True, agora é False
    expressao = not(15 / 3 >= 5)  # Antes era True, agora é False



def listas():
    """
    Listas são um dos 4 conjuntos em python. É o conjunto mais utilizado, por ser flexível.

    Listas são:
    - Mutáveis (É possível modificar seus elementos por meio de métodos)
    - Ordenadas (Possuem uma ordem definida)
    - Duplicadas (Aceitam elementos duplicados)
    """

    # Com anotação de tipo
    lista: list = []

    # Sem anotação de tipo
    lista = []

    # Métodos
    # append("elemento"): adiciona um elemento no fim da lista;
    # remove("elemento"): remove o elemento especificado;
    # pop(): remove o último elemento da lista;
    # clear(): limpa toda a lista, isso é, remove todos os elementos e deixa vazia;
    # insert(posicao: int, "elemento"): adiciona um elemento especifico na posição especifica;
    # sort(): Ordena a lista;
    # reverse(): Inverte todos os elementos da lista (O último é o primeiro e vice-versa);
    # index("elemento"): Retorna a posição do elemento na lista, mas ocorrerá erro caso não exista;
    # count("elemento"): Retorna a quantidade de vezes que o elemento aparece na lista, 0 caso não exista;

    frutas = ["Maçã", "Abacaxi", "Pêra", "Laranja"]
    frutas.append("Limão")  #  ['Maçã', 'Abacaxi', 'Pêra', 'Laranja', 'Limão']
    frutas.append("Tangerina")  #  ['Maçã', 'Abacaxi', 'Pêra', 'Laranja', 'Limão', 'Tangerina']

    frutas.remove("Maçã")  # ['Abacaxi', 'Pêra', 'Laranja', 'Limão', 'Tangerina']
    frutas.pop()  #  ['Abacaxi', 'Pêra', 'Laranja', 'Limão']
    frutas.clear()  #  []

    frutas.insert(12, "Morango")  # ['Morango']  (Nesse caso adicionou na primeira posição, pois não existia posição 12)
    frutas.append("Banana")  # ['Morango', 'Banana']
    frutas.append("Maracujá")  # ['Morango', 'Banana', 'Maracujá']
    frutas.append("Laranja")  # ['Morango', 'Banana', 'Maracujá', 'Laranja']

    frutas.sort()  # ['Banana', 'Laranja', 'Maracujá', 'Morango']
    frutas.reverse()  # ['Morango', 'Maracujá', 'Laranja', 'Banana']

    print(frutas.index("Banana"))  # 3
    print(frutas.count("Banana"))  # 1

    print(frutas)  # ['Morango', 'Maracujá', 'Laranja', 'Banana']


def tuplas():
    """
    Tuplas são um dos conjuntos em python. Tuplas são utilizadas raramente, em um contexto muito peculiar.

    Tuplas são:
    - Ordenadas (Possuem uma ordem definida)
    - Imutáveis (Não é possível alterar os elementos de uma tupla com métodos)
    - Duplicadas (Aceitam valores duplicados)

    Curiosidade: Tuplas são formadas por parênteses, porém, para criar uma tupla,
    não é necessário usar parênteses, uma tupla pode ser escrita apenas com seus
    elementos e cada separado por vírgulas.
    """

    tupla: tuple = ()
    tupla = ()

    tupla = ("elemento1", "elemento2")  # Isso é uma tupla
    tupla = ("elemento1")  # Isso é uma tupla
    tupla = "elemento1", "elemento2"  # Isso é uma tupla
    tupla = "elemento1",  # Isso é uma tupla, pois possui uma vírgula, por mais estranho que pareça
    tupla = "elemeto1"  # Isso não é uma tupla, é uma variável do tipo str (string)

    # Métodos: Tuplas possuem apenas dois métodos, mas estes não alteram a tupla, apenas retornam uma informação.
    # count("elemento"): Retorna a quantidade de elementos que o elemento especificado aparece na tupla
    # index("elemento"): Retorna em qual posição da tupla o elemento especificado está localizado na tupla
    profissoes = ("Engenheiro", "Astronauta", "Cientista", "Programador")
    print(profissoes.count("Astronauta"))  # 1
    print(profissoes.index("Programador"))  # 3


def sets():
    """
    Sets são um dos conjuntos em python. São menos utilizadas, pois sets tem consigo algumas funcionalidades bem especificas que funcionam num momento certo, mas em outro não.

    Sets são:
    - Mutáveis (É possível modificar seus elementos por meio de métodos)
    - Não ordenados (Não possuem uma ordem definida - seus elementos são "embaralhados")
    - Não duplicados (Não aceitam elementos duplicados)
    """

    # Cuidado: Definir um set vazio pode ser considerado um dicionário (um outro conjunto em python)
    meu_set: set = set()
    meu_set = set()


    # Métodos
    # add("elemento"): adiciona um elemento numa posição aleatória, pois um set é desordenado.
    # remove("elemento"): remove um elemento especifico
    # pop(): remove um elemento aleatório
    # clear(): limpa todos os elementos do set

    nomes = {"Felipe", "Maria", "João", "Felipe", "João"}
    print(nomes)  # {'João', 'Felipe', 'Maria'} -> Não aceitam elementos duplicados e não possuem ordem!

    nomes.add("Fernando")  # {'Fernando', 'João', 'Felipe', 'Maria'}
    nomes.remove("Maria")  # {'Felipe', 'João', 'Fernando'}
    nomes.clear()  # set()

    nomes.add("Fernanda")  # {'Fernanda'}
    nomes.add("Tiago")  # {'Tiago', 'Fernanda'}
    nomes.add("Lucas")  # {'Tiago', 'Fernanda', 'Lucas'}


def dicionarios():
    """
    Dicionários é um dos conjuntos em python, e organiza seus elementos com chaves, semelhantes aos sets.
    Dicionários possuem pares de chaves e valores, que são separados pelo sinal de dois pontos (:)
    Dicionários são:
    - Ordenados (Possuem uma ordem definida)
    - Mutáveis (É permitido modificar e alterar um dicionários através de métodos)
    - Não duplicados (Não aceitam CHAVES duplicadas)

    sintaxe básica
    dicionario = {
    "chave": "valor"
    }
    """

    # Exemplo do dia a dia
    # Luiz é quem cadastra as pessoas num hotel. Ele fica na recepção todos os dias, fazendo cadastros e de vez em quando verificando e checando o hotel em um todo. Podemos fazer uma simulação do trabalho de Luiz usado Python.
    preco_diario = 0
    hotel = {
        "numero do aparamento": {
            "numero de pessoas": 0,
            "nomes": [],
            "idades": [],
            "dias": 0 * preco_diario
        }
    }

    # Preenchendo com informações simuladas, teriamos algo como:
    preco_diario = 670
    hotel = {
        145: {
            "numero de pessoas": 5,
            "nomes": ["Felipe", "Maria", "Lucas", "Gustavo", "José"],
            "idades": [13, 45, 8, 21, 52],
            "preço": 7 * preco_diario
        },

        315: {
            "numero de pessoas": 2,
            "nomes": ["Fernando", "Julia"],
            "idades": [34, 29],
            "preço": 28 * preco_diario
        }
    }

    print(hotel)
    # Luiz pode usar métodos para verificar informações mais rapidamente.
    # Imprimindo partes especificas
    numero_pessoas_apartamento1 = hotel[145]["numero de pessoas"]
    numero_pessoas_apartamento2 = hotel[315]["numero de pessoas"]
    print(f"Número de pessoas totais: {numero_pessoas_apartamento1 + numero_pessoas_apartamento2}") # Número de pessoas totais: 7

    # Iteração
    # Retorna as chaves
    for chave in hotel.keys():
        print(chave)

    # Retorna os valores das chaves
    for valor in hotel.values():
        print(valor)

    # Retorna ambos chaves e valores
    for chave, valor in hotel.items():
        print(chave, valor)


dicionarios()




def estruturas_de_condicao():
    """
    As estruturas de condição ou simplesmente condicionais, são estruturas que executam um bloco de código baseado na sua condição. Um bloco será apenas executado caso a condição seja verdadeira.

    Exemplo do dia a dia:
    Está chovendo.
    Se estiver chovendo, eu levo um guarda-chuva
    Se não estiver chovendo, eu não levo um guarda-chuva.

    É possível verificar uma condição quantas vezes forem necessárias, seja uma vez, duas, ou... Infinitas!

    Sintaxe
    if condicao:
    <bloco de código>
    else:
    <bloco de código>
    """

    # Exemplo simples com uma condicional 
    chovendo = True
    if chovendo == True:
        print("Está chovendo")
    # Saída: Está chovendo

    # Exemplo simples com duas condicionais
    pets = 5
    if pets > 0:
        print("Tem ao menos um pet")
    else:
        print("Não tem pets")
    # Saída: Tem ao menos um pet

    # Exemplo com elif
    frutas = 0
    if frutas > 15000:
        print("Tem mais de 15 mil frutas")
    elif frutas <= 1 and frutas >= 15000:
        print("Tem entre 10 mil frutas a 15 mil frutas")
    else:
        print("Não tem nenhuma fruta")
    # Saída: Não tem nenhuma fruta


    # Condicionais aninhadas
    # São condicionais dentro de outras condicionais, há uma hierarquia, como uma árvore, uma família (pais e filhos)
    idade = 15
    altura = 1.65

    if idade >= 12:
        if altura >= 1.55:
            print("Acesso Liberado")
        else:
            print("Altura insuficiente")
    else:
        print("Deve ter ao menos 12 anos")
    # saída: Acesso Liberado

    nome = "owner"
    senha = "owner"

    if nome == "admin":
        if senha == "admin":
            print("Acessado liberado. Bem-vindo ao Banco!")
        else:
            print("Acesso negado, senha incorreta")
    else:
        print("Acesso negado, nome incorreto")

    # Caso você algum dia precisa verificar alguma variável booleana, não é necessário usar a comparação de igualdade.
    # Imagine que tenhamos a variável "lampada", que é uma variável booleana e queremos verificar se é True ou False.
    # Primeiro Jeito: Verificar se lâmpada é True
    lampada = True
    if lampada == True:
        print("A lâmpada está acessa")
    else:
        print("A lâmpada está apagada")

    # Primeiro Jeito: Verificar se lâmpada é False
    if lampada == False:
        print("A lâmpada está apagada")
    else:
        print("A lâmpada está acessa")

    # Podemos simplificar isso sem usar a comparação de igualdade.
    # Segundo jeito e mais recomendado: Verificar se lâmpada é True
    lampada = True
    if lampada:
        print("A lâmpada está apagada")
    else:
        print("A lâmpada está acessa")

    # E Segundo jeito: Verificar se lâmpada é False
    if not lampada:
        print("A lâmpada está apagada")
    else:
        print("A lâmpada está acessa")


    # Operador Ternário
    # O operador ternário é uma simplificação para uma estrutura condicional. Funciona perfeitamente para duas condições, apenas em uma linha. É possível verificar múltiplas condições, porém é necessário fazer uma gambiarra, e é algo difícil de comprrender. Neste caso, quando é necessário utilizar mais de 2 comparações, utilize o if, elif, else.
    # Sintaxe
    # <bloco de código verdadeiro> if condição else <bloco de código falso>
    cor = "Azul"
    ternario = "A cor é azul" if cor == "Azul" else "A cor não é azul"
    print(ternario) # A cor é azul

    # comparação com uma condicional simples
    cor = "Azul"
    if cor == "Azul":
        print("A cor é azul")
    else:
        print("A cor não é azul")


def estruturas_de_repeticao():
    """
    Estruturas de repetição são excelentes para repetir um bloco de código, pois é exatamente isso que fazem.
    Existe o loop while e o loop for.
    O loop for é o mais utilizado, pela sua sintaxe e sem necessidade de flags.

    Loop: um loop é uma repetição.
    Flag: um flag é uma variável que altera de valor a cada repetição que a estrutura de repetição executar.

    Nos loops, assim como nas condicionais, utilizamos uma condição para verificar se a estrutura de repetição vai executar ou não.
    Diferentemente das condicionais, loops executam uma bloco de código ENQUANTO a condição for verdadeira.

    Exemplo do dia-a-dia
    João foi ao supermercado e estava precisando de 15 sabonetes. João se aproximou de uma prateleira de sabonetes, e coletou uma a uma, seguindo a seguinte lógica:
    "Tenho 0 sabonetes, e enquanto eu não tiver 15 sabonetes, vou pegando mais um sabonete, e contando os sabonetes."
    João começa a coletar os sabonetes e colocar na cesta, ele começa: Peguei um sabonete, coloquei na cesta. Peguei dois sabonetes, coloquei na cesta. Peguei quatro, cinco, seis... doze, treze, quatorze sabonetes e coloquei na cesta. Peguei 15 sabonetes, coloquei na cesta e pronto, tenho 15 sabonetes.
    Essa é a mesma lógica que pode ser aplicada em uma estrutura de repetição.
    """

    # Loop While
    # o loop while funciona com uma flag, uma variável que muda de valor a cada repetição. Vamos ver um exemplo prático do João.
    sabonetes = 0  # João não tinha nenhum sabonete
    while sabonetes < 15:  # Enquanto sabonetes for menor que 15:
        sabonetes += 1  # Aumentamos a variável sabonete em 1 a cada repetição que o while completar
        print(f"Peguei + 1 sabonete, agora tenho {sabonetes} sabonetes")  # Imprime o valor dos sabonetes

    """
    Peguei + 1 sabonete, agora tenho 1 sabonetes
    Peguei + 1 sabonete, agora tenho 2 sabonetes
    ...
    Peguei + 1 sabonete, agora tenho 14 sabonetes
    Peguei + 1 sabonete, agora tenho 15 sabonetes
    """

    # Exemplo do dia a dia
    # Maria foi abastecer seu carro. Chegou no posto de gasolina, o funcionário do posto perguntou a quantidade de litros de gasolina. Maria respondeu: 45 litros, e então o funcionário começou a encher. Podemos simular isso em python, com o while.
    litros_gasolina = 0
    while litros_gasolina <= 45:  # Enquanto litros de gasolina for menor ou igual a 45:
        print(f"Litros abastecidos: {litros_gasolina}")  # Imprime a quantidade de litros para visualizar
        litros_gasolina += 5  # Incrementamos +5 a variável litros de gasolina

    """
    Saída:
    Litros abastecidos: 0
    Litros abastecidos: 5
    Litros abastecidos: 10
    ...
    Litros abastecidos: 35
    Litros abastecidos: 40
    Litros abastecidos: 45
    """


    # Exemplo de um jogo
    # Felipe está jogando Mario. Felipe está em primeira colocação no ranking do jogo.
    # O objetivo de Felipe é coletar o máximo de moedas possíveis. Podemos fazer algo semelhante no python, ou em outras palavras, simular o jogo do Mario com as moedas.
    moedas = 0  # Felipe inicia toda partida com 0 moedas
    sobreviveu = True  # Indica se o Felipe sobreviveu durante a partida e não morreu para nenhum objeto do jogo
    while moedas <= 50 and sobreviveu:  # Enquanto moedas for menor ou igual que 50 e sobrevieu for verdadeiro:
        print(f"Moedas coletadas: {moedas}")  # Imprime a quantidade de moedas coletadas
        moedas += 1  # Incrementa + 1 na variável moedas a cada repetição

    """
    Saída:
    Moedas coletadas: 0
    Moedas coletadas: 1
    Moedas coletadas: 2
    ...
    Moedas coletadas: 49
    Moedas coletadas: 50
    """






