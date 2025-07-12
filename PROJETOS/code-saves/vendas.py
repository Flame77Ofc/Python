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

print(f'{"ID":<3} {"Nomes":<20} {"Vendas":<10}')
for i, nome in enumerate(nomes):
    print(f'{i+1:<3} {nomes[i]:<20} {vendas[i]:<10}')
print(f'Total de vendas: {total}')