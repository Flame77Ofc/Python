# Crie uma função que recebe uma palavra inicial e faz o extrato de qualquer palavra que começa com a palavra 
def teste(palavra, lista):
  palavra = palavra.title()
  lista2 = []
  for i in lista:
    i = i.title()
    if i.startswith(palavra):
      lista2.append(i)
  return lista2
print(teste('fe', ['Feijão', 'macarrão', 'sopa', 'feliz']))
print(teste('po', ['porta', 'parque', 'passáro', 'pique-nique', 'porco', 'galinha']))
