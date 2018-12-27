# Es basicamente lo mismo que try catch en JS. Lo utilizamos para probar ejecutar una parte del script
# que puede no funcionar y en el caso que haya un error podemos alertarlo y se sigue ejecutando el codigo posterior.
# var1 = "Esta variable si existe"
# var2 = 2

# print(var1*var2)
# try:
# 	print(var4 * var1)
# except Exception as e:
# 	print("Esa variable no existe")
# else:
# 	pass

# print("Se deberia poder imprimir este texto")

# Tambien se pueden definir errores especificos en el except para poder manejarlos acorde su tipo:
# var3 = "Otra variable existente"
# var4 = 3
# var6 = "Ultima variable existente"

# try:
# 	print(var3,var4,var6*2)
# 	# print(var3,var4,var5,var6*var3)
# 	# print(1/0)
# 	# print(else var3)
# except(TypeError, NameError):
# 	print("Aqui ocurrio un error de tipo de dato o nombre")
# except ZeroDivisionError:
# 	print("No se puede dividir entre 0")
# except SyntaxError:
# 	print("Aqui ocurrio un error de sintaxis invalida")					#No me anda este except revisar
# else:
# 	print("No hubo errores")
# 	pass
# finally:
# 	print("Try/except finalizado")

# print("Adios!")

# Generar mis propios errores para poder manejarlos:

class CreateError(Exception):
	def __init__(self, valor):
		self.valorError=valor
	def __str__(self):
		print("No se pudo ejecutar el script utilizando ",self.valorError)

m= 7
n= 0

try:
	if n == 0:
		raise CreateError()
except:
	print("Es imposible dividir un numero en 0")
else:
	pass

print("Hasta la vista baby")





