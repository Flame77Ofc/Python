# Set ⇒ No dicionário, os valores são representados por 'variáveis' Já no set não.
planetaAnao = {'Plutão', 'Ceres', 'Eris', 'Humea', 'Makemake'}
print('planeta anão',planetaAnao)

astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
print('astros',astros)
astros_set = set(astros)
print('astros set',astros_set)

astros1 = {'Lua', 'Vênus'}
astros2 = {'Lua', 'Vênus', 'Cometa de Halley'}
# juntar set (mesma funcionalidade, os dois códigos são da mesma funcionalidade.):
print('Juntar',astros1 | astros2)
print('Juntar',astros2.union(astros2))

astros1.add('Urano')
astros1.add('Sol')

# Remover:
# Remove: se o item não estiver na lista, dará um erro, o que não acontece com o discard
# discard >>>>>>> remove
astros1.remove('Lua')
astros1.discard('Olho de Deus')
astros1.pop() # Remove um elemento aleatório - nesse caso
print('astros 1',astros1)