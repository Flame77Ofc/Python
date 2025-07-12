import requests
from bs4 import BeautifulSoup
from datetime import datetime
from ..settings import headers

temperaturas = []
climas = []
print('-------------------------------')
def molde(site: str, elemento: str, atributo: str, conteudo_atributo: str, simbolo: str, elemento2: str = False, atributo2: str = False, conteudo_atributo2: str = False):
    try:
        site = site
        r = requests.Session().get(site, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        temperatura = soup.find(elemento, attrs={atributo: conteudo_atributo}).getText().strip().replace(simbolo, '')
        if '.' in temperatura:
            fim = temperatura.index('.')
            temperatura = temperatura[:fim]
        temperatura = int(temperatura)
        temperaturas.append(temperatura)

        print(f'Temperatura Registrada Com Sucesso: {temperatura}')
    except:
        print('Ops! Algum Erro... Pulando para o próximo.')

    try:
        if elemento2:
            clima = soup.find(elemento2, attrs={atributo2: conteudo_atributo2}).getText().strip()
            print(f"Informações adicionais: {clima}")
            climas.append(clima)
    except:
        pass

    print('-------------------------------')


def resumo():
    media = round(sum(temperaturas) / len(temperaturas), 1)
    print(f"A média de temperatura é de {media}")
    for informacao in climas:
        print(f"- {informacao}")

    agora = datetime.now()
    data = agora.strftime('%d/%m/%Y %H:%M:%S')
    with open('temperaturas.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'Atualizado em {data}\nTemperaturas: {temperaturas}\nA temperatura registrada foi de {media}°C\n\n')
