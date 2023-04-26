class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def sale(self, percentual):
      self.price=self.price-(self.price * (percentual/100))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name=value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value,str):
            value=float(value.replace('R$', ''))
        self._price=value


p1 = Product('CAMISETA', 50)
p1.sale(10)
print(p1.name,p1.price)

p2=Product('caneca', 'R$15')
p2.sale(10)
print(p2.price)