# Programação Orientada a Objetos (POO):
# Já pensou alguma vez em trazer coisas do mundo real para o computador? O POO é capaz de modelar essas coisas. Você pode criar objetos, pessoas, materiais, qualquer coisa do mundo físico para um molde para o programa. Vamos lá!
# Imagine um cliente interessado em uma compra de um carro. O cliente, quando vai em uma concessionária, está interessado com algumas características do carro, como o valor, o modelo, a cor, a marca, entre outros. Vamos represenntar isso no mundo da programação.

# Primeiramente criaremos uma classe. Para fazer isso, utiliza-se a palavra-chave class seguida em um nome seguido pelos dois pontos(:), vamos utilizar carro. Importante lembrar que o primeiro caractere do nome da classe deve ser em maiúsculo, ficando assim 'Carro':
class Carro:
    # Em seguida, criamos uma função, com o nome __init__ seguido por parênteses e dentro dos parênteses os argumentos. Deve ter o self como argumento obrigatório para poder executar com êxito. Logo após o self, separamos por vírgulas os argumentos que queremos. Vamos colocar os argumentos: carro, modelo, cor, marca, preco. Dentro do bloco de código da função, colocamos o seguinte:
    # self.argumento = argumento. Veja como fica:
    def __init__(self, carro, modelo, cor, marca, preco):
        self.carro = carro
        self.modelo = modelo
        self.cor = cor
        self.marca = marca
        self.preco = preco

# Já podemos criar nossas variáveis! Veja como criar uma variável e atribuir seus valores aos da classe:
Lamborghini = Carro('Lamborghini', 'RXT3500', 'azul', 'RW Sports', 3400000) # Atribuímos a variável os respectivos valores da classe.
print(f'Carro: {Lamborghini.carro}') # Imprimimos na tela o valor que quisermos
print(f'Modelo do carro: {Lamborghini.modelo}')
print(f'Cor do carro: {Lamborghini.cor}')
print(f'Preço do carro: {Lamborghini.preco}')