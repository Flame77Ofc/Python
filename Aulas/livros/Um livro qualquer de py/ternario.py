# Operador Ternário
pet = False
mensagem = 'Eu tenho um pet' if pet == True else 'Queria ter um pet!'
print(mensagem)


# Comparação operador ternário vs if...else
# Operador Ternário: 
luz = input("Como está a luz na sinaleira agora?: ")
luz = luz.lower()

sinaleira = 'pare' if luz == 'vermelha' or luz == 'vermelho' else 'atenção' if luz == 'amarela' or luz == 'amarelo' else 'vá' if luz == 'verde' else 'cor desconhecida'

# If...else:
if luz == 'vermelha' or luz == 'vermelho':
    sinaleira = 'pare'
elif luz == 'amarela' or luz == 'amarelo':
    sinaleira = 'atenção'
elif luz == 'verde':
    sinaleira == 'vá'


print(sinaleira)