# Lê todas as linhas de um arquivo
with open('002/arquivo.txt', 'r', encoding='utf-8') as arquivo:
    linhas = len(arquivo.readlines())
    print(linhas)