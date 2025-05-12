# Funções com argumentos pre-definidos
def informacoes(nome='usuário'):
    mensagem = f'Olá, {nome}! Que bom te ver aqui!'
    print(mensagem)


informacoes('João') # Caso o usuário digitar o seu nome, aparecerá normalmente.
informacoes() # Mas se o usuário não digitar nada, o nome será usuário.