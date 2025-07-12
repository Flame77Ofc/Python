import random
import operator
jogo = {
        'jogador1': random.randint(1, 6),
        'jogador2': random.randint(1, 6),
        'jogador3': random.randint(1, 6),
        'jogador4': random.randint(1, 6)
    }
ranking = dict()

print('Valores sorteados:')
for chave, valor in jogo.items():
    print(f'{chave} jogou {valor}')

ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print(ranking)