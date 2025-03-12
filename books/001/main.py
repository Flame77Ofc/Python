class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __call__(self):
        return f"{self.name} is {self.age} years old."

poopy = Dog('poopy', 6)
print(poopy())