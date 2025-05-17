# Supermercado: O Usuário informa a quantidade de produtos, e em seguida, o programa pergunta quais são os produtos, junto com os preços.

quantidade = int(input("Digite a quantidade de produtos: "))

lista_produtos = []
total = 0

for i in range(1, quantidade+1):
  produto = input(f"Digite o nome produto {i}: ")
  lista_produtos.append(produto)
  preco = float(input(f"Digite o preco do produto {i}: "))
  total += preco

lista_produtos = ", ".join(lista_produtos)
print(f"O total dos produtos são: {total} reais.")
print(f"Os produtos são: {lista_produtos}")