# Pede ao usuário digitar um id, e se achar, mostra uma mensagem, se não, outra
# id's pre-definidos
usuarios = []
identificadores = []

usuario = input('Digite o seu nome de usuário: ')
if len(usuario) < 6 or ' ' in usuario:
    print('Deve ser maior que 5 letras e não pode conter espaços')
else:
    identificador = (len(identificadores) + 1) * 16
    usuarios.append(usuario)
    identificadores.append(identificador)

    for identificador, usuario in zip(identificadores, usuarios):
        print(identificador, usuario)

# pergunta = int(input("Busque pelo id: "))

# if pergunta in identify:
#     print("O id está!")
# else:
#     print("Id não cadastrado!")