# Concatenação: Usada para juntar strings.
# string1 = 'Olá'
# string2 = 'Mundo'
# concatenacao = string1 + string2 # O resultado será OláMundo pois esquecemos do espaço
# concatenacao = string1 + ' ' + string2 # Apenas colocar um espaço: Olá Mundo
# print(concatenacao)


# Utilizando f-strings: Um método melhor
amigo1 = 'Pedro'
amigo2 = 'João'
print(f'{amigo1} e {amigo2} são melhores amigos')

# nome = 'Felipe'
# sobrenome = 'Araújo'
# print(nome + ' ' + sobrenome)

# Indexação: Acessando caracteres de strings
# O índice de strings é uma forma de acessar um caractere ou uma sequência de caracteres. O índice sempre começa do 0, e vai até a última palavra de uma string, que é a quantidade da string -1.
# Os índices podem ser positivos e negativos
# nome_do_estabelecimento = 'La Praire'
# # ìndices positivos:     012345678
# # índices negativos:    -987654321
# nome_do_estabelecimento[4] # r
# nome_do_estabelecimento[-8] # a
# # Também é possível acessar sequências da string (Fatiamento de Strings)
# Os fatiamento de Strings sempre serão assim:
# string[inicio:fim +1] # fim+1 porque é a sintaxe do python.
# Se você quer ir do índice 1 até o 6, na verdade estaria indo do 1 até o 5. Então incremente mais um, ficando:
# string[1:6+1] Ou simplesmente string[1:7] (Mais recomendável)
# nome_do_estabelecimento[1:6] # a Pra
# nome_do_estabelecimento[-5:-1] # rair
# Nesse caso, estará acessando a partir do índice da string 4 até o final da string.
# string[indice:(acessará o final da string)]
# nome_do_estabelecimento[4:] # raire
# Nesse caso, estará acessando o começo da string até o 
# string[(começo atééé...):índice]
# print(nome_do_estabelecimento[:6]) # La Pra
# acessando a quantidade de caracteres de uma string com a função len()
# string = 'Acessando a quantidade de caracteres dessa String'
# print(len(string)) # Apenas coloque len() e dentro dos parentêses a string que você quiser

# EXERCÍCIOS
# 1. Crie uma string e imprima seu comprimento usando len().
    # string = 'Python é legal!'
    # print(len(string))
# 2. Crie duas strings, concatene-as e imprima a string resultante.
    # itens1 = 'Caneta'
    # itens2 = 'Lápis'
    # mochila = itens1 + ' e ' + itens2
    # print(mochila)
# 3. Imprima a string "Mat" usando a notação de fatia para especificar o intervalo correto de caracteres na string "Matemática"
    # string = 'Matemática'
    # print(string[:3])


# MÉTODOS DE STRING
# Convertendo strings para maiúsculas e minúsculas: Utilizando o .upper(), .lower(), .capitalize(), .title()

# Convertendo uma string em letras maiúsculas: Usando o .upper()
# string = 'lucas costa'
# string = string.upper()
# print(string) # LUCAS COSTA

# objeto = 'bola de futebol'
# print(objeto.upper()) # BOLA DE FUTEBOL


# Convertendo para minúsculas: Utilizando o .lower()
# string = 'MInhA StrING'
# string = string.lower()
# print(string) # minha string

# local = 'MONTE da NEVADA'
# print(local.lower()) # monte da nevada  


# Convertendo apenas o primeiro caractere para maiúsculo da string com o .capitalize()
# string = 'marcos antonio'
# string = string.capitalize()
# print(string) # Marcos antonio

# local = 'monte olimpo'
# print(local.capitalize()) # Monte olimpo
# Convertendo as letras iniciais de uma string para maiúsculas com o .title()
# string = 'prazer em conhecer você'
# string = string.title()
# print(string) # Prazer Em Conhecer Você

# nome = 'joão costa dos santos'
# print(nome.title()) # João Costa Dos Santos



# Removendo espaços desnecessários de uma string: Utilizando .strip()
# string = '  texto        ' # Veja que há diversos espaços desnecessários antes e depois do conteúdo principal(texto)
# string = string.strip()
# print(string)

# nome = '      João'
# print(nome.strip())


# # Verificando se uma string começa ou termina com uma sequência especifica de caracteres: utlizando o startswith e o endswith
# # As funções startswith e endswith retornam um valor booleano (True ou False) dependendo de seu conteúdo
# comida = 'pizza'
# termina = comida.endswith('zza') # Verifica se pizza termina com 'zza'
# print(termina)

# comida = 'arroz'
# comeca = comida.startswith('arr') # Verifica se arroz começa com 'arr'
# print(comeca)



# # EXERCÍCIOS
# # 1. Escreva um programa que converta as seguintes strings para minúsculas: "Animais", "Helefante", "Abelha", "Crocodilo". Imprima cada string em minúsculas em uma linha separada.
# string1 = 'Animais'
# string2 = 'Helefante'
# string3 = 'Abelha'
# string4 = 'Crocodilo'
# print(string1.lower())
# print(string2.lower())
# print(string3.lower())
# print(string4.lower())

# # 2. Repita o exercício 1, mas converta cada string para maiúsculas em vez de minúsculas.
# print(string1.upper())
# print(string2.upper())
# print(string3.upper())
# print(string4.upper())

# # 3. Escreva um programa que remova os espaços em branco das seguintes strings e, em seguida, imprima as strings com os espaços em branco removidos
# string1 = " Filet Mignon"
# string2 = "Brisket "
# string3 = " Cheeseburger "
# print(string1.strip())
# print(string2.strip())
# print(string3.strip())

# # 4. Escreva um programa que imprima o resultado de .startswith("be") em cada uma das seguintes strings:
# string1 = "Becomes"
# string2 = "becomings"
# string3 = "BEAR"
# string4 = "  bEautiful"

# print(string1.startswith('be'))
# print(string2.startswith('be'))
# print(string3.startswith('be'))
# print(string4.startswith('be'))
# # 5. Usando as mesmas quatro strings do exercício 4, escreva um programa que use métodos de string para alterar cada string de modo que  startswith("be") retorne True para todas elas.
# string1 = "Becomes"
# string2 = "becomings"
# string3 = "BEAR"
# string4 = "  bEautiful"
# string4 = string4.strip()

# string1 = string1.lower()
# string2 = string2.lower()
# string3 = string3.lower()
# string4 = string4.lower()

# print(string1.startswith('be'))
# print(string2.startswith('be'))
# print(string3.startswith('be'))
# print(string4.startswith('be'))


# Encontrar um caractere em uma string: utilizando o .find()
# O find retorna o índice em que o caractere se encontra.
# frase = 'Estou aprendendo Python'
# print(frase.find('aprendendo'))


# substituir um caractere ou uma sequência de caracteres por outra com o método .replace()
# .replace('caracteres antigos', 'novos caracteres')
# string = 'Olá, Mundo'
# string = string.replace('Mundo', 'Marte')
# print(string)