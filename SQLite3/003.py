import sqlite3
nome = input("Digite o seu nome: ")
senha = input("Digite a sua senha: ")

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS pessoas (
               nome TEXT,
               senha TEXT
    )""")

cursor.execute("INSERT INTO pessoas (nome, senha) VALUES (?, ?)", (nome, senha))

conexao.commit()
conexao.close()