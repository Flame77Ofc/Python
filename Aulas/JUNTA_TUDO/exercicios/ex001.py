# Problema: Você foi contratado(a) para fazer um serviço para o INSS (Instituto Nacional do Seguro Social) do Brasil. O trabalho consiste em criar um programa que diga a pessoa o ano que ela poderá se aposentar. Você deve perguntar a pessoa, o nome, a idade e criar uma mensagem dizendo em qual ano ela irá aposentar. Considere que todas as pessoas podem se aposentar aos 65 anos de idade.

nome = input('Qual o seu nome? ')
idade = int(input('Quantos anos você tem? '))
ano_atual = int(input('Em que ano estamos? '))

if idade >= 65:
    print(f'{nome}, você já pode se aposentar!')
else:
    anos_restantes = 65 - idade
    ano_aposentadoria = ano_atual + anos_restantes
    print(f'{nome}, você poderá se aposentar em {ano_aposentadoria}, daqui a {anos_restantes} anos.')
