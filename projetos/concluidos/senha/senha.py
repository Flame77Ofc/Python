import random

tamanho = int(input('Digite o tamanho da senha: '))
def senhas_aleatorias(tamanho: int) -> str:
    especiais = "#@!$%"
    minusculos = "abcdefghijklmnopqrstuvwxyz"
    maiusculos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    senha = ''
    if tamanho < 8 or tamanho > 30:
        return f'A senha deve ter tamanho maior que 8 ou menor que o limite de caracteres (30)'
    else:
        for i in range(tamanho):
            if i % 6 == 0:
                senha += random.choice(especiais)
            elif i % 5 == 0:
                senha += random.choice(minusculos)
            elif i % 4 == 0:
                senha += random.choice(maiusculos)
            elif i % 3 == 0:
                senha += random.choice(especiais)
            elif i % 2 == 0:
                senha += random.choice(numeros)
            else:
                letra = random.choice([maiusculos, minusculos, numeros])
                senha += random.choice(letra)
        
        return senha
print(senhas_aleatorias(tamanho))
