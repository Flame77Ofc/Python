# Faça um programa que leia três valores (A, B, C) e mostre-os na ordem lida.  Em seguida, mostre-os em ordem crescente e decrescente.
lista = []

A = int(input('Digite o primeiro valor: '))
B = int(input('Digite o segundo valor: '))
C = int(input('Digite o terceiro valor: '))

lista.append(A)
lista.append(B)
lista.append(C)

print(f'A ordem da lista normal é {lista}')
print(f'A ordem crescente da lista é {sorted(lista)}')
print(f'A ordem decrescente da lista é {sorted(lista, reverse=True)}')