# Tipos de dados primitivos e saída de dados
# Pede ao usuário dois números e imprime a soma entre eles
n1 = input("Digite um número")
n2 = input("Digite outro número")
soma = n1 + n2

print('A soma entre os dois números é', soma)

# O problema é que esquecemos de formatar para um tipo de dado
# Para corrigir isso basta adicionar int antes do input
n1 = int(input("Digite um número"))
n2 = int(input("Digite outro número"))
soma = n1 + n2

print('A soma entre os dois números é', soma)


# Conhecendo os tipos de dados
# int - Números inteiros: 
# 12
# -5
# 594

# float - Números com vírgula(Utiliza-se o ponto): 
# 4.59
# 12.00
# 3.14159275438491158751359187

# bool - Só aceitam o valor verdadeiro(True) e falso(False): 
# True
# False
# str - Textos delimitados por aspas simples ou duplas: 
# 'um texto'
# 'Gustavo Guanabara'
# "Python"