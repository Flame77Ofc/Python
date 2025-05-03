nome = input('Por favor, digite seu nome inteiro: ')
nota = int(input('Por favor, digite a sua nota: '))

with open('arquivos/arquivo.txt', 'a+') as arquivo:
    arquivo.seek(0)
    conteudo = arquivo.read()

    if nome in conteudo:
        print("O aluno já está cadastrado!")
    elif nota < 0 or nota > 10:
        print(f'A nota é inválida! Deve estar entre 0 e 10.')
    else:
        print('Cadastrado realizado!')
        arquivo.write(f'{nome} tem a nota {str(nota)}\n')