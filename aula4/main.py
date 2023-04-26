#ASSOCIAÇÃO:::: fazer uma classe conversar com outra , nesse caso nenhuma das classes vai depender da outra.
from classes import Writer
from classes import Pen
from classes import WritingMachine

w1=Writer('joazinho')
print(w1.name)

p1=Pen('bic')
print(p1.type)
machine=WritingMachine()
print(machine)