<!--  O que falta agora? -->

# [ ] - Verificar se o usuário está logado em todas as páginas




import os

pasta = 'meu'

try:
    os.rmdir(pasta)
    print(f"Pasta '{pasta}' removida com sucesso.")
except:
    pass
