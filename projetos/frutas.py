# O que falta: Colocar um limite de compras de batata, colocar um saldo, e criar o minijogo que cria esse saldo
# Mensagem de boas-vindas
print(f'Bem-vindo ao mercado! Escolha entre:\n1: maçã\n2: banana\n3: batata\n4: alface')

# O preço das frutas
maca = 1.50
banana = 1.39
batata = 1.69
alface = 2.50

# Armazenando o preço de cada fruta no array frutas
frutas = [maca, banana, batata, alface]

# Utilizando Tratamento de Erros e Exceções
try:
    # O código se repete, e atráves do uso do break, para o loop.
    while True:
        user = int(input('Digite o valor, por favor: '))
        if (user > 4) or (user <= 0):
            print('Um valor entre 1 a 4!')
        if (user == 1):
            print(f'Certo, o valor da maçã é {maca}')
            total_macas = int(input('Quer quantas maçãs? '))
            print(f'Ficou num total de R${round(total_macas * maca, 2)}')
            break
        if (user == 2):
            print(f'Ótimo, o valor da banana é R${banana}')
            total_bananas = int(input('Quer quantas bananas? '))
            print(f'Ficou num total de R${round(total_bananas * banana, 2)}')
            break
        if (user == 3):
            print(f'Boa escolha! o valor da batata é R${(batata)}')
            total_batatas = int(input('Quer quantas batatas? '))
            print(f'Ficou num total de R${(total_batatas * batata)}')
            break
        if (user == 4):
            print(f'Excelente! O valor do alface é R${alface}')
            total_alface = int(input('Quer quantas batatas? '))
            print(f'Ficou num total de R${round(total_alface * alface, 2)}')
            break
except:
    print('Ooops, algo deu errado!')