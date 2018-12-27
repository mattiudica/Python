try:
	valor = input('Introduce cualquier numero a continuacion: ')
	valor = int(valor)
	
except ValueError:
	print('No ingresaste un numero')
else:
	print(type(valor))


