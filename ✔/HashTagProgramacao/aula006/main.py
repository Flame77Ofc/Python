# Exercícios com Bibliotecas
import os

lista_arquivos = os.listdir("HashTagProgramacao/arquivos")
for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        print('Movimentar', arquivo)