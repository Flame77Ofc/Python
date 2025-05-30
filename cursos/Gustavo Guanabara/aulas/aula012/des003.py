info = dict()
info['nome'] = input('Digite o nome do jogador:\n>>>')
info['partidas'] = int(input(f'Quantas partidas {info["nome"]} jogou?\n>>>'))
info['gols'] = []

total = 0
for i in range(info['partidas']):
    gols = int(input(f"Quantos gols {info['nome']} fez na partida {i+1}?\n>>>"))
    info['gols'].append(gols)
    total += gols

print(info)

print(f'O nome do jogador é {info['nome']}')
print(f'Os gols que {info['nome']} fez foi {info['gols']}')
print(f'O total de gols que {info['nome']} fez foi {total}')

print(f'O jogador {info['nome']} jogou {info['partidas']} partidas')
for i in range(info['partidas']):
    print(f'Na partida {i+1}, fez {info["gols"][i]} gols')