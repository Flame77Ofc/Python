# Crie uma função que conte quantas palavras há em seu parâmetro
def palavras(string:str) -> int:
  string = string.split()
  return len(string)
print(palavras('Maria gosta de pudim'))
print(palavras('João ganhou um presente de Natal'))
print(palavras('Pedro'))
