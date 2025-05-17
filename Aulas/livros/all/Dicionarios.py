# Dicionários: Apresenta chaves e valores, que podem ser acessados e modificados
compras = {
  'Arroz': 3.45,
  'Feijão': 2.90,
  'Macarrão': 4.50
}
print(compras)
print(compras['Arroz'])

compras['Sushi'] = 1.35
compras['Tomate'] = 0.35
print(compras)


# keys: Chaves do dicionário(Indetificadores)
print(compras.keys())

# values: Valores ou elementos do dicionário
print(compras.values())


# Dicionários
dicionario = {
  1: "Maçã",
  2: "Laranja",
  3: "Morango",
  4: "Pepino",
  5: "Alface"
}

dicionario[6] = "Beterraba"
print(dicionario)
dicionario[1] = "Pera"
print(dicionario)

# del: deleta um elemento ou o próprio dicionário
del dicionario[2]
print(dicionario)
"del dicionario" # deleta o dicionário

# keys: exibe as palavras-chave (identificadores) dos elementos.
keys = dicionario.keys()
print(keys) # 1,3,4,5,6
# values: exibe os elementos que são identificados pelas palavras-chaves
values = dicionario.values()
print(values) # 'Pera', 'Morango', 'Pepino', 'Alface', 'Beterraba'

# in e not in: verifica se alguma palavra-chave ou elemento está no dicionário
print(1 not in keys) # O identificador 1 não está no dicionário? False
print(12 in keys) # O identificador 12 está no dicionário? False
print("Morango" in values) # O elemento Morango está no dicionário? True
print("Banana" not in values) # O elemento Banana não está no dicionário? True


string = 'lanchonete'
print(string.center(73, '-'))

lanchonete = {
  "Salgado": 4.50,
  "Lanche": 6.50,
  "Suco": 3.00,
  "Refrigerante": 3.50,
  "Doce": 1.00
}
print(lanchonete.items())

for i, x in lanchonete.items():
  print(i + ':', x)

alunos = {
  "Aluno1": 8,
  "Aluno2": 3,
  "Aluno3": 4,
  "Aluno4": 7,
  "Aluno5": 10,
}
media = sum(alunos.values())
print(media / len(alunos))



















# Dicionários possuem chave e valor, onde as chaves são identificadores(tipo índices em listas) para os valores/elementos.
frutas = {
    'Maçã': 3.50,
    'Laranja': 2.99,
    'Abacaxi': 4.50,
    'Goiaba': 2.99,
    'Uva': 1.99
#   chave: valor
}

print(frutas['Maçã']) # Imprime o valor da chave
frutas['Goiaba'] = 5.99
print(frutas)

quantidade = len(frutas)
print(quantidade)

chaves = frutas.keys()
# print(chaves)
valores = frutas.values()
# print(valores)
itens = frutas.items()
# print(itens)

for chave, valor in itens: # Imprime os itens em um efeito visual melhor
    print(chave, valor)

# deleta um elemento
del frutas['Uva'], frutas['Abacaxi']
print(frutas)

# popitem: remove o último elemento do dicionário
frutas.popitem()
print(frutas)

# pop: remove um item pela chave
frutas.pop('Maçã')

print(frutas)
# get('valor', 'valor se não for encontrado'): Retorna o valor da chave
print(frutas.get('Abacaxi', 'Fruta não foi encontrada'))


# limpa todos os valores
frutas.clear()