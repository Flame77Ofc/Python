# Diretório
# Diretório atual: getcwd()
import os
diretorio_atual = os.getcwd()
print(diretorio_atual)

# Lista de diretório: listdir()
pasta = 'C:\Programação\Python'
resultado = os.listdir(pasta)
print(resultado)

# Criar um novo diretório: mkdir()
os.mkdir('teste')