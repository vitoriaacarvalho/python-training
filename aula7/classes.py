"""pra eu nao ter que fazer isso aqui:
class Client:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
"""
#Fazemos isso:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_name=self.__class__.__name__
class Client(Person):
    pass

class Student(Person):
    pass