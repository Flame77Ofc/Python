# Trocar valores entre duas variáveis
x = 5
y = 10

troca = x, y = y, x
print(f'Troca: {troca}, x: {x}, y: {y}')


# Operador Condicional Ternário
lampada = not True
print('a lampada está acessa' if lampada else 'a lampada está apagada')
#      'expressão True'         condição         'expressão False'
# Se lampada for True, imprima: 'a lampada está acessa' se não, imprima: 'a lampada está apagada'



# Conta quantas linhas há no código
i = 0
with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo.readlines():
        i += 1

    print(i)