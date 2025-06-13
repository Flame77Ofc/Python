# Lista de Compras
import time

def adicionar():
    produto = input('Digite o produto/alimento: ').strip().title()
    preco = float(input('Digite o preço do produto: '))

    carrinho[produto] = preco

def remover():
    if len(carrinho) > 0:
        remover = input('Digite o produto/alimento que deseja remover: ').strip().title()
        if remover in carrinho:
            carrinho.pop(remover)
        else:
            print('Não foi possível encontrar este item. Tente novamente.')
    else:
        print('Não é possível remover itens com o carrinho vazio.')
    
def caixa():
    if len(carrinho) > 0:
        total = 0
        for valor in carrinho.values():
            total += valor
        print('Analisando cada item', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)
        print(f'\nO preço total de todos os itens é de R${round(total, 2)}')
        return True
    else:
        print('Não é possível ir ao caixa sem nenhum item.')
        return False


def visualizar():
    if len(carrinho) > 0:
        print('=== LISTA DE COMPRAS ===')
        for chave, valor in carrinho.items():
            print(f'{chave:<25}{valor}')
    else:
        print('Nenhum item no carrinho.')

carrinho = {}

while True:
    print('\n=== MENU ===')
    print('1: Adicionar um item ao carrinho')
    print('2: Remover um item do carrinho')
    print('3: Ver o carrinho')
    print('4: Ir ao caixa')
    print('5: Sair')

    menu = int(input('Digite o menu:\n>>>'))
    while menu not in range(1, 6):
        menu = int(input('Digite corretamente.\nDigite o menu:\n>>>'))

    if menu == 1:
        adicionar()
    elif menu == 2:
        remover()
    elif menu == 3:
        visualizar()
    elif menu == 4:
        if caixa():
            break
    elif menu == 5:
        break
