class Conta:

    def __init__(self, numero,titular,saldo,limite):
        print("construindo objeto...{}".format(self))
        self.numero=numero
        self.titular=titular
        self.saldo=saldo
        self.limite=limite
    
    def extrato(self):
        print("saldo {} do titular {}".format(self.saldo,self.titular))

    def deposita(self, valor):
        self.saldo+=valor

    def saca(self,valor):
        self.saldo-=valor

    def extrato(self):
        return self.saldo
