try:
	w = open('txt_writeEj.txt','r')
except:
	print('Error opening file')
	exit()
else:
	# Al utilizar metodo .read() si el archivo es muy extenso puede saturar la memoria cuidado
	# El argumento es opcional e indica el numero de bytes a leer.
	# print(w.read())
	while True:
		print(w.readline())
		if w.readline()=='':
			print("""
					Fin del archivo""")
			break

# El metodo .readlines() devuelve un iterable de todo el archivo dividido por sus caracteres de escape
# incluidas las lineas vacias. Puedo hacer un for loop para recorrer e imprimir cada elemento de la lista.
