quantidade = int(input("Quantos vendedores há?: "))

nomes = []
vendas = []
total = 0

for i in range(quantidade):
    nome = input('Digite o nome do vendedor: ')
    nome = nome.title()
    venda = int(input(f"Quanto que {nome} vendeu?: "))

    nomes.append(nome)
    vendas.append(venda)
    total += venda


for i, nome in enumerate(nomes):
    print(f'{i} | nome: {nomes[i]} | vendeu: {vendas[i]}')
print(f'Total de vendas: {total}')