#---METODOS DE LISTAS---
lista1 = [1,'dos',3,]
buscar = 'dos'
tupla1 = ('uno',2,'tres')


#print (buscar in lista1)			#Metodo in nos permite averiguar si un elemnto se encuentra o no en una lista
									#Devuelve True or False.

#print (lista1.index('dos'))		#Metodo .index() devuelve el indice de un elemento dentro de la lista,
									#Si no se encuentra devuelve error.

if buscar in lista1:
	print(lista1.index(buscar))
else:
	print('El elemento no existe en la lista')
	lista1.append(buscar)			#Metodo .append() agrega un elemento() a una lista en la ultima posicion.
	print(lista1)

lista1.insert(2,"nuevo")			#Metodo .insert() agrega un elemento a la lista en un indice determinado.	
print(lista1)		

print(lista1.count(1))				#Metodo .count() devuelve la cantidad de veces que se repite un elemento en la lista.
					
lista1.extend(tupla1)				#Metodo .extend() agrega el iterable pasado por parametro a otra lista.
print(lista1)		

lista1.pop()						#Metodo .pop() eleminina el ultimo elemento de la lista, o el indice que se le pase como parametro.
print(lista1)						

lista1.remove(1)					#Metodo .remove() borra el valor() de un elemento en la lista pero este espacio queda vacio,
print(lista1)						#no se elimina como con pop().

lista1.reverse()					#Metodo .reverse() invierte el orden e indice de los elementos en la lista.
print(lista1)
	