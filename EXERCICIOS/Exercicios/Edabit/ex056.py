# Um grupo de amigos decidiu criar uma sociedade secreta. O nome será a primeira letra de cada integrante do grupo, com ordem alfabética. Crie um programa que faça isso.
def sociedade(*nomes):
  letras = ''
  for i in nomes:
    letras += i[0]
  letras = sorted(letras)
  return ''.join(letras)
print(sociedade('Pedro', 'Maria', 'Gustavo'))
print(sociedade("Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"))
