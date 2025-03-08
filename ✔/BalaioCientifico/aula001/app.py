# Arrays
frutas = ['banana', 'maçã', 'laranja', 'abacaxi', 'uva']
saldoAlunos = [500, 2500, 7350, 1290, 45000]
numPacientes = [23, 54, 36, 45, 12, 34]
# Método para contar: utiliza-se o len()
print(len(frutas))
print(len(saldoAlunos))
print(len(numPacientes))

# Também é possível usar o len para contar caracteres:
print(len('Testando'))


# Acessando um item da lista
print(frutas[2])
# Acessando múltiplos elementos da lista:
print(frutas[0:4])
print(frutas)


# Adicionar novo elemento na lista
frutas.append('abacate')
print(frutas)

# Juntar listas
saldoAlunos.extend(numPacientes)
print(saldoAlunos)