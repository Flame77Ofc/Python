idades = 0
maior = 0
homem = ''
feminino = 0

for i in range(1, 5):
    print(f"PESSOA {i}")

    nome = input('Digite o nome da pessoa: ').title()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Qual o sexo? [M/F]').upper()
    idades += idade 

    if sexo == 'M' and idade > maior:
        maior = idade
        homem = nome
    elif sexo == 'F':
        if idade < 20:
            feminino += 1
media = idades / 4
print(f'A media das idades é {media}')
print(f'O homem mais velho é {homem} e tem {maior} anos')
print(f'Mulheres com menos de vinte anos: {feminino}')

