#laços de repetição
#print('Carregando')
#print('Carregando')
#print('Carregando')

# Mostra 'Carregando' 3x no terminal
for palavra in range(1, 4):
    print('Carregando')

# Conta de um em um, até chegar em 5
for item in range(0, 6): 
    print(item)


# Conta de 0 até 5, mas pula de 2 em 2.
for item in range(0, 6, 2):
    print(item)


# Exibir cada nome:
nomes = ['Gabriel', 'Julia', 'Maria', 'João']
for nome in nomes:
    print(nome)