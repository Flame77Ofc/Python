"""Escreva uma função que converta horas e minutos em segundos"""
def coverter(horas = 0, minutos = 0):
	# 1 hora equivale a 3600 segundos
	return (horas * 3600) + (minutos * 60)
print(coverter())