# IMC
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2) 

print(f'O seu IMC é {imc}')

if imc < 18.5:
    print('Abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Peso normal')
elif 25 <= imc < 30:
    print('Sobrepeso')