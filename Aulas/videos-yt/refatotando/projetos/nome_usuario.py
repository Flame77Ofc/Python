nome = input('escolha um username ')
lista_nomes = ['PedrozinnGamer46777', 'Mariazinha99', 'Flame']
while True:
    if nome in lista_nomes:
        nome = input('Por favor, escolha outro username. Este já está incluso ')
    else:
        lista_nomes.append(nome)
        print(lista_nomes)
        break