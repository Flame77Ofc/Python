# Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. Faça um programa que leia nome, sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
# - Homens ganham 5% de desconto
# - Mulheres ganham 13% de desconto

nome = input('Digite o seu nome: ').strip().title()
sexo = input(f'{nome}, Digite o seu sexo [M/F]: ').strip().upper()
while sexo not in ['M', 'F']:
    sexo = input(f'{nome}, Digite corretamente [M/F]: ').strip().upper()
valor = float(input('Qual foi o valor das compras? '))

if sexo == 'M':
    desconto = valor * 0.05
    preco = valor - desconto
    print(f'Como você é homem, o preço final da compra com desconto será de R${preco} reais')
elif sexo == 'F':
    desconto = valor * 0.13
    preco = valor - desconto
    print(f'Como você é mulher terá um super desconto de 13%, então sua compra agora custa R${preco} reais!')