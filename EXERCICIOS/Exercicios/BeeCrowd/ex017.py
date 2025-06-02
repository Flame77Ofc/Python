"""Este programa deve ler uma variável inteira X inúmeras vezes (deve parar quando o valor no arquivo de entrada for igual a zero). Para cada valor lido imprima a sequência de 1 até X, com um espaço entre cada número e seu sucessor.
"""

x = int(input('Digite o número: '))
for i in range(1, x+1):
    print(i, end=' ')