import random

tamanho = int(input('Digite o tamanho da senha: '))
def senhas_aleatorias(tamanho: int) -> str:
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@!$%"
    senha = ''
    if tamanho < 8 or tamanho > 30:
        return f'A senha deve ter tamanho maior que 8 ou menor que o limite de caracteres (30)'
    else:
        for _ in range(tamanho):
            senha += random.choice(caracteres)
        return senha
print(senhas_aleatorias(tamanho))
