# Crie um programa que solicite a entrada de 5 números pelo usuário, armazenando-os em um vetor, e então monte outro vetor com os valores do primeiro multiplicados por 5. Exiba os valores dos dois vetores na tela, simultaneamente, em duas colunas (um em cada coluna), uma posição por linha.
principal = [[], []]   
vetor = []
multiplica = []

for i in range(5):
    numero = int(input(f'Digite o número {i+1}: '))
    vetor.append([numero])

numero = 0
for x in vetor:
    multiplica.append([vetor[numero][0] * 5])
    numero += 1

principal[0] = vetor
principal[1] = multiplica
for i in principal:
    print(i)
