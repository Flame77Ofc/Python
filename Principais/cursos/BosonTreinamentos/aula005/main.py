semana = {
    1: 'Segunda-feira',
    2: 'Terça-feira',
    3: 'Quarta-feira',
    4: 'Quinta-feira',
    5: 'Sexta-feira',
    6: 'Sábado',
    7: 'Domingo',
}

print(f"\n{semana}\n")
print(semana[1])
print(len(semana))

# atualizar um elemento
semana[1] = 'Sextiriana-feira'
print(semana)

# excluir um elemento
del semana[5]
print(semana)

# exibir os itens do dicioanário
print(semana.items())

for i in semana:
    print(i)

for i in semana.keys():
    print(i)

for i in semana.values():
    print(i)
for i, x in semana.items():
    print(i, x)

# apagar todos os elementos
semana.clear()

# apagar o próprio dicionário
del semana
"print(semana) # erro"
