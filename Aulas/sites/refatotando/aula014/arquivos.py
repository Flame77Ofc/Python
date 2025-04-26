"""
r - leitura
a - incrementa
w - escrita
"""


# arquivo de leitura
arquivo = open("aula014/meutexto.txt", "r")
print(arquivo.read()) # Lê todo o conteúdo
arquivo.close()

# arquivo de escrita
arquivo2 = open("aula014/meutexto2.txt", "w")
arquivo2.write("SQL")
arquivo2.close()

# arquivo de incrementação
arquivo3 = open("aula014/meutexto3.txt", "a")
arquivo3.write('SQL\n')
arquivo3.close()