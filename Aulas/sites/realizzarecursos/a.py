# Pede ao usuário para digitar o número de repetições, que repete n vezes numeros. Os números são somados e calculado a média entre eles.
while True:
    repeticoes = int(input("Digite o número de repetições: "))
    total = 0

    if repeticoes == 0 or repeticoes == 1:
        print("Por favor, digite um número válido.")
    else:
        for i in range(repeticoes):
            numero = int(input("Digite um número: "))
            total = total + numero

        media = total / repeticoes

        print(f"O total é {total}")
        print(f'A média é {media}')
        break