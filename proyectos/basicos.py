while True:
	vol = int(input("Introduzca el Volúmen:	"))
	if vol <= 100 and vol >= 0: break

def check_volume(vol):
	if vol <= 20: return("bajo")
	elif vol <= 80: return("medio")
	else: return("alto")

print("El volúmen es", check_volume(vol))
