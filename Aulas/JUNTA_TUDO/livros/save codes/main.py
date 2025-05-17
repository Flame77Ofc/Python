nomes = []
while True:
    nome = input('Digite um nome para ser armazenado ou digite quit para sair: ')
    nome = nome.lower()
    if nome == 'quit':
        break
    else:
        nome = nome.title()
        nomes.append(nome)
print(nomes)