# Escrita: w
arquivo = open('arquivo.txt', 'w', encoding='utf-8')
arquivo.write('Hello, World!')
arquivo.close()

# Leitura: r
arquivo2 = open('arquivo.txt', 'r', encoding='utf-8')
print(arquivo2.read())
arquivo2.close()

# Acrescentar: a
with open('arquivo.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Olá, Mundo!')
