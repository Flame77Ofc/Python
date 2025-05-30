import aula014.des001.moeda as m

preco = float(input('Digite o preço:\n>>>'))
print(f'Aumentando em 10%, o preço seria {m.aumentar(preco, 10)}')
print(f'Diminuindo em 13%, o preço seria {m.diminuir(preco, 13)}')
print(f'Duplicando, o preço seria {m.dobro(preco)}')
print(f'A metade do preço seria {m.metade(preco)}')