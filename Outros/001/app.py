# pass
# A instrução pass não faz nada. Pode ser usada quando a sintaxe exige uma instrução, mas a semântica do programa não requer nenhuma ação. Por exemplo:
class MinhaClasseVazia:
    pass

def soma(x, y):
    pass


# match
cor = (input("Insira sua escolha de 'vermelho, 'azul' ou 'verde': "))
match cor:
    case 'vermelho':
        print("Eu vejo vermelho!")
    case 'verde':
        print("Grama é verde")
    case 'azul':
        print("O céu é azul :)")