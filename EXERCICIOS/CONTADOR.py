try:
    with open('arquivo.txt', "r") as f:
        numero = int(f.read())
except:
    numero = 0

numero += 1

with open('arquivo.txt', "w") as f:
    f.write(str(numero))
