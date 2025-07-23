# Dicionário: Possui chave e valor, onde chave se parece com o índice de uma lista e o valor se parece com o elemento. É mutável, odernado e não aceita repetidos nas suas chaves.

# Primeira maneira
dicionario = {
    "nome": "Gabriel",
    "idade": 12,
    "cidade": "Paris"
}
print(dicionario)

# Segunda maneira
dicionario = dict(nome="Lucas", idade=27, cidade="Florida")
print(dicionario)


# Não pode haver chaves repetidas (O dicionário sobrebõem com a chave mais recente)
cores = {
    "cor": "Azul",
    "cor": "Vermelho"
}
print(cores) # {'cor': 'Vermelho'}


print("\n\n")

# Iterando sobre a chave, o valor e ambos (itens).
informacoes = {
    "nome": "Felipe",
    "idade": 15,
    "gênero": "masculino"
}

for chave in informacoes.keys():
    print(chave)

for valor in informacoes.values():
    print(valor)

for chave, valor in informacoes.items():
    print(chave, valor)