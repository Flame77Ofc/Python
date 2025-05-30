# Erros e Exceções
try:
    y = 6
    print(y / 0)
except:
    print('Erro')

try:
    y = 6
    print(y / 0)
except ZeroDivisionError as erro:
    print(f'Erro: {erro}')



try: # Executa se não houver erros
    primt('Olá')
except: # Executa se houver erros
    print('Falhou')
else:  # Executa se o bloco try não houver erros
    print('O bloco try funcionou')
finally: # Executa sempre
    print('Bloco finally executado.')






try:
    variavel = input('Digite algo: ')
    print(int(variavel) / 2)
except Exception as erro:
    print(f'Erro: {erro}')