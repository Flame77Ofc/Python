# Funções pre-definidas
def prazer(nome='anônimo'):
    mensagem = f'Olá, {nome}'
    print(mensagem)
prazer()


# *args: Recebem múltiplos argumentos
def mensagens(*mensagem):
    print(mensagem)
mensagens('Olá, Mundo!', 'Prazer em te conhecer!', 'Bom dia!')

def prazer(*nomes):
    for nome in nomes:
        mensagem = f'Prazer, {nome}!'
        print(mensagem)
prazer('Luiz', 'Paulo', 'Pedro')


# *kwargs
def pedido(**dados):
    print('Olá, o que deseja?')
    print(dados)
pedido(hamburguer = 'Big Mac', refrigerante = 'H2o', batatas = True)

