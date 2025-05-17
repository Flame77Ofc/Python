# exercicios py
1. Um aluno iniciou seus estudos em geometria plana e, para

validar se suas respostas estão corretas, solicitou sua ajuda. Sa-
bendo que , construa um programa para

auxiliar esse aluno.

2. Agora o mesmo aluno precisa que você construa um progra-
ma para calcular o comprimento de uma circunferência. Para

isso, o aluno informará ao programa o raio da circunferência.
Sabe-se que .

3. Construa um programa que leia 2 números reais informados
pelo usuário. Ao fim, o programa deve calcular e imprimir:
a. a soma dos dois valores
b. o produto entre eles

4. Implemente um programa que converta o valor de uma ve-
locidade média em km/h para m/s. Para isso, o usuário deve

informar o valor da velocidade média. Sabe-se que o fator utili-
zado para essa conversão é 3,6.

7. Uma imobiliária paga aos seus corretores um salário base
de R$ 1.500,00. Além disso, uma comissão de R$ 200,00 por
cada imóvel vendido e 5% do valor de cada venda. Construa
um programa que solicite o nome do corretor, a quantidade
de imóveis vendidos e o valor total de suas vendas. Ao fim, o
programa deve calcular e escrever o salário final do corretor de
imóveis.

8. Construa um programa que receba do usuário o valor do
salário mínimo atual. Na sequência, o programa deve solicitar
que o usuário informe o valor do seu salário mensal. Ao fim, o programa deve calcular a quantidade de salários mínimos re-
cebidos pelo usuário.





1. Write a for loop that prints out the integers 2 through 10, each on
a new line, using range().
2. Write a while loop that prints out the integers 2 through 10. (Hint:
You’ll need to create a new integer first.)
3. Write a function called doubles() that takes a number as its input
and doubles it. Then use doubles() in a loop to double the number 2
three times, displaying each result on a separate line. Here’s some
sample output:
4
8
16





1. Using break, write a program that repeatedly asks the user for some
input and quits only if the user enters "q" or "Q".
2. Using continue, write a program that loops over the numbers 1 to
50 and prints all numbers that are not multiples of 3.



1. Create a tuple literal named cardinal_numbers that holds the strings
"first", "second", and "third", in that order.
2. Using index notation and print(), display the string at index 1 in
cardinal_numbers.
3. In a single line of code, unpack the values in cardinal_numbers into
three new strings named position1, position2, and position3. Then
print each value on a separate line.
4. Using tuple() and a string literal, create a tuple called my_name that
contains the letters of your name.
5. Check whether the character "x" is in my_name using the in keyword.
6. Create a new tuple containing all but the first letter in my_name using
slice notation.

1. Create a list named food with two elements, "rice" and "beans".
2. Append the string "broccoli" to food using .append().
3. Add the strings "bread" and "pizza" to food using .extend().

4. Print the first two items in the food list using print() and slice no-
tation.

5. Print the last item in food using print() and index notation.
6. Create a list called breakfast from the string "eggs, fruit, orange
juice" using the string .split() method.
7. Verify that breakfast has three items using len().

8. Create a new list called lengths using a list comprehension that con-
tains the lengths of each string in the breakfast list.




1. Create a tuple called data with two values. The first value should
be the tuple (1, 2), and the second value should be the tuple (3,
4).
2. Write a for loop that loops over data and prints the sum of each
nested tuple. The output should look like this:
Row 1 sum: 3
Row 2 sum: 7
3. Create the list [4, 3, 2, 1] and assign it to the variable numbers.
4. Create a copy of the numbers list using the [:] slice notation.
5. Sort the numbers list in numerical order using .sort().


100000. Challenge: List of lists
Write a program that contains the following lists of lists:
universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]
Define a function, enrollment_stats(), with a single parameter. This
parameter should be a list of lists in which each individual list contains
three elements:
1. The name of a university
2. The total number of enrolled students
3. The annual tuition fees
enrollment_stats() should return two lists, the first containing all the
student enrollment values and the second containing all the tuition
fees.
Next, define two functions, mean() and median(), that take a single list
argument and return the mean or median of the values in each list,
respectively.
Using universities, enrollment_stats(), mean(), and median(), calculate
the total number of students, the total tuition, the mean and median
numbers of students, and the mean and median tuition values.
Finally, output all values and format the output so that it looks like
this:
******************************
Total students: 77,285
Total tuition: $ 271,905
Student mean: 11,040.71
Student median: 10,566
Tuition mean: $ 38,843.57
Tuition median: $ 39,849
******************************




1. Create an empty dictionary named captains.
2. Using square bracket notation, enter the following data into the
dictionary one item at a time:
• 'Enterprise': 'Picard'
• 'Voyager': 'Janeway'
• 'Defiant': 'Sisko'
3. Write two if statements that check if "Enterprise" and "Discovery"
exist as keys in the dictionary. Set their values to "unknown" if the
key does not exist.
4. Write a for loop to display the ship and captain names contained
in the dictionary. For example, the output should look something
like this:
The Enterprise is captained by Picard.
5. Delete "Discovery" from the dictionary.
6. Bonus: Make the same dictionary by using dict() and passing in
the initial values when you first create the dictionary.

1. Create a list with the names of friends and colleagues. Calculate the average length of the names.

2. Create a list with the names of friends and colleagues. Search for the name John using a for loop. Print not found if you didn't find it. (Hint: use else).

3. Create a list of tuples of first name, last name, and age for your friends and colleagues. If you don't know the age, put in None. Calculate the average age, skipping over any None values. Print out each name, followed by old or young if they are above or below the average age.

1. Create a variable, age, set to your age. Create another variable, old, that uses a condition to test whether you are older than 18. The value of old should be True or False.

2. Create a variable, name, set to your name. Create another variable, second_half, that tests whether the name would be classified in the second half of the alphabet? What do you need to compare it to?

3. Create a list, names, with the names of people in a class. Write code to print 'The class is empty!' or 'Class has enrollments.', based on whether there are values in names. (See the tip in this chapter for details).

4. Create a variable, car, set to None. Write code to print 'Taxi for you!', or 'You have a car!'. based on whether or not car is set (None is not the name of a car).



4.1. Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes
informações:
a) tamanho da lista.
b) maior valor da lista.
c) menor valor da lista.
d) soma de todos os elementos da lista.
e) listar em ordem crescente.
f) listar em ordem decrescente.
4.2. Gere uma lista contendo os múltiplos de 3 entre 1 e 50.
4.3. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
4.4. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
4.5. Faça um Programa que leia 10 números inteiros e armazene-os num vetor. Separe os
números pares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três
vetores.
4.6. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as
em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as
temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por
extenso: 1 – Janeiro, 2 – Fevereiro,..).
4.7. Crie uma lista com os nomes dos super-heróis que devem participar da
Iniciativa Vingadores seguindo a ordem:
• Homem de Ferro
• Capitão América
• Thor
• Hulk
• Viúva Negra
• Gavião Arqueiro
4.8. No exercício anterior, inclua o Homem-Aranha no final da lista e imprima em qual
posição está o Thor.

4.9. No exercício anterior, infelizmente, a Viúva Negra e o Homem de Ferro não fazem mais
parte da Iniciativa Vingadores, então retire-os da lista.
4.10. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e
a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve
fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo
atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).


6.1. Escreva um programa para encontrar a soma S = 3 + 6 + 9 +.... + 333.
6.2. Escreva um programa que leia 10 notas e informe a média do aluno.
6.3. Escreva um programa que leia um número de 1 a 10, e mostre a tabuada desse número.
6.4. Faça um programa que peça as quatro notas de 5 alunos, calcule e armazene num vetor a
média de cada aluno.
6.5. Usando o código anterior, imprima o número de alunos com média maior ou igual a 7.0.
6.5. Elaborar um programa para ler 10 números e imprimir a soma, o maior e o menor
desses números.
6.6. Elaborar um programa para calcular a soma de 1 até 50.

Exercício 3.7 Faça um programa que peça dois números inteiros. Imprima a soma
desses dois números na tela.

Exercício 3.8 Escreva um programa que leia um valor em metros e o exiba con-
vertido em milímetros.

Exercício 3.9 Escreva um programa que leia a quantidade de dias, horas, minutos
e segundos do usuário. Calcule o total em segundos.

Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve
solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
e do novo salário.

Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o per-
centual de desconto. Exiba o valor do desconto e o preço a pagar.

Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

Exercício 3.13 Escreva um programa que converta uma temperatura digitada em
°C em °F.


Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
dia e R$ 0,15 por km rodado.

Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá. Exiba o total em dias.



Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
casa a comprar dividido pelo número de meses a pagar.


Exercício 5.14 Escreva um programa que leia números inteiros do teclado. O pro-
grama deve ler os números até que o usuário digite 0 (zero). No final da execução,

exiba a quantidade de números digitados, assim como a soma e a média aritmética.



Exercício 5.16 Execute o programa (Listagem 5.14) para os seguintes valores: 501,
745, 384, 2, 7 e 1.

Exercício 5.17 O que acontece se digitarmos 0 (zero) no valor a pagar?

Exercício 5.18 Modifique o programa para também trabalhar com notas de R$ 100.

Exercício 5.19 Modifique o programa para aceitar valores decimais, ou seja, também
contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,50.


Exercício 5.20 O que acontece se digitarmos 0,001 no programa anterior? Caso ele
não funcione, altere-o de forma a corrigir o problema.

Exercício 5.21 Reescreva o programa da listagem 5.14 de forma a continuar execu-
tando até que o valor digitado seja 0. Utilize repetições aninhadas.

Exercício 5.22 Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
Repita até que a opção saída seja escolhida.

Exercício 5.23 Escreva um programa que leia um número e verifique se é ou não
um número primo. Para fazer essa verificação, calcule o resto da divisão do número
por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma
dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são
primos e que 2 é o único número primo que é par.

Exercício 5.24 Modifique o programa anterior de forma a ler um número n. Imprima
os n primeiros números primos.

Exercício 5.25 Escreva um programa que calcule a raiz quadrada de um número.

Utilize o método de Newton para obter um resultado aproximado. Sendo n o nú-
mero a obter a raiz quadrada, considere a base b=2. Calcule p usando a fórmula

p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule
p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o
quadrado de p for menor que 0,0001.

Exercício 5.26 Escreva um programa que calcule o resto da divisão inteira entre dois
números. Utilize apenas as operações de soma e subtração para calcular o resultado.

Exercício 5.27 Escreva um programa que verifique se um número é palíndromo.
Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
Exemplos: 454, 10501



Exercício 6.4 O que acontece quando não verificamos se a lista está vazia antes de
chamarmos o método pop?

Exercício 6.5 Altere o programa da listagem 6.21 de forma a poder trabalhar com
vários comandos digitados de uma só vez. Atualmente, apenas um comando pode
ser inserido por vez. Altere-o de forma a considerar operação como uma string.
Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos
e, finalmente, a saída do programa.

Exercício 6.6 Modifique o programa para trabalhar com duas filas. Para facilitar

seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendi-
mento da fila 2. O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2.

Exercício 6.8 Modifique o primeiro exemplo (Listagem 6.23) de forma a realizar
a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de
saída do while.

Exercício 6.9 Modifique o exemplo para pesquisar dois valores. Em vez de apenas
p, leia outro valor v que também será procurado. Na impressão, indique qual dos
dois valores foi achado primeiro.

Exercício 6.10 Modifique o programa do exercício 6.9 de forma a pesquisar p e v
em toda a lista e informando o usuário a posição onde p e a posição onde v foram
encontrados.



Exercício 6.12 Altere o programa da listagem 6.33 de forma a imprimir o menor
elemento da lista.

Exercício 6.13 A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior
temperatura, assim como a temperatura média.


Exercício 6.17 Altere o programa da listagem 6.53 de forma a solicitar ao usuário o
produto e a quantidade vendida. Verifique se o nome do produto digitado existe
no dicionário, e só então efetue a baixa em estoque.

Exercício 6.18 Escreva um programa que gere um dicionário, onde cada chave seja
um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida.
Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}



Exercício 7.1 Escreva um programa que leia duas strings. Verifique se a segunda
ocorre dentro da primeira e imprima a posição de início.
1a string: AABBEFAATT
2a string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT

Exercício 7.2 Escreva um programa que leia duas strings e gere uma terceira com
os caracteres comuns às duas strings lidas.
1a string: AAACTBF
2a string: CBT
Resultado: CBT
A ordem dos caracteres da string gerada não é importante, mas deve conter todas
as letras comuns a ambas.


Exercício 7.3 Escreva um programa que leia duas strings e gere uma terceira apenas
com os caracteres que aparecem em uma delas.
1a string: CTA
2a string: ABC
3a string: BT
A ordem dos caracteres da terceira string não é importante.

Exercício 7.4 Escreva um programa que leia uma string e imprima quantas vezes
cada caractere aparece nessa string.
String: TTAAC
Resultado:
T: 2x
A: 2x
C: 1x

Exercício 7.5 Escreva um programa que leia duas strings e gere uma terceira, na
qual os caracteres da segunda foram retirados da primeira.
1a string: AATTGGAA
2a string: TG
3a string: AAAA

Exercício 7.6 Escreva um programa que leia três strings. Imprima o resultado da
substituição na primeira, dos caracteres da segunda pelos da terceira.
1a string: AATTCGAA
2a string: TG
3a string: AC
Resultado: AAAACCAA



Exercício 8.1 Escreva uma função que retorne o maior de dois números.
Valores esperados:
máximo(5,6) == 6
máximo(2,1) == 2
máximo(7,7) == 7

Exercício 8.2 Escreva uma função que receba dois números e retorne True se o
primeiro número for múltiplo do segundo.
Valores esperados:
múltiplo(8,4) == True
múltiplo(7,3) == False
múltiplo(5,5) == True


Exercício 8.3 Escreva uma função que receba o lado (l) de um quadrado e retorne
sua área (A = lado2
).
Valores esperados:
área_quadrado(4) == 16
área_quadrado(9) == 81

Exercício 8.4 Escreva uma função que receba a base e a altura de um triângulo e
retorne sua área (A = (base x altura)/2).
Valores esperados:
área_triângulo(6, 9) == 27
área_triângulo(5, 8) == 20


Exercício 8.11 Escreva uma função para validar uma variável string. Essa função
recebe como parâmetro a string, o número mínimo e máximo de caracteres. Retorne
verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo,
e falso em caso contrário.

Exercício 8.12 Escreva uma função que receba uma string e uma lista. A função
deve comparar a string passada com os elementos da lista, também passada como
parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso em caso contrário.


Exercício 8.15 Utilizando a função type, escreva uma função recursiva que imprima
os elementos de uma lista. Cada elemento deve ser impresso separadamente, um
por linha. Considere o caso de listas dentro de listas, como L=[1, [2,3,4,[5,6,7]]].
A cada nível, imprima a lista mais à direita, como fazemos ao indentar blocos
em Python. Dica: envie o nível atual como parâmetro e utilize-o para calcular a
quantidade de espaços em branco à esquerda de cada elemento.


1. Construa um programa no qual um usuário informe a sua
estatura em metros e o programa converta-a para centímetros.

# 1. Construa um programa que receba um número inteiro positivo informado pelo usuário. Caso ele seja par, o programa deve calcular o seu quadrado. Mas, se ele for ímpar, deve ser calculado o seu cubo. Ao fim, o programa deve imprimir o valor calculado.



<!-- Concluídos -->
# Exercicio 1: Criar uma função que recebe um número e faz uma contagem regressiva desse número:
def contador(numero):
    for i in range(numero, 0, -1):
        print(i)
contador(15)
contador(5)


# Exercício 2: Criar uma função que recebe uma lista e retorna o maior número dessa lista:
def maior_numero(lista):
    maior = -1
    for i in lista:
        if i > maior:
            maior = i
    print(maior)
maior_numero([17, -5, 45, 9, 92, 64, 56])

# Implementar uma função que receba um dicionário e retorne a soma, a média e a variação dos valores.
notas = {
    'João Alberto': 6.70,
    'Maria Carvalho': 9.68,
    'Luiz Paulo Costa': 4.76
}

total = 0
for value in notas.values():
    total += value

 
media = round(total / len(notas.values()), 2)
print(media)
print(total)






Os professores de Educação Física estão organizando uma seletiva para montar a equipe de natação. Para isso, eles con- vocaram os 7 melhores tempos da última competição e mar-caram o tempo de cada um dos nadadores, na prova dos 25 metros, estilo nado livre.
Considerando que não houve tempos iguais, construa um programa que leia o nome e o tempo (em segundos) de cada atleta e, em seguida, gere o seguinte relatório:
a. nadador com o melhor tempo;
b. nadador com o pior desempenho;
c. tempo médio dos nadadores e;

3. Uma turma de formandos está vendendo rifas para angariar

recursos financeiros para sua cerimônia de formatura. Cons-
trua um programa para cadastrar os nomes das pessoas que

compraram a rifa. Ao fim, o programa deve sortear o ganhador
do prêmio e imprimir o seu nome.

4. Crie um programa que solicite o usuário um número N ím-
par maior que 1. Em seguida, preencha uma lista com N núme-
ros inteiros positivos (suponha que o usuário sempre digitará

números inteiros positivos). Selecione o elemento que está no centro da lista. Ao final, calcule e escreva o fatorial do elemento
selecionado.
5. Crie um programa que declare uma lista L, a qual você pode

preenchê-la manualmente. Em seguida, o programa deve cal-
cular a média geométrica entre o menor e o maior elemento da

lista L. Ao fim, o programa deve imprimir a média geométrica
encontrada.

6. Crie um programa que leia um valor N, tal que N > 1. O pro-
grama deve gerar, aleatoriamente, uma lista L. Por fim, o pro-
grama deve calcular e imprimir a média geométrica dos N ele-
mentos da lista..

7. Crie um programa que gere, aleatoriamente, uma matriz M,
com elementos no intervalo [0, 1]. A quantidade de linhas e de
colunas de M devem ser informadas pelo usuário. Ao fim, o
programa deve informar se M é uma matriz nula.
8. Crie um programa no qual o usuário informe o número de
linhas e o número de colunas de uma matriz M e, em seguida,
o usuário deve digitar os elementos de M. Ao fim, o programa
deve informar se M é uma matriz identidade.

1. Construa um programa que utilize um dicionário cujas chaves são
os códigos do produto e os valores são o nome do produto, o preço
unitário e a quantidade comprada, como no exemplo a seguir.
CHAVE VALOR
Código Nome Preço Unitário Qtde Comprada
1 Monitor LED 24” 599,99 1
2 Teclado wireless 49,26 1
3 Mouse wireless 19,90 1
4 Cartucho colorido 54,00 2

2. Crie um programa para cadastrar matrícula, nome e salário
dos funcionários de uma empresa. Ao fim, o programa deve

mostrar todos os funcionários cadastrados e, em seguida, au-
mentar para R$ 1.800,00 o salário dos funcionários com salá-
rios inferiores a R$ 1.500,00. Depois do aumento salarial, o pro-
grama deve exibir a nova listagem.


1. Um usuário do departamento de vendas de uma empresa ne-
cessita de um relatório que apresente seus clientes potenciais.

Para isso, é necessário que o relatório seja ordenado do cliente
que mais comprou para o que menos comprou. Os dados de
entrada são razão social e valor total de compras. Considere a
razão social como sendo a chave identificadora do cliente.
2. Construa um programa no qual o usuário informe o nome, a

estatura e o peso de vários alunos de uma turma. Após o cadas-
tro, o programa deve imprimir o nome e o IMC de cada aluno

ordenados pelo nome do aluno.


3. Construa um programa que cadastre diversos voos aéreos,
bem como sua origem e seu destino. Considere o número do
voo como sendo a chave. Com base no que foi armazenado
no dicionário, o programa deve informar a quantidade de voos
cuja origem é Natal.
4. Com base no dicionário da questão anterior, construa um

programa para remover os voos cujo destino é Recife. Em se-
guida, imprima a nova listagem de voos.

5. Ainda com base no dicionário da questão 3, construa um pro-
grama em que, após os voos terem sido cadastrados, o usuário

possa modificar a origem e/ou o destino de um determinado
voo. Ao fim, o programa deve imprimir a nova listagem de voos.

6. Crie um programa para uma nova plataforma de vídeo sob
demanda o qual deve armazenar o título da série e o nome
dos 2 principais atores. Ao final, o programa deve exibir uma
listagem contendo, de forma ordenada, o nome da série e os
nomes dos atores.

7. Modifique o programa anterior de modo que o usuário infor-
me o nome de uma série e o novo programa indique os nomes

dos atores principais. Caso a série não esteja cadastrada, o pro-
grama deve informar isso ao usuário.

8. Construa um programa que utilize um dicionário para repre-
sentar a tabela abaixo.

Código Nome                Valor (R$)
1      Monitor LED 24”     599,99
2      Teclado wireless    49,26
3      Mouse wireless      19,90
4      Cartucho colorido   54,00
O programa deve aplicar um desconto de 10% sobre os produ-
tos com o valor acima de R$ 50,00 e acrescentar à descrição a

string (em promoção). O novo dicionário ficará como a tabela
abaixo.
Código Nome Valor (R$)
1 Monitor LED 24” (em promoção) 539,99
2 Teclado wireless 49,26
3 Mouse wireless 19,90
4 Cartucho colorido (em promoção) 48,60




É muito comum precisar calcular a soma dos elementos de
uma lista. Esse tipo de atividade pode ser necessário em vários
pontos de um programa. Embora as listas possuam um método
chamado sum(), que é utilizado para calcular a soma dos seus
elementos, apenas para que você compreenda a utilização de
funções, crie uma função para calcular a soma dos elementos
de uma lista de inteiros.