class Shopping_cart:

	def __init__(self, product):
		self._products = []
		
	def add_product(self, product):
		self._products.append(product)

	def get_products(self):
		for product in self._products:
			print product.get_name()

class Product:
	
	def __init__(self, name):
		_name = name

	def set_name(self, name):
		_name = name

	def set_price(self, price):
		_price = price

	def get_name(self):
		return self._name

sam = Shopping_cart()
sam.add_product(Product("cheese"))
sam.get_products()
