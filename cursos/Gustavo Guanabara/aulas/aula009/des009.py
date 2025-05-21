idades = 0
homens = 0
mulheres20 = 0

while True:
    idade = int(input("Digite a idade: "))
    while idade < 0 or idade > 100:
        idade = int(input("Digite a idade corretamente: "))

    sexo = input("Digite o sexo: ").upper()
    while sexo not in ['M', 'F']:
        sexo = input("Digite o sexo: ").upper()
    
    if idade > 18:
        idades += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres20 += 1

    continuar = input("Deseja continuar? [S/N]: ").upper()
    while continuar.upper() not in ['S', 'N']:
        continuar = input("Deseja continuar? [S/N]: ").upper()
    if continuar.upper() == 'N':
        break

    
print(f'Há {idades} {'pessoa' if idades == 1 else 'pessoas'} com mais de 18 anos.')
print(f'Há {homens} {'homem' if homens == 1 else 'homens'}.')
print(f'Há {mulheres20} {'mulher' if mulheres20 == 1 else 'mulheres'} com menos de 20 anos.')