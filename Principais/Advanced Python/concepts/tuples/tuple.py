# Tuplas são imutáveis, ordenadas e permitem elementos duplicados

tupla = ("pessoa1", "pessoa2")
print(tupla) # ('pessoa1', 'pessoa2')

# del tupla[0] # Erro
# tupla.remove("pessoa1") # Erro

# Únicas funções
print(tupla.index("pessoa1")) # 0
print(tupla.count("pessoa2")) # 1


# Os parênteses são opcionais. Quando há varios elementos separados por vírgulas e estes são atribuídos a uma variável, aquele conjunto de elementos vira uma tupla
elementos = ("Fogo", "Terra", "Ar", "Água") # Tupla
print(elementos)

elementos = "Fogo", "Terra", "Ar", "Água" # Tupla
print(elementos)


# Cuidado: Quando há apenas um elemento cercado por parênteses, ainda é considerado uma string.
string = ("texto") # String


# Tuplas também possuem índice.
cores = ("Azul", "Amarelo", "Verde", "Vermelho")
print(cores[2]) # Verde
print(cores[1:]) # ('Amarelo', 'Verde', 'Vermelho')

print("Azul" in cores)


# Convertendo tupla para lista
animais = ("Elefante", "Macaco", "Rinoceronte", "Gato", "Cachorro", "Coelho")
lista_animais = sorted(list(animais))
print(lista_animais) # ['Cachorro', 'Coelho', 'Elefante', 'Gato', 'Macaco', 'Rinoceronte']

# Curiosidade: Tuplas são mais "leves" em bytes em comparação com listas
