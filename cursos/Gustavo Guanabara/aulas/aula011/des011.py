boletim = []

i = 0
while True:
    i += 1

    nome = input("Digite o nome do(a) aluno(a):\n>>>").strip().title()
    n1 = float(input("Digite a primeira nota do(a) aluno(a):\n>>>"))
    while n1 < 0 or n1 > 10:
        n1 = float(input("Digite a primeira nota corretamente:\n>>>"))

    n2 = float(input("Digite a segunda nota do(a) aluno(a):\n>>>"))
    while n2 < 0 or n2 > 10:
        n2 = float(input("Digite a segunda nota corretamente:\n>>>"))

    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])

    continuar = input('Deseja continuar? [S/N]:\n>>>').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Digite corretamente! [S/N]:\n>>>').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

print(f'{"Pos":<8}{"Nome:":<10}{"Notas:":<12}{"Média":<15}\n' + "-"*38)
for cont in range(i):
    print(f'{cont+1:<6}  {boletim[cont][0]:<7}   {boletim[cont][1]}   {media}')
