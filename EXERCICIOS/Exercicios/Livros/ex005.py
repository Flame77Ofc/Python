# Escreva um algoritmo que leia a idade em ano, mes e dias e mostre a idade em dias

anos = int(input('Digite os anos: '))
meses = int(input('Digite os meses: '))
dias = int(input('Digite os dias: '))

def mostra_dias(anos, meses, dias):
    dias = (anos * 365) + (meses * 30) + dias
    return dias

print(mostra_dias(anos, meses, dias))
