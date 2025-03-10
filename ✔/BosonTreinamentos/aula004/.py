# Importação de módulos e gerenciamento de pacotes com pip
# Importando o módulo inteiro
import math

# Importando funções específicas do módulo math
from math import ceil, floor, sqrt

# Também é possível renomear um módulo usando 'as'
import math as matematica

# Importando o módulo random
import random

# Gerando um número aleatório entre 1 e 500
num = random.randint(1, 500)

# Exemplos de uso das funções do módulo math
print(matematica.floor(45.6))   # Arredonda para baixo
print(math.floor(56))           # Arredonda para baixo
print(math.ceil(56.0001))       # Arredonda para cima
print(math.sqrt(81))            # Raiz quadrada
print(num)                      # Exibe o número aleatório gerado