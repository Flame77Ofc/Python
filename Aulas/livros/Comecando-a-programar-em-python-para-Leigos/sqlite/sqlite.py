import sqlite3

# Conecta ao banco de dados (se não existir, ele é criado)
conn = sqlite3.connect('meubanco.db')
cursor = conn.cursor()

# Cria a tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        password TEXT
    )
''')

# Menu de opções
print("\n=== Menu ===")
print("1. Adicionar novo usuário")
print("2. Listar usuários")
opcao = input("Escolha uma opção: ")

if opcao == '1':
    # Adicionar usuário
    name = input("Informe seu nome: ")
    password = input("Informe sua senha: ")
    cursor.execute('INSERT INTO users (name, password) VALUES (?, ?)', (name, password))
    conn.commit()
    print("Usuário adicionado com sucesso!")

elif opcao == '2':
    # Listar usuários
    cursor.execute('SELECT * FROM users')
    usuarios = cursor.fetchall()
    print("\n=== Lista de Usuários ===")
    for usuario in usuarios:
        print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Senha: {usuario[2]}")

else:
    print("Opção inválida!")

# Fecha a conexão
conn.close()