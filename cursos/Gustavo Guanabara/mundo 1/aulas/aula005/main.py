# Manipulação de Textos
frase = 'Curso em Vídeo Python'
#índices 012345678901234567890
print(frase)

print(frase[9])
print(frase[2:16])
print(frase[4:20:2])
print(frase[:9])
print(frase[12:])

# Comprimento da frase
frase = 'Aprendendo com o Guanabara'
comprimento = len(frase)
print(comprimento)

# Contando quantas vezes um caractere está presente numa frase
texto = 'Romeu e Julieta'
contar = texto.count('e')
print(contar)


# Encontrar em qual índice está um caractere ou um uma sequência de caractere
frase = 'Encontrando'
find = frase.find('cont')
print(find) # 2 (isso significa que se encontra no índice 2)


# Verificando se uma sequência ou caractere ESTÁ ou NÃO ESTÁ numa frase
frase = 'Aprendendo python com o Gustavo Guanabara'
print('python' in frase) # verdadeiro
print('gustavo' in frase) # falso (minúsculos)
print('JavaScript' not in frase) # verdadeiro


# substituir uma string por outra
texto = 'Amo aprender python com o Guanabara'
substituir = texto.replace('python', 'javascript')
print(substituir) # Amo aprender javascript com o Guanabara


# maiúsculas
texto = 'Curso em Vídeo'
maiusculas = texto.upper()
print(maiusculas) # CURSO EM VÍDEO

# minusculas
canal = 'Curso em Vídeo'
minusculas = canal.lower()
print(minusculas) # curso em vídeo




# removendo espaços antes e depois do conteúdo principal
texto = '        Alguns espaços em branco   '
remove_espacos = texto.strip()
print(remove_espacos) # Alguns espaços em branco



# Dividir strings
frase = 'Curso em vídeo'
dividir = frase.split()
print(dividir) # ['Curso', 'em', 'vídeo']

# Juntar strings divididas
juntar = '-'.join(dividir)
print(juntar) # Curso-em-vídeo


# Strings de múltiplas linhas
string = """Um exemplo de
uma string que
tem váris
linhas!
"""







#   -   -   -   -   -   -   -   -   -   Desafios   -   -   -   -   -   -   -   -   -
# Escreva um programa que leia o nome de uma pessoa e imprime:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo sem considerar espaços
# Quantas letras tem o primeiro nome
# nome = input("Digite o seu nome: ").strip()
# nome = nome.strip()
# print(nome.upper())
# print(nome.lower())
 
# print(len(nome.replace(' ', '')))

# nome = nome.split()
# print(f'Seu primeiro nome é {nome[0]} e tem {len(nome[0])} caracteres')



# Faça um programa que leia um número entre 0 a 9999 e mostre cada um dos digitos separados
# numero = int(input('Digite um número: '))
# numero = str(numero)

# print(numero[0])
# print(numero[1])
# print(numero[2])
# print(numero[3])






# Um programa que verifica se uma cidade começa com 'Santo', deve ter manipulações de textos
# cidade = input("Qual cidade você nasceu? ").strip().lower()

# print(cidade.startswith('santo'))



# Um programa que verifica se tem 'Silva' dentro do nome de uma pessoa
# nome = input('Qual o seu nome? ').strip().lower()
# print('silva' in nome)



# frase = input("Digite uma frase: ").strip().lower()
# print(f'A palavra a aparece {frase.count('a')} vezes')
# print(f'A primeira letra a apareceu na posição {frase.find('a') + 1}')
# print(f'A última letra a apareceu na posição {frase.rfind('a') + 1}')




nome = input("Digite o seu nome completo: ").strip().title().split()
print(f'O seu primeiro nome é {nome[0]} e seu último nome é {nome[-1]}')