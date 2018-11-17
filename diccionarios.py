#---DICCIONARIOS---
#No tienen indice como las listas y tuplas, tienen claves asociadas a sus valores.
#La clave puede ser cualquier tipo de dato inclusive tuplas, excepto listas y diccionarios.
#Se pueden modificar los valores asignados a cada clave pero NO la clave misma.
#No es posible hacer slice.

tc = (2, "chau", True)
d = {'Clave1':1,
	2:True,
	'Clave3':tc,
	}
print (d[2])