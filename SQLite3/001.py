import sqlite3
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS pessoas (
               nome TEXT,
               idade INTEGER
    )""")

cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, idade))

conexao.commit()
conexao.close()