# Pirâmide de Estrelas
def stars_piramid(quantity: int):
    if quantity < 1 or quantity > 100:
        print("A quantidade deve estar entre 1 a 100.")
        return None

    for number in range(1, quantity+1):
        print("*" * number)


quantity = int(input("Digite a quantidade de 1 a 100:\n>>> "))
stars_piramid(quantity)
