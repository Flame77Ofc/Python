# Crie uma função que simule a chance de ser impostor no Among Us. Considere a fórmula: (numero_impostores / quantidade_jogadores) * 100
def AmongUs(impostores: int, jogadores: int) -> int:
  formula = round((impostores / jogadores) * 100)
  return f'{formula}%'
print(AmongUs(2, 16))
print(AmongUs(1, 10))
print(AmongUs(2, 5))
