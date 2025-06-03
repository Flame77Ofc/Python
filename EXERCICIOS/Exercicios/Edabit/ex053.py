# Dada uma lista, retorne True se há mais números ímpares do que números pares, se não, retorne False
def mais(lista):
  pares = impares = 0
  for elemento in lista:
    if elemento % 2 == 0:
      pares += 1
    else:
      impares += 1
  return True if impares > pares else False
print(mais([1]))
print(mais([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(mais([13452394823795273847528572346]))
