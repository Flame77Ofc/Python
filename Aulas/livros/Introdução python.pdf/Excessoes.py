# try:

# except:

# finally:

try: # Tenta executar esse bloco de código
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
except: # Se dar erro, vai para esse bloco
    print('Valor incorreto!')
else: # Se try conseguir executar, vai executar o bloco else
    print('Número correto')
finally: # Esse bloco sempre será executado independente do valor do try
    soma = num1 + num2
    print(soma)