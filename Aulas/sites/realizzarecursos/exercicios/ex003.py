camisa = 25
quantidade = int(input(f"Cada camisa: {camisa} reais. Quantas unidades quer? "))
total = camisa * quantidade

if quantidade <= 5:
    total = total * 0.97
if quantidade <= 10:
    total = total * 0.95
else:
    total = total * 0.93
print(round(total), 'reais')