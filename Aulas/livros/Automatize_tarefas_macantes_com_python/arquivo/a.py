# Gerenciador de senhas
site = input('Digite o nome do site: ')
senha = input('Digite a senha: ')

with open('arquivo/senhas.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(f'{site}, {senha}\n')