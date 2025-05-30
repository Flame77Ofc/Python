# Lists Comprehensions
# <expressão> for <elemento> in <iterável> if <condição>
lista = ['Pato', 'Coelho', 'Dinossauro', 'Macaco', 'Rinoceronte', 'Baleia', 'Besouro', 'Tartaruga']
new_list = [f"{x}✅" if 'a' in x.lower() else f'{x}❌' for x in lista]
# ['Pato✅', 'Coelho❌', 'Dinossauro✅', 'Macaco✅', 'Rinoceronte❌', 'Baleia✅', 'Besouro❌', 'Tartaruga✅']




# Gera um número aleatório entre 1 a 7, 10 vezes
from random import randrange
a = [randrange(1, 7) for numero in range(10)]
# [2, 3, 2, 1, 1, 5, 2, 4, 3, 5]





# Duas maneiras diferentes de filtrar valores.
# List Comprehensions e iteração
# funcionarios = ['Amanda', 'Felipe', 'Maria', 'Pedro', 'João', 'Carlos', 'Matheus']
# vendas = [35, 155, 360, 450, 725, 125, 390]

"""funcionarios = []
vendas = []
while True:
    funcionario = input('Digite o nome do funcionário:\n>>>').strip().title()
    venda = int(input(f'Digite a venda de {funcionario}:\n>>>'))

    funcionarios.append(funcionario)
    vendas.append(venda)

    continuar = input('Deseja continuar? [S/N]\n>>>').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Digite corretamente:\n>>>').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

for id, x in enumerate(funcionarios):
    if vendas[id] >= 250:
        print(id, x, vendas[id])
    elif vendas[id] < 250:
        print(id, x, vendas[id])



a = [[x, vendas[id]] for id, x in enumerate(funcionarios) if vendas[id] >= 250]
b = [[x, vendas[id]] for id, x in enumerate(funcionarios) if vendas[id] < 250]
print(f'Lista de funcionários que fizeram mais de 250 vendas: {a}')
print(f'Aqueles que fizeram menos de 250: {b}')

"""



def dobro(lista):
    for item in lista:
        print(item * 2)
dobro([4, 7, 8, 12, 3, 6])