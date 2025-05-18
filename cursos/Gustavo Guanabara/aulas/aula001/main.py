# Variáveis
# As variáveis armazenam valores no espaço da memória
nome = 'Gustavo Guanabara'
# nome recebe o valor Gustavo Guanabara
idade = 14
peso = 75.80

# Imprimindo os valores das variáveis
print(nome, idade, peso)



# Interação com o usuário: utilizando o input
nome = input('Qual é o seu nome? ')
print(nome) # Imprimindo o nome que o usuário digitar


# Desafios
# 1. Um script python que leia o nome do usuário e mostra uma mensagem de boas vindas
nome = input("Qual é o seu nome? ")
print('O seu nome é ' + nome)


# 2. Crie um script python que leia o dia o mês e o ano de uma pessoa e mostre uma mensagem com a data formatada
dia = int(input('Qual o dia da sua data de nascimento? '))
mes = int(input('Qual o mês da sua data de nascimento? '))
ano = int(input('Qual o ano da sua data de nascimento? '))
print('Você nasceu no dia', dia, 'no mês', mes, 'e no ano', ano)


# 3. Crie um script python que pede ao usuario dois números e faça a soma deles
numero1 = int(input('Digite o primeiro número '))
numero2 = int(input('Digite o segundo número '))
print('A soma dos dois números é', numero1 + numero2)