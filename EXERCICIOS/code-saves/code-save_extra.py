# Para cada 6 cafés que uma pessoa compra, ganha +1 café extra. Crie uma função que faça isso
def cafeteria(cafes):
  gratis = cafes // 6
  return cafes + gratis
print(cafeteria(2))
print(cafeteria(12))
print(cafeteria(37))


# Para cada 1 litro de água, recebe +0.5 mls de água
def adquirir(agua):
  extra = (agua // 1) * 0.5
  return agua + extra
print(adquirir(5))
print(adquirir(14))
print(adquirir(0.6))
print(adquirir(1))