from datetime import datetime
agora = datetime.now()

nome = input('escolha um username')

arquivo = open("dados.txt", "a+")
arquivo.write(f"{nome} fez login em {agora}\n")

arquivo.seek(0)
print(arquivo.read())

arquivo.close()