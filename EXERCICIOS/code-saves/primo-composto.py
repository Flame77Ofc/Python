def primo(numero):
    lista = [item for item in range(1, numero + 1) if numero % item == 0]
    if len(lista) == 2:
        return f'O número {numero} é primo. Divisores: {lista}'
    else:
        return f'O número {numero} é composto. Divisores: {lista}'
print(primo(16))
print(primo(17))
print(primo(37))
print(primo(24))