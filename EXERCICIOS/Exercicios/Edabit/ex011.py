"""Crie uma função que retorne o número de pontos baseado na vitória, no empate e na derrota de um time de futebol. Sabendo que vitória ganha 3 pontos, empate ganha 1 e derrota 0"""

def pontos(vitoria, empate, derrota):
    return (vitoria * 3) + (empate * 1) + (derrota * 0)
print(pontos(0, 0, 1))
