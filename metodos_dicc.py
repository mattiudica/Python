
d = {'Clave1':1,
	2:True,
	'Clave3':'vamo lo pibe',
	}
d2 = d.copy()								#Metodo .copy() copia el contenido de un dicc a otro.
print(d,d2)

print('Clave3' in d)						#Metodo para buscar si una clave existe(True) o no(False) en el diccionario.
											#Reemplaza al antiguo metodo .has_key()

print(d.items())							#Metodo .items() sin parametro, devuelve una serie de tuplas por cada par
											#clave/valor.

print(d.keys())								#Metodo .keys() sin parametro, devuelve una lista conteniendo solo las claves del dicc.

print(d.values())							#Metodo .values(), idem .keys() pero con los valores.

print(d)
print(d.pop('Clave3',False))				#Metodo .pop(valor,d), elimina el valor pasado por parametro, d es opcional y es el retorno
print(d)									#que elijamos en caso de que el valor no se encuentre, va a reemplazar al Error.
											#Usar si quiero capturar el elemento aparte de removerlo del dicc.

del d['Clave1']								#Metodo del diccionario[], elimina elemento por su clave.
print(d)									#Usar simplemente para borrar el elemento del dicc
											
d.clear()									#Metodo .clear() borra todo el contenido dejando un diccionario vacio.
print(d)

d['clave_nueva'] = 'llenando nuevamente'	#Asi agrego elementos al diccionarios.
print(d)


#Usar si quiero capturar el elemento aparte de removerlo del dicc.
#Usar simplemente para borrar el elemento del dicc