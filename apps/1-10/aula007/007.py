# POO ⇒ Classes
class User:
    nome = 'Gabriel'
    sobrenome = 'Goulart'
    def nomeCompleto(self):
        return self.nome + ' ' + self.sobrenome
print(User().nomeCompleto())




# Com constructor em py
class User2:
    def __init__(self):
        self.nome2 = 'Gabriel'
obj = User2()
print(obj.nome2)