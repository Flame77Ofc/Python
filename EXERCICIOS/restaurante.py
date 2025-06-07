# Crie um restaurante que simule um restaurante real. Deve verificar se o horário passa das 10 horas e 30 minutos da noite. Caso esteja mais que 10 horas, o programa irá mostrar 'Restaurante Fechado' e deverá ser o fim do programa. Deve ter um menu de opções:
"""
[1]: Ver o cardápio
[2]: Ver que horas são

"""
import datetime
hora = datetime.datetime.now().strftime('%H')
minuto = datetime.datetime.now().strftime('%M')

data = hora, minuto
fechamento = data[0] > '22' and data[1] > '30'
print(f'Agora são {data[0]}:{data[1]}')

if fechamento:
    print('Restaurante Fechado')
else:
    print('Restaurante Aberto')