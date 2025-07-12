i = 1
while True:
    tabuada = int(input("Qual tabuada você quer? "))

    if tabuada < 1:
        break
    while i <= 10:
        print(f'{tabuada} x {i} = {tabuada * i}')
        i += 1
    i = 1
    
print("Volte sempre!")