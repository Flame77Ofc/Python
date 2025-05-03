# read (leitura)
arquivo = open('arquivos/arquivo.txt', 'r')
"""print(arquivo.read()) # lê todo o arquivo
print(arquivo.readlines()) # lê linha por linha"""

palavras = arquivo.read()
lista_palavras = palavras.split()
print(len(lista_palavras))
arquivo.close()