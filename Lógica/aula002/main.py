ex1 = 'Criar uma lista que, exiba todos os valores da lista, mas se encontrar a idade 12, para de exibir os valores'
print(ex1)
age = [34, 56, 78, 12, 39, 54, 15, 22, 76, 90, 31, 28, 40, 67]
for item in age:
    print(item)
    if item == 12:
        break

ex2 = '\nCriar uma lista que, exiba todos os valores da lista, mas se encontrar o valor aleatório, para de exibir.'
print(ex2)
import random
age = [34, 56, 78, 12, 39, 54, 15, 22, 76, 90, 31, 28, 40, 67]
rand_age = random.choice(age)
for item in age:
    print(item)
    if item == rand_age:
        break