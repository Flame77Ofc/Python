## Módulos

import math
# math
print(4 ** 1//2)
print(int(math.sqrt(4)))
print(math.floor(5.6))
print(math.ceil(7.1))


import random
# random
# Com listas
nomes = ['Gabriel', 'Julia', 'João', 'Pedro', 'Maria']
print(random.choice(nomes))

# Com números> mostra números aleatórios de 1 a 12
print(random.randint(1, 12))

# string
from string import ascii_lowercase
print(ascii_lowercase)

# Importando pelo arquivo
import support
teste = support.Teste()
print(teste.a)
print(teste.alguns_metodos())

print(support.var)

print(support.add_2_nums(3, 7))