#Condicionais
lampada = True
if lampada == True:
    print('Ligada')
else:
    print('Desligada')

faltas = int(input('Quantas vezes você faltou?'))
if faltas == 1 :
    print('Você faltou, se faltar novamente, será suspenso!')
elif faltas >= 2:
    print("Você está suspenso")
else:
    print("Você faltou 0 dias, parabéns!")