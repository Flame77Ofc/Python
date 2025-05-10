# Os dicionários não possuem índice, apenas chave: valor. A chave é semelhante a um índice, pois identifica o elemento
Ranking = {
    1: 'Pedro Luiz',
    2: 'José Gaúcho Costa',
    3: 'Matheus Henrique',
    4: 'Rafael Moto'
#   chave: 'valor'
}
# Acessando seus valores
print(Ranking[1])
# print(Ranking[1:3]) Fatiamento não é possível em dicionários

Ranking.keys() # => Retorna as chaves do dicionário: 1, 2, 3, 4
Ranking.values() # => Retorna os elementos/valores do dicionário: 'Pedro Luiz', 'José Gaúcho Costa', 'Matheus Henrique', 'Rafael Moto'
Ranking.items() # => Retorna a chave e o valor

# Alterando seus valores
Ranking[1] = 'Maria de Moura'
print(Ranking)

# Imprime a chave e o valor do dicionário com uma visualização melhor
for chave, valor in Ranking.items():
    print(chave, valor)

# del: deleta um elemento ou o próprio dicionário
"""del Ranking[1]
del Ranking"""

# clear: Limpa todo o dicionário
"Ranking.clear()"