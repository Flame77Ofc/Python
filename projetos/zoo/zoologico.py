import datetime
with open('arquivo.txt', 'a+', encoding='utf-8') as arquivo:
    arquivo.seek(0)
    conteudo = arquivo.read()

    nome = input("Digite o seu nome:\n>>>")
    animais = []

    repeticoes = int(
        input("Digite o número de animais que deseja cadastrar:\n>>>"))
    print("Digite o nome do animal" if repeticoes ==
          1 else "Digite os nomes dos animais: ")

    for repeticao in range(repeticoes):
        animal = input(">>>").title()
        while animal in animais:
            print("Esse animal já está na lista. ")
            animal = input(">>>").title()
        animais.append(animal)

    view = ', '.join(animais)

    agora = datetime.datetime.now().strftime('%H:%M em %d/%m/%Y')
    

    arquivo.write(
        f'{nome} cadastrou {len(animais)} {'animal' if repeticoes == 1 else 'animais'} às {agora}. {f"O animal é {view}" if repeticoes == 1 else f"São eles: {view}"}.\n')
