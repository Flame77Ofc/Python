portao = False
cartao = False
pergunta = input('Você tem o cartao? ')
prg = pergunta.lower()
if prg == 'sim':
    portao == True
    print('Pode entrar')
elif prg in {'não', 'nao'}:
    portao = False
    print('Acesso negado')
else:
    print('Erro, tente novamente')