# Operadores Ternários
"""
x = int(input("Digite um número: "))
print("par" if x % 2 == 0 else 'impar')
"""
lista = [4, 8, 1, 7, 9, 1, 8, 3, 0, 12, 3]
print(lista)

for i in lista:
    if i == lista[5]:
        print("Quinto elemento:", lista[5])
    else:
        print(i)


try:
    numero = int(input('Digite um número: '))
except:
    print("O valor está errado!")
else:
    print("Fim!")