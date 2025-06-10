try:
    with open('arquivo.txt', 'a+', encoding='utf-8') as arquivo:
        tem = False
        arquivo.seek(0)
        conteudo = arquivo.read()

        arquivo.seek(0)
        last_user = arquivo.readlines()[-1]

        symbol_one = last_user.find('🔺')
        symbol_two = last_user.find('🐍')
        symbol_three = last_user.find('✅')

        search_ID = int(last_user[symbol_one+5:symbol_two]) + 16

        search_username = last_user[symbol_two+2:symbol_three]
        username = input('Digite o seu nome de usuário:\n>>>').strip()

        arquivo.seek(0)

        for linha in arquivo.readlines():
            if username == search_username:
                tem = True
                break

        if tem:
            print('Já existe este nome de usuário!')
        else:
            arquivo.write(f'🔺ID: {search_ID}🐍 {username}✅\n')
            
except:
    try:
        with open('arquivo.txt', 'a+', encoding='utf-8') as arquivo:
            arquivo.seek(0)
            arquivo.write(f'🔺ID: 0🐍 Null✅\n')
    except:
        print('Erro!')