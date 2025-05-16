# Tratamento de Erros e Exceções
# Algumas vezes você pode prever um erro utilizando as exceções embutidas do python, assim evitando que erros estraguem o seu programa
# sintaxe do try... except
# try:
#     <TENTAR executar este bloco de código>
# except:
#     <mas se a tentativa de execução falhar, EXECUTE este bloco de código> # Semelhante a condicionais


# ----------EXEMPLO----------
try: # Tenta executar esse bloco de código:
    numero = int(input("Digite um NÚMERO: "))
except: # Mas se falhar, então o programa executará esse pois viu que era um erro
    print('Ah, pedi para digitar um número :(')


# Existem diversas Exceções de Erros que você pode tratar, cada um com seu nome específico.
# - Divisão de um número por zero: ZeroDivisionError
# - Erro de valor: ValueError
# - Erro de Indentação: IndentationError
# Mas você pode simplesmente usar um except para todos os tipos de erros.
try:
    numero = int(input("Digite um NÚMERO: "))
    print(numero / 0)
except ZeroDivisionError:
    print('ERRO: Divisão de um número por 0')
