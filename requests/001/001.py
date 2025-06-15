import requests

# GET = PEGAR INFORMAÇÕES (GET = RECOLHER, CONSEGUIR, COLHER, PEGAR, OBTER, CONQUISTAR)
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
print(requisicao) # 200

print(requisicao.json()) # {'USDBRL': {'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Americano/Real Brasileiro', 'high': '5.5925', 'low': '5.52722', 'varBid': '0.0105', 'pctChange': '0.189852', 'bid': '5.5411', 'ask': '5.5441', 'timestamp': '1749835985', 'create_date': '2025-06-13 14:33:05'}, 'EURBRL': {'code': 'EUR', 'codein': 'BRL', 'name': 'Euro/Real Brasileiro', 'high': '6.43087', 'low': '6.35324', 'varBid': '-0.028714', 'pctChange': '-0.447363', 'bid': '6.38978', 'ask': '6.40615', 'timestamp': '1749835659', 'create_date': '2025-06-13 14:27:39'}, 'BTCBRL': {'code': 'BTC', 'codein': 'BRL', 'name': 'Bitcoin/Real Brasileiro', 'high': '603642', 'low': '572800', 'varBid': '-16468', 'pctChange': '-2.734', 'bid': '585798', 'ask': '585847', 'timestamp': '1749835989', 'create_date': '2025-06-13 14:33:09'}}


# Minha requisição com o firebase (https://console.firebase.google.com/project/requests-python-d3352/database/requests-python-d3352-default-rtdb/data?hl=pt-br)
requisicao = requests.get('https://requests-python-d3352-default-rtdb.firebaseio.com/.json') # <- colocar '.json' ao final do link obrigatoriamente.
print(requisicao.json())


# POST = ENVIAR INFORMAÇÕES (POST = POSTAR, PUBLICAR, ENVIAR)
informacoes = '{"Nome": "Flame2"}' # Precisa ser string
requisicao = requests.post('https://requests-python-d3352-default-rtdb.firebaseio.com/.json', informacoes)
print(requisicao)
print(requisicao.json())



# PATCH = ATUALIZAR UMA INFORMAÇÃO (PATCH = ATUALIZAR, RENOVAR, ALTERAR ALGO EXISTENTE;)
informacoes = '{"Nome": "Felipe", "Sobrenome": "Castanhari", "Idade": 34}'
requisicao = requests.patch('https://requests-python-d3352-default-rtdb.firebaseio.com/-OSeQiNYIu7oEbZPxxaK.json', informacoes)
print(requisicao)
print(requisicao.json())


# DELETE = DELETAR UMA INFORMAÇÃO (DELETE = DELETAR, EXCLUIR)
requisicao = requests.delete('https://requests-python-d3352-default-rtdb.firebaseio.com/-OSeSSFX4HGDkplaXee3.json')
print(requisicao)
print(requisicao.json())
