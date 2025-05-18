nome = input('escolha um username ')

arquivo = open("projetos/arquivos/dados.txt", "a+")
arquivo.write(f"{nome}\n")


arquivo.seek(0)
print(arquivo.read())

arquivo.close()