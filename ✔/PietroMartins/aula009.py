# Dicionários
pessoa = {
    'nome': 'Teste',
    'peso': 0.0,
    'idade': 0,
}
print(pessoa)
nome = str(input('Informe seu nome ' ))
peso = float(input('Informe seu peso ' ))
idade = int(input('Informe sua idade ' ))

pessoa['nome'] = nome
pessoa['peso'] = peso
pessoa['idade'] = idade
print(pessoa)