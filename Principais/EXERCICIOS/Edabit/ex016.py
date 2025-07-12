"""Crie uma função que receba dois argumentos e retorne True se ao menos um valor for 10 ou se a soma dos números for 10."""
def isTen(x, y):
    return (x == 10 or y == 10) or (x + y == 10)
print(isTen(5, 6))
print(isTen(10, 0))
print(isTen(8, 10))
print(isTen(2, 8))