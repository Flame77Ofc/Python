"Código com escopo local e global"
# x = 3

# def func():
#     x = 2
#     print(f"Dentro da função, x vale {x}")

# func()
# print(f"Fora da função, x vale {x}")

"Código resolvido definindo x como global dentro da função:"
x = 3

def func():
    x = 2
    print(f"Dentro da função, x vale {x}")

func()
print(f"Fora da função, x vale {x}")