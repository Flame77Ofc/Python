# Listas
notas = [5,6,3,4,10,4,9]
print(notas)

n1 = [4,1,7,2,9,1]
n2 = [3,8,1,4,4,9]
valores = n1 + n2
print(sorted(valores)) # Mostra uma versão ordenada (crescente) da lista, sem modificar ela.
print(sorted(valores, reverse=True)) # Mostra uma versão ordenada (decrescente) da lista, sem modificar ela.
print(sum(valores)) # Soma os valores da lista
print(min(valores)) # Mostra o menor valor da lista
print(max(valores)) # Mostra o maior valor da lista
print(1 in valores) # Mostra se determinado valor está na lista, retorna um valor booleano