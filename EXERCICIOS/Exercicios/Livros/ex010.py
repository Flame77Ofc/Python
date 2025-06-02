# Crie um programa que verifica se o saldo da pessoa - o produto é maior que o 0 e diga se é possível realizar o pagamento
def loja(saldo, compra):
  preco = saldo - compra
  print(f'Preço final: {preco}')
  return 'É possível realizar o pagamento' if preco >= 0 else 'Não é possível realizar o pagamento'

luis = loja(3400, 1200)
print(luis)

vitoria = loja(12000, 5600)
print(vitoria)

amanda = loja(2340, 7850)
print(amanda)
