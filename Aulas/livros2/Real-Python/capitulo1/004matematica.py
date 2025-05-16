# Operadores Aritméticos: São os usados no dia a dia, como adição, subtração, multiplicação e divisão
# adicao = 6 + 7
# subtracao = 4 - 5
# multiplicacao = 4 * 6
# divisao = 12 / 4 # A divisão sempre retornará um número float
# divisao = 12 // 4 # A divisão de 2 barras retornará um int
# exponenciacao = 2**4
# resto = 12 % 5 # O resto retornará o resto da divisão, ou seja, o número que sobrou. 12 / 5 = 10, e sobrou 2 para chegar em 10, então o resto de 12 % 5 é 2

# Alternando a Ordem de Precedência com os parênteses
# Quando você quer alterar a ordem de execução de uma expressão, é utilizado os parênteses
# Você quer fazer o cálculo 12 + 5 * 3, então você queria a saída 34, mas o computador executa a ordem em que os operadores são superiores a outros, e como multiplicação é superior a adição, executará primeiro a multiplicação.
# expressao = 12 + 5 * 2 # 22
# Corrigindo
# expressao = (12 + 5) * 2 # 34


# Arredondando um número de casas decimais grandes com o round()
# round(numero, casas decimais)
# print(round(456.6545821247, 3)) # Irá mostrar o número com apenas 3 casas decimais após a vírgula


# Mostrando os números com estilo: Utilizando f-strings
numero = 12.567
print(f'O número é {numero}')