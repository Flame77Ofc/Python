# with open ('arquivos/arquivo.txt', 'w') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.write('Linha 3\n')

with open ('arquivos/arquivo.txt', 'r') as arquivo:
    linhas = len(arquivo.readlines()) + 1
    print(linhas)


with open ('arquivos/arquivo.txt', 'a') as arquivo:
    arquivo.write(f'Linha {linhas}\n')

