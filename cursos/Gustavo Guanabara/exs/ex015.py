# Escolher um aluno
import random
aluno1 = input("Digite o nome do aluno 1 ")
aluno2 = input("Digite o nome do aluno 2 ")
aluno3 = input("Digite o nome do aluno 3 ")
aluno4 = input("Digite o nome do aluno 4 ")

alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_escolhido = random.choice(alunos)

print(f'O aluno escolhido para limpar o quadro é {aluno_escolhido}')