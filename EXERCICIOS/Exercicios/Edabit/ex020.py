"""Crie uma função que retorne a area de um retângulo a partir da largura e altura, porém se não for válido, então retornará -1"""
def area(x, y):
    return y * x if x > 1 and y > 1 else -1
print(area(10, 11))