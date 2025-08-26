# Crie um programa que verifica em que posições há disjuntores ligados e desligados
disjuntores = [True, False, False, False, True, True, False, False, True, False]

pos = 0
for disjuntor in disjuntores:
    if disjuntor:
        print(pos)

    pos += 1