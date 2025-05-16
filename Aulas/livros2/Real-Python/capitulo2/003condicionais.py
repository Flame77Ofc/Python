# OPERADORES DE COMPARAÇÃO: Comparam expressões e retornam um booleano (True ou False)
# MAIOR QUE
# Compara se a expressão da esquerda é maior do que o da direita
5 > 6 # 5 é maior que 6? False
21 > 5 # 21 é maior que 5? False

# MENOR QUE
# Compara se a expressão da esquerda é menor do que o da direita
7 < 9 # 7 é menor que 9? True
5 < 1 # 5 é menor que 1? False

# MAIOR OU IGUAL QUE
# Compara se a expressão da esquerda é maior ou igual do que o da direita
5 >= 5 # 5 é maior ou igual a 5? True
7 >= 2 # 7 é maior ou igual a 2? True

# MENOR OU IGUAL QUE
# Compara se a expressão da esquerda é menor ou igual do que o da direita
4 <= 9 # 4 é menor ou igual a 9? True
12 <= 4 # 12 é menor ou igual a 4? False

# DIFERENTE DE
# Compara se a expressão da esquerda e o da direita são diferentes, isso é, não são iguais
4 != 5 # 4 é diferente de 5? True
9 != 9 # 9 é diferente de 9? False

# IGUAL A
# Compara se ambas expressões são iguais
5 == 3 # 5 é igual a 3? False
6 == 7 # 6 é igual a 7?



# OPERADORES LÓGICOS: Retornam valores booleanos(True e False)
# and
# Retorna True apenas se ambas expressões forem True. Se ao menos uma expressão for False, então retornará False.
False and True # Uma ou ambas expressões precisam ser False para retornar um False, nesse caso também retornará False, pois uma expressão é False
6 > 5 and 2 < 10 # 6 É maior que 5 e 2 é menor que 10? 6 é maior que 5 e 2 é menor que 10, então será True
5 < 3 and 9 == 9 # 5 É maior que 3 e 9 é igual a 9? 5 não é menor que 3 e 9 é igual a 9, mas o retornará False pois uma expressão é False

# or
# Retorna True se ao menos um valor for True. Retornará False se ambos os valores forem False.
True or False # Uma expressão é True e a outra False, porém é necessário apenas uma expressão para retornar True
6 == 5 or 2 > 1 # 6 é igual a 5 ou 2 é maior que 1? 6 não é igual 5, porém 2 é maior que 1, retornando True
2 != 2 or 9 + 5 == 15  # 2 é diferente de 2 ou 9+5 é igual a 15? 2 não é diferente de 2, e 9+5 não é 14, portanto, as duas expressões são falsas, retornando False

# not
# Inverte uma expressão booleana, True se transforma em False e vice-versa.
not True # Retornará Falso
not False # Retornará True
not 5 > 6 or 5 > 10 # Retornará True, pois 5 > 6 foi alterado para True, e basta um valor ser True que retornará True.


# CONDIÇÕES
# Condições são caminhos que o programa deve seguir dependendo de uma condição. Para que um bloco de código seja executado, a condição deverá ser verdadeira(True), assim alterando o fluxo de execução de um programa. Mas se a condição for falsa, o programa também poderá executar outro bloco de código
# Sintaxe Básica
# if condição: # Se a condição for verdadeira...
#     <bloco de codigo>
# else: # Mas se a condição for falsa...
#     <bloco de codigo>

# ---------EXEMPLOS---------
# O programa verifica se a variável 'chovendo' é True, e executará um bloco de código específico.
chovendo = True # Chovendo é verdadeiro (Está chovendo)
if chovendo == True: # Se estiver chovendo, então execute esse bloco de código:
    print('Está chovendo!') # Imprimir "Está chovendo!"
else: # Mas se não estiver chovendo, isto é, se chovendo for False, execute esse bloco de código:
    print('Não está chovendo!') # Imprimir "Não está chovendo!"


# O programa verifica se 2 + 2 é 4 e executa um bloco de código dependendo do resultado.
if 2 + 2 == 4:
    print('2 + 2 é 4!')
else:
    print('Como assim, 2 + 2 não é 4?')


# O programa verifica em que cor o semáforo está. O código a seguir apresenta a palavra-chave 'elif', que compara outra condição.
cor = 'vermelho' 
if cor == 'vermelho': # Verifica se o semáforo é vermelho e executa o seguinte código:
    print('Semáforo vermelho! Pare!')
elif cor == 'verde': # Verifica se o semáforo é verde e logo executa:
    print('Semáforo verde! Vá!')
elif cor == 'amarelo': # Verifica se o semáforo é amarelo e executa o seguinte código:
    print('Semáforo amarelo! Espere!')
else: # Porém, se as cores não estiverem entre aquelas já citadas, executará 'Cor desconhecida', pois não existe essa cor em um semáforo
    print('Cor desconhecida!')


