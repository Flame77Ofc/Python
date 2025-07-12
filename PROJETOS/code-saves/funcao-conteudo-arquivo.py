# Crie um programa que receba o nome de um arquivo como parâmetro e retorne o conteudo do arquivo

def ler(arquivo):
    with open (arquivo, 'r', encoding='utf-8') as arquivo:
        arquivo.seek(0)
        conteudo = arquivo.read()
    return conteudo
print(ler('readme.md'))