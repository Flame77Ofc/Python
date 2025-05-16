# Listas são sequências ordenadas e mutáveis (É possível alterar seus elementos) e possuem índices. Seus elementos são cercados por colchetes [] e cada elemento é separado por vírgulas. O índice é o identificador de um elemento, e começa do 0 até a quantidade de elementos - 1. Por exemplo, se uma lista tem 50 elementos, o primeiro índice será 0 e o último será a quantidade -1, que é 49.
# sintaxe básica
# lista = ['e1', 'e2', 'e3']

lista = ['elemento1', 'elemento2', 'elemento3']
# índices:    0            1            2
# Acessando os elementos pelo índice
# Para acessar um elemento pelo seu índice, basta seguir a seguinte sintaxe:
# nome_da_lista[índice]
# Sabendo que os índices inciam em 0, vamos tentar acessar o elemento1 utilizando o seu índice:
print(lista[0]) # elemento1
# Acessando o elemento 2, que está no índice 1
print(lista[1])
# Acessando o elemento 2, que está no índice 2
print(lista[2])

# Você também pode acessar todos os elementos de uma lista apenas pelo seu nome
print(lista)

# Listas também aceitam diferentes tipos de dados
lista = ['Pedro', 15, True, 'Maria', False]
# índices  0       1    2      3        4
lista[1]

# Verificando qual o maior e o menor item da lista com a função max e min
# Vamos supor que você tem uma lista de vendas e quer procurar qual o maior e a menor venda da lista. Você pode fazer isso manualmente, mas dependendo do tamanho da lista, pode ficar incontável. Por isso que servem as funções max() e min(). Vamos ver como elas funcionam.
vendas = [120, 456, 123, 986, 965, 329, 943, 542, 239, 236, 823, 967, 327, 432, 534, 976, 321, 743, 658, 735, 885, 364, 785, 984, 651, 798]
# Essa lista é relativamente grande, e é difícil achar o maior número logo de cara, então vamos utilizar a função max:
# sintaxe:
# max(lista)
print(max(vendas))
# Bem fácil, não é? Agora como achar o menor número da lista? Vamos ver como funciona o min:
# sintaxe: min(lista)
print(min(vendas))
# Bem fácil também! que tal ver mais um exemplo?

# Queremos achar a maior idade e a menor idade nesta lista:
idades = [34, 12, 43, 65, 86, 87, 21, 33, 43, 90, 32, 43, 45, 15, 56, 23, 54, 43, 7, 8]
# Já sabe como fazer?
print(max(idades)) # Imprimindo o maior elemento
print(min(idades)) # Imprimindo o menor elemento


# Também é possível somar os elementos de uma lista, sim!!! Vamos ver como funciona:
# Vamos supor que você tem a tarefa de somar todas as notas de 15 alunos de uma escola, uma tarefa bem fácil! Vamos ver:
notas = [8, 9, 1, 4, 5, 6, 7, 4, 4, 5, 7, 10, 2, 4, 8]
# para somar todos os valores, utiliza-se a função sum(lista):
soma = sum(notas)
# Muito fácil também, concorda??


# QUANTIDADE DE ELEMENTOS: função len()
# Imagine que você tenha uma lista gigantesca, e você quer saber a quantidade de elementos que ela possui. É justamente isso que a função len faz!
# Veja essa lista:
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana", "Karine", "Lucas", "Maria" "Nicolas", "Olivia", "Patrick", "Quezia", "Rafael", "Sofia", "Tiago", "Ursula", "Vitória", "William", "Xuxa", "Yasmin", "Zeca", "Amanda", "Bruna", "Caio"]
# Muitos itens, não é mesmo? Mas podemos descobrir rapidinho utilizando a função len:
quantidade = len(nomes)
print(quantidade)

# vejamos outro exemplo:
personagens = ['Bob', 'Patrick', 'Siri Cascudo', 'pirata do caribe', 'lula molusco']
print(len(personagens))


# Vamos supor que você quer acessar o último elemento de uma lista, mas a lista é gigante. É aí que entram os índices negativos.
# índices negativos são iguais aos índices positivos normais mas agora ocorre uma inversão. O último índice é o -1 e o primeiro depende de quantos elementos uma lista tem. Vamos criar a seguite lista:
cores = ['vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'violeta', 'roxo', 'marrom', 'preto', 'branco', 'cinza', 'rosa', 'bege']
# negativos  -13       -12         -11      -10       -9        -8       -7       -6        -5       -4       -3       -2      -1
# a lista é enorme, e você quer acessar o último elemento, o bege.
# para isso, basta colocar o índice -1, pois -1 sempre será o último elementod de toda e qualquer lista, não importa o seu tamanho.
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
# veja a seguinte lista:
estados_sul = ['Paraná', 'Rio Grande do Sul']
# Está faltando Santa Catarina, então vamos adicionar utilizando a função append
# sintaxe:
# lista.append('elemento')
estados_sul.append('Santa Catarina')
# Siples demais! Mas uma coisa importante a lembrar é que a função append sempre adiciona os elementos no último índice ou seja, após adicionar um elemento, esse elemento passa a ser o último elemento
# Vamos ver outros exemplos
IAs = ['ChatGPT', 'DeepSeek', 'Grok']
# Queremos adicionar Sider, já sabe como?
IAs.append('Sider')
# Moleza!

# E também podemos adicionar elementos no índice que quisermos!
# A função insert te permite adicionar um elemento no índice que desejar, mas sem substituir o elemento que estava naquele índice.
# Veja alguns exemplos:
mamiferos = ['Baleia', 'Morcego']
#indices        0          1
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
intrusor = fila[1] = 'Intrusor' # Uma coisa que deixei passar é que você pode também criar variáveis nesse tipo de situação, e é a mesma coisa



# Juntando listas
# Já pensou juntar listas para criar uma nova lista? Com o python isso é possível, utilizando a função extend! Vamos ver como funciona!
# Vamos supor que temos duas listas, e queremos unir todas em apenas uma, veja o exemplo:
# sintaxe básica:
# lista1.extend(lista2)
planetas = ['Terra', 'Marte', 'Vênus']
estrelas = ['Sol', 'Sagittarius A']
planetas.extend(estrelas)
# A lista de planetas agora há planetas e estrelasm ficando assim: ['Terra', 'Marte', 'Vênus', 'Sol', 'Sagittarius A']

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

# Vamos ver para números
numeros = [4, 8, 12, 5, 9, -4, 0, 5, 6, -6, 120, 450, 32, 21, 7]
numeros.sort() # Lista organizada
print(numeros) 

# OK, mas e se precisar ordenar em ordem decrescente?
# Simples, apenas utilize a função reverse! Veja como fica:
nomes = ['Pedro', 'João', 'Maria', 'Zazu', 'Antônio']
nomes.sort() # Primeiro ordenamos a lista normalmente
nomes.reverse() # Depois invertemos a ordem, ficando em ordem decrescente!
print(nomes)


# Verificando se um elemento está na lista
# É possível verificar se um elemento está na lista utilizando as palavras-chave in e not in. Vamos ver como funciona:
passaros = ['Tucano', 'Bem-te-vi', 'Quero-Quero']
# vamos verificar se Tucano está na lista
'Tucano' in lista # Tucano está na lista? O programa verifica e retorna um valor booleano (True ou False)
# Agora vamos verificar se Pombo não está na lista
'Pombo' not in lista # Pombo não está na lista? O programa novamente analisa e retorna um booleano (True ou False)