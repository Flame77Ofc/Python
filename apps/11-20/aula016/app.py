"""O pass em Python é uma instrução usada como um espaço reservado quando uma declaração é exigida sintaticamente, mas nenhuma ação precisa ser executada. Quando o `pass` é executado, nada acontece.  

Ele pode ser usado em funções, estruturas condicionais (`if-else`), loops (`for`, `while`) e classes para evitar erros de sintaxe enquanto o código está em desenvolvimento.  
"""
### Exemplos:  

def add():
    pass  # Função sem implementação

def subtract():
    pass  

if 55:
    pass  # Bloco if sem código
else:
    pass  

pets = ["cat", "dog", "rabbit"]
for pet in pets:
    pass  # Loop sem corpo

class Student:
    pass  # Classe vazia

print("Hello World!")  # O código continua normalmente