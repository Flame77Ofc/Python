# arquivo = open('aula018/arquivo.txt', 'w', encoding='utf-8')
# for i in range(1, 11):
#     arquivo.write(f'Linha {i}\n')


# arquivo.close()




with open('aula018/arquivo.txt', 'r', encoding='utf-8') as arquivo:
    arquivo.seek(0)
    for i in range(1, 11):
        print(arquivo.readline())