# Funções
# def nome_da_função (argumentos):
#     instruções
def mensagem():
    print('Você recebeu uma mensagem')
    msg = input('Quer ver essa mensagem? ')
    msglower = msg.lower()

    if msglower in {'sim', 'yes', 'yea', 'si'}:
        print('Eu estou aprendendo Python!')
    else:
        print('Cancelado')
mensagem()



def multiplicacao(x,y):
    return x * y
print(multiplicacao(34, 59.57))