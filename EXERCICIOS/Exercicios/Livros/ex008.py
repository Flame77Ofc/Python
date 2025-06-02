# Crie uma função que retorne a velocidade média de uma pessoa. Conside que: velocidade = distancia percorrida / tempo

distancia = int(input('Digite a distância em metros: '))
tempo = int(input('Digite os segundos: '))

velocidade = int((distancia / tempo) * 3.6)

print(f'A velocidade média é de {velocidade}Km/h')
