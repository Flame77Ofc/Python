# cont = 1
# while True:
#     print(cont)
#     if cont == 5:
#         break
#     cont = cont + 1

nomes = ['Carlos', 'Alberto', 'Marcos', 'Pedro', 'João', 'Gabriel', 'Bernardo', 'Julia', 'Amanda', 'Terezinha']

for nome in nomes:
    if nome == 'Gabriel':
        print(nome + ',', nomes.index('Gabriel'))  # Mostra o índice de 'Gabriel'
        break