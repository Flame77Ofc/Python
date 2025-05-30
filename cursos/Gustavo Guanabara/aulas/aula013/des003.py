import datetime

nascimento = int(input('Em que ano você nasceu?\n>>>'))
def voto(nascimento):
    idade = datetime.datetime.now().year - nascimento
    if idade >= 18:
        return f'Com {idade} anos, seu voto é obrigatório'
    elif idade >= 16:
        return f'Com {idade} anos, seu voto é opcional'
    else:
        return f'Com {idade} anos, seu voto é negado'
    
print(voto(nascimento))