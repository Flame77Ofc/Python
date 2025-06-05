# Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.
def idade(anos: int, meses: int, dias: int) -> int:
  dias += anos * 365
  dias += meses * 30

  return dias
print(idade(14, 0, 0))
print(idade(16, 2, 18))
