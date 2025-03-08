import pandas as pd

# Criando um DataFrame simples
data = {
    'Nome': ['Gabriel', 'Julia'],
    'Idade': [14, 15],
    'Cidade': ['São Paulo', 'Rio de Janeiro']
}

variavel = pd.DataFrame(data)

# Exibindo o DataFrame
print(variavel)