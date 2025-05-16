# O primeiro passo é fazer a instalação do python. Para fazer isso, basta ir no site oficial do python (https://www.python.org/downloads/) e instalar o interpretador. Depois pesquise por VScode e instale-o também. Se ficou confuso, recomendo ver o vídeo: (https://www.youtube.com/watch?v=ukaAzNqyMFc)



# Variável é um espaço na memória de um computador cujo seu papel é armazenar dados ou expressões para uso posterior
# Pense como num baú onde você pode armazenar itens para poder usar depois





# Entradas do usuário e conversão de tipos
# Entradas de usuários são informações que você pede ao usuário que estará executando o seu código. Você pode pedir coisas fictícias como nome, idade, cpf, cidade. Essas informações são guardadas na memória RAM, e depois que o usuário informa suas informações o computador simplesmente esqeuce, a não ser que os dados são passados para outro arquivo.
# Exemplos de entrada de usuário
# Entradas de usuário são feitas utilizando a palavra-chave input. Vamos ver como isso funciona.
nome = input('Digite o seu nome: ') # Uma variável guarda uma entrada de usuário e pede ao usuário seu nome
print(nome) # O programa exibe o que o usuário digitou na variável nome

# Vamos supor que digitei "Lucas" na variável nome. Logo após isso, o programa exibe "Lucas" no console

# Se você quer perguntar ao usuário informações que envolvem números, como por exemplo sua idade, seu cpf, ou um número qualquer, você deve usar a palavra int() antes do input. Vamos ver como ficaria isso:
# Incorreto:
idade = input("Digite a sua idade: ")
print(type(idade)) # Será do tipo string (caractere)

# Correto:
idade = int(input("Digite a sua idade: "))
print(type(idade)) # Será do tipo int (inteiro)

# Incorreto:
pets = input("Digite a quantidade de pets que você possui: ")
print(type(pets)) # tipo string (caractere)

# Correto:
pets = int(input("Digite a quantidade de pets que você possui: "))
print(type(pets)) # Será do tipo int (inteiro)