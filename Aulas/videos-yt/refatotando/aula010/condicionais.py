# Estruturas condicionais
sede = True

if sede:
    print('Beber água')
else:
    sede = False
    print('Satisfeito')


quente = True

if quente:
    print('Colocar regata')
else:
    print('Colocar casaco')


temperatura = 19

if temperatura >= 30:
    print('Quente')
elif temperatura >= 14:
    print('Frio')
else:
    print('Neve')




carro = True
moto = False

if carro or moto:
    print('Dirigir')
else:
    print('Ir à loja comprar um automóvel')




meio_dia = True
saude_boa = True

if meio_dia and saude_boa:
    print("Vou caminhar")
else:
    print("Vou ficar em casa")




num1 = int(input("Digite um número "))
num2 = int(input("Digite um número "))

if num1 == num2:
    print('Os números são iguais')
elif num1 > num2:
    print('O número 1 é maior que o número 2')
elif num1 < num2:
    print('O número 1 é menor que o número 2')