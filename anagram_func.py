# funcion que tome de un input una palabra y devuelva un anagrama de esa palabra:
from functools import reduce

cadena = input("Ingresa una palabra: ")

def anagramFunc(palabra):
	sortList = sorted(palabra, reverse=True)
	reduceAnag = reduce(lambda x,y : x + y,sortList)
	print(reduceAnag.lower())

anagramFunc(cadena)

