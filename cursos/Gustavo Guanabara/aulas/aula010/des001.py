tupla = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
    "dezoito", "dezenove", "vinte"
)

while True:
    numero = int(input("Digite um número entre 0 e 20:\n>>> "))
    while numero < 0 or numero > 20:
        numero = int(input("Valor inválido. Digite um número entre 0 e 20:\n>>> "))

    print(f"Você digitou o número: {tupla[numero]}")

    continuar = input("Deseja continuar? [S/N]:\n>>> ").strip().upper()
    while continuar not in ('S', 'N'):
        continuar = input("Entrada inválida. Deseja continuar? [S/N]:\n>>> ").strip().upper()

    if continuar == 'N':
        break
