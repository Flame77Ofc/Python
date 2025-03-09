# Manipulando arquivos
# Mode
# r - leitura
# a - append/Incrementar
# w - escrita
# x - criar arquivo
# r+ - leitura + escrita

arquivo = open("Refatorando/aula008/aula008.txt","a")
print(arquivo.write("\nBanco de Dados"))
arquivo.close()