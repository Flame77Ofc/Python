expressao = input("Digite a expressão:\n>>>")
esquerdo = expressao.count('(')
direito = expressao.count(')')

if (esquerdo == direito):
    print("Expressão correta")
else:
    print('Expressão incorreta')