arquivos = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt"] # Criando a lista de arquivos

arquivo = "arquivo4.txt" # Atribuindo em uma variável o arquivo4
arquivos.append(arquivo) # Adicionando a variável arquivo ao final da lista

arquivos.sort(reverse=True) # Ordenando a lista em ordem decrescente
print(arquivos)

# Iterando sobre cada item da lista
for arquivo in arquivos:
    print(arquivo)

# Criando arquivos com o nome de cada item da lista
for arquivo in arquivos:
    with open(f"lists/{arquivo}", "w", encoding='utf-8') as arq:
        arq.write(f"Este é o arquivo {arquivo}")



carros = ["Ferrari", "Volkswagen", "Ford", "Honda", "Porsche", "Jeep", "Chevrolet", "Toyota"]
primary = [initial for initial in carros if initial[0] < "M"] # Pega os carros que sua primeira letra é menor que M

print(primary)