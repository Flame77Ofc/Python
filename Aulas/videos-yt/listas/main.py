# Listas
nomes = ['João', 'Maria', 'Tereza']
# Índices   0       1         2
print(nomes)
print(nomes[2])
print(f"Alunos: {len(nomes)}")


notas = [8, 4, 10]
#Índices 0  1   2
print(notas)
print(notas[1])
print(f"Notas: {len(notas)}")


dados = ['Pedro', 45, True, 'Maria', False, 'Roberto', 'Carlos', True, 23]
# Índices   0      1    2     3       4         5          6      7    8
print(dados)
print(dados[6])
print(f"Total de dados: {len(dados)}")


# Unir listas: Utilizando o extend
nomes.extend(notas)
print(nomes)

# In
lista = ['Marco', 'Antonio']
print('Felipe' in lista)
print('Marco' in lista)
