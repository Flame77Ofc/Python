# ex048: Crie uma lógica que leia um número inteiro e passe para um procedimento ParOuImpar() que vai verificar e mostrar na tela se o valor passado como parâmetro é PAR ou ÍMPAR.

numero = int(input('Digite um número: '))

def ParOuImpar(numero):
    print('PAR' if numero % 2 == 0 else 'ÍMPAR')


ParOuImpar(numero)


# ex049: Crie uma função que retorne o número de pontos baseado na vitória, no empate e na derrota de um time de futebol. Sabendo que: vitória = 3 pontos, empate = 1 ponto e derrota = 0 pontos
def retorna_numero_pontos(vitoria, empate, derrota):
    pontos_vitoria = vitoria * 3
    pontos_empate = empate * 1
    pontos_derrota = 0

    total = pontos_vitoria + pontos_empate + pontos_derrota
    return f"Os pontos totais são de {total}"


if __name__ == "__main__":
    print(retorna_numero_pontos(15, 2, 5))  # Os pontos totais são de 47
    print(retorna_numero_pontos(23, 12, 8))  # Os pontos totais são de 81
    print(retorna_numero_pontos(3, 3, 54))  # Os pontos totais são de 12


# ex050: Crie uma função que retorne o quadrado de um número
def retorna_quadrado(numero: int):
    if numero.is_integer():
        quadrado = numero ** 2
        return f"O quadrado de {numero} é {quadrado}"


if __name__ == "__main__":
    print(retorna_quadrado(15))
    print(retorna_quadrado(23))
    print(retorna_quadrado(0))
    print(retorna_quadrado(-4))


# ex051: Escreva uma função que tem como argumento minutos e converta para segundos
def converte_minutos_para_segundos(minutos: int):
    if minutos.is_integer():
        segundos = minutos * 60
        return f"O total de segundos é {segundos}"

    return "Os minutos devem ser inteiros."


if __name__ == "__main__":
    print(converte_minutos_para_segundos(5))
    print(converte_minutos_para_segundos(12))
    print(converte_minutos_para_segundos(10))
