# 1. Apenas um nível de indentação por método (Exemplos simples)
import requests


def scraping_sem_fail_first(site: str):
    r = requests.get(site)

    if r.status_code == 200:
        json = r.json()

        if json is not None:
            return json
        else:
            return "JSON não encontrado."
    else:
        return "Falha na conexão."


def scraping_com_fail_first(site: str):
    r = requests.get(site)
    json = r.json()

    if r.status_code != 200:
        return "Falha na conexão."

    if json is None:
        return "JSON não encontrado."

    return json

