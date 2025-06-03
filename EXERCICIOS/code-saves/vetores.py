pessoas = [['Maria', 25], ['Gustavo', 13]]

for i in pessoas:
    print(f'{i[0]} tem {i[1]} anos de idade')
total = 0
for p in pessoas:
    total += p[1]
    
print(total)
