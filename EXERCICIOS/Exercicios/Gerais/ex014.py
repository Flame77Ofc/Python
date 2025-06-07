# A partir de uma lista você deve criar uma nova lista com o primeiro e último elemento. Para isso você deve criar uma função que faça essa criação automaticamente. Crie uma função que sirva para qualquer tamanho de lista.
def first_last(lista):
  lista2 = []
  if len(lista) > 2:
    lista2 = [lista[0], lista[-1]]
    return lista2
  else:
    return 'Não foi possível criar, a lista deve ter mais de 2 elementos'
print(first_last([2, 3, 4, 5, 6, 7]))
