#---METODOS DE CADENAS Y OBJETOS---
s = 'Hola MUNDO! Soy el nuevo en Python'
i = ';'
j = ['h','o','l','a']

print (len(s))
print (s.count("o",0,len(s)))#El metodo .count(valor,inicio, fin) donde inicio
					 		 #y fin son opcionales,diferencia mayusculas de minusculas.

print(s.lower())
print(s.upper())

print(s.replace("l"," ",2))  #El metodo .replace(valor,nuevo,repeticiones), donde valor es
						     #lo que queremos quitar, nuevo lo que queremos agregar, repet es opcional.							

print(s.split("e",1))	     #El metodo .split(separador,maxsplit) borra el separador y divide la cadena.
							 #Maxsplit es opcional. Si .split() queda vacio separa por cada espacio en blanco.

print(s.find())				 #El metodo .find(valor,inicio,fin) busca y devuelve la posicion del valor.
							 #Inicio y fin son opcionales. Si hago .rfind busca el valor de atras para adelante.

print(i.join(j))			 #El metodo .join() recibe como parametro una elemento tipo secuencia (tupla, lista).
							 #Devuelve un string con los elementos de la secuencia separados por el valor dado.
