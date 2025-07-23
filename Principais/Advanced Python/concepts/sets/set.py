# Sets são conjuntos mutáveis, não possuem ordem e não aceitam elementos duplicados

conjunto = {"abelha", "formiga", "abelha"}
print(conjunto) # {"abelha", "formiga"} ou {"formiga", "abelha"}

conjunto.add("formiga") # Adiciona formiga
print(conjunto) # {'formiga', 'abelha'}

conjunto.remove("formiga") # Remove a formiga
conjunto.add("borboleta") # Adiciona borboleta
print(conjunto) # {'abelha', 'borboleta'}

conjunto.pop() # Remove um elemento aleatório
print(conjunto)
