# Crie uma função para verificar quantas vezes 'd' aparece numa frase
def contagem(texto):
  return texto.lower().count('d')
print(contagem('Pedro e seus amigos estão brincando de esconde-esconde'))
print(contagem('Domingo é um belo dia ensolarado no parque'))
