# Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

velocidade = int(input('Digite a velocidade do carro: '))
multa = 0
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f'Sua multa é de R${multa} reais por ultrapassar o limite!')
else:
    print('Parabéns pela sua velocidade!')