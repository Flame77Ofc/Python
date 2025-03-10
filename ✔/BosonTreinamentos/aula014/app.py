# Manipulação de arquivos
"""
r: ler
manipulador = open('BosonTreinamentos/aula014/arquivo.txt', 'r', encoding='utf-8')
print(manipulador.read())
manipulador.close()
"""

"""
w:escrever(substitui todo o texto atual)
manipulador = open('BosonTreinamentos/aula014/arquivo.txt', 'w', encoding='utf-8')
print(manipulador.write('Escrever'))
manipulador.close()
"""

"""
a: escrever(Adiciona texto, não substitui)
manipulador = open('BosonTreinamentos/aula014/arquivo.txt', 'a', encoding='utf-8')
print(manipulador.write('Escrever'))
manipulador.close()"""