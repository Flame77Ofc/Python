import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.6422.113 Safari/537.36 "
        "Edg/125.0.2535.67"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
        "application/signed-exchange;v=b3;q=0.7"
    ),
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Ch-Ua": (
        '"Chromium";v="125", "Microsoft Edge";v="125", '
        '"Not.A/Brand";v="24"'
    ),
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "DNT": "1",
    "TE": "trailers"
}

site = input("Qual o nome do site que você deseja faz scraping?\n>>>").strip()


def scraping(site: str):
    try:
        # Faz a conexão com o site
        r = requests.Session().get(site, headers=headers)

        # Transforma o html orginal em um objeto do BeautifulSoup
        soup = BeautifulSoup(r.content, 'html.parser')

        titulo = soup.find('h1')
        paragrafos = soup.find_all('p')

        if titulo and paragrafos:
            yield f"Título encontrado: {titulo.getText().strip()}"

            yield "Parágrafos encontrados:"
            for paragrafo in paragrafos:
                yield f"{paragrafo.getText().strip()}\n"
        else:
            yield f"Não foi possível encontrar informações sobre {site}."
    except requests.exceptions.MissingSchema:
        yield f"Impossível encontrar o site \"{site}\""


for i in scraping(site):
    print(i)
