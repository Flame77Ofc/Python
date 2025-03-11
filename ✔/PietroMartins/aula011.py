# Arquivos
"""
arquivo = open('caminho', 'modo')
modos:
r: leitura ⇒ arquivo.read()
w: escrita ⇒ arquivo.write('código, codigo, código')
a: leitura + escrita

IMPORTANTE: fechar o arquivo ⇒ arquivo.close()


Boa prática:
with open('arquivo', 'modo') as arquivo:
    código
    código
        código
        código
    código
        código
"""

nome_arquivo = input('Digite o nome do arquivo ')
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    while True:
        palavra = input('Digite uma palavra. /exit para encerrar. ')
        if palavra == '/exit':
            break
        arquivo.write(f'{palavra}\n')

print('Palavras armazenadas')
with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print('Conteúdo')
    print(conteudo)