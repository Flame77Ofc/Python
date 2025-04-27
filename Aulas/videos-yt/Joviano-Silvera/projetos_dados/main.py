nome = input("Digite o seu nome: ")  # Pede o nome do usuário

try:
    with open("dados.txt", "r") as arquivo:  # Tenta abrir o arquivo 'dados.txt' para leitura
        linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
        number = len(linhas) + 1  # Define o número como a quantidade de linhas + 1
except FileNotFoundError:  
    number = 1  # Se o arquivo não existir, começa com o número 1

with open("dados.txt", "a") as arquivo:  # Abre o arquivo para adicionar dados (modo append)
    arquivo.write(f"{nome} user {number}\n")  # Escreve o nome e o número do usuário no arquivo

print(f"Usuário {nome} registrado como user {number}!")  # Exibe uma mensagem confirmando o registro