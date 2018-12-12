# # FUNCION QUE RECIBE UNA FUNCION Y DEVUELVE UNA NUEVA FUNC
# def decorador(funcion):
# 	def funciondDecorada(*args,**kwargs):
# 		print('Funcion ejecutada ',funcion.__name__)
# 		return funcion(*args,**kwargs)
# 	return funciondDecorada

# # def funcRest(n,m):
# # 	print(n-m)
# # print(decorador(funcRest)(5,3)) #paso*1

# # La sintaxis de las versiones nuevas de python permite simplificar el paso*1 de este modo:
# @decorador
# def funcRest(n,m):
# 	return n-m

# print(funcRest(14,7))

# Ejercicio ejemplo decoradores
log = False
user = 'mattiudica'

def succesLog(f):
	def check(*args,**kwargs):
		if user == 'mattiudica':
			log = True
			f(*args,**kwargs)
		else:
			log = False
			print('No tiene permisos para ejecutar ', f.__name__)
	return check


def decorador(funcion):
	def funciondDecorada(*args,**kwargs):
		print('Funcion ejecutada ',funcion.__name__)
		funcion(*args,**kwargs)
	return funciondDecorada
# Las funciones decoradas se pueden concatenar unas con otras, lo hacen de abajo para arriba(1.decorador,2.succesLog):
@succesLog
@decorador
def funcRest(n,m):
	print(n-m)

funcRest(14,7)

# La llamada de los @decoradores añidados es equivalente a esto:
# login = succesLog(decorador(funcRest))
# login(14,7)