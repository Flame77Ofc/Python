import sqlite3, random
# O que falta: colocar o saldo aleatório, colocar um menu de seções, tratar as excessões do menu


nome = input('Por favor, informe o seu nome: ')
pizza = input('Qual o nome da pizza que você quer? ')
tamanho = int(input("Por favor, digite qual será o tamanho da pizza: "))
quantidade = int(input("Quantas pizzas quer? "))


conexao = sqlite3.connect('pizzas.db')
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS pedido (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               pizza TEXT,
               tamanho INTEGER,
               quantidade INTEGER
        )""")

cursor.execute("INSERT INTO pedido (nome, pizza, tamanho, quantidade) VALUES (?, ?, ?, ?)", (nome, pizza, tamanho, quantidade))




# pedidos
pedidos = cursor.fetchall()

# Exibe os resultados
for pedido in pedidos:
    print(pedido)

conexao.commit()
conexao.close()