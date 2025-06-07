# Faça um jogo de apostas onde o jogador 1 diz se aposta que o dado vai cair em menos ou igual 3 ou mais que 3. Automaticamenete o jogador 2 fica com a outra parte que o jogador 1 escolheu.
from random import randint
dado = randint(1, 6)
print(f"{'Bem vindo ao jogo da aposta'.center(50, '-')}")
print(f'Digite "-" (sinal de subtração) se acha que o dado vai cair em 3 ou menos ou "+" (sinal de adição) se acha que o dado vai cair mais de 3:')
jogador1 = input('>>> ').strip().upper()
while jogador1 not in ['-', '+']:
  jogador1 = input('Digite um valor válido:\n>>> ').strip().upper()

print(f"Você ganhou! O dado caiu no número {dado}" if (jogador1 == '-' and dado <= 3) or (jogador1 == '+' and dado > 3) else f"Você perdeu, Jogador 2 venceu! O dado caiu no número {dado}")
