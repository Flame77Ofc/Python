# Um pesquisador de lingua portuguesa quer lhe contratar para elaborar um robô capaz de identificar se uma palavra é palindroma ou não. Você deve criar um robo que peça a pessoa para inserir uma palavra e a resposta seja uma mensagem dizendo se é uma palavra palindroma ou não.
def a(string: str) -> bool:
  string = string.lower()
  return 'A palavra é um palindromo' if string[::-1] == string else 'A palavra não é um palíndromo'
print(a('Banana'))
print(a('Ana'))
print(a('Arara'))
