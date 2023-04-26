"""
COMPOSIÇÃO= o relacionamento mais acoplado de todos eles
se a classe principal for apagada todos os objetos que usarem ela vao deixar de funcionar
"""
from classes import Client, Address
client1=Client('vitoria',19)
print(client1.addresses)
client1.insert_address("joao pessoa","paraiba")
print(client1.address_list())
print(client1)