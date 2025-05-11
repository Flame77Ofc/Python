class Cliente:
    def __init__(self, nome, telefone, cpf):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf

    def mostrar_informacoes(self):
        informacoes = {
            'nome': self.nome,
            'telefone': self.telefone,
            'cpf': self.cpf
        }
        for chave, valor in informacoes.items():
            print(f'{chave}: {valor}')
    
clienteID1 = Cliente('João Victor da Silva', '(49) 9732-5091', '387.213.980-21')
clienteID1.mostrar_informacoes()