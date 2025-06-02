"""Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
"""
def lanches(i, preco, lanche):
    if identificador == i:
        preco = preco
        quantidade = int(input(f'Deseja quantos {lanche}? '))
        print(f'O preço é R${preco * quantidade}')


print("""ID    Lanche              Preço
1:    Cachorro Quente     4.00,
2:    X-Salada            4.50,
3:    X-Bacon             5.00,
4:    Hambúrguer         2.00,
5:    Refrigerante        1.50"""
)

identificador = int(input('Deseja qual lanche? '))

lanches(1, 4.00, 'Cachorro Quente')
lanches(2, 4.50, 'X-Saladas')
lanches(3, 5.00, 'X-Bacons')
lanches(4, 2.00, 'Hambúrguers')
lanches(5, 1.50, 'Refrigerantes')