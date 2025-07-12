# Crie um programa que verifica em que posições há disjuntores ligados e desligados
disjuntores = [True, False, False, False, True, True, False, False, True, False]

posicao = 1
for i in disjuntores:
  if i:
    print(posicao)
  posicao += 1
