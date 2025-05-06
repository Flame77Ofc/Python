quantidade = int(input("Digite quantos alunos há: "))

nomes = []
notas = []

for i in range(1, quantidade + 1):
    nome = input(f'Digite o nome do aluno {i}: ')
    nome = nome.title()
    nota = int(input(f'Qual a nota de {nome}? '))

    while nota < 0 or nota > 10:
        print('A nota deve ser entre 0 e 10!')
        nota = int(input(f'Qual a nota de {nome}? '))
        continue

    nomes.append(nome)
    notas.append(nota)


soma = sum(notas)
media = soma / len(notas)

for nome, nota in zip(nomes, notas):
    pass
print(f'A soma das notas é {soma}')
print(f'A média das notas é {media}')


with open('notas.txt', 'a') as arquivo:
    arquivo.write(f'{str(nome)} {str(nota)}\n')