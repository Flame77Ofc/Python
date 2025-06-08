# Crie um restaurante que simule um restaurante real. Deve verificar se o horário passa das 10 horas e 30 minutos da noite. Caso esteja mais que 10 horas, o programa irá mostrar 'Restaurante Fechado' e deverá ser o fim do programa. Deve ter um menu de opções:
"""
[1]: Ver o cardápio


"""
from datetime import datetime
import random
import time

def linhas(mensagem):
    print(f"""{'-' * 50}
{mensagem.center(50)}
{'Horário:'.rjust(25)} {data[0]}:{data[1]}
{'Restaurante fecha às 22:30'.center(50)}
{'-' * 50}""")
    
def mostrar_cardapio():
    global preco_comida
    preco_comida = 0

    while True: 
        print("""CARDÁPIO
    [1]: Batatas Fritas - R$15 reais (500 gramas)       [6]: Feijão - R$6 reais (230 gramas)
    [2]: Coca-Cola - R$12 reais (2 litros)              [7]: Macarrão - R$6 reais (140 gramas)
    [3]: Frango - R$4 reais (250 gramas)                [8]: Tilápia - R$2 reais (100 gramas)
    [4]: Sprite - R$7 reais (2 litros)                  [9]: H2O - R$6 reais (2 litros)
    [5]: Arroz - R$4 reais (450 gramas)                 [10]: Sair""")
        
        cardapio = int(input('Digite o cardápio:\n>>>'))

        while cardapio <= 0 or cardapio > 10:
            cardapio = int(input('Por favor, digite corretamente.\nDigite o cardápio:\n>>>'))
        
        if cardapio == 1:
            preco_comida += 15
        elif cardapio == 2:
            preco_comida += 12
        elif cardapio == 3:
            preco_comida += 4
        elif cardapio == 4:
            preco_comida += 7
        elif cardapio == 5:
            preco_comida += 4
        elif cardapio == 6:
            preco_comida += 6
        elif cardapio == 7:
            preco_comida += 6
        elif cardapio == 8:
            preco_comida += 2
        elif cardapio == 9:
            preco_comida += 6

        elif cardapio == 10:
            while preco_comida == 0:
                print('Deve-se escolher ao menos um alimento.')
                mostrar_cardapio()


            else:
                print('Seu pedido está sendo preparado...')

                segundos = 15

                while segundos > 0:
                    print(f'{segundos:02d}', end='\r', flush=True)
                    time.sleep(1)

                    if segundos == 0:
                        segundos = 59
                    else:
                        segundos -= 1

                print('00:00')
                break
        print('Adicionado com sucesso!')


data = datetime.now().strftime('%H'), datetime.now().strftime('%M')

if data[0] > '22' and data[1] > '30':
    print(f'Agora são {data[0]}:{data[1]}')
    print('Restaurante Fechado')
    print('Volte sempre!')
else:
    idades = []
    desconto = 0
    preco_entrada = 0
    linhas('Bem vindo(a) ao Restaurante!')

    print('CADASTRO DE PESSOAS')
    pessoas = int(input('São quantas pessoas?\n>>> '))
    while pessoas <= 0:
        pessoas = int(input('Por favor, digite corretamente\n>>> '))

    for pessoa in range(pessoas):
        idade = int(input(f'Digite a idade da pessoa {pessoa+1}\n>>> '))
        while idade <= 0 or idade > 120:
            idade = int(input(f'Idade excedeu o limite.\nDigite a idade da pessoa {pessoa+1}\n>>> '))

    idades.append(idade)
    preco_entrada += 15

    if idade < 10:
        desconto += 0.05
    elif idade >= 10 and idade < 18:
        desconto += 0.03
    elif idade >= 18:
        desconto += 0.02

    preco_entrada -= (preco_entrada * desconto)
    print(f'O preço por todas as pessoas é de R${preco_entrada} reais.')


    mostrar_cardapio()

total = preco_entrada + preco_comida

print(f'O preço total é de R${total} reais')



