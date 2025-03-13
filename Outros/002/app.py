arquivo = open('file.txt', 'w')

while True:
    pergunta = input('Digite: ')  # Solicita entrada do usuário
    if pergunta.lower() == 'exit':  # Se for "exit", encerra o loop
        break
    arquivo.write(pergunta + '\n')  # Escreve a entrada no arquivo com quebra de linha

arquivo.close()  # Fecha o arquivo após sair do loop
print("Arquivo salvo e fechado.")