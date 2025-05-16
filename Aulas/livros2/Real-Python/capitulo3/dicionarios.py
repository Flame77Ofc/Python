# Dicionários: São semelhantes as listas, são mutáveis (É possível alterar seu conteúdo), porém não possuem índices, mas sim pares de CHAVE e VALOR. As chaves vão identificar os valores por isso são únicas, como os índices. Vamos esclarecer:
# Vamos supor que estavamos no mercado, e fomos até a seção de frutas. Um dicionário ficaria assim:
frutas = {
    'Maçã': 0.99,
    'Laranja': 1.39,
    'Abacaxi': 1.99
#    chave: valor
}
print(frutas)
# Pode-se perceber que criamos um dicionário com o nome de frutas, e a primeira chave é Maçã, com o valor de 0.99 reais, seguido por uma vírgula obrigatória para separar os pares de chave-valor. Jamais esqueça das vírgulas após o término de um par chave-valor.
# Os dicionários podem ser escritos assim:
frutas = {'Maçã': 0.99, 'Laranja': 1.39, 'Abacaxi': 1.99}
# As duas formas estão corretas, mas eu usarei a primeira forma.

# Vamos ver mais um exemplo de dicionário
dados_pessoais = {
#   'nome': idade
    'João Lucas': 14,
    'Maria Fernanda': 23,
    'Alexandre Ferreira': 37
}
# Aqui criamos um dicionário onde guarda informações de 3 pessoas. Não é uma boa escolha utilizar isso num dicionário, Já que pode acontecer de duas pessoas terem o mesmo nome, e um dicionário pode haver apenas uma chave única. Um bom caso seria usar dicionários para coisas realmente únicas, como um cpf, numero de telefone, ou um próprio id único

# Vamos explorar o que é possível fazer com os dicionários
dados = {
    1: 'Henrique da Costa',
    2: 'Felipe dos Santos',
    3: 'Arthur Feitosa',
    4: 'Marcos Teixera',
    5: 'Fábio Alberto'
#   chave: valor
}
# Acessando o valor de um dicionário pela sua chave
# Para acessar o valor de um dicionários, basta colocar qual é a sua chave:
# dicionario[chave]
dados[2] # Felipe dos Santos
dados[5] # Fábio Alberto

# Alterando chaves e valores explicitamente
# Para criar chaves e valores, basta especificar qual será o nome da chave e qual será o seu valor. 
# - Se você alterar uma chave que já existe, então apenas substituirá o valor antigo pelo novo
# - Mas se não existir a chave, então é criada uma nova chave com o novo valor
#  Vamos ver como isso funciona:
# dicionario[chave] = 'substituição de valor/novo valor'
dados[3] = 'Marco Antônio' # A chave '3' já existe, então apenas substituirá
dados[6] = 'Luiza Moura' # A chave não existe, então será criada uma nova chave com o valor 'Luiza Moura'
print(dados)



dados = {
    1: 'Henrique da Costa',
    2: 'Felipe dos Santos',
    3: 'Arthur Feitosa',
    4: 'Marcos Teixera',
    5: 'Fábio Alberto'
#   chave: valor
}


# deletando pares chave-valor de um dicionário
# utilizando o del
# sintaxe: del dicionario
del dados[2] # Deleta o par de chave-valor da chave 2, ou seja, deleta a chave e o valor
del dados[4]


dados = {
    1: 'Henrique da Costa',
    2: 'Felipe dos Santos',
    3: 'Arthur Feitosa',
    4: 'Marcos Teixera',
    5: 'Fábio Alberto'
#   chave: valor
}



# As chaves e os valores são muito úteis para visualizar os dados de um dicionários mais facilmente
# Acessando as chaves do dicionário
# sintaxe: dicionario.keys()
chaves = dados.keys()

# Acessando os valores do dicionário
# sintaxe: dicionario.values()
valores = dados.values()

# Acessando os itens do dicionário
# sintaxe: dicionario.items()
itens = dados.items()


# Verificando se uma chave está no dicionário
1 in dados.keys() # O programa verifica se 1 está presente nas chaves do dicionário
'Fábio' in dados.values() # O programa verifica se 'Fábio' está presente nos valores do dicionário
'Henrique' not in dados.values() # O programa verifica se 'Henrique' não está presente nos valores do dicionário



# Criando dicionários dentro de outros dicionários
# Já pensou em ter dicionários dentro de dicionários? Parece um pouco confuso, mas é tão simples quanto um dicionário comum. Vamos ver como isso funciona.
pessoas = {
    'João Miguel': {
        'idade': 14,
        'cidade': 'Cidade dos Astronautas',
        'rua': 'Rua dos Capixabas'
    },
    'Lucas Ferreira': {
        'idade': 23,
        'cidade': 'Cidade do Folclore',
        'rua': 'Rua dos Caçadores'
    }
}
# Para acessar a lista, as coisas mudam um pouco. Veja como que fica:
# dicionario[chave][chave]
print(pessoas['João Miguel']['idade']) # 14