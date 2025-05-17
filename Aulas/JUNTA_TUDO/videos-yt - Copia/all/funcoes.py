# Funções
def espaco():
    print()

def bigmac():
    print('Sanduiche BIG MAC')
print("Inicio")
bigmac()
print("Fim")

espaco()

def prazer(nome):
    print(f"Oii, {nome}!")
prazer('Rafael')


def nascimento():
    idade = int(input('Qual é a sua idade? '))
    print(f'Você nasceu em {2025 - idade} ou {2025 - idade - 1}')
nascimento()

espaco()

def pedir_batata(tamanho):
    print('batata', tamanho)
pedir_batata('grande')





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

