# Crie uma função que retorna True se duas torres podem se atacar se não retorne False
def torre(posicao1, posicao2):
  return True if (posicao1[1] == posicao2[1]) or (posicao1[0] == posicao2[0]) else False
print(torre('A8', 'E8'))
print(torre('H4', 'H8'))
print(torre('A1', 'B2'))
print(torre('H4', 'H8'))
print(torre('H4', 'H8'))
