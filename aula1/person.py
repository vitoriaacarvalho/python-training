from datetime import datetime
class Person:
     #nao lembro como faz o ano
     def __init__(self,name, age, eating=False, talking=False):
          self.name=name
          self.age=age
          self.eating=eating
          self.talking=talking

     def talk(self, topic):
          if self.eating:
               print(f"{self.name} cant talk right now")
               return
          elif self.talking:
               print(f"{self.name} is already talking")
               return
          print(f"{self.name} is talking about {topic}")
          self.talking=True

     def stop_talking(self):
          if not self.talking:
               print(f"{self.name} isnt even talking right now")
               return
          print(f"{self.name} stopped talking")

     def eat(self, food):
          if self.eating:
               print(f"{self.name} is already eating")
               return
          elif self.talking:
            print(f"{self.name} is already talking")
            return
          print(f"{self.name} is eating {food}")
          self.eating=True

     def stop_eating(self):
          if not self.eating:
               print(f"{self.name} is not eating anything")
               return
          print(f"{self.name} just stopped eating")
          self.eating=False


