repeticoes = int(input("Quantas vezes deseja repetir?\n>>>"))
vogais = ('a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ', 'u', 'ú')
letras = ''

for repeticao in range(repeticoes):
    palavra = input('Digite a palavra:\n>>>').strip().lower()
    for letra in palavra:
        if letra in vogais:
            letras += f'{letra} '
    print(f'A sua palavra tem as seguintes vogais: {letras}')
    letras = ''