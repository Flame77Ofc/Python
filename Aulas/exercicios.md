# Exercício 9.3 Crie um programa que leia os arquivos pares.txt e ímpares.txt e que
# crie um só arquivo pareseimpares.txt com todas as linhas dos outros dois arquivos,
# de forma a preservar a ordem numérica.

# Exercício 9.4 Crie um programa que receba o nome de dois arquivos como pa-
# râmetros da linha de comando e que gere um arquivo de saída com as linhas do

# primeiro e do segundo arquivo.

# Exercício 9.5 Crie um programa que inverta a ordem das linhas do arquivo pares.
# txt. A primeira linha deve conter o maior número; e a última, o menor.

Exercício 9.6 Modifique o programa da listagem 9.6 para imprimir 40 vezes o
símbolo de = se este for o primeiro caractere da linha. Adicione também a opção
para parar de imprimir até que se pressione a tecla Enter cada vez que uma linha
iniciar com . como primeiro caractere.

Exercício 9.7 Crie um programa que leia um arquivo-texto e gere um arquivo de
saída paginado. Cada linha não deve conter mais de 76 caracteres. Cada página
terá no máximo 60 linhas. Adicione na última linha de cada página o número da
página atual e o nome do arquivo original.

Exercício 9.8 Modifique o programa anterior para também receber o número de
caracteres por linha e o número de páginas por folha pela linha de comando.

Exercício 9.9 Crie um programa que receba uma lista de nomes de arquivo e os
imprima, um por um.

Exercício 9.10 Crie um programa que receba uma lista de nomes de arquivo e que
gere apenas um grande arquivo de saída.

Exercício 9.11 Crie um programa que leia um arquivo e crie um dicionário onde
cada chave é uma palavra e cada valor é o número de ocorrências no arquivo.

Exercício 9.12 Modifique o programa anterior para também registrar a linha e a
coluna de cada ocorrência da palavra no arquivo. Para isso, utilize listas nos valores
de cada palavra, guardando a linha e a coluna de cada ocorrência.

Exercício 9.13 Crie um programa que imprima as linhas de um arquivo. Esse pro-
grama deve receber três parâmetros pela linha de comando: o nome do arquivo,

a linha inicial e a última linha a imprimir.

Exercício 9.14 Crie um programa que leia um arquivo-texto e elimine os espaços
repetidos entre as palavras e no fim das linhas. O arquivo de saída também não
deve ter mais de uma linha em branco repetida.

Exercício 9.15 Altere o programa da listagem 7.5, o jogo da forca. Utilize um arqui-
vo em que uma palavra seja gravada a cada linha. Use um editor de textos para

gerar o arquivo. Ao iniciar o programa, utilize esse arquivo para carregar a lista de
palavras. Experimente também perguntar o nome do jogador e gerar um arquivo
com o número de acertos dos cinco melhores.

Exercício 9.16 Explique como os campos nome e telefone são armazenados no
arquivo de saída.

Exercício 9.17 Altere o programa para exibir o tamanho da agenda no menu principal.

Exercício 9.18 O que acontece se nome ou telefone contiverem o caractere usado
como separador em seus conteúdos? Explique o problema e proponha uma solução.

Exercício 9.19 Altere a função lista para que exiba também a posição de cada
elemento.

Exercício 9.20 Adicione a opção de ordenar a lista por nome no menu principal.

Exercício 9.21 Nas funções de altera e apaga, peça que o usuário confirme a alte-
ração e exclusão do nome antes de realizar a operação em si.

Exercício 9.22 Ao ler ou gravar uma nova lista, verifique se a agenda atual já foi
gravada. Você pode usar uma variável para controlar quando a lista foi alterada
(novo, altera, apaga) e reinicializar esse valor quando ela for lida ou gravada.

Exercício 9.23 Altere o programa para ler a última agenda lida ou gravada ao ini-
cializar. Dica: utilize outro arquivo para armazenar o nome.

Exercício 9.24 O que acontece com a agenda se ocorrer um erro de leitura ou
gravação? Explique.

Exercício 9.25 Altere as funções pede_nome e pede_telefone de forma a receberem
um parâmetro opcional. Caso esse parâmetro seja passado, utilize-o como retorno
caso a entrada de dados seja vazia.

Exercício 9.26 Altere o programa de forma a verificar a repetição de nomes. Gere
uma mensagem de erro caso duas entradas na agenda tenham o mesmo nome.

Exercício 9.27 Modifique o programa para também controlar a data de aniversário
e o e-mail de cada pessoa.

Exercício 9.28 Modifique o programa de forma a poder registrar vários telefones
para a mesma pessoa. Permita também cadastrar o tipo de telefone: celular, fixo,
residência, trabalho ou fax.

Escreva um programa que peça 2
números e exiba o maior deles.

Escreva um programa que pergunte
um número e escreva a tabuada de
multiplicar deste (1 até 10)


1. Crie uma lista com números de 1 à 10
2. Remova o elemento da posição 2
3. Remova o elemento de valor 5
4. Acrescente 11 e 12 ao fim da lista
5. Acrescente 0 no início da lista
6. Exiba o tamanho da lista


• Faça um programa que utilize
listas para gerenciar uma agenda
de telefones.
o A agenda deve guardar nome e telefone de
várias pessoas.
o Operações a suportar: inclusão, exclusão,
alteração, pesquisa, listagem e ordenação.
o Em todos as opções o nome do indivíduo será
utilizado como chave de pesquisa.
o Utilize menu.


1. Crie um programa no qual o usuário informe 2 números inteiros: a e b. Para que o programa continue sua execução, verifique se a < b. Se sim, calcule a soma dos números inteiros no intervalo [a, b]. Caso contrário, informe uma mensagem de erro.

2. Um professor de Matemática deseja construir um programa para gerar uma Progressão Aritmética (PA). Para isso, devem ser informados 3 argumentos: a) primeiro termo, b) quantidade de termos e c) razão.

3. Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria (considere que o usuário informou cinco medicamentos distintos). O programa deve informar o nome e o preço do medicamento mais barato, bem como a média aritmética dos preços informados.


4. Imagine um sistema de caixa eletrônico. Construa um pro-
grama que receba a senha de um correntista para validar o seu

acesso ao sistema. Considere que a senha fictícia do correntista
é 123456. Considere as seguintes restrições:
• quando a senha estiver correta, mostrar a mensagem:
“Olá, <SEUNOME>. Seja bem-vindo ao nosso banco!"
• quando o usuário errar a senha pela primeira vez,
mostrar a mensagem: “Senha incorreta! Você ainda
tem 2 tentativas.”
• se o usuário errar a senha pela segunda vez, mostrar

a mensagem: “Senha incorreta! Você ainda tem 1 ten-
tativa.”

• se o usuário errar a senha novamente, mostrar a men-
sagem “Sua senha foi bloqueada! Por favor, dirija-se a

um de nossos caixas.” e o programa deve ser encerrado.



5. Os professores de Educação Física estão organizando uma

seletiva para montar a equipe de natação. Para isso, eles con-
vocaram os 7 melhores tempos da última competição e mar-
caram o tempo de cada um dos nadadores, na prova dos 25

metros, estilo livre.
Considerando que não houve tempos iguais, construa um pro-
grama que leia o nome e o tempo (em segundos) de cada atleta

e, em seguida, gere o seguinte relatório:
a. nome do nadador com o melhor tempo
b. nome do nadador com o pior desempenho
c. tempo médio dos nadadores e
d. quantidade de atletas com o tempo entre 12s e 15s


6. Construa um programa que receba uma lista contendo a esta-
tura dos alunos de uma escola. Crie um relatório que informe a

a. menor estatura
b. maior estatura
c. média das estaturas informadas

7. Crie um programa no qual o usuário informe a idade de um
número indeterminado de alunos. Para encerrar a leitura dos
dados, o usuário deve informar uma idade negativa. No final,
o programa deve mostrar a média aritmética entre a maior e a
menor idade.



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

Crie um programa no qual o usuário informe um número inteiro positivo N e armazene-o em uma variável. Em seguida, o usuário deve digitar N números. Ao fim, o programa deve im-primir a média aritmética dos N números digitados.
2. Para construir o programa a seguir, considere que os usuá-rios só informarão números inteiros positivos. Crie um progra-ma que receba 5 números digitados e, ao fim, exibir quantos números são pares.
Construa um programa para fazer uma pequena entrevista com os alunos de uma turma. Na entrevista, são informados o sexo e a idade de cada aluno. Considere que o usuário não sabe quan-tos alunos existem na turma. O programa deve exibir a quantida-de de homens acima de 18 anos e a quantidade de mulheres de qualquer idade. Para encerrar o programa, o usuário deve infor-mar uma idade negativa.
. Crie um programa no qual o usuário informe 2 números intei-ros: a e b. Para que o programa continue sua execução, verifique se a < b. Se sim, calcule a soma dos números inteiros no intervalo [a, b]. Caso contrário, informe uma mensagem de erro.

2. Um professor de Matemática deseja construir um programa para gerar uma Progressão Aritmética (PA). Para isso, devem ser informados 3 argumentos: a) primeiro termo, b) quantida-de de termos e c) razão.

3. Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria (considere que o usuário in-

101
formou cinco medicamentos distintos). O programa deve in-formar o nome e o preço do medicamento mais barato, bem como a média aritmética dos preços informados.
4. Imagine um sistema de caixa eletrônico. Construa um pro-grama que receba a senha de um correntista para validar o seu acesso ao sistema. Considere que a senha ficticia do correntista.

é 123456. Considere as seguintes restrições:

quando a senha estiver correta, mostrar a mensagem: "Olá, <SEUNOME>. Seja bem-vindo ao nosso banco!"

quando o usuário errar a senha pela primeira vez, mostrar a mensagem: "Senha incorreta! Você ainda tem 2 tentativas."


se o usuário errar a senha pela segunda vez, mostrar a mensagem: "Senha incorreta! Você ainda tem 1 ten-tativa."

se o usuário errar a senha novamente, mostrar a men-sagem "Sua senha foi bloqueadal Por favor, dirija-se al um de nossos caixas." e o programa deve ser encerrado.

5. Os professores de Educação Física estão organizando uma seletiva para montar a equipe de natação. Para isso, eles con-vocaram os 7 melhores tempos da última competição e mar-caram o tempo de cada um dos nadadores, na prova dos 25 metros, estilo livre.

Considerando que não houve tempos iguais, construa um pro-grama que leia o nome e o tempo (em segundos) de cada atleta e, em seguida, gere o seguinte relatório:

a. nome do nadador com o melhor tempo

102

INTRODUÇÃO A PYTHON

b. nome do nadador com o pior desempenho

c. tempo médio dos nadadores e

d. quantidade de atletas com o tempo entre 12s e 15s.

6. Construa um programa que receba uma lista contendo a esta-tura dos alunos de uma escola. Crie um relatório que informe a

a. menor estatura

b. maior estatura

c. média das estaturas informadas


7. Crie um programa no qual o usuário informe a idade de um número indeterminado de alunos. Para encerrar a leitura dos dados, o usuário deve informar uma idade negativa. No final, o programa deve mostrar a média aritmética entre a maior e a menor idade.



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


6.7 Pessoas: comece com o programa escrito para Exercício 6.1 (página 138). Crie dois dicionários novos representando pessoas diferentes e armazene todos os três dicionários em uma lista chamada people. Percorra sua lista de pessoas com um loop. À medida que percorre a lista,
exiba tudo o que sabe sobre cada pessoa.
6.8 Animais de estimação: Crie vários dicionários, em que cada dicionário representa um animal de estimação diferente. Em cada dicionário inclua o tipo de animal e o nome do dono. Armazene esses dicionários em uma lista chamada pets. Depois, percorra sua lista com um loop e, enquanto faz isso, exiba tudo o que sabe sobre cada animal de estimação. 
6.9 Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em três nomes para usar como chave no dicionário e armazene de um a três lugares favoritos para cada pessoa.
Agora, para que este exercício fique ainda mais interessante, peça a alguns amigos que lhe
digam alguns de seus lugares favoritos. Percorra o dicionário com um loop e exiba o nome de
cada pessoa e seus lugares favoritos.
6.10 Números favoritos: Modifique seu programa do Exercício 6.2 (página 138) para que cada
pessoa possa ter mais de um número favorito. Depois, exiba o nome de cada pessoa com seus
números favoritos.
6.11 Cidades: Crie um dicionário chamado cities. Utilize o nome de três cidades como chaves de
seu dicionário. Crie um dicionário de informações sobre cada cidade e inclua o país em que a
cidade está, sua população aproximada e um fato sobre essa cidade. O nome das chaves para o
dicionário de cada cidade devem ser alguma coisa como country, population e fact. Exiba o
nome de cada cidade e todas as informações que você armazenou a respeito.
6.12 Extensões: Agora que já estamos trabalhando com exemplos complexos o suficiente para
que sejam mais desenvolvidos de diferentes maneira, use um dos programas de exemplo deste
capítulo e o amplie, adicionando chaves e valores novos, alterando o contexto do programa ou
melhorando a formatação da saída.


7.4 Ingredientes de pizza: Escreva um loop que solicite ao usuário uma série de ingredientes de
pizza até que ele forneça o valor 'quit'. À medida que cada ingrediente é fornecido, exiba uma
mensagem informando que esses ingredientes estão sendo adicionados à pizza.
7.5 Ingressos de cinema: Um cinema cobra preços de ingressos diferentes, dependendo da idade
da pessoa. Se a pessoa for menor de 3 anos, o ingresso é gratuito; se tiver entre 3 e 12 anos, o
ingresso custa U$S10; e caso tenha mais de 12 anos, o ingresso custa US$15. Escreva um loop
que pergunte a idade dos usuários e, em seguida, informe o preço do ingresso do cinema.
7.6 Três saídas: Crie diferentes versões do Exercício 7.4 ou 7.5 que executem cada uma das
seguintes tarefas, pelo menos uma vez:
• Use um teste condicional na instrução while para interromper o loop.
• Use uma variável active para controlar o tempo que o loop é executado.
• Use uma instrução break para sair do loop quando o usuário inserir o valor 'quit'.
7.7 Infinito: Escreva e execute um loop infinito. (Para encerrar o loop, pressione CTRL+C ou
feche a janela que exibe a saída.)


7.8 Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com o nome de diversos
sanduíches. Depois, crie uma lista vazia chamada finished_sandwiches. Percorra a lista de
pedidos de sanduíches com um loop e exiba uma mensagem para cada pedido, como: Seu lanche
de atum está pronto. Conforme cada sanduíche é preparado, passe-os para a lista de sanduíches
prontos. Após todos os sanduíches terem sido preparados, exiba uma mensagem enumerando
cada um deles.
7.9 Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, assegure-se de que o
sanduíche 'pastrami' apareça na lista pelo menos três vezes. Faça mais um código perto do início
de seu programa, exibindo uma mensagem que informe que a lanchonete está sem pastrami e,
em seguida, use um loop while para remover todas as ocorrências de 'pastrami' em
sandwich_orders. Faça questão de que nenhum sanduíche de pastrami acabe em
finished_sandwiches.
7.10 Férias tão sonhadas: Crie uma pesquisa que pergunte aos usuários sobre as férias de seus sonhos. Crie um prompt mais ou menos assim: Se pudesse visitar qualquer lugar do mundo, para onde iria? Inclua um bloco de código que exiba os resultados dessa pesquisa.


8.3 Camiseta: Crie uma função chamada make_shirt() que aceita um tamanho e o texto que deve ser estampado na camiseta. A função deve exibir uma frase resumindo o tamanho da camiseta e a mensagem estampada nela. Chame a função uma vez usando argumentos posicionais para criar uma camiseta. Chame a função uma segunda vez usando argumentos nomeados.
8.4 Camisetas grandes: Modifique a função make_shirt() para que as camisetas sejam grandes por padrão com a seguinte frase estampada: Eu amo Python. Escreva uma camiseta grande e uma média com a mensagem padrão e uma camiseta de qualquer tamanho com uma frase diferente.
8.5 Cidades: Escreva uma função chamada describe_city() que aceite o nome de uma cidade e de seu país. A função deve exibir uma simples frase, como Reykjavik fica na Islândia. Forneça ao parâmetro do país um valor default. Chame sua função para três cidades diferentes e, pelo menos, para uma que não esteja no país default.

8.6 Nome de cidades: Escreva uma função chamada city_country() que recebe o nome de uma cidade e seu país. A função deve retornar uma string formatada como esta: "Santiago, Chile" Chame sua função com pelo menos três pares cidade-país e exiba os valores retornados.
8.7 Álbum: Escreva uma função chamada make_album() que crie um dicionário representando um álbum de música. A função deve ter o nome de um artista e o título de álbum, e deve retornar um dicionário com essas duas informações. Utilize a função para criar três dicionários representando álbuns distintos. Exiba cada valor de retorno para mostrar que os dicionários estão armazenando adequadamente as informações do álbum. Use None para adicionar um parâmetro opcional ao make_album() que possibilite armazenar o
número de músicas em um álbum. Se a linha chamadora incluir um valor para o número de
músicas, adicione esse valor ao dicionário do álbum. Crie, pelo menos, uma nova chamada de
função que inclua o número de músicas em um álbum.
8.8 Álbuns de usuários: Comece com seu programa do Exercício 8.7. Escreva um loop while que
possibilite aos usuários inserir o artista e o título de um álbum. Após receber essas informações,
chame make_album() com a entrada do usuário e exiba o dicionário criado. Não se esqueça de
incluir um valor de saída no loop while.

8.9 Mensagens: Crie uma lista com uma série de mensagens curtas de texto. Passe a lista para uma função chamada show_messages(), que exiba cada mensagem de texto.
8.10 Enviando mensagens: Comece com uma cópia do seu programa do Exercício 8.9. Escreva uma função chamada send_messages() para exibir cada mensagem de texto e passe cada mensagem para uma nova lista chamada sent_messages à medida que é exibida. Após chamar a função, exiba ambas as listas para ter certeza de que as mensagens foram corretamente transferidas.
8.11 Mensagens arquivadas: Comece sua tarefa a partir do Exercício 8.10. Chame a função send_messages() com uma cópia da lista de mensagens. Após chamar a função, exiba ambas as listas para mostrar que a lista original reteve suas mensagens.


9.1 Restaurante: Crie uma classe chamada Restaurant. O método __init__() para Restaurant deve
armazenar dois atributos: restaurant_name e cuisine_type. Crie um método chamado
describe_restaurant() que exiba essas duas informações e um método chamado open_restaurant()
que exiba uma mensagem sinalizando que o restaurante está aberto.
Crie uma instância chamada restaurant a partir da sua classe. Exiba os dois atributos
individualmente e, em seguida, chame ambos os métodos.
9.2 Três restaurantes: Comece com sua classe do Exercício 9.1. Crie três instâncias diferentes da
classe e chame describe_restaurant() para cada instância.
9.3 Usuários: Crie uma classe chamada User. Crie dois atributos chamados first_name e
last_name e diversos outros atributos que normalmente são armazenados em um perfil de
usuário. Crie um método chamado describe_user() que exiba um resumo das informações do
usuário. Crie outro método chamado greet_user() que exiba um cumprimento personalizado ao usuário.
9.4 Pessoas atendidas: Comece com o seu programa do Exercício 9.1 (página 208). Adicione um
atributo chamado number_served com um valor default de 0. Crie uma instância chamada
restaurant a partir dessa classe. Exiba o número de clientes que o restaurante atendeu e, em
seguida, altere este valor e o exiba novamente.
Adicione um método chamado set_number_served() que possibilita definir o número de clientes
atendidos. Chame esse método com um novo número e exiba mais uma vez o valor.
Adicione um método chamado increment_number_served(), o qual possibilita aumentar o
número de clientes atendidos. Chame esse método com qualquer número que quiser e que possa
representar quantos clientes foram atendidos em, digamos, um dia de atividade comercial.
9.5 Tentativas de login: Adicione um atributo chamado login_attempts à sua classe User do
Exercício 9.3 (página 209). Crie um método chamado increment_login_attempts() que
incrementa o valor de login_attempts em 1. Crie outro método chamado reset_login_attempts()
que redefine o valor de login_attempts para 0.
Crie uma instância da classe User e chame increment_login_attempts() diversas vezes. Exiba o
valor de login_attempts para verificar que foi incrementado corretamente e, em seguida, chame
reset_login_attempts(). Exiba login_attempts novamente a fim de ter certeza de que foi
redefinido para 0.