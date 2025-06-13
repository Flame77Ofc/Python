import json

try:
    with open('arquivo.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
except:
    with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
        arquivo.write('{}')

with open('arquivo.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)


nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

dados.update({nome: {'Idade': idade}})

with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
