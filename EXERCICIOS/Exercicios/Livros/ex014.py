# Faça um programa que leia uma frase e exiba o número de palavras.
frase = input('Digite uma frase ou um texto: ').strip()
frase = frase.split()
print(f"Há {len(frase)} palavras na sua frase/texto")
