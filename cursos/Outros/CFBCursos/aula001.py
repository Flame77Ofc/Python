num = 1
nome = 'Bruno'

curso = 'Curso de Python'
print(curso)

    

# Python não precisa de ;, mas pode ser escrito duas instruções
# em apenas uma linha usando o ;. Veja:
texto = 'Aprendendo Python'; print(texto)


"""Comentário de múltiplas linhas
Comentario
linha1
linha2"""


num1 = num2 = num3 = 0
print(num1, num2, num3)


# Variáveis
# Tipos de dados
x = 2
print(type(x)) # int

x = True
print(type(x))

# Laços de repetição
# While: É executado o bloco de código que está dentro dele enquanto uma condição for verdadeira
x = 0

while x < 10:
    print(x)
    x += 1

# for in: São mais utilizados do que as While. A grande diferença que ocorre no for é que a repetição já está determinada.
for contador in range(1, 11):
    print(contador)

# O for também serve como um iterador
for letra in 'python':
    print(letra)

