aluno = {
    'nome': input('Digite o nome do aluno:\n>>>').strip().title(),
    'media': float(input("Digite a média do aluno:\n>>>")),
}
print(f'O nome do(a) aluno(a) é {aluno["nome"]}')
print(f'A média do(a) aluno(a) é {aluno["media"]}')
if aluno["media"] > 6:
    aluno["situacao"] = 'Aprovado'
else:
    aluno["situacao"] = 'Reprovado'
print(f'A situação do(a) aluno(a) é {aluno["situacao"]}')

for item, valor in aluno.items():
    print(f'{item} = {valor}')