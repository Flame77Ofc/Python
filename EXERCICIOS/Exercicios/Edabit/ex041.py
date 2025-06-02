# Crie uma função que conte quantas letras maiúsculas possui uma string
def maiusculas(string: str) -> int:
  total = 0
  for i in string:
    if i.isupper():
      total += 1
  return total if total >= 1 else 'A string não possui nenhuma letra maiúscula'
print(maiusculas('Há MuiTas Aves Naquela ÁrvoRe'))
print(maiusculas('os oceanos são belos'))
