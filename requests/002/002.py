import requests

url_base = 'https://pokeapi.co/api/v2/'

def pokemon(nome):
    url = f"{url_base}/pokemon/{nome}"
    resposta = requests.get(url)
    print(resposta) # <Response [200]>
    print(resposta.json())

nome_pokemon = 'pikachu'
pokemon(nome_pokemon)