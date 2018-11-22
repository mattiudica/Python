
#def prueba(fX):						
#	return fX()						#El parametro fX toma como variable a la func(porEnviar) que se ejecuta al retornar fX(), y hace el return 5+5.	

#def porEnviar():
#	return 5+5						

#print(prueba(porEnviar))			#Al escribir la funcion con los () se ejecuta. Si es sin parentesis solo la uso como variable y la puedo ejecutar luego al llamarla, por esto son func de orden superior.
									#Si hiciera prueba(porEnviar()) daria error

def selection(operation):
	def add(num1,num2):
		return num1 + num2
	def subtract(num1,num2):
		return num1 - num2
	if operation == '+':
		return add
	elif operation == '-':
		return subtract
	else:
		return 'That operation is not available'

funcSave1 = selection('+')
funcSave2 = selection('-')
funcSave3 = selection('/')

print (funcSave1(7,2))
print (funcSave2(7,2))
print (funcSave3)
