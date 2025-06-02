# Crie uma função que verifica qual(is) o(s) único(s) elemento(s) que não se repete(m) numa lista
def nao_repete(lista: list):
  repete = [i for i in lista if lista.count(i) == 1]
  return repete
print(nao_repete([12, 5, 6, 12, 12, 5]))
print(nao_repete(['a', 'b', 'b', 'c', 'd', 'c']))
