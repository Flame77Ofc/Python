# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando 0.50 por km para viagens até 200km a 0.45 para viagens longas
# Se a distancia for menor que 200, então pagará 0.50, mas se não, pagará 0.45.
distancia = int(input("Qual será a distância em KM? "))

if distancia <= 200:
    pagamento = distancia * 0.50
else:
    pagamento = distancia * 0.45
print(f'Você tem a pagar: {pagamento}')