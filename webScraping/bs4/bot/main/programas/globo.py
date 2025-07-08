import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
init(autoreset=True)

from ..settings import headers


r = requests.Session().get('https://meuguia.tv/programacao/canal/GRD', headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')


paginas = int(input('Quer quantas páginas? (Máximo 8 páginas)\n>>>'))
while paginas not in range(1, 9):
    paginas = int(input('Digite corretamente. Quer quantas páginas? (Máximo 5 páginas): \n>>>'))

contador = 0
for programa in soup.find_all('li'):
    if programa.find('div', attrs={'class': 'ad'}):
        pass
    else:
        try:
            if len(programa.attrs) == 1:

                dia = programa.getText()
                print(dia)

                divisor = 'divider' in programa.get('class')
                if divisor:
                    contador += 1
                    if contador == paginas:
                        break


            titulo = programa.find('h2').getText()
            horario = programa.find('div', attrs={'class': 'lileft time'}).getText()

            print(f"{Style.BRIGHT + Fore.GREEN + titulo} {Fore.LIGHTWHITE_EX + '->'} {Style.BRIGHT + Fore.LIGHTBLUE_EX + horario}")

        except:
            pass
