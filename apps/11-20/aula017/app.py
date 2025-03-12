# Classes e Objetos ⇒ POO
"""
class ClassName:
    statements(s)
"""


# Class Básica
class Person:
    first_name = 'Gabriel'
    last_name = 'Goulart'
    age = 14

obj = Person()
print(obj.first_name)
print(obj.last_name)
print(obj.age)


# Class com Atributos
class Student:
    def __init__(self, id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age

student1 = Student(369, 'Gabriel Goulart', 14)


# Classe com Atributos e funções
class Estudante:
    def __init__(self, name):
        self.name = name

    def Ola_Estudante(self):
        print('Olá', self.name)
        
estudante1 = Estudante('Gabriel')
estudante1.Ola_Estudante()