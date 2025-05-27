tupla = (
    "Palmeiras",
    "Flamengo",
    "Cruzeiro",
    "Red Bull Bragantino",
    "Fluminense",
    "Ceará",
    "Bahia",
    "Corinthians",
    "Mirassol",
    "Atlético-MG",
    "Botafogo",
    "Grêmio",
    "São Paulo",
    "Internacional",
    "Vasco da Gama",
    "Fortaleza",
    "Vitória",
    "Santos",
    "Juventude",
    "Sport",
)

print(f'Os 5 primeiros colocados foram {tupla[:5]}')
print(f'Os 4 últimos colocados foram {tupla[-4:]}')

print(f'A lista em ordem alfabética é {sorted(tupla)}')

print(f'Fluminense está na posição {tupla.index('Fluminense')+1}')