# Crie um programa que diga a pessoa o ano que ela poderá se aposentar. Você deve perguntar a pessoa, o nome, a idade e criar uma mensagem dizendo em qual ano ela irá aposentar. Considere que todas as pessoas podem se aposentar aos 65 anos de idade.

from datetime import datetime
nome = input('Digite o seu nome: ')
idade = int(input(f'{nome}, Digite a sua idade: '))
ano = datetime.now().year
aposentadoria = (ano - idade) + 65
print(f'Você irá se aposentar em {aposentadoria}' if idade < 65 else f'{nome}, você já se aposentou!')

