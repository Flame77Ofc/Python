# Strings
texto = 'Aprendendo python com AL SWEIGART'
# Indexação
texto[3]
texto[4:13]
print(texto[-8:])
print(texto[3:-6])

# operadores in e not in
'python' in texto
'javascript' not in texto

mensagem = 'PyThoN'
mensagem.upper()
mensagem.lower()
mensagem.isupper()
mensagem.islower()



mensagem = 'Aprender python é muito legal'
print(''.join(mensagem))
print(mensagem.split())


mensagem = '    Python '
mensagem = mensagem.strip()
print(mensagem)


docstring = """
Uma string com
múltiplas linhas
de código!
"""
print(docstring)