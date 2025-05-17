# O módulo random
# Imagine brincar de adivinhar o número, mas quem escolher o número é o seu computador e quem faz os chutes é você?? Hah, com o módulo random isso é muito possível e simples fácil de fazer!
# random é um módulo do python que permite que o próprio computador possa escolher números, letras ou até elementos de uma lista! Vamos ver como funciona o random!
# Imagine o seguinte: Você dizer ao computador para escolher um número entre 1 a 100, então vamos ver como fazer isso agora!
# Primeiro importamos o módulo random, basta digitar import random
import random
# A seguir utilizamos o comando random.radint(inicio, fim), onde inicio é o número que desejamos que o computador comece a escolher, e o número fim é o número que desejamos que o computador termine de escolher. Como queremos que ele escolha de um número de 1 a 100, então ficará assim:
escolha = random.randint(1, 101)
print(escolha) # 92

# Repare que dentro dos parênteses de randint, o número começa do 1 e ter,ina até 101, nesse caso na verdade termina em 100, pois o término é sempre subtraído em 1. Mas tirando isso, é super fácil de entender!

# Ok, agora vamos supor que você tenha uma lista, e queira que o computador escolha um elemento dessa lista. Você pode fazer isso utilizando o random.choice(lista). Vamos ver num exemplo:
alimentos = ['Arroz', 'Macarrão', 'Strogonoff']
elemento = random.choice(alimentos)
print(elemento)

# Pronto, simplesmente isso!

# Agora que tal criar um mini joguinho em que você tenta acertar o número aleatório que o programa criar?
# Vamos criar um programa onde seu objetivo é acertar o número que o computador acertar:
import random
numero = random.randint(1, 101)
while True:
    palpite = int(input("Qual é o seu palpite? "))
    if palpite > 101 or palpite < 0:
        print('Por favor, digite um número entre 1 a 100!')
    elif palpite > numero:
        print('Chute alto!')
    elif palpite < numero:
        print('Chute baixo!')
    elif palpite == numero:
        print('Você acertou!')
        break
# Vamos entender: Primeiro importamos o módulo random, depois criamos a variável numero, que recebe um número aleatório entre 1 a 100. Logo em seguida criamos um loop while True, e perguntamos o palpite para o usuário. O programa avalia se o palpite é maior que 101 ou menor que 0 (exceções) e depois verifica se é maior ou menor que o número. A última condição verifica se o palpite é igual ao número aleatório gerado, se for, imprime na tela 'Você acertou' e quebra o loop para não ser executado eternamente.