# Crie um programa que diga a pessoa o ano que ela poderá se aposentar. Você deve perguntar a pessoa, o nome, a idade e criar uma mensagem dizendo em qual ano ela irá aposentar. Considere que todas as pessoas podem se aposentar aos 65 anos de idade.

# from datetime import datetime
# nome = input('Digite o seu nome: ')
# idade = int(input(f'{nome}, Digite a sua idade: '))
# ano = datetime.now().year
# aposentadoria = (ano - idade) + 65
# print(f'Você irá se aposentar em {aposentadoria}' if idade < 65 else f'{nome}, você já se aposentou!')




# A partir de uma lista você deve criar uma nova lista com o primeiro e último elemento. Para isso você deve criar uma função que faça essa criação automaticamente. Crie uma função que sirva para qualquer tamanho de lista.
def first_last(lista):
  lista2 = []
  if len(lista) > 2:
    lista2 = [lista[0], lista[-1]]
    return lista2
  else:
    return 'Não foi possível criar, a lista deve ter mais de 2 elementos'
print(first_last([2, 3, 4, 5, 6, 7]))



# Você foi contratado(a) por uma empresa de e-commerce e foi solicitado a você que faça uma limpeza nos cadastros de clientes duplicados. Os cadastros dos clientes estão em uma lista e você deve gerar uma lista nova sem os valores duplicados.
def limpeza(lista):
  for elemento in lista:
    if lista.count(elemento) > 1:
      lista.remove(elemento)

  lista.sort()
  return lista
print(limpeza(['Gabriel', 'Gabriel', 'Rodrigo', 'Maria', 'Rodrigo', 'Joana', 'Rodrigo']))
print(limpeza(['João', 'Fernando', 'Márcio', 'Fernando', 'Fernanda', 'Rogério', 'Luiza', 'Luiza', 'Paula']))
print(limpeza([110, 220, 330, 440, 330, 220, 110, 220]))


# Um pesquisador de lingua portuguesa quer lhe contratar para elaborar um robô capaz de identificar se uma palavra é palindroma ou não. Você deve criar um robo que peça a pessoa para inserir uma palavra e a resposta seja uma mensagem dizendo se é uma palavra palindroma ou não.
def a(string: str) -> bool:
  string = string.lower()
  return 'A palavra é um palindromo' if string[::-1] == string else 'A palavra não é um palíndromo'
print(a('Banana'))
print(a('Ana'))
print(a('Arara'))



# Crie uma função que receba uma lista de números e retorne todos os números da lista menores que 5
def menores5(lista):
  menores = [item for item in lista if item < 5]
  return menores if len(menores) > 0 else 'A lista não possui nenhum número menor que 5'
print(menores5([1, 2, 3, 4, 5, 6]))
print(menores5([4, 8, 12, 3, 6, 9]))
print(menores5([550, 220, 430, 340, 125]))



# Crie uma função que receba um número e retorne a lista de divisores desse número de 1 até esse mesmo número. Também diga se este número é primo
def divisores(numero):
  lista = [item for item in range(1, numero+1) if numero % item == 0]
  if len(lista) > 2:
    return f'O número é composto, com os divisores: {lista}'
  else:
    return f'O número é primo, o único divisor é 1 e ele mesmo: {lista}'
  return lista
print(divisores(16))
print(divisores(32))
print(divisores(160))
print(divisores(17))


# Faça um programa que leia três valores (A, B, C) e mostre-os na ordem lida.  Em seguida, mostre-os em ordem crescente e decrescente.
lista = []

A = int(input('Digite o primeiro valor: '))
B = int(input('Digite o segundo valor: '))
C = int(input('Digite o terceiro valor: '))

lista.append(A)
lista.append(B)
lista.append(C)
print(f'A ordem da lista normal é {lista}')
lista.sort()
print(f'A ordem crescente da lista é {lista}')
lista.reverse()
print(f'A ordem decrescente da lista é {lista}')


# Escreva um programa que lê o tamanho do lado de um quadrado e imprime um quadrado daquele tamanho com asteriscos. Seu programa deve usar laços de repetição e funcionar para quadrados com lados de todos os tamanhos entre 1 e 20.
# Por exemplo, para lado igual a 5:
# *****
# *****
# *****
# *****
# *****
quadrado = int(input('Digite o tamanho do quadrado: '))
if quadrado < 0 or quadrado > 20:
  print('O quadrado é muito grande! Deve ser entre 1 a 20')
else:
  for _ in range(quadrado):
    print(quadrado * '*')


# Faça um programa que recebe a altura de um triangulo em um número inteiro e imprima-o utilizando asteriscos. Veja o Exemplo: 
# Entrada: 5
# *
# **
# ***
# ****
# *****
triangulo = int(input('Digite a altura do triângulo: '))
if triangulo <= 0 or triangulo > 20:
  print('Altura atingida. Deve ser entre 1 a 20.')
else:
  for i in range(triangulo+1):
    print(i * '*')
