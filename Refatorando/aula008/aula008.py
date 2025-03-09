# Manipulando arquivos
# Mode
# r - leitura
# a - append/Incrementar
# w - escrita
# x - criar arquivo
# r+ - leitura + escrita

arquivo = open("Refatorando/aula008/aula008.txt","r")
arquivo.readable()
print(arquivo.read())
print(arquivo.readlines())
arquivo.close()