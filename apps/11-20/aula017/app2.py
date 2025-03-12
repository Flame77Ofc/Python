# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def andar(self):
        print(self.name + ' andou')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def som(self):
        print(self.name + ' latiu')

cachorro = Dog('Puppy')
cachorro.andar()
cachorro.som()