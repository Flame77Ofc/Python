# Bloco de notas
from datetime import datetime
data = datetime.now().strftime('%d, %B %Y')


def view():
    global linhas
    linhas = 0
    for linha in arquivo.readlines():
        linhas += 1
        if linhas == 1:
            continue
        print(linha.strip())

with open('bloco-notas.txt', 'a+', encoding='utf-8') as arquivo:
    arquivo.seek(0)
    conteudo = arquivo.read()

    if 'Senha' not in conteudo:
        senha = input('Defina uma senha: ')
        arquivo.write(f'Senha: {senha}᚛\n')

    arquivo.seek(0)
    
    inicio = conteudo.find(' ')
    fim = conteudo.find('᚛')

    password = conteudo[inicio+1:fim]
    print(password)

    verificacao = input('Digite a sua senha:\n>>>')

    if verificacao == password:
        print('Acesso confirmado')
    else:
        print('Acesso negado')


    # Opção de menus
    print('Opções do menu\n[1]: Ver meu bloco de notas\n[2]: Escrever no meu bloco de notas')
    menu = int(input('O que deseja fazer?\n>>>'))

    while menu not in [1, 2]:
        menu = int(input('Digite corretamente!\n>>>'))

    if menu == 1:
        arquivo.seek(0)
        view()
    elif menu == 2:
        texto = input('Modo escrita ativado. Digite no seu bloco de notas!\n>>>')
        arquivo.write(f'{data}\n{texto}\n\n')
    

    arquivo.seek(0)
    print(f'Linhas: {linhas-1}')