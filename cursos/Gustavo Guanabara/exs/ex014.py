# Um programa que imprime o resultado a partir de algumas informações sobre alugueis de carros
dias = int(input('Quantos dias está alugado? '))
km = int(input('Quantos Kms rodados? '))
pagamento = (dias * 60) + (km * 0.15)
print(f'O total a pagar é {pagamento} reais')