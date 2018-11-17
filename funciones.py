#---FUNCIONES---
def function1(cad,num3):
	print(cad*num3)

function1("Matt",7)

#Al agregarle *al tercer parametro, guardo los argunmentos nuevos que le pase a la func
#en una tupla.
def function2(cadena1,num4,*algomas):
	print(cadena1*num4)
	for cadena in algomas:
		print(cadena*num4)

function2("Matias",2,"cadena1aca","jeje")

#Al agregarle **al tercer parametro, en vez de guardarse en una tupla los argunmentos se guardan
#en un diccionario.
def function3(cadena1,num4,**alguitomas):
	print(cadena1*num4)
	print(alguitomas['numeroextra'])

function3("Matias",2,cadenaextra='diccionario',numeroextra=7)

#Utilizando return
def my_function(num1,num2):
	return num1 + num2

result = my_function(6,6)
print(result)
