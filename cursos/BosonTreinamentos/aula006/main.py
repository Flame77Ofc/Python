# Sets: Não aceitam valores duplicados, são aleatórios
planetas_anoes = {'Makemake', 'Hamea', 'Plutão', 'Eris'}
print(len(planetas_anoes))
# not in e in
print('Makemake' in planetas_anoes)
print('Lua' not in planetas_anoes)

for astro in planetas_anoes:
    print(astro.upper())

# Unindo e juntando sets    
astros1 = {'terra', 'marte', 'jupiter', 'sol'}
astros2 = {'terra', 'marte', 'jupiter', 'sol', 'lua'}
print(astros1 | astros2)
print(astros1.union(astros2))

# adicionando elementos
astros = {'Lua', 'Marte', 'Jupiter'}
astros.add('Sol')
print(astros)

# removendo elementos
astros.remove("Lua") # Remove um elemento especificado
print(astros)
astros.pop() # Remove um valor aleatório, pois sets não são ordenados.
print(astros)