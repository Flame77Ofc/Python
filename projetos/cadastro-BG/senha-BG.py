import json

try:
    with open('arquivo.json', 'r') as arquivo:
        dados = json.load(arquivo)
except:
    with open('arquivo.json', 'w') as arquivo:
        dados = {
            'ID': 0,
            'Usuário': None
        }
        json.dump(dados, arquivo)
    
with open('arquivo.json', 'r') as arquivo:
    dados = json.load(arquivo)

identificador = len(dados) * 16
nome = input('Digite o seu nome de usuário: ').strip()

dados.update({'ID': identificador,'Usuário': nome})

with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
