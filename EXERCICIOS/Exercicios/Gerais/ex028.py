# Crie um programa que receba o nome de um arquivoa como parâmetro e retorne o conteudo do arquivo
def saida(arquivo):
    with open (arquivo, 'r', encoding='utf-8') as arquivo:
        arquivo.seek(0)
        conteudo = arquivo.read()
    return conteudo
print(saida('readme.md'))