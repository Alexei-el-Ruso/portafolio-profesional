"""
Cristian Alexei Romero Martinez
Código de Python
Ingeniería en Sistemas Computacionales


"""

class Silla:
	def __init__(self, color, material, patas):
		self.__color:str = color
		self.__material:str = material
		self.__patas:int = patas
		self.__disponible = True

	def __del__(self):
		print("Silla eliminada")

	def sentarse(self, usuario):
		if usuario != None:
			self.__disponible = False

	def levantarse(self):
		self.__disponible = True

	def pintar(self, color:str):
		self.__color = color

	def ver_color(self):
		return self.__color

	def examinar_material(self):
		return self.__material

	def contar_patas(self):
		return self.__patas

mysilla = Silla("Rojo", "Madera", 4)
print(mysilla.ver_color())
mysilla.pintar("Negro")
print(mysilla.ver_color())
