# Listas são mutáveis, permitindo alterar seus elementos.
animais = ['Galinha', 'Gato', 'Crocodilo', 'Rinoceronte']
animais = ', '.join(animais) # Juntando os itens da lista.
animais

receita = 'leite, ovos, farinha, massa, fermento'
receita = receita.split() # Separando cada item individualmente.
receita

text = list('Python')
text

# acessando um elemento pelo índice
cores = ['Azul', 'Vermelho', 'Amarelo', 'Verde', 'Roxo', 'Branco', 'Preto', 'Bege']

cores[0]
cores[2:6]
cores[3:7]

'Rosa' in cores # False
'Azul' in cores # True
'Amarelo' not in cores # False

for cor in cores: # Listas são iteráveis: É possível acessar cada elemento individualmente com um iterador usando o loop for
    pass # print(cor)

# Alterando o valor de uma lista pelo índice
cores[2] = 'Cinza'
cores


# FUNÇÕES COM LISTAS
# lista.insert(índice, elemento): Adiciona um elemento no índice especificado.
lista = ['Pedro', 'João', 'Rafael']
lista.insert(2, 'Maria')

# lista.pop(índice opcional): Se especificar o índice: Remove o elemento do índice especificado; Se não especificar o índice: Remove o último elemento.
lista.pop() # Sem especificar o índice -> Remove o último elemento
lista.pop(1) # Especificando o índice -> Remove o elemento em que o índice está.

# lista.append(elemento): Adiciona um elemento no último índice da lista.
lista.append('Lucas')

# sum: Soma todos os números da lista.
lista = [3, 8, 12, 5]
soma = sum(lista)

min(lista) # Retorna o menor número da lista
max(lista) # Retorna o maior número da lista

# lista.extend: Junta duas listas.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2) # [1, 2, 3, 4, 5, 6]

# sort: ordena os elementos da lista em ordem crescente
lista.sort()

# List Comprehensions -> Um atalho para o for loop
numeros = [1, 2, 3, 4, 5, 6]

mais1 = [num+1 for num in numeros] # List Comprehensions -> Atalho

for num in numeros: # Loop for
    print(num + 1)

