# Dicas Python
# Usar um traço para um loop for indice que aquela variável é desnecessária ou é temporária
# Um loop for normal
for i in range(5):
  print(i+1)

# Um loop com traço que indica que a variável é desnecessária, não tem utilidade para o loop
for _ in range(5):
  print('Contando')
