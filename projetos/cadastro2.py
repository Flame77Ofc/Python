nome = input("Por favor, digite seu nome completo: ")
nota = int(input(f"Qual é a sua nota, {nome}?: "))

with open("arquivo.txt", "a+") as arquivo:
    arquivo.seek(0)
    conteudo = arquivo.read()

    if nome in conteudo:
        print("O aluno já está cadastrado.")
    elif nota < 0 or nota > 10:
        print("Nota inválida!")
    else:
        arquivo.write(f"{nome} tem a nota {nota}\n")
        print("Cadastro realizado.")
