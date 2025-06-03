# Crie um função que receba como argumento um dicionário de nome de estudantes e retorne a lista de estudantes em ordem alfabética
def estudantes(dicionario):
  lista = [i for i in dicionario.values()]
  lista.sort()
  return lista
print(estudantes({'Estudante 1': 'Pedro', 'Estudante 2': 'Maria', 'Estudante 3': 'Gustavo'}))
print(estudantes({"Estudante 1" : "Steve",
  "Estudante 2" : "Becky",
  "Estudante 3" : "John"}))
