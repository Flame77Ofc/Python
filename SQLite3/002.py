import sqlite3

with sqlite3.connect('banco_dados.db') as conexao:
    nome = input("Digite o seu nome: ")
    senha = input("Digite a sua senha: ")
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome TEXT, senha TEXT)")
    cursor.execute("INSERT INTO pessoas (nome, senha) VALUES (?, ?)", (nome, senha))
