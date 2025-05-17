# Sets são sequências desordenadas(Não possuem uma ordem especifica, a ordem de seus elementos é aleatória) e são muito úteis em situações específicas. Os sets, diferentemente das listas, possuem chaves, e cada elemento também é separado por vírgulas. Os sets não aceitam valores repetidos, isso é muito bom para eliminar todos os valores de uma lista comum, por exemplo. Vamos ver um exemplo:
lista = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'b', 'b', 'c']
lista = set(lista)
lista = list(lista)
print(lista) # ['a', 'b', 'c']

# Vamos mergulhar no mundo dos sets!
# Vamos supor que queremos fazer um bolo. Alguém muito inexperiente em culinária separou os igredientes, veja:
igredientes = {'Farinha', 'Trigo', 'Madeira', 'Alface'}
# índices          0         1         2          3
print(igredientes)

# Você vê os igrediente e se pergunta: "Por que Madeira e Alface estão entre os igredientes?" Você precisa achar algum jeito de remove-los! Por sorte existe a função remove, vamos ver!

# a função remove é responsável por remover algum elemento dentro de um set. Basta dizer o nome do elemento e ele será removido. Vamos remover os igredientes que não fazem sentido:
# sintaxe: set.remove('elemento')
igredientes.remove('Madeira')
print(igredientes) # {'Farinha', 'Alface', 'Trigo'}
# Isso! Removemos a Madeira! Agora vamos remover o Alface! 
igredientes.remove('Alface')
print(igredientes) # {'Farinha', 'Trigo'}

# Ok, o bolo está com apenas dois igredientes, precisamos de mais! Vamos adicionar o fermento!
# Podemos adicionar um elemento com a função add. Ficaria assim:
igredientes.add('Fermento')
print(igredientes) # {'Trigo', 'Farinha', 'Fermento'}
# Ainda faltam igredientes, vamos adiconar mais!
igredientes.add('Açucar')
igredientes.add('Ovos')
igredientes.add('Leite')
igredientes.add('Manteiga')
print(igredientes) # {'Açucar', 'Farinha', 'Fermento', 'Ovos', 'Trigo', 'Leite', 'Manteiga'}
# Ah, agora sim! Já temos todos os igredientes!


# Imagine agora temos um set que possui algumas frutas dentro dele:
frutas = {'Maçã', 'João', 'Banana', 'Pedro', 'Vinicius', 'Abacaxi', 'Limão', 'Felipe', 'Macarrão', 'Peixes'}
# Mas espera. Essa lista está cheia de coisas que não são frutas! Podemos remover cada elemento um por um, mas isso seria trabalhoso. Uma maneira mais fácil é limpar a lista toda de uma vez e utilizar a função add para adicionar novas frutas posteriormente.
# Limpando a lista
# Com os sets é possível limpar a lista utilizando a função clear:
# sintaxe: set.clear()
frutas.clear()
print(frutas) # set() Isso mostra que o set está vazio e não possui nenhum elemento. Ótimo, agora vamos adicionar os elementos na lista

frutas.add('Maçã')
frutas.add('Banana')
frutas.add('Limão')
frutas.add('Abacaxi')
print(frutas) # {'Banana', 'Maçã', 'Limão'}

# Para ter certeza, vamos verificar se os elementos estão no set:
print('Maçã' in frutas) # True
print('Banana' in frutas) # True
# E também vamos verificar se os elementos antigos não estão mais no set:
print('Vinicius' not in frutas) # True
print('Pedro' not in frutas) # True

# Perfeito, só faltou verificar quantas frutas nosso set possui. Vamos fazer isso utilizando a função len
quantidade = len(frutas)
print(quantidade) # 4

# Ótimo, isso mostra que os sets são muito poderosos e apresentam muitas funcionalidades!