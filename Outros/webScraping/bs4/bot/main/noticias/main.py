from . import noticias

print('Qual noticia deseja ver?')
print('1 - GLOBO')
print('2 - BBC')
print('3 r7')
print('4 - Todas')

escolha = int(input('Digite:\n>>>'))
while escolha not in range(1, 5):
    escolha = int(input('Digite novamente.\n>>>'))
if escolha == 1:
        noticias.globo()
elif escolha == 2:
    noticias.bbc()
elif escolha == 3:
    noticias.r7()
else:
    noticias.globo()
    noticias.bbc()
    noticias.r7()