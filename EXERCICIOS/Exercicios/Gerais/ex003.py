# Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desses nomes na tela. Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa em que o usuário os digitou, um por linha.

lista = [] 
for i in range(5):
    nome = input(f'Digite o nome {i+1}: ').strip().title()
    lista.append([nome])

print(f'A lista dos nomes é {lista}')
print(f'A lista em ordem reversa é: ')
lista_reversa = reversed(lista)
for i in lista_reversa:
    print(i)
