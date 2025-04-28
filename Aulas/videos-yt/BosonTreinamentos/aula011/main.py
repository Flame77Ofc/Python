# POO em Python :(
class Veiculo:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    buzinar = lambda self: print(f"O {self.nome} buzinou")

fusca = Veiculo("Fusca", "Branco")
fusca.buzinar()