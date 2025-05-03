cadeiras = int(input('Quantas cadeiras tem na sua sala?: '))
alunos = int(input('Quantos alunos tem na sua sala?: '))

assentos = cadeiras - alunos

if cadeiras < alunos:
    print('Há mais cadeiras do que alunos.')
elif cadeiras == alunos:
    print('Todos os assentos ocupados!')
else:
    print(f'Há {assentos} assentos disponíveis')