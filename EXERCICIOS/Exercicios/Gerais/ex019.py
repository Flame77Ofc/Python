# Escreva um programa que lê o tamanho do lado de um quadrado e imprime um quadrado daquele tamanho com asteriscos. Seu programa deve usar laços de repetição e funcionar para quadrados com lados de todos os tamanhos entre 1 e 20.
# Por exemplo, para lado igual a 5:
# *****
# *****
# *****
# *****
# *****
quadrado = int(input('Digite o tamanho do quadrado: '))
if quadrado < 0 or quadrado > 20:
  print('O quadrado é muito grande! Deve ser entre 1 a 20')
else:
  for _ in range(quadrado):
    print(quadrado * '*')
