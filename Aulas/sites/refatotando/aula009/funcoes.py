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