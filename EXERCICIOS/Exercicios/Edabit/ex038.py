# Para cada 6 cafés que uma pessoa compra, ganha +1 café extra. Crie uma função que faça isso
def cafeteria(cafes):
  gratis = cafes // 6
  return cafes + gratis
print(cafeteria(2))
print(cafeteria(12))
