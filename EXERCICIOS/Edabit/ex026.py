# Crie um programa que tem a possibilidade de converter reais para doláres e vice-versa. Considere que: 1 dolár = R$6
def conversor(tipo: str, quantidade: float) -> float:
    tipo = tipo.lower()
    if tipo == 'doláres' or tipo == 'dolares':
      conversao = round(quantidade * 6, 2)
      return f'Você tem R${conversao} reais'
    elif tipo == 'reais':
      conversao = round(quantidade / 6, 2)
      return f'Você tem ${conversao} doláres'
    else:
      return 'Algo de errado. Tente novamente'

print(conversor('dolares', 5))
print(conversor('reais', 5))
print(conversor('dolares', 12000))
print(conversor('reais', 55600))
print(conversor('reais', 65.90))
