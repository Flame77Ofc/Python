# Operadores Aritméticos
# Os operadores aritméticos são responsáveis por fazer os cálculos básicos em um programa. São eles:
"""
Adição (+)
Subtração (-)
Multiplicação (*)
Divisão (/)
Divisão Inteira(//)
Exponenciação (**)
Módulo (%)
"""
# vamos ver como cada um funciona
5 + 2 == 7 # Realiza a soma entre os dois números
5 - 2 == 3 # Subtrai o número da esquerda pelo número da direita
5 * 2 == 10 # Multiplica os dois números
5 / 2 == 2.5 # Divide o número da esquerda pelo número da direita
5 // 2 == 2 # Divide mas retorna um inteiro, sem a parte decimal
5 ** 2 == 25 # Realiza a exponenciação entre dois números
5 % 2 == 1 # É o resto da divisão

# Ordem de precedência
"""
1. ()
2. **
3. *, /, //, %
4. +, -
"""
# Os parênteses alteram a ordem em que as expressões serão executadas

# Exercícios
5 + 3 * 2 == 11 # Porque é feita primeira a multiplicação entre 3 * 2 e depois a soma entre o resultado da multiplicação + 5
(5 + 3) * 2 == 16 # Porque é feita primeira a expressão que está dentro dos parênteses


mensagem = 'Oi'
print(mensagem * 5) # OiOiOiOiOi