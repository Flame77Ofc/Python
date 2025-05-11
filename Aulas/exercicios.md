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