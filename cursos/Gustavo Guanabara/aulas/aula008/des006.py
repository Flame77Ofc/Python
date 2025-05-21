import datetime
ano = datetime.datetime.now().year

menor = 0
maior = 0

for i in range(7):
    nascimento = int(input("Qual a data de nascimento da pessoa? "))
    nascimento -= ano
    if nascimento < 21:
        menor += 1
    else:
        maior += 1

print(f'Pessoas de maior de idade: {maior}')
print(f'Pessoas de menor de idade: {menor}')