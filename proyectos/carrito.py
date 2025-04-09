"""
Cristian Alexei Romero Martinez
Código de Python
Ingeniería en Sistemas Computacionales
"""

class Carrito:
	productos_en_venta = [
		["Manzana", 10],
		["Pera", 7],
		["Sandía", 30],
		["Coco", 60],
		["Apio", 22]
	]
	def __init__(self):
		self.productos = []
		self.max_cap : int = 10
		self.total_sumado : float = 0.0

	def anadirProducto(self,no_producto,cantidad):
		if self.max_cap - cantidad < 0:
			print("Error: Cantidad de productos excedida.")
			return
		self.productos.append([no_producto, cantidad])
		self.max_cap -= cantidad
		print(f"Producto {self.productos_en_venta[no_producto][0]} añadido.")

	def removerProducto(self,no_producto,cantidad):
		for i in self.productos:
			if i[0] == no_producto:
				if i[1] - cantidad <= 0:
					print(f"Se han eliminado todos los {productos_en_venta[no_producto][0]} del carrito")
					del idea
				else:
					i[1] -= cantidad
					print(f"Se han eliminado {cantidad} {self.productos_en_venta[no_producto][0]} del carrito")
				self.max_cap += cantidad
				return
			else: print("Producto no encontrado dentro del carrito.")

	def comprar(self):
		total : float = 0.0
		ticket = []
		for p in self.productos:
			nombre = self.productos_en_venta[p[0]][0]
			precio : float = self.productos_en_venta[p[0]][1]
			cantidad : int = p[1]
			subtotal : float = precio * cantidad
			ticket.append([nombre, precio, cantidad, subtotal])
			total += subtotal
		return ticket, total

	def reiniciar(self):
		self.productos = []
		self.max_cap : int = 10
		self.total_sumado : float = 0.0

# Crear función de pago con cambio. Añadir funciones extra.
opt1 = ["Añadir Producto", "Retirar Producto", "Ver carrito", "Comprar productos", "Cancelar compra"]
mycar = Carrito()

def arrprint():
	for p in range(len(mycar.productos_en_venta)):
		print(str(p)+".-",mycar.productos_en_venta[p][0]+" a solo $"+str(mycar.productos_en_venta[p][1]))

def carrprint():
	for p in mycar.productos:
		print(p[0],".- ",mycar.productos_en_venta[p[0]][0], " x ", p[1])

def menu(opt):
	gate = True
	for n in range(len(opt)):
		print("	"+str(n+1)+".	"+opt[n])
	print("	0.	Salir")
	while gate:
		try: r = int(input("	<<	"))
		except ValueError: print("Valor Inválido")
		else:
			if r >= 0 and r < len(opt):
				return r

def new_product():
	arrprint()
	gate = True
	while gate:
		try: no_prod = int(input("Ingrese el número del producto:	"))
		except ValueError: print("Valor inválido")
		else: gate = False
	gate = True
	while gate:
		try: cantidad = int(input("Ingrese la cantidad del producto:	"))
		except ValueError: print("Valor inválido")
		else: gate = False
	mycar.anadirProducto(no_prod, cantidad)
#	print(mycar.productos)

def remove_product():
	carrprint()
	gate = True
	while gate:
		try: no_prod = int(input("Ingrese el número del producto:	"))
		except ValueError: print("Valor inválido")
		else: gate = False
	gate = True
	while gate:
		try: cantidad = int(input("Ingrese la cantidad del producto:	"))
		except ValueError: print("Valor inválido")
		else: gate = False
	mycar.removerProducto(no_prod, cantidad)

def payment(total_a_pagar):
	gate = True
	while gate:
		try: valuacion = float(input("Ingrese el valor del billete o moneda ingresada:	"))
		except ValueError: print("Moneda o billete no reconocido.")
		else:
		    if valuacion < total_a_pagar: print("Cantidad insuficiente.")
		    else:
    			total_a_pagar -= valuacion
    			if total_a_pagar <= 0:
    				gate = False
	print("Retornando:") #Si, pude haber hecho una función, pero el tiempo me comía.
	billetes = [500,200,100,50,20,10,5,2,1,0.5]
	for c in billetes:
		u : int = -total_a_pagar // c
		if u > 0:
			if c > 10: print(u, "billetes de",c)
			else: print(u, "monedas de",c)
			total_a_pagar += u * c

def buy():
	print("")
	ti, to = mycar.comprar()
	for i in ti:
		print(i[0], i[1], i[2], i[3])
	print("Total: $"+str(to)+"\n")
	payment(to)

while True:
	match menu(opt1):
		case 0: break
		case 1: new_product()
		case 2: remove_product()
		case 3: carrprint()
		case 4: buy()
		case 5: mycar.reiniciar()
