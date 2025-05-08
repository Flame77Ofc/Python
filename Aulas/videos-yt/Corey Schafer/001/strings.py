message = 'Hello, World!'
print(message)  # Exibe a mensagem inicial

doc_string = """This is a
doc string
and allow you
to write in 
many lines"""
print(doc_string)  # Exibe uma string de múltiplas linhas

# Calcula e exibe o número de caracteres em uma string
name = 'Gabriel'
print(len(name))  # Mostra o comprimento da string 'name'

message = 'I love learn python!'
print(len(message))  # Mostra o comprimento da string 'message'

# Indexação: acessa caracteres ou trechos de uma string por seus índices
print(name[0])  # Exibe o primeiro caractere de 'name'
print(name[0:4])  # Exibe os caracteres do índice 0 ao 3
print(message[3:11])  # Exibe a substring do índice 3 ao 10
print(message[:6])  # Exibe os primeiros 6 caracteres
print(message[8:])  # Exibe a partir do índice 8 até o final

# Manipulação de letras maiúsculas e minúsculas
gift = 'toy car'
print(gift.upper())  # Converte toda a string para maiúsculas
print(gift.lower())  # Converte toda a string para minúsculas
print(gift.capitalize())  # Capitaliza apenas a primeira letra
print(gift.title())  # Capitaliza a primeira letra de cada palavra

# Conta ocorrências de um caractere ou substring
print(gift.count('y'))  # Conta quantas vezes 'y' aparece em 'gift'

# Localiza a posição (índice) de um caractere ou substring
print(gift.find('r'))  # Retorna o índice da primeira ocorrência de 'r'

# replace: substitui uma letra ou palavra por outra
gift = 'toy'
print(gift.replace('toy', 'bus'))

# concatenação de variáveis
greeting = 'Hello'
name = 'Flame'
message = greeting + ' ' + name
print(f"{greeting}, {name}! How are you?")