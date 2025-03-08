# Funções
# Calcular imc
def imc(peso, altura):
    imc = peso/(altura**2)
    if imc < 18.5:
        print('Magreza')
    elif imc >= 18.5 and imc <= 24.9:
        print('Normal')
    elif imc >= 25.0 and imc <= 29.9:
        print('Sobrepeso')
    elif imc >= 30.0 and imc <= 39.9:
        print('Obesidade')
    else:
        print('Muito acima da obesidade')
imc(32.0, 1.50)