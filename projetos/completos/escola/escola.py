quantidade = int(input("Digite quantos alunos há: "))

geral = []
nomes = []
notas = []

for i in range(1, quantidade + 1):
    nome = input(f'Digite o nome do aluno {i}: ').strip().title()
    nota = int(input(f'Qual a nota de {nome}? '))

    while nota < 0 or nota > 10:
        print('A nota deve ser entre 0 e 10!')
        nota = int(input(f'Qual a nota de {nome}? '))
        continue

    geral.append([nome, nota])


try:
    with open('escola/notas.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{geral}\n')
except:
    print('Erro desconhecido.')
else:
    print('Cadastro realizado com sucesso!')