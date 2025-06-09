with open('arquivo.txt', 'a+', encoding='utf-8') as arquivo:
    arquivo.seek(0)
    conteudo = arquivo.read()

    palavra = input('Digite uma palavra: ')

conteudo = conteudo.replace(palavra, '')

with open('arquivo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(conteudo)