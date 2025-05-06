# Escrita: w
arquivo = open('arquivo.txt', 'w', encoding='utf-8')
arquivo.write('João')
arquivo.close()

# Leitura: r
arquivo2 = open('arquivo.txt', 'r', encoding='utf-8')
print(arquivo2.read())
arquivo2.close()