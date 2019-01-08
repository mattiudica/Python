# Todo valor que reciba desde el teclado se guarda en la variable valor y se imprime
# valor = input()						
# print(valor+' es de tipo', type(valor))
# Va a ser siempre de type str a menos que lo convierta.
try:
	valor = input('Prueba el raw input ingresando cualquier valor en el teclado: ')
	valor = int(valor)
except:
	print(valor + ' es de tipo str.')
else:
	print(valor,' es de tipo int.')

