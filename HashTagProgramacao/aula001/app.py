texto = 'estou aprendendo python'
print(texto)


faturamento = 2500
custo = 250
lucro = faturamento - custo
print(f'Faturamento: {faturamento} Custo: {custo}, lucro: {lucro}')


email_cliente = 'qualquercoisaaleatoria@gmail.com'
email_cliente.upper() # Maiúsculo
email_cliente.lower() # Minúsculo

# Encontrar a posição de um caractere (Começa do 0) (Se não encontrar, aparecerá -1)
print(email_cliente.find('@'))


# Tamanho do texto
print(len(email_cliente))


# Capturar um caractere
print(email_cliente[22])


# Capturar uma parte do texto (Começa do 0)
print(email_cliente[4:15])


# Trocar parte do texto:
novo_email = email_cliente.replace('gmail.com', 'hotmail.com')
print(novo_email)


# Capitalize: Deixa a primeira letra de palavra em uppercase e o resto em minúsculo
nome = 'joão é legal'
print(nome.capitalize()) # João é legal
# Title: Deixa toda a primeira letra de uma palavra em uppercase sem excessão
nome = 'joão é legal'
print(nome.title()) # João É Legal