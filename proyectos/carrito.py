"""
Cristian Alexei Romero Martinez
Código de Python
Ingeniería en Sistemas Computacionales


"""

class Carrito:

	def __init__(self):
		self.productos = {}
		self.max_cap : int = 10
		self.total_sumado : float = 0.0

	def añadirProducto(self,nuevo_producto,cantidad,precio):
		if self.max_cap - cantidad < 0:
			print("Error: Cantidad de productos excedida.")
			return
		self.productos[nuevo_producto] = {"Cantidad":cantidad,"Precio":precio}
		self.max_cap -= cantidad
		self.total_sumado += cantidad*precio
		print(f"Producto {nuevo_producto} añadido.")

	def removerProducto(self,producto):
		try:
			self.total_sumado -= self.productos[producto]["Cantidad"] * self.productos[producto]["Precio"]
			self.max_cap += self.productos[producto]["Cantidad"]
			self.productos.pop(producto)
		except KeyError: print(f"Producto {producto} no encontrado.")
		else: print(f"Producto {producto} removido.")

	def coolprint(self):
		for p in self.productos:
			print(p)

# Crear función de pago con cambio. Añadir funciones extra.

mycar = Carrito()
mycar.añadirProducto("Papas",2,10.50)
mycar.coolprint()
print(mycar.total_sumado,mycar.max_cap,"\n")
mycar.añadirProducto("Zanahorias",5,32.00)
mycar.coolprint()
print(mycar.total_sumado,mycar.max_cap,"\n")
mycar.removerProducto("Papas")
mycar.coolprint()
print(mycar.total_sumado,mycar.max_cap,"\n")
mycar.removerProducto("Zanahorias")
mycar.coolprint()
print(mycar.total_sumado,mycar.max_cap,"\n")
