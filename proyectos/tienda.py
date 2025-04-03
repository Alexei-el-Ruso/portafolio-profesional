#	Tienda
#	Cristian Alexei Romero Martinez
#	Diccionario de productos

#	Definición
class Producto:

	def __init__(self,nom,desc,precio:int,cant:int):
		self.caracteristicas = {
			"Producto": nom,
			"Descripción": desc,
			"Precio": precio,
			"Cantidad": cant
		}

	def __del__(self):
		print(self.caracteristicas["Producto"], " ha sido liminado")

	def mod_desc(self,new_desc):
		self.caracteristicas["Descripción"] = new_desc

	def add_stock(self,cant_agr:int):
		self.caracteristicas["Cantidad"] += cant_agr

	def calc_subtotal(self,cant:int):
		return self.caracteristicas["Precio"] * cant

	def sell(self,cant_vend:int):
		self.caracteristicas["Cantidad"] -= cant_vend
		return self.caracteristicas["Precio"] * cant_vend

#	Ejecución
prods_list = []

def menu(show):
	Lpd : bool = True
	print("		Buen día, Usuario")
	print("	1. Nuevo producto")
	if show:
		print("	2. Eliminar producto")
		print("	3. Modificar descripción de producto")
		print("	4. Comenzar venta de productos")
	print("	0. Salir")
	r = input(" << ")
	while Lpd:
		try:
			r = int(r)
		except ValueError:
			print("Respuesta inválida")
		else:
			if show and r <= 4 and r >= 0: Lpd = False
			elif r == 1: Lpd = False
	return r

def mostrar_productos(productos):
	print("\nID	Nombre		Descripción		Precio	Cantidad")
	for p in range(len(productos)):
		print(p,"	",productos[p].caracteristicas["Producto"],"	",productos[p].caracteristicas["Descripción"],"	",productos[p].caracteristicas["Precio"],"	",productos[p].caracteristicas["Cantidad"])
	print("")

def nuevo_producto():
	return Producto(
        input("Ingrese el producto:     "),
        input("Ingrese su descripción:  "),
	float(input("Ingrese su precio:       ")),
	int(input("Ingrese su cantidad:     "))
        )

while True:
	resp = menu(len(prods_list)>0)
	match resp:
		case 0: break
		case 1:
			prods_list.append(None)
			prods_list[-1] = nuevo_producto()
			mostrar_productos(prods_list)
		case 2:
			mostrar_productos(prods_list)
			i = None
			while i == None or i < 0 and i >= len(prods_list):
				i = int(input("ID:  "))
			del prods_list[i]
		case 3:
			mostrar_productos(prods_list)
			i = None
			while i == None or i < 0 and i >= len(prods_list):
				i = int(input("ID:  "))
			prods_list[i].mod_desc(input("Ingrese la nueva descripción:	"))
			print(prods_list[i].caracteristicas["Producto"],"    ",prods_list[i].caracteristicas["Descripción"]," ",prods_list[i].caracteristicas["Precio"],"      ",prods_list[i].caracteristicas["Cantidad"])
		case 4:
			en_venta : bool = True
			venta_reciente = []
			mostrar_productos(prods_list)
			while en_venta:
				i = input("Ingrese el ID del producto a vender (vacío para terminar):	")
				if (i == ""): en_venta = False
				else:
					i = int(i)
					c = int(input("Ingrese la cantidad:	"))
					venta_reciente.append(Producto(prods_list[i].caracteristicas["Producto"],prods_list[i].caracteristicas["Descripción"],prods_list[i].caracteristicas["Precio"],c))
					prods_list[i].sell(c)
			mostrar_productos(prods_list)
			mostrar_productos(venta_reciente)
