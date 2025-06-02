import sqlite3
from datetime import datetime
from random import randrange


agora = datetime.now().strftime('%H:%M:%S, %d/%m/%Y')
livros = []

with open('livraria.txt', 'a+', encoding='utf-8') as arquivo:
    arquivo.seek(0)
    conteudo = arquivo.read()

    nome = input('Digite o seu nome: ').strip().title()
    idade = int(input('Digite a sua idade: '))

    quantidade = int(input('São quantos livros? '))
    for i in range(quantidade):
        preco = randrange(25, 85, 5)
        livro = input('Digite o nome do livro: ').strip().title()
        print(f'O preço detse livro é R${preco},00')
        livros.append(f'{livro, preco}')

    livraria = [livro for livro in livros]
    livraria = ', '.join(livraria).title()
    
    # texto = f'{nome} de {idade} anos comprou os livros {livraria} às {agora}\n'
    texto = f'[\nnome: {nome}\nidade: {idade}\nlivros: {livraria}\ndata: {agora}]\n'
    arquivo.write(texto)

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS dados (
    nome TEXT,
    idade INT,
    livros TEXT
)
""")

cursor.execute("INSERT INTO dados (nome, idade, livros) VALUES (?, ?, ?)", (nome, idade, livraria))

conexao.commit()
conexao.close()