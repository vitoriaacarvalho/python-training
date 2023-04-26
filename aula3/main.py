#Encapsulamento
class Database:
    def __init__(self):
        self.__dados={}
    #quando temos um atributo com _ antes do nome é quase que um atributo privado, a recomendação é nao mexer nele
    #um _ significa: privado porem de forma sutil, dois __ significa 100% privadissimo nao recomenda voce a usar
    def insert_client(self,id,name):
        if 'clientes' not in self.__dados:
            self.__dados['clientes']={id:name}
            return
        self.__dados['clientes'].update({id:name})

    def clients_list(self):
        for id,name in self.__dados['clientes'].items():
            print(id,name)

    def delete_client(self,id):
        del self.__dados['clientes'][id]

base=Database()
base.__dados='ooooiiiii'
print(base.__dados)
"""
base=Database()
base.insert_client(1,'otavio')
base.insert_client(2,'vivi')
base.insert_client(3,'rosa')
print(base._dados)
base.delete_client(1)

base._dados= 'uma outra coisa'
base.clients_list()"""