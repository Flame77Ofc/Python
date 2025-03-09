# Manipulando arquivos
# Mode
# r - leitura
# a - append/Incrementar
# w - escrita
# x - criar arquivo
# r+ - leitura + escrita

arquivo = open("Refatorando/aula008/aula0083.txt","w")
arquivo.write('C#\n')
arquivo.write('Java\n')
arquivo.write('C++\n')
arquivo.close()