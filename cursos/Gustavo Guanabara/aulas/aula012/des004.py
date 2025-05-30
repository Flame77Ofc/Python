info = dict()
total = 0
i = -1
repet = 0
mulheres = []

while True:
    repet += 1
    i += 1
    nome = input('Digite o nome da pessoa:\n>>>').strip().title()
    idade = int(input('Digite a idade da pessoa:\n>>>'))
    
    while idade > 100 or idade < 0:
        idade = int(input('Digite a idade corretamente:\n>>>'))

    sexo = input('Digite o sexo da pessoa [M/F]:\n>>>').strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input('Digite o sexo corretamente [M/F]:\n>>>').strip().upper()

    if sexo == 'F':
        mulheres.append(nome)

    info[i] = [nome, int(idade), sexo]

    continuar = input('Deseja continuar [S/N]?\n>>>').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Digite corretamente:\n>>>').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

print(info)
print(f'Ao todo temos {i+1} pessoas cadastradas')
for a in range(i+1):
    total += info[a][1]
total /= repet
print(f'A média das idades é {total} anos')
print(f'As mulheres cadastradas foram {', '.join(mulheres)}')
# print(f'A média de idade é {info}')