# generator como una funcion para crear un iterador pero no hace falta declarar los metodos next e iter son automaticos
# Contiene yield, lo que se diferencia de return porque no corta la funcion, pausa el estado de la funcion y se puede retomar despues del yield.

# Esta funcion hace lo mismo que la class ListIter
# de iterator_class.py, pero mucho mas acotado

def listIterator(list):
	for i in list:
		yield i

b = [1, 2, 3, 6, 5, 4]

myList = listIterator(b)

# print(next(myList))
# print(next(myList))
# print(next(myList))
# print(next(myList))
# print(next(myList))
# print(next(myList))

for num in myList:
	print(num)