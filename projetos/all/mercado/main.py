carrinho = {}

def view():
    print('COMPRAS'.center(30, '='))
    for produto, preco in carrinho.items():
        print(f'{produto} {preco}')
    print('='*30)

while True:
    print("Selecione o menu:\n[1]: Adicionar item\n[2]: Remover item\n[3]: Ver carrinho\n[4]: Sair")
    menu = int(input('>>>'))

    while menu > 4 or menu < 1:
        print('Por favor, selecione uma das opções')
        menu = int(input('>>>'))

    if menu == 1:
        produto = input('Digite o produto que deseja adicionar:\n>>>').strip().title()
        preco = int(input('Digite o preço do produto:\n>>>'))
        carrinho.update({produto: preco})
        print('Item adicionado com sucesso')
    elif menu == 2:
        remover = input('Qual produto deseja remover?\n>>>').strip().title()
        while remover not in carrinho:
            print('Lista de compras:')
            view()
            remover = input('Este produto não está no carrinho! Digite novamente:\n>>>').strip().title()
        del carrinho[remover]
        print('Item removido com sucesso')
    elif menu == 3:
        view()
    elif menu == 4:
        if len(carrinho) == 0:
            print('Nenhum item no carrinho')
        else:
            view()
        break
