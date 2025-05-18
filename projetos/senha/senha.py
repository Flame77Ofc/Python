def archive():
        global nome, senha, conteudo, arquivo
        arquivo = open('arquivo.txt', 'a+', encoding='utf-8')
        arquivo.seek(0)
        nome = input('Digite o seu nome de usuário: ')
        senha = input('Digite a sua senha: ')
        conteudo = arquivo.read()


while True:
    # Talvez um menu de remover o usuário, mas mais pra frente!
    menu = int(input('1: Cadastrar\n2: Entrar\n3: Sair\n'))
    if menu == 1: # Opção 1 => Cadastrar
        archive()

        if nome in conteudo: # Verifica se esse usuário já está logado
            print('O usuário já está cadastrado! Tente Entrar!')
            break
        else: # Se não estiver logado, o cadastro é realizado
            print('Cadastro realizado com sucesso!')
            arquivo.write(f'{nome}, {senha}\n')
            break

    elif menu == 2: # Opção 2 => Entrar
        archive()
        if nome in conteudo and senha == senha:
             print('Entrou com sucesso!')
             break
        else:
             print('Erro!')
             break

    elif menu == 3: # Opção 3 => sair
        break


# Se o nome está, porém a senha está incorreta OU Se o usuário não existir
# O que eu tenho que fazer: O ponteiro do mouse tem que começar na senha, para fazer isto, é preciso pegar o tamanho do nome(e mais 2, pois tem espaço e vírgula) e armazenar a senha buscada em outra variavel, para mais tarde fazer uma comparação.
arquivo.close()

