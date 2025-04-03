"""
Cristian Alexei Romero Martinez
Código de Python
Ingeniería en Sistemas Computacionales
Introducción a Ingeniería en Sistemas Computacionales

Sistema de regustro de almacén y venta de productos en tiendas minoristas

"""

class Store:
	# La información que se guardará sobre cada uno de los productos
	def __init__(self, unique_name_title:str, quantity_title:str, price_title:str, *other_data):
		self.cols = (quantity_title, price_title)+other_data
		self.n_data = len(self.cols)
		self.products = {}
		self.id = unique_name_title

	def __del__(self):
		pass

	# Nuevo producto.
	def newProduct(self):
		name = input(self.id+":	")
		self.products[name] = {}
		for n in range(self.n_data):
			if n == 0: self.products[name][self.cols[n]] = int(input(self.cols[n]+":	"))
			elif n == 1: self.products[name][self.cols[n]] = float(input(self.cols[n]+":	"))
			else: self.products[name][self.cols[n]] = input(self.cols[n]+":	")
		print("New Product Added.")

	# Elimina un producto existente
	def deleteProduct(self, product_name):
		try: self.products.pop(product_name)
		except KeyError: print("Error: Product Not Found.")
		else: print("Product Removed.")

	# Vender producto existente
	def sell(self, product_name, quantity:int=1):
		try: product = self.products[product_name] # Nota: ¿Se puede mejorar?
		except KeyError: print("Error: Product Not Found.")
		else:
			if self.products[product_name][self.cols[0]] > 0:
				self.products[product_name][self.cols[0]] -= quantity
				# Returns the subtotal
				return quantity * self.products[product_name][self.cols[1]]
			else: print("Invalid Operation.")

	# Añade cantidad la cantidad a un producto
	def addToInventory(self, product_name, quantity:int=1):
		try:
			self.products[product_name][self.cols[0]] += quantity
		except KeyError: print("Error: Product Not Found.")
		else: print("Product quantity added to inventory.")

	# Actializa el precio de un producto
	def updatePrice(self, product_name, new_price):
		try: self.products[product_name][self.cols[1]] = new_price
		except KeyError: print("Error: Product Not Found.")
		else: print("Price change applied.")

	# Actualiza un dato que no sea la cantidad ni el precio
	def mod(self, product_name, data_camp, new_value):
		try:
			if data_camp != self.cols[0] and data_camp != self.cols[1]:
				self.products[product_name][data_camp] = new_value
			else:
				print("Invalid Operation.")
		except KeyError: print("Error: Product Not Found.")
		else: print("Change applied.")

def menu(show):
	lpd : bool = True
	print("		Buen día, Usuario")
	print("	1. Nuevo producto")
	if show:
		print("	2. Eliminar producto")
		print("	3. Modificar producto")
		print("	4. Vender producto")
	print("	0. Salir")
	while lpd:
		try:
			r = int(input(" << "))
		except ValueError:
			print("Respuesta inválida")
		else:
			return r

def mod_menu():
	print("		Ingrese el campo a modificar")
	print(" 1. ")

mystore = Store("Nombre","Cantidad","Precio","Descripción", "etc")

while True:
	match menu(mystore.n_data > 0):
		case 0: break
		case 1: mystore.newProduct()
		case 2: mystore.deleteProduct(input("Ingrese el nombre del producto a eliminar:	"))
		case 3:
			mystore.mod(
				input("Ingrese el nombre del producto:	"),
				input("Ingrese el campo a modificar:	"),
				input("Ingrese el nuevo valor:	")
			)
		case 4:
			print(
					"Subtotal:",
					mystore.sell(input("Ingrese el nombre del producto:	"), int(input("Ingrese la cantidad:	")))
				)
	print(mystore.products)
