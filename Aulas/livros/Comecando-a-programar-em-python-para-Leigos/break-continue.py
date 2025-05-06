# break: Utilizado para parar imediatamente um loop.
for i in range(1, 10):
  if i == 3:
    break
  print(i)

print("Fim do loop")

# continue: Utilizado para pular determinado objeto especificado.
for i in range(1, 5):
  if i == 2:
    continue
  print(i)