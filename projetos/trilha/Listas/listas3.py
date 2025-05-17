# Listas
vendas = [123, 27, 98, 56, 87, 34]
# Somar o total de vendas
total_vendas = sum(vendas)
print(total_vendas)

# quantidade de itens na lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

# max e min
print(max(vendas))
print(min(vendas))

# acessar posição
print(vendas[4])
print(vendas[-1]) # acessar o último elemento


# Verificar se existe tal item numa lista > retorna booleano
# lista_produtos = ['iphone', 'airpod', 'ipad', 'macbook']
# produto_procurado = input('Digite o produto: ')
# produto_procurado = produto_procurado.lower()
# print(produto_procurado in lista_produtos)


# Manipulação de listas
# adicionar um item:
lista = ['João', 'Maria', 'Antônio']
lista.append('Carlos')
print(lista)

# remover um item:
lista.remove('João') # pelo nome
print(lista)
lista.pop(2) # pelo índice
print(lista)

# editar um item:
lista[1] = 'Pedro'
print(lista)

# contar quantas vezes um item aparece na lista
lista = ['Maria', 'Maria', 'Maria', 'Pedro', 'Pedro', 'João']
print(lista.count('Maria'))

# ordenar uma lista
precos = [450, 250, 150, 600, 1200, 3400, 120, 340, 760, 455]
print(sorted(precos))

lista_nomes = ['Fernando', 'Maria', 'Gabriel', 'Julia']
# lista_nomes.sort(reverse=True)
# print(lista_nomes)
# print(list(reversed(lista_nomes)))