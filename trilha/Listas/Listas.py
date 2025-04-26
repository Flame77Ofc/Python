# Listas
cores = ['azul', 'vermelho', 'amarelo', 'verde']
len(cores) # Mostra quantos itens a lista tem.

elementos = ['Água', 'Fogo', 'Terra', 'Vento']
#               0      1        2        3
elementos[1] # Pelo índice
elementos[1:3] # De um índice até outro


# Adicionando
comidas = ['Arroz', 'Feijão', 'Macarrão', 'batata', 'pizza', 'carne']
comidas.append('abóbora') # Adicionar um elemento no último índice
comidas.insert(3, 'alface') # Adicionar um elemento no índice especificado

# Deletar determinado item pelo índice
nomes = ['Maria', 'José', 'Alberto']
del nomes[2]

# Remover determinado item pelo valor
recibo = [560, 345, 120, 155]
recibo.remove(560)

# Remover todos os itens do índice:
jogadores = ['proplayer123', 'mariazinhajj43', 'arthur6673']
jogadores.clear()

# Remover o último item 
frutas = ['abacaxi', 'pera', 'uva']
frutas.pop()

# Juntar listas
comprasMesJaneiro = [650, 125, 1200, 450, 45, 75]
comprasMesFevereiro = [430, 120, 430, 20, 340]
comprasMesJaneiro.extend(comprasMesFevereiro)


# Conta quantas vezes um item aparece
jogadoresFut = ['CR7', 'Messi', 'Pelé', 'Maradona', 'CR7']
jogadoresFut.count('CR7')


# Ordena os elementos da lista em ordem crescente por padrão. (Ordem decrescente: lista.sort(reverse=True))
numeros = [5, 9, 1, 2, 4, 3, 7, 6, 8]
numeros.sort(reverse=True)


# Inverte os itens da lista
nums2 = [1, 5, 3, 7, 2, 8, 4]
nums2.reverse()
print(nums2)