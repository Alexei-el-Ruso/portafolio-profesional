lista_productos = []

n:int = int(input("Introduzca el número de productos a registrar:	"))

#lista_productos *= n
#for u in range(len(lista_productos)):
#	lista_productos = input("Ingrese el nombre de un producto:	")

for _ in range(n):
	lista_productos.append(input("Ingrese el nombre de un producto:      "))

print(lista_productos)
