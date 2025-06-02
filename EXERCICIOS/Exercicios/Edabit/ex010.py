"""Um fazendeiro precisa contar quantas pernas de animais há no seu sítio. Crie uma função que faça a soma das pernas sabendo que as galinhas tem 2 pernas, vacas tem 4 e porcos tem 4."""
def pernas(galinhas, vacas, porcos):
    return (galinhas * 2) + (vacas * 4) + (porcos * 4)
print(pernas(5, 2, 8))