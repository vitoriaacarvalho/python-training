from classes import ShoppingCart, Product

carrinho=ShoppingCart()
print(carrinho)
p1=Product('camiseta', 50)
p2=Product('iphone', 6000)
carrinho.insert_products(p1)
carrinho.insert_products(p2)
print(carrinho.products[0].name)