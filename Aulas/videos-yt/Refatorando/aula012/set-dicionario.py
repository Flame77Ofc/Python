# Set: set é um tipo de lista que possui seus valores aleatórios, ou seja, são desordenados. Não aceitam elementos duplicados
frutas = {"Maçã", "Laranja", "Maçã", "Maçã"}
print(frutas) # {'Maçã', 'Laranja'} ou {'Laranja', 'Maçã'}

frutas.add("Pera")

frutas.remove("Maçã")

frutas.pop()


# Dicionários: São desordenados
meses = {
    "Jan": "Janeiro",
    "Fev": "Fevereiro",
    "Mar": "Março",
    "Abr": "Abril",
    "Mai": "Maio",
    "Jun": "Junho",
    "Jul": "Julho",
    "Ago": "Agosto",
    "Set": "Setembro",
    "Out": "Outubro",
    "Nov": "Novembro",
    "Dez": "Dezembro"
}
# Diferença entre imprimir pelo índice e pelo get:
print(meses["Jan"]) # Se o valor não for encontrado, dará erro.
print(meses.get("Jan", "Dezembro")) # Se o valor não for encontrado, exibirá "None" ou o padrão especificado(Dezembro)